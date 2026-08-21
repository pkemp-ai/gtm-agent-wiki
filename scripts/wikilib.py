#!/usr/bin/env python3
"""Shared helpers for the gtm-agent-wiki bookkeeping scripts.

These scripts are the deterministic half of the GTM wiki's maintenance story
(SPEC 2.5, 14): models synthesize, scripts validate. Everything here is
Python 3 standard library only, so a deployment can run the scripts anywhere
a Python interpreter exists -- no package manager, no environment setup.

Front matter subset
-------------------
The spec (4.1) uses YAML front matter, but only a small, flat subset of
YAML. Rather than depend on a YAML library, ``parse_front_matter`` hand-rolls
a parser for exactly the subset the spec exhibits:

* The file's first line is ``---``; the block ends at the next ``---``
  (or ``...``) on a line of its own.
* Flat ``key: value`` pairs only. Keys match ``[A-Za-z0-9_-]+``.
* Scalar values: bare words, or single-/double-quoted strings. Scalars are
  never type-coerced -- every value stays a string.
* Inline lists: ``[a, b, "c d"]``. No block (``- item``) lists.
* Inline dicts, one level deep: ``{by: maintain, at: 2026-08-19T09:00:00Z}``.
* Trailing ``# comments`` are stripped (outside quotes and brackets).
* No deeper nesting, no multiline scalars, no anchors or aliases.

Anything outside this subset is reported as a parse error, which lint
surfaces as a front-matter finding. This is deliberate: front matter is a
machine surface, and a constrained grammar keeps it diffable and boring.

Inert text
----------
Two kinds of text in a wiki file are not wiki content and must never be
scanned as claims, links, or headings: fenced code blocks (which quote
formats, including claim tags, on purpose) and HTML comments (authoring
notes and template guidance). ``visible_lines`` returns a copy of the file
with both blanked out, preserving line and column positions so findings
still point at real coordinates. The one structural exception is a
``<!-- tier: -->`` marker (SPEC 6): a heading's tier override changes what
rules apply to its section, so ``parse_sections`` reads it from the *raw*
line rather than the masked one -- a comment holding real machinery, not
decoration, is the single case this module treats differently.

Claim parsing
-------------
``split_claim_candidate`` + ``looks_like_claim_tag`` are the one definition
of "what counts as a claim tag" shared by every check and script that needs
it -- lint's claim-hygiene family, the doctrine-provenance check, and
``census_claims`` for the digest. Three deployments in the end-to-end test
each hand-computed claim counts for the same wiki and got three different
numbers; the fix is one shared reader, not three careful ones.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path

# --------------------------------------------------------------------------
# Spec vocabulary (SPEC 4-6, taxonomy.md)
# --------------------------------------------------------------------------

TIERS = ("doctrine", "state", "runbook", "reference", "system")

CONFIDENCE_LABELS = ("confirmed", "source-backed", "inferred", "contested", "watchlist")

#: Front-matter fields required on every canonical file and reference page
#: (SPEC 4.1). ``generated`` and ``tags`` were dropped in 0.2 — they are
#: neither required nor written. Empty ``last-verified`` / ``evidence-as-of``
#: is the documented encoding of "never" / "no evidence yet"; the key must
#: still be present.
REQUIRED_FIELDS = (
    "type",
    "description",
    "owner",
    "sources",
    "update-cadence",
    "staleness-horizon",
    "evidence-as-of",
    "last-verified",
)

#: Provenance prefixes that do not name a sources.md entry (SPEC 4.2):
#: human-originated (interview:, doc:) and agent inference (inference:).
NON_MANIFEST_PROVENANCE = ("interview", "doc", "inference")

#: Provenance prefixes a doctrine claim may cite directly -- the two
#: human-originated, non-manifest kinds (SPEC 4.2's locator table). A claim
#: citing anything else (a manifest source id, or ``inference:``) needs one
#: of SPEC 17.3's three exceptions to sit in a ``type: doctrine`` file.
DOCTRINE_ALLOWED_PREFIXES = ("interview", "doc")

#: SPEC 17.3(b) / taxonomy.md's three permanent evidence sections: the only
#: place non-H-class provenance may be the *sole* tag on a doctrine
#: assertion, because the section holds evidence in its own words rather
#: than a decision. Keyed by root-level filename; heading slug is matched
#: at any level, since channel-styles.md repeats ``### Examples`` per
#: channel section.
EVIDENCE_SECTIONS = {
    "icp-personas.md": ("customer-language",),
    "voice.md": ("exemplars",),
    "channel-styles.md": ("examples",),
}

#: sources.md cadence vocabulary (SPEC 10) in days. Used for the manifest
#: health check: a cursor that has not advanced in 2x its cadence is stalled.
#: ``interview`` cadences are human-paced and have no computable window.
CADENCE_DAYS = {
    "per-run": 1,
    "daily": 1,
    "weekly": 7,
    "monthly": 30,
    "quarterly": 90,
}

#: System files defined in SPEC 12 / taxonomy. Exempt from front-matter
#: requirements and from the orphan check (their formats are fixed by the
#: spec and every wiki cites them constantly).
SYSTEM_BASENAMES = ("open-questions.md", "changelog.md", "sources.md")

#: Default top-level order from SPEC 3 -- used to sort the AGENTS.md
#: inventory table so it reads in taxonomy order, not filesystem order.
#: Local additions (files not in this tuple) sort after, alphabetically.
CANONICAL_ORDER = (
    "business-core.md",
    "icp-personas.md",
    "voice.md",
    "channel-styles.md",
    "compliance-guardrails.md",
    "glossary.md",
    "growth.md",
    "competitors.md",
    "customers.md",
    "events.md",
    "product-releases.md",
    "partners.md",
    "account-ownership.md",
    "pipeline.md",
    "content-assets.md",
    "metrics.md",
    "crm.md",
    "gtm-tools.md",
    "open-questions.md",
    "changelog.md",
    "sources.md",
)

#: Directories never scanned as wiki content.
EXCLUDED_DIRS = (".git", ".archive", ".obsidian", "node_modules", "__pycache__")

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PROVENANCE_RE = re.compile(r"^([A-Za-z0-9][A-Za-z0-9._-]*):(\S.*)$")
#: Candidate claim tag: a bracket containing at least one pipe (SPEC 4.2).
#: Validation of the parts happens in the caller.
CLAIM_CANDIDATE_RE = re.compile(r"\[([^\[\]\n]*\|[^\[\]\n]*)\]")
#: Standard markdown link (image prefix captured so callers can ignore it).
LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
BLOCK_ANCHOR_RE = re.compile(r"\^([A-Za-z0-9-]+)\s*$")
#: Any caret-prefixed token, wherever it sits on the line -- used to catch
#: SPEC 4.2's "last token on its line" rule being broken. Excludes footnote
#: markers (``[^1]``), which are a different convention this format doesn't use.
ANCHOR_TOKEN_RE = re.compile(r"(?<!\[)\^[A-Za-z0-9-]+")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
#: An HTML-comment tier override on a heading line (SPEC 6): ``<!-- tier:
#: state -->`` or ``<!-- tier: state, sensitive -->`` (extra qualifiers after
#: the first comma are ignored -- only the tier keyword itself is structural).
TIER_MARKER_RE = re.compile(r"<!--\s*tier:\s*([a-z][a-z, -]*?)\s*-->", re.IGNORECASE)
#: ``verified: <date>`` execution stamp on a runbook entry (SPEC 8 note 3).
#: The lookbehind keeps front matter's ``last-verified:`` out of the match.
VERIFIED_STAMP_RE = re.compile(r"(?<![\w-])verified:\s*(\d{4}-\d{2}-\d{2})")
#: ``unverified: {since: ..., reason: ..., question: ...}`` entry state
#: (SPEC 8 note 3) -- counted, never validated in depth; a malformed dict
#: is still one unverified entry for decay-counting purposes.
UNVERIFIED_STAMP_RE = re.compile(r"(?<![\w-])unverified:\s*\{")
#: A trailing ``!internal`` flag on a claim's date field (SPEC 4.2):
#: ``[confirmed | interview:x | 2026-08-19 !internal]``.
INTERNAL_FLAG_RE = re.compile(r"^(.*?)\s+!internal$")
#: A line-range fragment on an archived line-oriented payload (SPEC 4.2):
#: ``#L214`` or ``#L214-231``.
LINE_FRAGMENT_RE = re.compile(r"^L(\d+)(?:-(\d+))?$")
#: A zero-based array-index fragment on an archived JSON payload (SPEC 4.2).
INDEX_FRAGMENT_RE = re.compile(r"^i-(\d+)$")


# --------------------------------------------------------------------------
# Findings
# --------------------------------------------------------------------------

ERROR = "error"
WARNING = "warning"


@dataclass
class Finding:
    """One lint/sync finding, printable as ``file:line: SEVERITY [check] msg``."""

    file: str
    line: int
    severity: str
    check: str
    message: str

    def render(self) -> str:
        return f"{self.file}:{self.line}: {self.severity.upper()} [{self.check}] {self.message}"


def emit_findings(findings: list, as_json: bool, extra: dict = None) -> int:
    """Print findings (text or JSON) and return the exit code (1 if any error)."""
    findings = sorted(findings, key=lambda f: (f.file, f.line, f.severity, f.check))
    errors = sum(1 for f in findings if f.severity == ERROR)
    warnings = sum(1 for f in findings if f.severity == WARNING)
    if as_json:
        payload = {
            "errors": errors,
            "warnings": warnings,
            "findings": [asdict(f) for f in findings],
        }
        if extra:
            payload.update(extra)
        print(json.dumps(payload, indent=2))
    else:
        for f in findings:
            print(f.render())
        print(f"{errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


# --------------------------------------------------------------------------
# Front matter
# --------------------------------------------------------------------------


@dataclass
class FrontMatter:
    present: bool = False
    closed: bool = False
    data: dict = field(default_factory=dict)
    errors: list = field(default_factory=list)  # [(line_number, message)]
    end_line: int = 0  # 1-based line number of the closing ``---``; 0 if none


def _strip_inline_comment(value: str) -> str:
    """Remove a trailing ``# comment`` outside quotes and brackets."""
    quote = None
    depth = 0
    for i, ch in enumerate(value):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth = max(0, depth - 1)
        elif ch == "#" and depth == 0 and (i == 0 or value[i - 1] in " \t"):
            return value[:i].rstrip()
    return value.strip()


