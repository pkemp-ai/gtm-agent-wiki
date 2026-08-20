# .archive/

Raw source pulls, one folder per run: `.archive/<source-id>/<run-id>/` (SPEC §11).
Every folder holds a `manifest.yaml` — fetched-at, the cursor or window used, the
query, item counts, warnings — plus the payloads exactly as fetched. Synthesis
reads from here, never from the live source, which is what makes every
`source-backed` claim in the wiki auditable and every run replayable.

Not markdown, not part of the readable wiki, required for audits. Committed to
the repo rather than gitignored, because it is the audit trail.

This example ships a **trimmed** archive: the runs that back the claims the wiki
leans on hardest, plus a few that demonstrate a mechanism (a quiet pull, an
H-class interview session, an inbox drop). It is not complete — several cited
locators, in particular `doc:` filenames from `intake/inbox/` and `gong:` call
ids, have no folder here, and every `crm-hubspot:report-…` locator names a
re-runnable report rather than a file. In a real deployment all of them would
resolve: SPEC §11's default is to keep everything, and a deployment that prunes
records the pruning in `changelog.md` and accepts that audits mark the affected
claims `unverifiable-archived`.
