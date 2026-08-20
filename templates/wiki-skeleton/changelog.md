---
type: system
description: "Append-only run log, newest first — every maintain run including no-ops, every interview session; the digest and the eval read from here"
owner: TBD
sources: []
update-cadence: per-run
staleness-horizon: n/a
evidence-as-of:
last-verified: 2026-08-19
---

# Changelog

<!-- Append-only, newest first. One entry per maintain run (no-ops included) and one
     per interview session (SPEC §12.2). Entry header:
     ## <ISO timestamp> · <run type> · sources: [<source-ids>]
     Bullets: per-file changes, supersessions with their class, intake processed,
     open questions added, and explicit "no changes" lines for quiet files. -->

## 2026-08-19T00:00Z · build · sources: []
- wiki initialized from templates/wiki-skeleton: all canonical, system, and intake files created; `evidence-as-of` left empty (no evidence yet); `last-verified: 2026-08-19` stamped on the template itself
- sources.md: +1 source (`intake-inbox` — the manual drop folder every deployment starts with)
- open-questions.md: initialized, backlog empty
- content pending: build interview to populate doctrine; first maintain run to populate state