def _parse_scalar(raw: str) -> str:
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    return raw


def _split_top_commas(raw: str) -> list:
    """Split on commas that sit outside quotes (the subset forbids nesting)."""
    parts, buf, quote = [], [], None
    for ch in raw:
        if quote:
            if ch == quote:
                quote = None
            buf.append(ch)
        elif ch in "\"'":
            quote = ch
            buf.append(ch)
        elif ch == ",":
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    if buf or parts:
        parts.append("".join(buf))
    return [p.strip() for p in parts]


def _parse_value(raw: str, lineno: int, errors: list):
    raw = raw.strip()
    if raw.startswith("["):
        if not raw.endswith("]"):
            errors.append((lineno, f"unterminated inline list: {raw!r}"))
            return raw
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(p) for p in _split_top_commas(inner) if p]
    if raw.startswith("{"):
        if not raw.endswith("}"):
            errors.append((lineno, f"unterminated inline dict: {raw!r}"))
            return raw
        out = {}
        inner = raw[1:-1].strip()
        if inner:
            for pair in _split_top_commas(inner):
                key, sep, val = pair.partition(":")
                if not sep:
                    errors.append((lineno, f"inline dict entry is not 'key: value': {pair!r}"))
                    continue
                out[key.strip()] = _parse_scalar(val)
        return out
    return _parse_scalar(raw)


