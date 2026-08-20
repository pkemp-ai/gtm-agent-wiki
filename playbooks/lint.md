# Lint — the wiki health check

For the agent running this playbook. Lint runs with **maintainer authority**: it is the only playbook besides maintain that repairs existing canonical claims — [evaluate.md](evaluate.md) writes only its own report and appended questions — and it must never run concurrently with a maintain run (SPEC §9, single writer). Everything lint does lands in one changelog entry (format at the end), including runs that find nothing.

Lint has two halves. The **deterministic pass** runs `scripts/lint.py` and triages its findings. The **model-judgment sweep** finds what no script can: contradictions, untagged claims, doctrine drift, coverage gaps, and structure that has outgrown its home. Keep the halves separate — never re-do by judgment what the script checks deterministically (SPEC §2.5), and never let the script's silence excuse skipping the sweep (SPEC §14 mandates both halves).

Fix rules that govern every edit in both halves:

1. **Never invent provenance, labels, dates, or evidence.** Recovery comes only from `changelog.md` and `.archive/`. A claim you cannot source is a question, not a repair.
2. **The write matrix applies to you** (SPEC §8). Lint's own conclusions are I-class: against doctrine you may only annotate — contested entries, open questions — never add, remove, or rewrite doctrine claims.
3. **Fixes are content-preserving.** Syntax, structure, links, bookkeeping. When you move text (roll-ups, fan-out, merges), claims move verbatim with their tags and topic keys.
4. **Never resolve a conflict yourself.** Contested entries per SPEC §4.3; resolution needs a higher provenance class or a human. Recency never wins. Supersession (§7) is the maintain run's job, done with evidence in hand — lint only surfaces.
5. **Every fix is a changelog line.** Cite file and topic key.

---

## Part 1 — deterministic pass

### Run the linter

From the wiki root, run `scripts/lint.py`. Each finding prints as `file:line: SEVERITY [check] message`, and the run exits nonzero on any error. Zero findings is still a run: log the no-op (SPEC §17.5).

The table below states what the deterministic layer must catch and why, drawn from SPEC §14 plus the checks the spec mandates elsewhere (§3, §15.3, §17.4) and the ones later findings added to the reference implementation. The spec's list binds whether or not a given deployment's script has caught up to it: compare `scripts/lint.py`'s own output — or its `--help` docstring — against the table below, and any check named here that the script does not yet emit, you run by hand and record as a deterministic finding, same as if the script had found it. A check the script skips is not a check the spec waives.

**`scripts/lint.py` is the source of truth for which of these are currently implemented, not this table.** The script gains checks over time (it is under active extension as this document is written); this table names what must eventually be caught and stays correct even when the two are briefly out of step. `system-files` and `sources-manifest` aren't in the table below because they check §17.4's conformance preconditions directly — system files exist, every source declares access and a cursor, ids resolve in both directions — rather than a single §14 row; run them regardless of whether they show up in either list.

**Severity** classifies the *kind* of finding, not its importance:

| Severity | Means | Disposition |
|---|---|---|
| `error` | Structural — something the spec requires is missing, malformed, or resolves to nothing | Fix mechanically, or open a question when the repair needs a human |
| `warning` | A scheduling or judgment signal — staleness, runbook decay, a broken source, a stalled cursor, a contested backlog over threshold, a size cap, a missing link anchor | Queue the work or escalate it; never dismiss it silently |

Warnings do not fail the run, so a clean wiki can still carry them — a source correctly marked `broken:` is the standing example. Two rules keep that honest: every warning gets a disposition in the changelog entry, and a warning that survives two consecutive lints is escalated. What the script deliberately does not flag: placeholder content (`owner: TBD`, empty `sources: []`, a `## Contested` section holding only prose), and anything inside a code fence or HTML comment — both are inert, so a template may show claim tags and entry schemas without them being read as content. A freshly copied skeleton lints clean for that reason.

### The checks

The first eleven mirror SPEC §14 exactly, in its order; the rest are lint failures the spec mandates elsewhere, or that later findings added to the reference implementation.

