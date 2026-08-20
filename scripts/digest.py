#!/usr/bin/env python3
"""Generate the periodic stakeholder digest from changelog.md.

The digest is the review-after loop that replaces approval gates (SPEC 8):
a stakeholder skims it, replies to the questions it surfaces, and those
replies come back through the interview playbook as H-class evidence. Claim
counts and contested/broken totals are read directly from the wiki files and
sources.md -- ground truth, never hand-written or inferred from changelog
prose (F9: two of three test deployments' stakeholder-facing digests
reported numbers roughly 2x the real ones because no single reader was
authoritative).

Usage:
    digest.py WIKI_DIR [--json] [--since YYYY-MM-DD] [--lint-report PATH]
                        [--audience internal|stakeholder] [--mark-sent]

Sections emitted:
    * Escalations -- the *newest* changelog entry's ``escalations:`` bullets
      only (SPEC 12.2 makes that line the digest pickup convention). Only
      the newest, not every entry in the window: an escalation restated run
      after run previously showed up once per run with no way to tell which
      copy was live (F9).
    * Changes by file -- changelog bullets grouped by the canonical file
      they touched, across every run in the window (no-ops included in the
      run count). A bullet may name several files (``a.md, b.md: ...``) and
      is then listed under each.
    * Claims on file -- the wiki-wide claim census by confidence label, plus
      ``inferred`` counts by file (``wikilib.census_claims`` -- the single
      source of these numbers, per F9).
    * Notable -- supersessions (still a changelog keyword match -- there is
      no structural record of a supersession event), contested entries (read
      from every file's own ``## Contested`` section, not a keyword match:
      the old classifier false-fired on a changelog line reporting the count
      had reached zero), and broken sources (read from sources.md's own
      ``broken:`` markers, not a keyword match on the word "broken").
    * Open questions -- the top 3 Active items from open-questions.md, in
      file order (the drip-interview queue, SPEC 12.1).
    * Lint escalations -- findings from a lint report, when one is passed via
      --lint-report (the --json output of lint.py, or a plain-text report).
      Omitted entirely for --audience=stakeholder: lint check names
      (``[doctrine-provenance]``, ``[claim-hygiene]``...) are unambiguously
      internal vocabulary.

--audience=stakeholder reorders the digest to lead with open questions (the
thing a stakeholder actually needs to act on) and strips internal vocabulary
that tested stakeholders named as their #1 driver of distrust in this
artifact: H/A/S/O/I-class markers, the ``source-backed``/``watchlist``
labels, ``^topic-key`` anchors, ``SPEC §n`` references, and playbook step
codes (``A5``, ``B4``...). --audience=internal (the default) is unchanged.

--mark-sent records this run's newest changelog date as ``last-digest-sent``
in ``.digest-state.json`` at the wiki root. A later run with no explicit
--since then defaults to since-last-sent instead of a flat 7-day window, so
digest-due-ness stops being inferred by eyeballing changelog prose (F9).

Exit codes: 0 = digest emitted; 1 = operational error (missing or empty
changelog, unreadable lint report, bad --since).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikilib import (  # noqa: E402
    ANCHOR_TOKEN_RE,
    CONFIDENCE_LABELS,
    census_claims,
    count_contested_entries,
    iter_md_files,
    parse_changelog,
    parse_iso_date,
    parse_open_questions_active,
    parse_sources_manifest,
    relpath,
    resolve_wiki_dir,
)

#: ``<file>.md: <what changed>``, or a comma-separated list of files sharing
#: one change line (``business-core.md, voice.md: doctrine ratified``).
FILE_BULLET_RE = re.compile(r"^((?:[\w./-]+\.md)(?:\s*,\s*[\w./-]+\.md)*):\s*(.*)$")
#: The digest pickup convention (SPEC 12.2).
ESCALATION_BULLET_RE = re.compile(r"^escalations?:\s*(.*)$", re.IGNORECASE)

#: Supersessions have no structural record to read instead -- a changelog
#: keyword match is still the best available signal for them. Contested and
#: broken-source counts are read from the wiki itself (see
#: collect_contested_summary / collect_broken_sources) precisely because the
#: keyword match on those two false-fired in the end-to-end test, including
#: on a changelog line reporting a count had reached zero (F9).
NOTABLE_RULES = (
    ("supersessions", re.compile(r"supersession|supersede", re.IGNORECASE)),
)
NOTABLE_TITLES = {
    "supersessions": "Supersessions",
}

#: Internal vocabulary stripped for --audience=stakeholder (F9): the
#: provenance-class markers, the two label words that read as pure jargon
#: (confirmed/inferred/contested are ordinary English and are left alone),
#: topic-key anchors, SPEC section references, and playbook step codes.
#: Step codes are deliberately [AB] only, not [A-H]: build.md's two phases
#: are the only ones the corpus uses, and widening to H collides with the
#: ordinary business abbreviation "H1"/"H2" (half-year).
STAKEHOLDER_STRIP_PATTERNS = (
    re.compile(r"\b[HASOI]-class\b"),
    re.compile(r"\b(source-backed|watchlist)\b", re.IGNORECASE),
    ANCHOR_TOKEN_RE,
    re.compile(r"\bSPEC\s*§?\s*\d+(?:\.\d+)*\b", re.IGNORECASE),
    re.compile(r"\b[AB]\d{1,2}\b"),
)


def strip_internal_vocabulary(text: str) -> str:
    """Remove the internal vocabulary --audience=stakeholder targets (F9),
    then tidy the punctuation and spacing stripping leaves behind. This is a
    strip, not a rewrite: a clause built around a now-removed "SPEC §17.3"
    or "A5" can still end on a dangling preposition, which the last pass
    below cleans up in the common case without attempting real grammar."""
    for pattern in STAKEHOLDER_STRIP_PATTERNS:
        text = pattern.sub("", text)
    text = re.sub(r"\(\s*\)", "", text)
    text = re.sub(r"\[\s*\]", "", text)
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\s+([,.;:)\]])", r"\1", text)
    text = re.sub(r"([(\[])\s+", r"\1", text)
    text = re.sub(r"[,;]\s*([).\]])", r"\1", text)
    text = re.sub(r"\s+(?:in|of|per|under|via)\s*$", "", text, flags=re.IGNORECASE)
    return text.strip()
#: Where digest.py persists last-digest-sent (F9) -- a dotfile at the wiki
#: root, plumbing rather than content, the way .archive/ is.
DIGEST_STATE_FILENAME = ".digest-state.json"


def load_lint_report(path: Path) -> dict:
    """Read a lint report: lint.py --json output, or plain text as fallback."""
    text = path.read_text(encoding="utf-8")
    try:
        data = json.loads(text)
    except ValueError:
        lines = [ln.strip() for ln in text.splitlines()
                 if " ERROR " in ln or " WARNING " in ln]
        return {"errors": sum(1 for ln in lines if " ERROR " in ln),
                "warnings": sum(1 for ln in lines if " WARNING " in ln),
                "items": lines}
    findings = data.get("findings", [])
    items = [
        f"{f.get('severity')} · {f.get('file')}:{f.get('line')}: "
        f"[{f.get('check')}] {f.get('message')}"
        for severity in ("error", "warning")
        for f in findings
        if f.get("severity") == severity
    ]
    return {"errors": data.get("errors", 0),
            "warnings": data.get("warnings"),
            "items": items}


def load_digest_state(root: Path) -> dict:
    """Read ``.digest-state.json`` (F9's last-digest-sent tracker), or {}."""
    path = root / DIGEST_STATE_FILENAME
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_digest_state(root: Path, state: dict) -> None:
    (root / DIGEST_STATE_FILENAME).write_text(
        json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def collect_contested_summary(root: Path) -> dict:
    """Current contested-entry count, read from every file's own
    ``## Contested`` section (ground truth) -- not a changelog keyword
    match, which false-fired on a bullet merely discussing the count,
    including one reporting it had reached zero (F9)."""
    by_file = {}
    for path in iter_md_files(root):
        rel = relpath(root, path)
        if rel.startswith("intake/") or rel.startswith("outbox/"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        n = count_contested_entries(text)
        if n:
            by_file[rel] = n
    return {"total": sum(by_file.values()), "by_file": dict(sorted(by_file.items()))}


def collect_broken_sources(root: Path) -> list:
    """Currently-broken sources, read from sources.md's own ``broken:``
    markers (ground truth) -- not a changelog keyword match on the word
    "broken", which the same false-firing problem afflicts (F9)."""
    path = root / "sources.md"
    if not path.is_file():
        return []
    out = []
    for s in parse_sources_manifest(path.read_text(encoding="utf-8")):
        broken = s.get("broken")
        if broken:
            since = broken.get("since", "?") if isinstance(broken, dict) else "?"
            error = broken.get("error", "") if isinstance(broken, dict) else ""
            out.append({"id": s.get("id", "?"), "since": since, "error": error})
    return out


def build_digest(root: Path, since, lint_report: dict = None, state: dict = None) -> dict:
    entries = parse_changelog((root / "changelog.md").read_text(encoding="utf-8"))
    if not entries:
        raise ValueError("changelog.md contains no parseable entries")

    newest = max(e.date for e in entries)
    state = state or {}
    if since is None:
        last_sent = parse_iso_date(state.get("last-digest-sent") or "")
        since = last_sent if last_sent is not None else newest - timedelta(days=7)
    window = [e for e in entries if e.date >= since]

    by_kind = {}
    changes_by_file = {}
    escalations = []  # only the newest entry that has any -- see loop below
    notable = {key: [] for key, _ in NOTABLE_RULES}
    for entry in window:
        by_kind[entry.kind or "run"] = by_kind.get(entry.kind or "run", 0) + 1
        entry_escalations = []
        for bullet in entry.bullets:
            esc = ESCALATION_BULLET_RE.match(bullet)
            if esc:
                if esc.group(1).strip():
                    entry_escalations.append(esc.group(1).strip())
                continue  # carried at the top; never also in Notable
            m = FILE_BULLET_RE.match(bullet)
            if m:
                names = [f.strip() for f in m.group(1).split(",")]
                for fname in names:
                    changes_by_file.setdefault(fname, []).append(
                        {"date": entry.date.isoformat(), "text": m.group(2),
                         "shared": len(names)}
                    )
            for key, pattern in NOTABLE_RULES:
                if pattern.search(bullet):
                    notable[key].append(
                        {"date": entry.date.isoformat(), "text": bullet}
                    )
        if entry_escalations and not escalations:
            # window is newest-first (SPEC 12.2); take the first (newest)
            # entry that has any and stop -- an older run's escalation line,
            # repeated verbatim run after run, previously showed up once per
            # run with no way to tell which copy was still live (F9).
            escalations = [{"date": entry.date.isoformat(), "text": t} for t in entry_escalations]

    oq_path = root / "open-questions.md"
    open_questions = []
    if oq_path.is_file():
        active = parse_open_questions_active(oq_path.read_text(encoding="utf-8"))
        for q in active[:3]:
            open_questions.append({
                "title": q["title"],
                "why": q["fields"].get("why-it-matters", ""),
                "target": q["fields"].get("target", ""),
            })

    return {
        "since": since.isoformat(),
        "until": newest.isoformat(),
        "runs": len(window),
        "by_kind": by_kind,
        "escalations": escalations,
        "changes_by_file": changes_by_file,
        "claim_census": census_claims(root),
        "contested": collect_contested_summary(root),
        "broken_sources": collect_broken_sources(root),
        "notable": notable,
        "open_questions": open_questions,
        "open_questions_file": oq_path.is_file(),
        "lint": lint_report,
        "last_digest_sent": state.get("last-digest-sent"),
    }


def _render_open_questions(d: dict, header: str) -> list:
    out = [f"## {header}", ""]
    if d["open_questions"]:
        for i, q in enumerate(d["open_questions"], start=1):
            out.append(f"{i}. **{q['title']}**")
            if q["why"]:
                out.append(f"   - why it matters: {q['why']}")
            if q["target"]:
                out.append(f"   - target: {q['target']}")
    elif not d["open_questions_file"]:
        out.append("open-questions.md is missing — that is a lint error.")
    else:
        out.append("No Active open questions. The backlog is clear.")
    out.append("")
    return out


def _render_escalations(d: dict, header: str) -> list:
    if not d["escalations"]:
        return []
    out = [f"## {header}", ""]
    for item in d["escalations"]:
        out.append(f"- {item['date']} · {item['text']}")
    out.append("")
    return out


def _render_changes_by_file(d: dict) -> list:
    out = ["## Changes by file", ""]
    if d["changes_by_file"]:
        for fname in sorted(d["changes_by_file"]):
            out.append(f"### {fname}")
            for change in d["changes_by_file"][fname]:
                shared = change.get("shared", 1)
                tag = f" (one change across {shared} files)" if shared > 1 else ""
                out.append(f"- {change['date']}{tag}: {change['text']}")
            out.append("")
    else:
        out.append("No file changes recorded in this window.")
        out.append("")
    return out


def _render_claims_internal(census: dict) -> list:
    out = ["## Claims on file", ""]
    by_label = census["by_label"]
    counts = " · ".join(f"{by_label[label]} {label}" for label in CONFIDENCE_LABELS)
    out.append(f"{census['total']} tagged claims: {counts}")
    out.append("")
    if census["inferred_by_file"]:
        parts = [f"{f} ({n})" for f, n in census["inferred_by_file"].items()]
        out.append("Inferred (unratified) claims by file: " + ", ".join(parts))
        out.append("")
    return out


def _render_claims_stakeholder(census: dict) -> list:
    by_label = census["by_label"]
    out = ["## What the wiki rests on", ""]
    total = census["total"]
    on_record = by_label["confirmed"] + by_label["source-backed"]
    clauses = []
    if on_record:
        clauses.append(f"{on_record} rest on your own word or on documents and records")
    if by_label["inferred"]:
        clauses.append(f"{by_label['inferred']} are the system's best guess, not yet confirmed")
    if by_label["contested"]:
        clauses.append(f"{by_label['contested']} are still disputed between two sources")
    if by_label["watchlist"]:
        clauses.append(f"{by_label['watchlist']} are an early, unconfirmed signal worth watching")
    sentence = f"{total} statements in total" if total else "No tagged statements yet"
    if clauses:
        sentence += ". " + "; ".join(clauses) + "."
    else:
        sentence += "."
    out.append(sentence)
    out.append("")
    if census["inferred_by_file"]:
        items = list(census["inferred_by_file"].items())
        shown = ", ".join(f"{f} ({n})" for f, n in items[:5])
        more = f", and {len(items) - 5} more" if len(items) > 5 else ""
        out.append(f"Guesses not yet confirmed, by file: {shown}{more}.")
        out.append("")
    return out


def _render_notable(d: dict, sanitize) -> list:
    out = ["## Notable", ""]
    any_notable = False
    for key in ("supersessions",):
        items = d["notable"].get(key, [])
        if not items:
            continue
        any_notable = True
        out.append(f"**{NOTABLE_TITLES[key]}**")
        for item in items:
            out.append(f"- {item['date']} · {sanitize(item['text'])}")
        out.append("")
    contested = d["contested"]
    if contested["total"]:
        any_notable = True
        by_file = ", ".join(f"{f} ({n})" for f, n in contested["by_file"].items())
        out.append("**Contested claims right now**")
        out.append(f"- {contested['total']} across {len(contested['by_file'])} file(s): {by_file}")
        out.append("")
    if d["broken_sources"]:
        any_notable = True
        out.append("**Broken sources & access**")
        for b in d["broken_sources"]:
            detail = f" — {b['error']}" if b["error"] else ""
            out.append(f"- {b['id']}: broken since {b['since']}{detail}")
        out.append("")
    if not any_notable:
        out.append("Nothing flagged: no supersessions, contested claims, or broken sources "
                   "right now.")
        out.append("")
    return out


def render_markdown(d: dict, audience: str = "internal") -> str:
    stakeholder = audience == "stakeholder"
    sanitize = strip_internal_vocabulary if stakeholder else (lambda t: t)

    out = [f"# Wiki digest · {d['since']} → {d['until']}", ""]
    kinds = ", ".join(f"{n} {k}" for k, n in sorted(d["by_kind"].items()))
    out.append(f"{d['runs']} changelog entr{'y' if d['runs'] == 1 else 'ies'} in window"
               + (f" ({sanitize(kinds)})." if kinds else "."))
    if d.get("last_digest_sent"):
        out.append(f"Since the last digest sent {d['last_digest_sent']}.")
    out.append("")

    # sanitize free-text fields in place so structured sections (the claims
    # census) are never run through the stakeholder strip a second time.
    if stakeholder:
        for item in d["escalations"]:
            item["text"] = sanitize(item["text"])
        for changes in d["changes_by_file"].values():
            for c in changes:
                c["text"] = sanitize(c["text"])
        for q in d["open_questions"]:
            q["why"] = sanitize(q["why"])
            q["target"] = sanitize(q["target"])

    claims_section = (_render_claims_stakeholder if stakeholder else _render_claims_internal)(
        d["claim_census"]
    )

    if stakeholder:
        # Leads with the drip-interview questions -- what a stakeholder is
        # actually here to act on (F9) -- ahead of everything else.
        out += _render_open_questions(d, "Questions for you")
        out += _render_escalations(d, "Needs your attention")
        out += _render_changes_by_file(d)
        out += claims_section
        out += _render_notable(d, sanitize)
        # Lint escalations are omitted for stakeholders: check names like
        # [doctrine-provenance] are unambiguously internal vocabulary.
    else:
        out += _render_escalations(d, "Escalations — read these first")
        out += _render_changes_by_file(d)
        out += claims_section
        out += _render_notable(d, sanitize)
        out += _render_open_questions(d, "Open questions — top of the backlog")
        if d["lint"] is not None:
            out.append("## Lint escalations")
            out.append("")
            warn = ("" if d["lint"]["warnings"] is None
                    else f", {d['lint']['warnings']} warning(s)")
            out.append(f"{d['lint']['errors']} error(s){warn}.")
            for item in d["lint"]["items"][:10]:
                out.append(f"- {item}")
            if len(d["lint"]["items"]) > 10:
                out.append(f"- … and {len(d['lint']['items']) - 10} more")
            out.append("")

    return "\n".join(out).rstrip() + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("wiki_dir", help="path to the deployed wiki directory")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--since", metavar="YYYY-MM-DD", default=None,
                        help="include changelog entries on/after this date "
                             "(default: since the last --mark-sent digest, or "
                             "7 days before the newest entry if none is recorded)")
    parser.add_argument("--lint-report", metavar="PATH", default=None,
                        help="lint report to fold in (lint.py --json output or text); "
                             "ignored for --audience=stakeholder")
    parser.add_argument("--audience", choices=("internal", "stakeholder"), default="internal",
                        help="internal (default): unabridged, file paths and lint findings "
                             "included. stakeholder: leads with open questions, strips "
                             "internal vocabulary, omits lint findings entirely (F9)")
    parser.add_argument("--mark-sent", action="store_true",
                        help="record this run's newest changelog date as last-digest-sent "
                             f"in {DIGEST_STATE_FILENAME}, so a later run's default --since "
                             "starts from here instead of a flat 7-day window (F9)")
    args = parser.parse_args(argv)

    root = resolve_wiki_dir(args.wiki_dir)
    if not (root / "changelog.md").is_file():
        print("error: changelog.md not found -- nothing to digest", file=sys.stderr)
        return 1

    since = None
    if args.since:
        since = parse_iso_date(args.since)
        if since is None:
            print("error: --since must be YYYY-MM-DD", file=sys.stderr)
            return 1

    lint_report = None
    if args.lint_report and args.audience != "stakeholder":
        report_path = Path(args.lint_report)
        if not report_path.is_file():
            print(f"error: lint report not found: {report_path}", file=sys.stderr)
            return 1
        lint_report = load_lint_report(report_path)

    state = load_digest_state(root)
    try:
        digest = build_digest(root, since, lint_report, state)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    markdown = render_markdown(digest, audience=args.audience)

    if args.mark_sent:
        save_digest_state(root, {**state, "last-digest-sent": digest["until"]})
        digest["last_digest_sent"] = digest["until"]

    if args.json:
        digest["markdown"] = markdown
        print(json.dumps(digest, indent=2))
    else:
        print(markdown, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