def parse_front_matter(text: str) -> FrontMatter:
    """Parse the constrained front-matter subset documented in the module docstring."""
    fm = FrontMatter()
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return fm
    fm.present = True
    key_re = re.compile(r"^([A-Za-z0-9_-]+):(.*)$")
    for i, line in enumerate(lines[1:], start=2):
        stripped = line.strip()
        if stripped in ("---", "..."):
            fm.closed = True
            fm.end_line = i
            break
        if not stripped or stripped.startswith("#"):
            continue
        if line[0] in " \t":
            fm.errors.append((i, "indented line -- the front-matter subset is flat 'key: value' only"))
            continue
        m = key_re.match(line)
        if not m:
            fm.errors.append((i, f"not a 'key: value' line: {stripped!r}"))
            continue
        key = m.group(1)
        raw = _strip_inline_comment(m.group(2))
        if key in fm.data:
            fm.errors.append((i, f"duplicate key {key!r}"))
            continue
        fm.data[key] = _parse_value(raw, i, fm.errors)
    if fm.present and not fm.closed:
        fm.errors.append((1, "front matter never closed with '---'"))
    return fm


# --------------------------------------------------------------------------
# Dates and durations
# --------------------------------------------------------------------------


def parse_iso_date(value: str):
    """Return a ``date`` or None. Accepts strict YYYY-MM-DD only."""
    if not isinstance(value, str) or not DATE_RE.match(value):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def parse_timestamp_date(value):
    """Return the date part of an ISO timestamp (or a bare date), else None.

    Cursors record ``last-run: 2026-08-12T09:00:00Z`` (SPEC 10); staleness
    arithmetic only ever needs the day.
    """
    if not isinstance(value, str):
        return None
    v = value.strip().strip("\"'")
    if not v or v.lower() in ("null", "~", "none"):
        return None
    return parse_iso_date(v.split("T", 1)[0].strip())


