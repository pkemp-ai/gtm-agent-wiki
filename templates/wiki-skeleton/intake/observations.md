# Observations — consumer intake buffer

Append-only. Consumer agents never edit canonical files (SPEC §9); anything learned mid-run lands here as an entry. The maintainer consumes this file on every run — each entry is promoted into canon per the write matrix, converted to an open question, or discarded with a changelog note — and removes processed entries (the changelog keeps the audit trail). The test for writing here: *would someone who wasn't on this run need this?*

<!-- Entry format (SPEC §9) — append below, one entry per discrete observation:

## 2026-08-19T15:42Z · <agent or session label>
- observation: <one actionable statement — three statements are three entries>
- suggested-target: <canonical file, e.g. competitors.md>
- evidence: <source-id>:<locator> — or interview:<person> / doc:<filename>
-->