| Check | A finding means |
|---|---|
| Front matter | A file fails to parse, is missing a required field (including `evidence-as-of`), or declares an invalid tier; a file carrying an `!internal` claim with no `read-restriction:` line (§4.2) |
| Staleness | **`evidence-as-of`** — never `last-verified` — is older than the file's `staleness-horizon` (§4.1). A flag is a prompt to re-verify, never a suspension: stale doctrine stays **binding** on consumers until amended, and guardrails never lapse by age |
| Runbook decay | A runbook entry's `verified:` stamp is past horizon; separately, `unverified:` entries are counted and escalated, so a file with zero verified entries stops passing silently (§8³) |
| Orphans | A page has no inbound links; nothing routes a reader to it (`outbox/` exempt, §3) |
| Broken links | An internal link or anchor resolves nowhere, or a provenance pointer's run folder, file, **or fragment** resolves to nothing in `.archive/` |
| Claim hygiene | A claim is missing its tag; a tag has a malformed label, provenance, or date; more than one date or provenance pointer in one tag; a topic key that isn't the last token on its line; a claim tag sitting inside a table cell (§4.2) |
| Doctrine provenance | A claim in a `type: doctrine` file carries non-H-class provenance and sits outside all three §17.3 exceptions — the one §17 conformance rule that had no deterministic backing before this check existed |
| Feeds consistency | A file's front-matter `sources:` names an id whose `feeds:` list omits that file, or the reverse (§10) |
| Contested backlog | A contested entry has no linked open question, or the wiki-wide backlog exceeds threshold |
| Manifest health | A source's access failed or declares none, or its cursor hasn't advanced in 2× its cadence (`status: pending-access` excluded — an onboarding gap, not an outage) |
| Size caps | A §13 violation: doctrine file over ~200 lines (warns at 250), any canonical file over 400, log past its rolling window, section past one screen |
| Top-level growth (§3) | A top-level file exists with no taxonomy entry in the deployment's `AGENTS.md` |
| Secrets (§15.3) | A high-entropy string or known key format appears in wiki content, **including inside `.archive/`** |
| Stale target | An Active open question names a `target:` file that carries no reference back to its `oq-` id — the write it's owed hasn't landed (§12.1) |

### Triage

Every finding gets exactly one disposition:

- **Fix mechanically** — the repair needs no knowledge a script or you don't already have.
- **Open question** — the repair needs something only a human knows. Append to `open-questions.md` per SPEC §12.1, targeting the affected file and claim.
- **Digest escalation** — a human should look soon. Escalations are recorded on the `escalations:` line of the lint changelog entry; the digest is generated from the changelog (SPEC §12.2), so that line is how they surface. Escalation does not exempt you from also filing the open question when one is warranted.