def parse_cadence(value):
    """Days between pulls for a sources.md cadence, or None if not computable."""
    if not isinstance(value, str):
        return None
    return CADENCE_DAYS.get(value.strip().strip("\"'").lower())


def parse_horizon(value):
    """Parse a staleness horizon.

    Returns ``("rolling", None)`` for rolling horizons (capped logs -- lint
    skips them), ``("days", n)`` for ``<n>d``, or ``(None, None)`` if
    unparseable.
    """
    if not isinstance(value, str):
        return (None, None)
    v = value.strip().lower()
    if v.startswith("rolling"):
        return ("rolling", None)
    m = re.match(r"^(\d+)\s*d$", v)
    if m:
        return ("days", int(m.group(1)))
    return (None, None)


# --------------------------------------------------------------------------
# Markdown scanning
# --------------------------------------------------------------------------


def fence_mask(lines: list) -> list:
    """Per-line booleans: True when the line is inside (or is) a code fence."""
    mask = []
    fence_char = None
    for line in lines:
        stripped = line.lstrip()
        m = re.match(r"^(`{3,}|~{3,})", stripped)
        if m:
            if fence_char is None:
                fence_char = m.group(1)[0]
                mask.append(True)
                continue
            if m.group(1)[0] == fence_char:
                fence_char = None
                mask.append(True)
                continue
        mask.append(fence_char is not None)
    return mask


def visible_lines(lines: list) -> list:
    """Blank out inert text: fenced code blocks and HTML comments.

    Returns a list the same length as ``lines``, with fenced lines emptied and
    HTML-comment spans replaced by spaces (so column offsets still line up).
    Comment spans may run across lines; fences win, because a fence quoting
    ``<!--`` is showing a format, not commenting anything out.
    """
    out = []
    in_comment = False
    for line, fenced in zip(lines, fence_mask(lines)):
        if fenced:
            out.append("")
            continue
        buf = []
        i = 0
        while i < len(line):
            if in_comment:
                end = line.find("-->", i)
                if end == -1:
                    buf.append(" " * (len(line) - i))
                    i = len(line)
                else:
                    buf.append(" " * (end + 3 - i))
                    i = end + 3
                    in_comment = False
                continue
            start = line.find("<!--", i)
            if start == -1:
                buf.append(line[i:])
                break
            buf.append(line[i:start])
            i = start
            in_comment = True
        out.append("".join(buf))
    return out


def github_slug(heading: str) -> str:
    """Approximate GitHub/Obsidian heading-anchor slugging."""
    h = heading.strip().lower()
    h = re.sub(r"[^\w\s-]", "", h)
    return re.sub(r"\s", "-", h)


