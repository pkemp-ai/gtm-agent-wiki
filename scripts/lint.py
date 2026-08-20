#!/usr/bin/env python3
"""Deterministic lint for a GTM wiki -- SPEC 14's deterministic table.

No model judgment. Every check here is a mechanical rule an agent should
never be trusted to remember; the lint playbook's second half (contradiction
sweeps, doctrine drift) is model work and lives outside this script.

Usage:
    lint.py WIKI_DIR [--json] [--today YYYY-MM-DD] [--contested-threshold N]

Checks (check name -> rule):
    system-files        AGENTS.md, sources.md, changelog.md, open-questions.md exist
    front-matter        front matter present, parses within the documented
                        subset, carries the required fields, declares a valid
                        tier; references/ pages declare type: reference; a
                        file containing an !internal claim declares
                        read-restriction: (SPEC 4.2)
    staleness           evidence-as-of (falling back to last-verified when
                        evidence-as-of is empty or absent) older than
                        staleness-horizon -- never last-verified when
                        evidence-as-of is present (SPEC 4.1); horizons parse
                        as '<n>d', 'rolling' is skipped; empty last-verified
                        is "never" and short-circuits the comparison
    runbook-decay       'verified: <date>' execution stamps older than the
                        file's horizon (SPEC 14: schedule an execution check);
                        per file, 'unverified:' entries counted against zero
                        'verified:' stamps, so a wiki with no execution
                        evidence at all no longer passes silently (SPEC 8 note 3)
    claim-hygiene       claim tags match [label | provenance | YYYY-MM-DD],
                        optionally ' !internal'; label is a spec confidence
                        label; provenance is source-id:locator; the date is a
                        real, non-future date; a table row's pipes are never
                        split into a claim -- a well-formed tag found in one
                        anyway is flagged as belonging in a trailing
                        provenance column instead (SPEC 4.2, F15)
    doctrine-provenance every claim in a type: doctrine file cites interview:
                        or doc: (SPEC 4.2's human-originated, non-manifest
                        prefixes), or sits inside one of SPEC 17.3's three
                        exceptions: a ## Contested section, a
                        taxonomy-designated evidence section, or a
                        <!-- tier: --> marked section
    anchor-mid-line     a ^topic-key token that is not the last token on its
                        line -- SPEC 4.2's anchor rule, checked at the
                        mistake's own location instead of surfacing as a
                        broken-link warning three files away
    untagged-anchor     a trailing ^topic-key with no claim tag on its line or
                        the paragraph above it (heading anchors exempt --
                        those are navigational, not claims)
    sources-manifest    front-matter sources: entries resolve to manifest ids;
                        claim-tag source-ids resolve to manifest ids (error for
                        source-backed claims, warning otherwise)
    feeds-consistency   sources.md feeds: and a file's own front-matter
                        sources: are two halves of one edge (SPEC 10) --
                        flagged in both directions: a source's feeds: naming
                        a file whose sources: doesn't name it back, and a
                        file's sources: naming a source whose feeds: doesn't
                        include it
    provenance-archive  provenance locators that point into the archive
                        (locator contains '/') resolve to a real file, checked
                        only when the source's archive directory exists; a
                        present #fragment is then resolved against the
                        payload for JSON (an id/ts value or #i-N index) and
                        line-oriented text (#L214 / #L214-231) -- resolving to
                        nothing is an error, a format this can't check (HTML,
                        PDF) is a warning (SPEC 4.2, 11)
    stale-target        an Active/Partially-answered/etc. open question's
                        target: names a file with no reference to that
                        question's ^oq-id anywhere in it -- a flag promised
                        and never written (SPEC 14)
    manifest-health     every source declares access and a cursor; sources
                        marked broken: and cursors stalled past 2x cadence
                        are surfaced for the digest (SPEC 10, 14)
    broken-link         internal markdown links resolve to a file; a
                        wiki-internal link's anchor resolving to nothing --
                        same-file '#frag' or a cross-file 'file.md#frag' --
                        is an error, not a warning (SPEC 4.4)
    orphan              pages with no inbound links (AGENTS.md, system files,
                        intake/, and outbox/ are exempt -- SPEC 3)
    contested           contested entries link to a specific open question
    contested-backlog   total contested entries above --contested-threshold,
                        which defaults to scaling with wiki size (one entry
                        per ~15 claims, floor 10) rather than a flat number,
                        so an honest first build does not fail by construction
                        (F22r); pass --contested-threshold to pin an exact value
    top-level-growth    a top-level file outside the canonical taxonomy has no
                        taxonomy entry in AGENTS.md (SPEC 3)
    size-cap            doctrine files > 250 lines, any canonical file > 400
                        lines, any section > 150 lines (warnings, per SPEC 13)
    secrets             known credential formats (AWS, sk-, ghp_, xox*, PEM)
                        and assignment-of-a-long-random-string (SPEC 15.3),
                        swept over both the readable wiki and every payload
                        under .archive/ -- the archive is part of the wiki
                        tree and part of the sweep (SPEC 11, 15.3); a hit
                        inside .archive/ also reports whether that run's
                        manifest.yaml records any masking

Severity rules. **Errors are structural**: something the spec requires is
missing, malformed, or points at nothing -- a defect no amount of context
excuses. **Warnings are scheduling and judgment signals** the lint playbook
triages into fixes, open questions, or digest escalations: staleness, runbook
decay, broken sources, stalled cursors, a contested backlog over threshold,
size caps, an untagged anchor, an archive fragment in a format this script
cannot mechanically check.

Three consequences of that split, all of which a freshly copied
templates/wiki-skeleton depends on:

* Placeholder content is not a defect. Empty ``sources: []``, ``owner: TBD``,
  and a section whose only content is guidance prose all pass -- the checks
  fire on *declared* structure, not on prose. The contested check, for
  instance, fires on a contested entry (a '### ' block, or claim-tagged
  bullets), never on an empty ``## Contested`` section.
* HTML comments and fenced blocks are inert (see wikilib.visible_lines).
  Template guidance may show claim tags, entry schemas, and example links
  without lint reading them as content. The one exception is a heading's own
  ``<!-- tier: -->`` marker, which doctrine-provenance and anything else
  scoped by ``wikilib.parse_sections`` reads from the raw line -- SPEC 6
  makes that comment structural, not decorative.
* A cursor that has never run (``last-run: null``) is not stalled, and a
  source with no computable cadence is not checked for staleness.

Exit codes: 0 = clean or warnings only; 1 = at least one error.
Warnings never fail the run.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import (  # noqa: E402
    ANCHOR_TOKEN_RE,
    BLOCK_ANCHOR_RE,
    CANONICAL_ORDER,
    CONFIDENCE_LABELS,
    DOCTRINE_ALLOWED_PREFIXES,
    ERROR,
    WARNING,
    CLAIM_CANDIDATE_RE,
    DATE_RE,
    HEADING_RE,
    LINK_RE,
    NON_MANIFEST_PROVENANCE,
    PROVENANCE_RE,
    REQUIRED_FIELDS,
    SYSTEM_BASENAMES,
    TIERS,
    UNVERIFIED_STAMP_RE,
    VERIFIED_STAMP_RE,
    Finding,
    archive_base,
    collect_anchors,
    doctrine_exempt,
    emit_findings,
    is_table_row,
    iter_md_files,
    looks_like_claim_tag,
    parse_cadence,
    parse_front_matter,
    parse_horizon,
    parse_iso_date,
    parse_open_questions,
    parse_sections,
    parse_sources_manifest,
    parse_timestamp_date,
    relpath,
    resolve_archive_fragment,
    resolve_wiki_dir,
    split_claim_candidate,
    unescape_pipes,
    visible_lines,
)

SECRET_PATTERNS = (
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("secret API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("GitHub token", re.compile(r"\bghp_[A-Za-z0-9]{36}\b")),
    ("Slack token", re.compile(r"\bxox[A-Za-z]-[A-Za-z0-9-]{10,}\b")),
    ("private key block", re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----")),
)
#: keyword = long-random-string -- the heuristic half of SPEC 15.3.
SECRET_ASSIGNMENT_RE = re.compile(
    r"(?i)\b(api[_-]?key|apikey|secret|token|passwd|password|credential)s?\b"
    r"\s*[:=]\s*[\"']?([A-Za-z0-9+/=_-]{24,})[\"']?"
)
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*://|^mailto:")
#: Contested entries wiki-wide above this count escalate in the digest
#: (SPEC 14, "backlog above threshold"). This is a *floor*, not the default:
#: an honest first build routinely clears ten real collisions (F22r), so the
#: effective threshold scales with wiki size unless --contested-threshold
#: pins an exact value (see Linter.effective_contested_threshold).
DEFAULT_CONTESTED_THRESHOLD = 10
#: One contested entry is unremarkable per this many total claims; below
#: that density the floor above still applies. Chosen so a build-sized wiki
#: (roughly 250-350 claims, per the corpus) scales to a threshold in the
#: high teens rather than firing on every first build.
CONTESTED_CLAIMS_PER_ENTRY = 15
#: A file containing an !internal claim must declare this (SPEC 4.2).
READ_RESTRICTION_INTERNAL = "internal-only"
INVENTORY_BLOCK_RE = re.compile(
    r"<!--\s*INVENTORY:START\s*-->.*?<!--\s*INVENTORY:END\s*-->", re.DOTALL
)


class Linter:
    def __init__(self, root: Path, today: date, contested_threshold: int = None):
        self.root = root
        self.today = today
        #: None means "scale with wiki size" (see effective_contested_threshold);
        #: an explicit --contested-threshold pins an exact value instead.
        self.contested_threshold_override = contested_threshold
        self.findings = []
        self.manifest = None  # list of source dicts, or None if sources.md missing
        self.manifest_ids = None  # set of ids, or None
        self.inbound = {}  # resolved Path -> set of linking relpaths
        self.contested_entries = 0  # wiki-wide count, for the backlog threshold
        self.total_claims = 0  # wiki-wide well-formed claim count, for scaling it
        self.file_sources = {}  # rel (root-canonical .md) -> set(front-matter sources:)
        self._anchor_cache = {}

    # -- helpers ----------------------------------------------------------

    def add(self, file, line, severity, check, message):
        self.findings.append(Finding(file, line, severity, check, message))

    def anchors_for(self, path: Path) -> set:
        if path not in self._anchor_cache:
            try:
                self._anchor_cache[path] = collect_anchors(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError):
                self._anchor_cache[path] = set()
        return self._anchor_cache[path]

    def is_exempt_surface(self, rel: str) -> bool:
        """System files (fixed formats) and outbox/ (sent artifacts, not
        canon -- SPEC 3): exempt from front matter and orphan checks."""
        return (rel in SYSTEM_BASENAMES or rel.startswith("intake/")
                or rel.startswith("outbox/"))

    def front_matter_required(self, rel: str) -> bool:
        if rel == "AGENTS.md" or self.is_exempt_surface(rel):
            return False
        if rel.startswith("references/"):
            return True
        return "/" not in rel  # every other top-level .md is canonical

    def is_root_canonical(self, rel: str) -> bool:
        return "/" not in rel and rel != "AGENTS.md" and rel not in SYSTEM_BASENAMES

    def effective_contested_threshold(self) -> int:
        """F22r: an honest first build routinely clears a flat threshold of
        ten, so the default scales with wiki size instead of firing on every
        build. An explicit --contested-threshold always wins."""
        if self.contested_threshold_override is not None:
            return self.contested_threshold_override
        return max(DEFAULT_CONTESTED_THRESHOLD, self.total_claims // CONTESTED_CLAIMS_PER_ENTRY)

    # -- whole-wiki checks --------------------------------------------------

    def check_system_files(self):
        for name in ("AGENTS.md",) + tuple(SYSTEM_BASENAMES):
            if not (self.root / name).is_file():
                self.add(name, 0, ERROR, "system-files", "required system file is missing")

    def load_manifest(self):
        path = self.root / "sources.md"
        if not path.is_file():
            return  # already an error from check_system-files
        self.manifest = parse_sources_manifest(path.read_text(encoding="utf-8"))
        self.manifest_ids = {s["id"] for s in self.manifest if s.get("id")}
        if not self.manifest_ids:
            self.add("sources.md", 1, ERROR, "sources-manifest",
                     "no source blocks found (expected at least one '- id: <source>' block)")

    def check_manifest_health(self):
        """SPEC 10 / 14: access declared, cursor present, breakage surfaced."""
        if not self.manifest:
            return
        for source in self.manifest:
            sid = source.get("id") or "<unnamed>"
            line = source.get("_line", 1)
            if not str(source.get("access") or "").strip():
                self.add("sources.md", line, ERROR, "manifest-health",
                         f"source {sid!r} declares no access -- every source states how "
                         "this deployment reaches it (SPEC 17.4)")
            if "last-run" not in source:
                self.add("sources.md", line, ERROR, "manifest-health",
                         f"source {sid!r} has no cursor.last-run -- freshness has no "
                         "mechanism without one (SPEC 10, 17.4)")
            broken = source.get("broken")
            if broken:
                since = broken.get("since", "?") if isinstance(broken, dict) else "?"
                self.add("sources.md", line, WARNING, "manifest-health",
                         f"source {sid!r} is marked broken since {since} -- surface it in "
                         "the digest; the cursor is held on purpose (SPEC 10)")
                continue  # a held cursor on a broken source is correct, not stalled
            last_run = parse_timestamp_date(source.get("last-run"))
            cadence_days = parse_cadence(source.get("cadence"))
            if last_run is None or cadence_days is None:
                continue  # never run, or human-paced: nothing to compute
            if last_run > self.today:
                self.add("sources.md", line, ERROR, "manifest-health",
                         f"source {sid!r} cursor last-run is in the future")
                continue
            age = (self.today - last_run).days
            if age > 2 * cadence_days:
                self.add("sources.md", line, WARNING, "manifest-health",
                         f"source {sid!r} cursor has not advanced in {age} days "
                         f"(2x its {source.get('cadence')} cadence is {2 * cadence_days}) -- "
                         "either the pull is failing silently or the source needs a "
                         "broken: marker (SPEC 10)")

    def check_contested_backlog(self):
        threshold = self.effective_contested_threshold()
        if self.contested_entries > threshold:
            scaling_note = (f" ({self.total_claims} claims wiki-wide, ~1 per "
                             f"{CONTESTED_CLAIMS_PER_ENTRY} is unremarkable)"
                             if self.contested_threshold_override is None else "")
            self.add("open-questions.md", 1, WARNING, "contested-backlog",
                     f"{self.contested_entries} contested entries wiki-wide, above the "
                     f"threshold of {threshold}{scaling_note} -- escalate in the digest "
                     "(SPEC 14); each one is an unresolved question a consumer must "
                     "surface both sides of")

    def check_top_level_growth(self, files):
        """SPEC 3: the canonical top level does not grow -- depth goes to references/."""
        agents = self.root / "AGENTS.md"
        if not agents.is_file():
            return
        # The inventory table is machine-generated, so a row in it is not a
        # taxonomy entry. Only hand-written prose counts as one.
        prose = INVENTORY_BLOCK_RE.sub("", agents.read_text(encoding="utf-8"))
        for path in files:
            rel = relpath(self.root, path)
            if "/" in rel or rel == "AGENTS.md" or rel in CANONICAL_ORDER:
                continue
            if rel not in prose:
                self.add(rel, 1, ERROR, "top-level-growth",
                         "top-level file outside the canonical taxonomy with no taxonomy "
                         "entry in AGENTS.md -- add one under deployment notes, or move "
                         "the page into references/ (SPEC 3)")

    def check_orphans(self, files):
        for path in files:
            rel = relpath(self.root, path)
            if rel == "AGENTS.md" or self.is_exempt_surface(rel):
                continue
            if not self.inbound.get(path.resolve()):
                self.add(rel, 1, ERROR, "orphan",
                         "no inbound links from any other wiki page (SPEC 4.4)")

    def check_feeds_consistency(self):
        """SPEC 10: a source's feeds: and a file's own sources: are two
        halves of one edge. Flagged in both directions -- this was the
        silent gate that shipped a stale price and blocked a CEO ruling in
        the end-to-end test, because nothing reconciled the two lists."""
        if not self.manifest:
            return
        for rel, sids in self.file_sources.items():
            stem = rel[:-3] if rel.endswith(".md") else rel
            for sid in sids:
                source = next((s for s in self.manifest if s.get("id") == sid), None)
                if source is None:
                    continue  # sources-manifest already reports the unknown id
                feeds = source.get("feeds")
                feeds = set(feeds) if isinstance(feeds, list) else set()
                if stem not in feeds:
                    self.add(rel, 1, ERROR, "feeds-consistency",
                             f"front matter names {sid!r} as a source, but {sid}'s feeds: "
                             f"list in sources.md does not include {stem!r} (SPEC 10)")
        for source in self.manifest:
            sid = source.get("id") or "<unnamed>"
            line = source.get("_line", 1)
            feeds = source.get("feeds")
            if not isinstance(feeds, list):
                continue
            for stem in feeds:
                target_rel = f"{stem}.md"
                sids = self.file_sources.get(target_rel)
                if sids is None:
                    self.add("sources.md", line, ERROR, "feeds-consistency",
                             f"source {sid!r} feeds {stem!r}, but {target_rel} was not "
                             "found or declares no front-matter sources: at all (SPEC 10)")
                elif sid not in sids:
                    self.add("sources.md", line, ERROR, "feeds-consistency",
                             f"source {sid!r} feeds {stem!r}, but {target_rel}'s "
                             f"front-matter sources: does not list {sid!r} (SPEC 10)")

    def check_stale_target(self):
        """F18/SPEC 14: an open question's target: is a write obligation.
        If the flag or the correction was actually written, the target file
        carries some reference to the question's own id -- resolving that
        is cheaper than trusting the maintainer's memory that it happened.
        """
        path = self.root / "open-questions.md"
        if not path.is_file():
            return
        entries = parse_open_questions(path.read_text(encoding="utf-8"))
        for entry in entries:
            oq_id = entry["key"]
            target_field = entry["fields"].get("target")
            if not oq_id or not target_field:
                continue
            for target in target_field.split(","):
                fname = target.strip().split("#", 1)[0].strip()
                if not fname:
                    continue
                target_path = (self.root / fname).resolve()
                if not target_path.is_file():
                    continue  # broken-link (or a bad path) is reported elsewhere
                try:
                    body = target_path.read_text(encoding="utf-8")
                except (OSError, UnicodeDecodeError):
                    continue
                if oq_id not in body:
                    self.add("open-questions.md", entry["line"], ERROR, "stale-target",
                             f"{entry['title']!r} (^{oq_id}) names target {fname!r}, but "
                             f"that file contains no reference to {oq_id!r} -- a flag was "
                             "promised and never written (SPEC 14)")

    def check_runbook_entries(self, rel: str, visible: list):
        """SPEC 8 note 3 / 14: count unverified: entries against verified:
        stamps, per file, so a runbook with execution evidence for nothing
        at all stops passing silently. ``unverified`` is legitimate on its
        own -- the escalation is specifically zero verified entries next to
        one or more unverified ones."""
        verified = sum(1 for line in visible for _ in VERIFIED_STAMP_RE.finditer(line))
        unverified = sum(1 for line in visible for _ in UNVERIFIED_STAMP_RE.finditer(line))
        if unverified and not verified:
            self.add(rel, 1, WARNING, "runbook-decay",
                     f"{unverified} unverified: entr{'y' if unverified == 1 else 'ies'} and "
                     "zero verified: stamps in this file -- schedule an access check; a "
                     "runbook with no execution evidence at all must not pass silently "
                     "(SPEC 8 note 3)")

    def check_archive_secrets(self):
        """SPEC 11/15.3: the archive is part of the wiki tree and part of
        the secret sweep -- a mandate-to-archive-raw that only greps the
        readable files points away from where a leaked key actually is."""
        archive = self.root / ".archive"
        if not archive.is_dir():
            return
        for path in sorted(archive.rglob("*")):
            if not path.is_file():
                continue
            rel = relpath(self.root, path)
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue  # a binary payload (image, PDF): nothing to scan as text
            note = self._archive_masking_note(path.parent)
            for lineno, line in enumerate(text.splitlines(), start=1):
                found = next((name for name, pattern in SECRET_PATTERNS if pattern.search(line)), None)
                if found is None:
                    m = SECRET_ASSIGNMENT_RE.search(line)
                    if m and re.search(r"[A-Za-z]", m.group(2)) and re.search(r"\d", m.group(2)):
                        found = f"{m.group(1)} assignment"
                if found:
                    self.add(rel, lineno, ERROR, "secrets",
                             f"possible {found} inside an archived payload{note} -- a "
                             "fetched export containing a credential must be masked before "
                             "archiving, with the masking recorded in the run manifest "
                             "(SPEC 11, 15.3)")

    def _archive_masking_note(self, run_dir: Path) -> str:
        manifest = run_dir / "manifest.yaml"
        if not manifest.is_file():
            return "; this run has no manifest.yaml to record masking"
        try:
            text = manifest.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return ""
        m = re.search(r"(?m)^masked:\s*(.*)$", text)
        if not m or not m.group(1).strip() or m.group(1).strip().lower() in ("[]", "none", "null", "~"):
            return "; this run's manifest.yaml records no masking"
        return "; this run's manifest.yaml claims masking, but this value is still verbatim"

    # -- per-file checks ----------------------------------------------------

    def lint_file(self, path: Path):
        rel = relpath(self.root, path)
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            self.add(rel, 0, ERROR, "front-matter", f"unreadable file: {exc}")
            return
        lines = text.splitlines()
        # Code fences and HTML comments are inert: they quote formats and hold
        # authoring notes, so no check reads them as wiki content -- except a
        # heading's own <!-- tier: --> marker, which parse_sections reads from
        # the raw line (SPEC 6).
        visible = visible_lines(lines)
        sections = parse_sections(lines)
        has_internal_claim = "!internal" in "\n".join(visible)

        fm = parse_front_matter(text)
        body_start = fm.end_line if fm.closed else 0
        is_doctrine = fm.present and fm.closed and fm.data.get("type") == "doctrine"

        if self.front_matter_required(rel):
            self.check_front_matter(rel, fm, has_internal_claim)
            self.check_staleness(rel, fm)
            self.check_sources_field(rel, fm)
            self.check_section_size(rel, visible)
        if self.is_root_canonical(rel):
            self.check_size(rel, fm, len(lines))

        for lineno, line in enumerate(visible, start=1):
            if lineno <= body_start or not line.strip():
                continue
            self.check_claims(rel, lineno, line, is_doctrine, sections)
            self.check_links(path, rel, lineno, line)
            self.check_runbook_decay(rel, lineno, line, fm)
            self.check_anchor_mid_line(rel, lineno, line)

        if not (rel == "AGENTS.md" or self.is_exempt_surface(rel)):
            self.check_contested(rel, visible)
            self.check_untagged_anchor(rel, visible)

        self.check_runbook_entries(rel, visible)
        self.check_secrets(rel, lines)

    def check_front_matter(self, rel: str, fm, has_internal_claim: bool = False):
        if not fm.present:
            self.add(rel, 1, ERROR, "front-matter", "missing front matter (SPEC 4.1)")
            return
        for lineno, msg in fm.errors:
            self.add(rel, lineno, ERROR, "front-matter", msg)
        if not fm.closed:
            return
        missing = [f for f in REQUIRED_FIELDS if f not in fm.data]
        if missing:
            self.add(rel, 1, ERROR, "front-matter",
                     "missing required field(s): " + ", ".join(missing))
        tier = fm.data.get("type")
        if tier is not None and tier not in TIERS:
            self.add(rel, 1, ERROR, "front-matter",
                     f"invalid tier {tier!r} (expected one of: {', '.join(TIERS)})")
        if rel.startswith("references/") and tier is not None and tier != "reference":
            self.add(rel, 1, ERROR, "front-matter",
                     "pages under references/ must declare type: reference (taxonomy)")
        if "sources" in fm.data and not isinstance(fm.data["sources"], list):
            self.add(rel, 1, ERROR, "front-matter",
                     "sources: must be an inline list, e.g. sources: [crm, slack-gtm]")
        if has_internal_claim and not str(fm.data.get("read-restriction") or "").strip():
            self.add(rel, 1, ERROR, "front-matter",
                     "file contains an !internal claim but declares no read-restriction: "
                     f"in front matter (expected e.g. read-restriction: {READ_RESTRICTION_INTERNAL} "
                     "-- SPEC 4.2)")

    def check_staleness(self, rel: str, fm):
        if not (fm.present and fm.closed):
            return
        hz_raw = fm.data.get("staleness-horizon")
        ea_raw = fm.data.get("evidence-as-of")
        lv_raw = fm.data.get("last-verified")
        # evidence-as-of is about the content, last-verified about attention
        # (SPEC 4.1): staleness always prefers the former when it is set, and
        # only falls back to the latter -- with its documented empty-means-
        # never short circuit intact -- while deployments migrate to it.
        if ea_raw:
            basis_raw, basis_field = ea_raw, "evidence-as-of"
        else:
            basis_raw, basis_field = lv_raw, "last-verified"
        if not basis_raw or not hz_raw:
            return  # missing/empty fields already reported, or documented "never"
        kind, days = parse_horizon(hz_raw)
        if kind == "rolling":
            return  # capped logs age out by windowing, not by horizon
        if kind is None:
            self.add(rel, 1, WARNING, "staleness",
                     f"unparseable staleness-horizon {hz_raw!r} (expected e.g. 90d, or rolling)")
            return
        basis = parse_iso_date(basis_raw)
        if basis is None:
            self.add(rel, 1, ERROR, "front-matter",
                     f"{basis_field} {basis_raw!r} is not a YYYY-MM-DD date")
            return
        if basis > self.today:
            self.add(rel, 1, ERROR, "front-matter", f"{basis_field} {basis_raw} is in the future")
            return
        overdue = (self.today - basis).days - days
        if overdue > 0:
            fallback_note = "" if basis_field == "evidence-as-of" else \
                " (no evidence-as-of set -- falling back to last-verified, SPEC 4.1)"
            self.add(rel, 1, WARNING, "staleness",
                     f"{basis_field} {basis_raw} is {overdue} day(s) past the {days}d "
                     f"horizon{fallback_note}")

    def check_runbook_decay(self, rel: str, lineno: int, line: str, fm):
        """SPEC 14: a runbook entry unverified past horizon needs re-execution.

        Keyed on the ``verified: <date>`` stamps SPEC 8 note 3 mandates, so it
        covers runbook files and the runbook sections state files carry (e.g.
        pipeline.md's 'How to source'), measured against the file's own horizon.
        """
        kind, days = parse_horizon(fm.data.get("staleness-horizon"))
        if kind != "days":
            return  # rolling or unset: the staleness check already reports it
        for m in VERIFIED_STAMP_RE.finditer(line):
            stamp = parse_iso_date(m.group(1))
            if stamp is None:
                continue
            if stamp > self.today:
                self.add(rel, lineno, ERROR, "runbook-decay",
                         f"verified stamp {m.group(1)} is in the future -- stamps record "
                         "an execution that happened")
                continue
            overdue = (self.today - stamp).days - days
            if overdue > 0:
                self.add(rel, lineno, WARNING, "runbook-decay",
                         f"verified: {m.group(1)} is {overdue} day(s) past the {days}d "
                         "horizon -- re-execute the entry; a failure marks it broken, "
                         "never deleted (SPEC 8)")

    def check_sources_field(self, rel: str, fm):
        if self.manifest_ids is None or not fm.closed:
            return
        sources = fm.data.get("sources")
        if not isinstance(sources, list):
            return
        for sid in sources:
            if sid not in self.manifest_ids:
                self.add(rel, 1, ERROR, "sources-manifest",
                         f"front-matter source {sid!r} is not declared in sources.md")
        if self.is_root_canonical(rel):
            self.file_sources[rel] = set(sources)

    def check_claims(self, rel: str, lineno: int, line: str, is_doctrine: bool, sections: list):
        in_table = is_table_row(line)
        for m in CLAIM_CANDIDATE_RE.finditer(unescape_pipes(line)):
            split = split_claim_candidate(m.group(1))
            if split is None:
                if in_table:
                    continue  # table syntax (cell-boundary pipes), not a mis-shaped
                              # claim -- SPEC 4.2's row convention has no brackets at all
                parts = [p.strip() for p in m.group(1).split("|")]
                # Only flag when it plausibly meant to be a claim tag.
                if parts[0] in CONFIDENCE_LABELS or DATE_RE.match(parts[-1]):
                    self.add(rel, lineno, ERROR, "claim-hygiene",
                             f"malformed claim tag {m.group(0)!r} "
                             "(expected [label | provenance | YYYY-MM-DD])")
                continue
            label, prov, dstr, _internal = split
            if not looks_like_claim_tag(label, prov, dstr):
                continue
            if in_table:
                self.add(rel, lineno, ERROR, "claim-hygiene",
                         f"claim tag {m.group(0)!r} inside a table cell -- a tag's pipes "
                         "collide with the table's own column syntax; use a trailing "
                         "`provenance` + `as-of` column instead (SPEC 4.2)")
                continue
            self.total_claims += 1
            if label not in CONFIDENCE_LABELS:
                self.add(rel, lineno, ERROR, "claim-hygiene",
                         f"unknown confidence label {label!r} "
                         f"(expected one of: {', '.join(CONFIDENCE_LABELS)})")
            pm = PROVENANCE_RE.match(prov)
            if not pm:
                self.add(rel, lineno, ERROR, "claim-hygiene",
                         f"malformed provenance {prov!r} (expected source-id:locator)")
            else:
                self.check_provenance(rel, lineno, label, pm.group(1), pm.group(2))
                self.check_doctrine_provenance(rel, lineno, pm.group(1), is_doctrine, sections)
            d = parse_iso_date(dstr)
            if d is None:
                self.add(rel, lineno, ERROR, "claim-hygiene",
                         f"invalid claim date {dstr!r} (expected a real YYYY-MM-DD date)")
            elif d > self.today:
                self.add(rel, lineno, ERROR, "claim-hygiene",
                         f"claim date {dstr} is in the future (dates record evidence capture)")
            elif d.year < 2000:
                self.add(rel, lineno, ERROR, "claim-hygiene",
                         f"claim date {dstr} fails sanity (before 2000)")

    def check_doctrine_provenance(self, rel: str, lineno: int, sid: str,
                                   is_doctrine: bool, sections: list):
        """SPEC 17.3: a doctrine claim is H-class or it doesn't belong there.

        Mechanically, that means the provenance prefix is one of the two
        human-originated, non-manifest kinds (SPEC 4.2's ``interview:`` /
        ``doc:``), or the claim sits inside one of the three named
        exceptions. This is the only §17 conformance item that had no
        deterministic backing before, and all three test wikis shipped
        violating it while self-certifying they hadn't.
        """
        if not is_doctrine or sid in DOCTRINE_ALLOWED_PREFIXES:
            return
        if doctrine_exempt(rel, sections, lineno - 1):
            return
        self.add(rel, lineno, ERROR, "doctrine-provenance",
                 f"doctrine claim cites {sid!r}, not a human-originated prefix "
                 "(interview:/doc:) -- move it under `## Contested`, a "
                 "taxonomy-designated evidence section, or a `<!-- tier: -->`-marked "
                 "section, or re-source it to H-class evidence (SPEC 17.3)")

    def check_provenance(self, rel: str, lineno: int, label: str, sid: str, locator: str):
        if sid in NON_MANIFEST_PROVENANCE:
            return
        if self.manifest_ids is not None and sid not in self.manifest_ids:
            severity = ERROR if label == "source-backed" else WARNING
            self.add(rel, lineno, severity, "sources-manifest",
                     f"provenance source {sid!r} is not declared in sources.md")
            return
        if "/" not in locator:
            return  # a system locator (e.g. crm:report-q3), not an archive path
        source = next((s for s in self.manifest or [] if s.get("id") == sid), None)
        base = archive_base(self.root, source)
        if not base.is_dir():
            return  # archive absent or relocated out of reach: cannot check
        path_part, _, fragment = locator.partition("#")
        target = base / sid / path_part
        if not target.is_file():
            self.add(rel, lineno, ERROR, "provenance-archive",
                     f"provenance {sid}:{locator} does not resolve under "
                     f"{base.name}/{sid}/ (SPEC 11)")
            return
        if not fragment:
            return
        resolved = resolve_archive_fragment(target, fragment)
        if resolved is False:
            self.add(rel, lineno, ERROR, "provenance-archive",
                     f"fragment '#{fragment}' not found in {sid}:{path_part} (SPEC 4.2)")
        elif resolved is None:
            self.add(rel, lineno, WARNING, "provenance-archive",
                     f"fragment '#{fragment}' on {sid}:{path_part} is not a JSON id/index "
                     "or a line reference this script can check -- verify it resolves by "
                     "hand (SPEC 4.2)")

    def _has_real_claim_tag(self, line: str) -> bool:
        for m in CLAIM_CANDIDATE_RE.finditer(unescape_pipes(line)):
            split = split_claim_candidate(m.group(1))
            if split and looks_like_claim_tag(split[0], split[1], split[2]):
                return True
        return False

    def check_anchor_mid_line(self, rel: str, lineno: int, line: str):
        """SPEC 4.2: the topic key is the last token on its line, or it is
        not a link target at all -- and the failure otherwise surfaces as a
        broken-link warning three files away instead of here (F20).

        Scoped to lines that actually *define* an anchor under SPEC's own
        convention -- a claim tag (``[label | provenance | date] ^key``) or
        a heading (``## Section ^key``) -- so prose that merely mentions an
        existing topic key mid-sentence (a changelog narrating what an
        update touched, a doc's own inline-code syntax example) is never
        mistaken for a botched definition.
        """
        if not (HEADING_RE.match(line) or self._has_real_claim_tag(line)):
            return
        matches = list(ANCHOR_TOKEN_RE.finditer(line))
        if not matches:
            return
        trailing = BLOCK_ANCHOR_RE.search(line)
        trailing_start = trailing.start() if trailing else -1
        for m in matches:
            if m.start() != trailing_start:
                self.add(rel, lineno, ERROR, "anchor-mid-line",
                         f"{m.group(0)!r} is not the last token on its line, so it is not "
                         "a valid block anchor -- move it to end the line (SPEC 4.2)")

    def check_untagged_anchor(self, rel: str, visible: list):
        """A trailing ``^topic-key`` invites citation; if the paragraph it
        sits in carries no claim tag at all, an untagged assertion reads as
        more authoritative than it is (F22i). Heading anchors are exempt --
        those are navigational (a persona header, a contested entry's own
        title), not claims.
        """
        for i, line in enumerate(visible):
            if not BLOCK_ANCHOR_RE.search(line):
                continue
            if HEADING_RE.match(line):
                continue
            j = i
            tagged = False
            while j >= 0:
                if j != i and (not visible[j].strip() or HEADING_RE.match(visible[j])):
                    break
                if CLAIM_CANDIDATE_RE.search(visible[j]):
                    tagged = True
                    break
                j -= 1
            if not tagged:
                key = BLOCK_ANCHOR_RE.search(line).group(1)
                self.add(rel, i + 1, WARNING, "untagged-anchor",
                         f"^{key} has no claim tag on its line or the paragraph above it")

    def check_links(self, path: Path, rel: str, lineno: int, line: str):
        for m in LINK_RE.finditer(line):
            target = m.group(3)
            if SCHEME_RE.match(target):
                continue
            if target.startswith("#"):
                if target[1:] not in self.anchors_for(path):
                    self.add(rel, lineno, ERROR, "broken-link",
                             f"anchor {target!r} not found in this file (SPEC 4.4)")
                continue
            path_part, _, fragment = target.partition("#")
            resolved = (path.parent / path_part).resolve()
            if not resolved.exists():
                alt = (self.root / path_part).resolve()
                resolved = alt if alt.exists() else resolved
            if not resolved.exists():
                self.add(rel, lineno, ERROR, "broken-link",
                         f"link target {target!r} does not resolve to a file")
                continue
            if resolved.suffix == ".md" and resolved != path.resolve():
                self.inbound.setdefault(resolved, set()).add(rel)
            if fragment and resolved.suffix == ".md":
                if fragment not in self.anchors_for(resolved):
                    self.add(rel, lineno, ERROR, "broken-link",
                             f"anchor '#{fragment}' not found in {path_part} (SPEC 4.4)")

    def check_contested(self, rel: str, visible: list):
        """SPEC 4.3: every contested *entry* links to a specific open question.

        An entry is a '### ' block under '## Contested', or -- when a file keeps
        a flat section -- claim-tagged bullets. A section holding nothing but
        prose ("None currently", or a template's guidance) declares no entry, so
        there is nothing to link and nothing to report.
        """
        section_start = None
        for i, line in enumerate(visible):
            if re.match(r"^##\s+Contested\s*$", line, re.IGNORECASE):
                section_start = i
                break
        if section_start is None:
            return
        end = len(visible)
        for j in range(section_start + 1, len(visible)):
            if re.match(r"^##\s+", visible[j]):
                end = j
                break
        section = visible[section_start + 1:end]
        entry_starts = [k for k, line in enumerate(section) if re.match(r"^###\s+", line)]
        if entry_starts:
            bounds = entry_starts + [len(section)]
            for a, b in zip(bounds, bounds[1:]):
                self.contested_entries += 1
                if "open-questions.md#" not in "\n".join(section[a:b]):
                    self.add(rel, section_start + 2 + a, ERROR, "contested",
                             "contested entry links to no specific open question -- "
                             "expected a link to open-questions.md#<oq-id> (SPEC 4.3)")
            return
        body = "\n".join(section)
        if not CLAIM_CANDIDATE_RE.search(body):
            return  # prose only: no entries declared here
        self.contested_entries += 1
        if "open-questions.md#" not in body:
            self.add(rel, section_start + 1, ERROR, "contested",
                     "contested section carries claims but links to no specific open "
                     "question -- expected open-questions.md#<oq-id> (SPEC 4.3)")

    def check_size(self, rel: str, fm, line_count: int):
        if line_count > 400:
            self.add(rel, line_count, WARNING, "size-cap",
                     f"{line_count} lines > 400 -- fan detail out to references/ (SPEC 13)")
        elif fm.data.get("type") == "doctrine" and line_count > 250:
            self.add(rel, line_count, WARNING, "size-cap",
                     f"doctrine file is {line_count} lines > 250 -- doctrine is read whole "
                     "by every consumer (SPEC 13)")

    def check_section_size(self, rel: str, visible: list):
        """SPEC 13's fan-out rule: a section past one screen (~150 lines) moves
        to references/, with a summary and a link left behind."""
        starts = [i for i, line in enumerate(visible) if re.match(r"^##\s+", line)]
        for a, b in zip(starts, starts[1:] + [len(visible)]):
            length = b - a
            if length > 150:
                self.add(rel, a + 1, WARNING, "size-cap",
                         f"section {visible[a].strip()!r} is {length} lines > 150 -- past one "
                         "screen it earns a references/ page, with a summary and a link left "
                         "behind (SPEC 13)")

    def check_secrets(self, rel: str, lines: list):
        # Secrets are scanned everywhere, code fences included -- pasted
        # config blocks are exactly where keys leak (SPEC 15.3).
        for lineno, line in enumerate(lines, start=1):
            for name, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    self.add(rel, lineno, ERROR, "secrets",
                             f"possible {name} -- credentials belong in a vault or "
                             "env var, referenced by name (SPEC 15.3)")
            m = SECRET_ASSIGNMENT_RE.search(line)
            if m:
                value = m.group(2)
                if re.search(r"[A-Za-z]", value) and re.search(r"\d", value):
                    self.add(rel, lineno, ERROR, "secrets",
                             f"{m.group(1)} assigned a long random-looking string -- "
                             "reference credentials by env-var name, never value (SPEC 15.3)")

    # -- driver -------------------------------------------------------------

    def run(self) -> list:
        self.check_system_files()
        self.load_manifest()
        self.check_manifest_health()
        files = iter_md_files(self.root)
        for path in files:
            self.lint_file(path)
        self.check_orphans(files)
        self.check_top_level_growth(files)
        self.check_feeds_consistency()
        self.check_stale_target()
        self.check_archive_secrets()
        self.check_contested_backlog()
        return self.findings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("wiki_dir", help="path to the deployed wiki directory")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--today", metavar="YYYY-MM-DD", default=None,
                        help="override 'today' for reproducible staleness checks")
    parser.add_argument("--contested-threshold", type=int, metavar="N", default=None,
                        help="contested entries above N escalate in the digest; default "
                             "scales with wiki size instead of a flat number -- one entry "
                             f"per ~{CONTESTED_CLAIMS_PER_ENTRY} claims, floor "
                             f"{DEFAULT_CONTESTED_THRESHOLD} -- so an honest first build "
                             "does not fail by construction (F22r)")
    args = parser.parse_args(argv)

    root = resolve_wiki_dir(args.wiki_dir)
    today = date.today()
    if args.today:
        today = parse_iso_date(args.today)
        if today is None:
            print("error: --today must be YYYY-MM-DD", file=sys.stderr)
            return 1

    linter = Linter(root, today, contested_threshold=args.contested_threshold)
    findings = linter.run()
    files_checked = len(iter_md_files(root))
    return emit_findings(findings, args.json, extra={"files_checked": files_checked})


if __name__ == "__main__":
    sys.exit(main())