| Check | Fix mechanically | Open question | Digest escalation |
|---|---|---|---|
| Front matter | Restore derivable fields: `evidence-as-of` from the run manifests that already record it, tier from the taxonomy, `sources` from the manifest's `feeds`, `read-restriction:` wherever an `!internal` claim exists | `owner` unknown; cadence or horizon needs a human call | — |
| Staleness | Queue the file's sources for the next maintain run | Doctrine past horizon → "is this still true?" (§14 mandates this) | A state file stale for the second consecutive lint — its source loop is failing |
| Runbook decay | On a full run, execute the entry now: success stamps `verified: <date>` (or `verified: <date> (against archive: …)` where only the archive is reachable); failure marks it **broken** with the error, never deleted (§8³) | An entry with no access route at all → `unverified: {since, reason: no-access, question}`, not a guess at `broken` | Any entry newly broken; any file whose verified count is zero |
| Orphans | Reference page whose parent is evident → add the summary-and-link from the parent (§4.4) | Home genuinely unclear → merge/retire candidate, hand to sweep 2.5 | — |
| Broken links | Target moved → repoint to the new location or anchor | — | Provenance pointer resolves to nothing in `.archive/` — file, run folder, or fragment — and the changelog records no pruning: a write-discipline bug, not a dead link |
| Claim hygiene | Malformed tag with unambiguous intent (date format, label typo, spacing, mid-line anchor) → repair; provenance recoverable from changelog/archive → restore it | Untagged claim not recoverable (procedure below) | — |
| Doctrine provenance | The claim already belongs in an evidence section or under a `<!-- tier: -->` marker that's simply missing → add the marker and changelog it | The claim doesn't fit an exception → ratify it (make the evidence H-class) or move it out of doctrine — a human call either way | Always — this is the conformance rule three test deployments self-certified past while violating |
| Feeds consistency | If the file's `sources:` already lists the id, widen the source's `feeds:` to include the file — `sources:` is authoritative for citation, `feeds:` only scopes pulls (SPEC §10), so this is the ordinary direction. If only `feeds:` names the file, add the id to the file's `sources:`. Changelog the correction either way | — | — |
| Contested backlog | Entry missing its open question → create and link one (§4.3 requires it) | — | Backlog above threshold (§14 mandates this) — **expected on a fresh build, and not itself a defect; see below** |
| Manifest health | Mark the failed source **broken** in `sources.md` (§10) | — | Every broken source; every cursor stalled past 2× cadence (`pending-access` sources excluded) |
| Size caps | Roll aged log entries into roll-ups and `references/`; fan out oversized sections per §13, claims verbatim | Doctrine file bloated with prose rather than structure → stakeholder trim | — |
| Top-level growth | — | — | Always — structural violation, and deciding whether the file earns a taxonomy entry is a human call |
| Secrets | Redact the value — in `.archive/` too — replace with the env-var name or vault location, and record the masking in the run manifest (§15.3, §11) | — | Always — rotation is a human decision, and versioned storage retains the value in history |
| Stale target | — | — | Always — an unmet write obligation is exactly what the digest exists to surface |

**A contested backlog above threshold right after a build or a large ingest is a healthy signal, not a defect — say so explicitly, because the instinct to shrink the number is wrong twice over.** Merging or softening a real collision to get under the threshold trades an honest, visible disagreement for a false claim, which is worse than the warning it silences. If the threshold itself is miscalibrated for the wiki's size or lifecycle stage, tune `--contested-threshold` or note the exemption for build-phase runs — never launder the backlog by hand.

**Untagged-claim recovery** (used here and in sweep 2.2):

1. Search `changelog.md` for the run that added the line; follow it into `.archive/`.
2. Evidence found and it supports the statement → tag with the recovered provenance and the evidence-capture date.
3. Not recoverable, state tier → tag `[inferred | inference:lint | <today>]` and open a question to ratify. The label is honest: you are the agent judging the statement plausible enough to keep, unratified.
4. Not recoverable, doctrine tier → annotate only. Leave the text, open a question ("what is the basis for X?"), and escalate if the claim is load-bearing.

---

## Part 2 — model-judgment sweep

2.1–2.3 are SPEC §14's model-judgment checks, in its order. 2.4 and 2.5 enforce rules the spec puts elsewhere: taxonomy coverage and the §3 omission record, and the §13 fan-out discipline.

**Run the sweep in a fresh context — never the one that drafted or last edited the files under review.** The agent that wrote a claim is the worst-positioned judge of whether it is tagged, contradicted, or drifting: a same-context sweep tends to confirm its own prior work rather than audit it, and the failure is invisible from the output alone — a sweep can report a clean pass while missing exactly the claims its author is blind to. Use a subagent, a new session, or hand the sweep to whoever runs the next lint cycle; what matters is that it did not hold the pen for the content it is now checking.

### 2.1 Contradiction hunt

Same topic, incompatible claims, no contested entry. Build a working index of topic keys and named entities across all files (including `references/`). For any topic asserted in more than one place, test compatibility.

- Incompatible → create the contested entry in the topic's canonical home (one home per concept — the taxonomy's boundary notes decide which file that is), both claims with their tags, a resolution path, and a linked open question (§4.3). Other files keep a link, not a copy.
- Duplicated but compatible → still a defect: collapse to the canonical home, leave links behind.
- Do not adjudicate. Even when the class hierarchy looks decisive, supersession belongs to a maintain run holding the evidence.