def collect_anchors(text: str) -> set:
    """All link-addressable anchors in a file: heading slugs + ^block-keys."""
    anchors = set()
    for line in visible_lines(text.splitlines()):
        m = HEADING_RE.match(line)
        if m:
            heading = re.sub(r"\s*\^[A-Za-z0-9-]+\s*$", "", m.group(2))
            anchors.add(github_slug(heading))
        b = BLOCK_ANCHOR_RE.search(line)
        if b:
            anchors.add(b.group(1))
    return anchors


def parse_sections(lines: list) -> list:
    """Every heading's line range, level, slug, and ``<!-- tier: -->`` override.

    One dict per heading, in document order: ``{"level", "slug", "tier",
    "start", "end"}``. ``start``/``end`` are 0-based line indices, ``end``
    exclusive, spanning to the next heading of equal-or-shallower level (or
    end of file) -- so containment (``start <= i < end``) answers "is line i
    inside this section", including nested subsections.

    This is how SPEC 17.3's three doctrine-provenance exceptions are found
    mechanically: a ``## Contested`` section, a taxonomy-designated evidence
    section (by filename + slug, see ``EVIDENCE_SECTIONS``), or a section
    carrying a ``<!-- tier: -->`` marker.

    Slugging reads the comment-masked view (``visible_lines``), matching
    ``collect_anchors`` exactly -- a heading's own tier comment must not
    perturb its anchor. The tier marker is the one place a comment is
    structural rather than decorative (SPEC 6), so it is read from the
    *raw* line at the same index instead.
    """
    masked = visible_lines(lines)
    fenced = fence_mask(lines)
    headings = []
    for i, line in enumerate(masked):
        if fenced[i]:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        text = re.sub(r"\s*\^[A-Za-z0-9-]+\s*$", "", m.group(2))
        tier_m = TIER_MARKER_RE.search(lines[i]) if i < len(lines) else None
        tier = tier_m.group(1).strip().split(",")[0].strip().lower() if tier_m else None
        headings.append({"level": len(m.group(1)), "slug": github_slug(text),
                          "tier": tier or None, "start": i})
    for idx, h in enumerate(headings):
        h["end"] = next((later["start"] for later in headings[idx + 1:]
                          if later["level"] <= h["level"]), len(lines))
    return headings


def doctrine_exempt(rel: str, sections: list, line_idx: int) -> bool:
    """SPEC 17.3's three exceptions, by section membership at ``line_idx``
    (0-based). ``rel`` is the file's root-relative path, used only to look
    up ``EVIDENCE_SECTIONS`` -- a same-named section in a different file
    keeps its ordinary doctrine rule.
    """
    evidence_slugs = EVIDENCE_SECTIONS.get(rel, ())
    for h in sections:
        if not (h["start"] <= line_idx < h["end"]):
            continue
        if h["slug"] == "contested" or h["slug"] in evidence_slugs or h["tier"]:
            return True
    return False


def is_table_row(line: str) -> bool:
    """A markdown table row: starts and ends with ``|`` once padding is
    stripped. SPEC 4.2's table convention holds no bracketed claim tags at
    all -- provenance is a bare ``source-id:locator`` in its own column --
    so a table row is never itself a claim candidate (F15)."""
    s = line.strip()
    return len(s) > 1 and s.startswith("|") and s.endswith("|")


def unescape_pipes(line: str) -> str:
    """Un-escape ``\\|`` before claim parsing.

    SPEC 4.2 forbids a claim tag inside a table cell -- the conformant form
    is a trailing ``provenance`` + ``as-of`` column -- but an author who
    tries it anyway escapes the tag's own pipes to survive the table's
    column splitting. Split naively on ``|`` and the backslash lands inside
    the label and provenance text instead of disappearing (F15); un-escaping
    first makes the split land where the author meant it to.
    """
    return line.replace("\\|", "|")


def split_claim_candidate(bracket_inner: str):
    """Split a claim-candidate bracket's inner text into ``(label,
    provenance, date, internal)``, or ``None`` if it is not a 3-part shape.

    Pass text already run through ``unescape_pipes``. Strips a trailing
    ``!internal`` flag (SPEC 4.2) off the date field so date parsing never
    sees it; ``internal`` reports whether the flag was present.
    """
    parts = [p.strip() for p in bracket_inner.split("|")]
    if len(parts) != 3:
        return None
    label, prov, dstr = parts
    internal = False
    m = INTERNAL_FLAG_RE.match(dstr)
    if m:
        dstr, internal = m.group(1).strip(), True
    return label, prov, dstr, internal


def looks_like_claim_tag(label: str, provenance: str, date_str: str) -> bool:
    """SPEC 4.2: treat a 3-part bracket as an attempted claim tag -- for
    hygiene errors and for the claim census alike -- when any one field is
    already tag-shaped, so a decorative bracket-with-pipe in ordinary prose
    does not false-fire."""
    return bool(
        label in CONFIDENCE_LABELS
        or DATE_RE.match(date_str)
        or PROVENANCE_RE.match(provenance)
    )


def iter_md_files(root: Path) -> list:
    """Every .md file in the wiki, excluding archive/VCS/tool directories."""
    files = []
    for path in sorted(root.rglob("*.md")):
        relparts = path.relative_to(root).parts
        if any(part in EXCLUDED_DIRS for part in relparts):
            continue
        files.append(path)
    return files