### 2.2 Untagged actionable claims

Read each file asking one question per sentence: *would a consumer agent act on this?* Numbers, named competitors, policy statements, "we always/never" constructions, and anything a copywriter would repeat are claims. If untagged, run the recovery procedure above. Prose that merely organizes claims needs no tag — the wiki is a claim registry, not a prose archive, so also flag sections where prose is doing a claim's job.

### 2.3 Doctrine drift

For each doctrine claim, scan the state files and the changelog since the last full lint for evidence accumulating against it — e.g. `icp-personas.md` defines the ICP as mid-market while `pipeline.md` trends and `customers.md` wins skew enterprise. Two or more independent evidence items pointing the same way → contested entry against the doctrine claim (annotation is permitted; rewriting is not) plus an open question. A single weak signal is not drift; leave it to the watchlist. Drift findings are the drip interview's highest-value inputs — say so in the open question's `why-it-matters`.

### 2.4 Coverage gaps

Compare the deployment against the taxonomy:

- Canonical files absent with no omission recorded in `AGENTS.md` → escalate (structural).
- Schema sections empty or missing while evidence for them visibly exists in intake, changelog, or archive (e.g. objections chatter in call pulls, but `icp-personas.md` has no objections content) → open question per gap, targeting the file and section.
- Intake observations repeatedly suggesting the same target with nowhere to land → the gap is real; open a question proposing where it lives, per the coverage map in [taxonomy.md](../spec/taxonomy.md).

### 2.5 Merge and split

Apply the fan-out discipline (§13) in both directions:

- **Split**: a canonical section past one screen (~150 lines) or serving a distinct retrieval need (a battlecard, a persona deep dive) → move to a `references/` page, leave a summary and link, link back from the new page.
- **Merge**: a reference page that is thin, stale, and duplicated by its parent's summary → fold it back and remove the page. Versioned storage makes this reversible; the changelog records it.

Claims move verbatim, tags and topic keys intact, in both directions.

---

## Cadence

| Step | Weekly light | Monthly full |
|---|---|---|
| `scripts/lint.py` + triage | yes | yes |
| Runbook execution checks | only entries already marked broken | every entry past horizon |
| 2.1 Contradiction hunt | files changed since last lint (the changelog tells you which) | all files |
| 2.2 Untagged claims | changed files | all files |
| 2.3 Doctrine drift | — | yes |
| 2.4 Coverage gaps | — | yes |
| 2.5 Merge / split | — | yes |

Run a full lint before any eval ([evaluate.md](evaluate.md)) so the eval measures content quality, not hygiene debt. A large ingest or restructure warrants an off-cycle light run.

## The changelog entry

One entry per lint run, no-ops included, newest first in `changelog.md`:

```markdown
## <ISO timestamp> · lint · scope: light|full
- deterministic: <n> files, <n> findings — <n> fixed, <n> to open questions, <n> escalated
  - <check>: <finding and disposition, one line each, citing file and topic key>
- sweep: <one line per sweep finding and disposition>
- open-questions: +<n> (<ids>)
- escalations: [<items the digest must carry>]
- no findings: <checks that came back clean>
```

Example:

```markdown
## 2026-08-19T09:00Z · lint · scope: full
- deterministic: 21 files, 4 findings — 2 fixed, 1 to open questions, 1 escalated
  - claim hygiene: malformed date fixed (competitors.md ^metricflow-upmarket)
  - staleness: voice.md 47d past horizon → oq-021 "voice attributes still current?"
  - runbook decay: crm.md win/loss pull re-executed, verified: 2026-08-19
  - manifest health: slack-gtm cursor stalled 3 weeks → escalated
- sweep: pipeline.md trends vs icp-personas.md ICP — enterprise drift, contested entry + oq-022
- open-questions: +2 (oq-021, oq-022)
- escalations: [slack-gtm cursor stalled 3 weeks]
- no findings: front matter, orphans, broken links, doctrine provenance, feeds consistency, contested backlog, size caps, top-level growth, secrets, stale target
```