def relpath(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


# --------------------------------------------------------------------------
# Claim census (SPEC 5, 14)
# --------------------------------------------------------------------------


def census_claims(root: Path) -> dict:
    """Wiki-wide claim counts by confidence label, plus ``inferred`` counts
    by file -- ground truth for the digest (F9).

    Two of three test deployments' stakeholder-facing digests hand-wrote
    claim counts that turned out roughly 2x the real number, because no
    single reader was authoritative and three artifacts in one run each
    invented a different total. This is that single reader: it applies the
    exact claim shape lint's own claim-hygiene check validates (escaped
    pipes unescaped, table rows excluded unless they hold a real tag, only
    well-formed labels counted), so the census and lint's findings can never
    silently disagree about what counts as a claim.

    Canon only: ``intake/`` (a staging buffer, not-yet-promoted) and
    ``outbox/`` (sent artifacts, which may quote canon claims back) are
    excluded to avoid double-counting.
    """
    by_label = {label: 0 for label in CONFIDENCE_LABELS}
    inferred_by_file = {}
    for path in iter_md_files(root):
        rel = relpath(root, path)
        if rel.startswith("intake/") or rel.startswith("outbox/"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for line in visible_lines(text.splitlines()):
            in_table = is_table_row(line)
            for m in CLAIM_CANDIDATE_RE.finditer(unescape_pipes(line)):
                split = split_claim_candidate(m.group(1))
                if split is None:
                    continue
                label, prov, dstr, _internal = split
                if label not in CONFIDENCE_LABELS or not looks_like_claim_tag(label, prov, dstr):
                    continue  # malformed or decorative -- lint reports the former separately
                if in_table:
                    continue  # SPEC 4.2: never a real claim tag in a table cell
                by_label[label] += 1
                if label == "inferred":
                    inferred_by_file[rel] = inferred_by_file.get(rel, 0) + 1
    return {
        "by_label": dict(by_label),
        "total": sum(by_label.values()),
        "inferred_by_file": dict(sorted(inferred_by_file.items())),
    }


def count_contested_entries(text: str) -> int:
    """How many contested *entries* one file's ``## Contested`` section
    holds (SPEC 4.3): ``###``-level sub-entries if present, else 1 if the
    flat section carries any claim-tagged bullet, else 0 (including when
    the section is absent or empty-by-decision).

    Shared ground truth for the digest's contested count (F9) -- previously
    a changelog keyword match on the word "contested" that false-fired on
    any bullet merely discussing a contested count, including one reporting
    it had reached zero.
    """
    lines = text.splitlines()
    sections = parse_sections(lines)
    contested = next((h for h in sections if h["level"] == 2 and h["slug"] == "contested"), None)
    if contested is None:
        return 0
    sub_entries = [h for h in sections
                   if h["level"] == 3 and contested["start"] < h["start"] < contested["end"]]
    if sub_entries:
        return len(sub_entries)
    visible = visible_lines(lines)
    body = "\n".join(visible[contested["start"] + 1:contested["end"]])
    return 1 if CLAIM_CANDIDATE_RE.search(body) else 0


# --------------------------------------------------------------------------
# Archive locators (SPEC 4.2, 11)
# --------------------------------------------------------------------------


def _json_walk_has_value(node, fragment: str, prefix: str, rest: str) -> bool:
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, (str, int, float)) and str(v) == fragment:
                return True
            if prefix and rest and k.lower() == prefix.lower() and str(v) == rest:
                return True
        return any(_json_walk_has_value(v, fragment, prefix, rest) for v in node.values())
    if isinstance(node, list):
        return any(_json_walk_has_value(item, fragment, prefix, rest) for item in node)
    return False


def _json_walk_has_index(node, n: int) -> bool:
    if isinstance(node, list):
        if 0 <= n < len(node):
            return True
        return any(_json_walk_has_index(item, n) for item in node)
    if isinstance(node, dict):
        return any(_json_walk_has_index(v, n) for v in node.values())
    return False


def resolve_archive_fragment(target: Path, fragment: str):
    """Best-effort SPEC 4.2 fragment resolution against an archived payload.

    Two conventions are attested for JSON: the fragment names a whole id
    value (``msg-5117`` against ``{"id": "msg-5117", ...}``), or a
    field-prefix plus a raw value (``ts-1755162000`` against ``{"ts":
    1755162000, ...}``, SPEC 4.2's own example) -- both are tried, walking
    every dict and list in the payload. ``#i-N`` addresses a zero-based
    array index anywhere in the structure. Line-oriented payloads (``.md``,
    ``.txt``, ``.csv``) resolve ``#L214`` / ``#L214-231`` against the
    payload's real line count.

    Returns ``True`` (resolved), ``False`` (a checkable format, and the
    fragment resolves to nothing -- SPEC 4.2: "a fragment that resolves to
    nothing is an error, not a warning"), or ``None`` (a format this
    function has no way to check -- HTML/PDF heading slugs and page
    numbers, or anything unreadable/malformed -- report as a warning
    rather than silence, so an auditor still knows to look by hand).
    """
    suffix = target.suffix.lower()
    try:
        raw = target.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if suffix == ".json":
        try:
            data = json.loads(raw)
        except ValueError:
            return None
        idx_m = INDEX_FRAGMENT_RE.match(fragment)
        if idx_m:
            return _json_walk_has_index(data, int(idx_m.group(1)))
        m = re.match(r"^([A-Za-z][A-Za-z0-9]*)-(.+)$", fragment)
        prefix, rest = (m.group(1), m.group(2)) if m else (None, None)
        return _json_walk_has_value(data, fragment, prefix, rest)
    if suffix in (".md", ".txt", ".csv"):
        m = LINE_FRAGMENT_RE.match(fragment)
        if not m:
            return None
        start = int(m.group(1))
        end = int(m.group(2)) if m.group(2) else start
        total = raw.count("\n") + (0 if raw.endswith("\n") else 1)
        return 1 <= start <= end <= total
    return None


# --------------------------------------------------------------------------
# sources.md manifest
# --------------------------------------------------------------------------


def parse_sources_manifest(text: str) -> list:
    """Parse the source blocks out of sources.md (SPEC 10).

    Each block starts at ``- id: <id>`` and absorbs the indented
    ``key: value`` lines that follow (including nested cursor fields, which
    flatten -- ``cursor.last-run`` lands as ``last-run``). Inline lists and
    dicts parse like front-matter values, so ``broken: {since: ..., error:
    ...}`` arrives as a dict. Each dict carries ``id``, the block's keys, and
    ``_line`` (the 1-based line of the ``- id:`` line).
    """
    sources = []
    current = None
    id_re = re.compile(r"^\s*-\s+id:\s*(.+)$")
    kv_re = re.compile(r"^\s+([A-Za-z0-9_-]+):\s*(.*)$")
    for lineno, line in enumerate(text.splitlines(), start=1):
        m = id_re.match(line)
        if m:
            current = {"id": _parse_scalar(_strip_inline_comment(m.group(1))), "_line": lineno}
            sources.append(current)
            continue
        if current is None:
            continue
        m = kv_re.match(line)
        if m:
            key = m.group(1)
            if key not in current:  # first occurrence wins (top-level over nested)
                current[key] = _parse_value(_strip_inline_comment(m.group(2)), lineno, [])
        elif line.strip() and not line.lstrip().startswith(("-", "`", "~", "#")):
            current = None  # dedent back to prose ends the block
    return sources


def archive_base(root: Path, source: dict) -> Path:
    """Archive directory for one source: default ``.archive/`` or its override."""
    override = (source or {}).get("archive", "default")
    if override in ("", "default", None):
        return root / ".archive"
    p = Path(override)
    return p if p.is_absolute() else root / p


# --------------------------------------------------------------------------
# changelog.md and open-questions.md (SPEC 12)
# --------------------------------------------------------------------------


@dataclass
class ChangelogEntry:
    date: date
    timestamp: str
    kind: str
    header: str  # everything after the timestamp
    bullets: list
    line: int


CHANGELOG_ENTRY_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})(\S*)\s*·\s*(.*)$")


def parse_changelog(text: str) -> list:
    """Parse changelog entries (newest first, per SPEC 12.2)."""
    entries = []
    current = None
    for lineno, line in enumerate(visible_lines(text.splitlines()), start=1):
        m = CHANGELOG_ENTRY_RE.match(line)
        if m:
            d = parse_iso_date(m.group(1))
            if d is None:
                current = None
                continue
            header = m.group(3).strip()
            kind = header.split("·")[0].strip() if header else ""
            current = ChangelogEntry(
                date=d,
                timestamp=m.group(1) + m.group(2),
                kind=kind,
                header=header,
                bullets=[],
                line=lineno,
            )
            entries.append(current)
            continue
        if line.startswith("## "):
            current = None
            continue
        if current is not None and re.match(r"^-\s+\S", line):
            current.bullets.append(line[2:].strip())
    return entries


def parse_open_questions(text: str, section: str = None) -> list:
    """Entries from open-questions.md, in file order (SPEC 12.1).

    Returns dicts: ``{"title", "key", "state", "fields": {...}, "line"}``.
    ``state`` is the enclosing ``## `` heading's text (Active, Partially
    answered, Answered, Delegated, Stale, or a deployment's own wording).
    Pass ``section`` (matched case-insensitively as a prefix, so "active"
    matches "Active") to scope to one state; omit it to walk every state --
    ``stale-target`` (lint) needs every state, since a promised flag can go
    unwritten regardless of where the question ended up.
    """
    entries = []
    state = None
    current = None
    for lineno, line in enumerate(visible_lines(text.splitlines()), start=1):
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) == 2:
            state = m.group(2).strip()
            current = None
            continue
        in_scope = section is None or (state or "").lower().startswith(section.lower())
        if not in_scope:
            if m and len(m.group(1)) == 3:
                current = None
            continue
        if m and len(m.group(1)) == 3:
            title = m.group(2).strip()
            key_m = BLOCK_ANCHOR_RE.search(title)
            key = key_m.group(1) if key_m else ""
            title = re.sub(r"\s*\^[A-Za-z0-9-]+\s*$", "", title)
            current = {"title": title, "key": key, "state": state, "fields": {}, "line": lineno}
            entries.append(current)
            continue
        if current is not None:
            fm = re.match(r"^-\s+([A-Za-z0-9_-]+):\s*(.*)$", line)
            if fm:
                current["fields"][fm.group(1)] = fm.group(2).strip()
    return entries


def parse_open_questions_active(text: str) -> list:
    """Active entries only -- the drip-interview queue (SPEC 12.1)."""
    return parse_open_questions(text, section="active")


# --------------------------------------------------------------------------
# CLI plumbing
# --------------------------------------------------------------------------


def resolve_wiki_dir(arg: str):
    """Validate and resolve the wiki directory argument. Exits 1 if invalid."""
    root = Path(arg).resolve()
    if not root.is_dir():
        print(f"error: not a directory: {arg}", file=sys.stderr)
        sys.exit(1)
    return root
