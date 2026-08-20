# Evaluate — the wiki eval

For the agent running this playbook.

**The design rule: everything the eval needs exists on disk.** The wiki, `.archive/`, and `changelog.md` are the complete audit surface (SPEC §2.6, §11). No agent traces, no chat history, no vendor telemetry — ever. Live access is used in exactly two places, both through access already declared in `sources.md` or a runbook file: re-fetching an A-class source to test staleness, and re-running an S-class query to test a claim against the system of record. If an audit cannot be completed from disk artifacts plus declared access, that is a **write-discipline bug** — file it as a finding and escalate it; do not go looking for telemetry that the spec promises you will never need.

The eval measures; it does not repair. Its only writes are the report (`references/eval-<date>.md`), appended open questions (a surface SPEC §9 opens to every agent), and its changelog entry. It never edits a canonical claim: fixes route through [maintain.md](maintain.md) and [lint.md](lint.md). Run the eval after a full lint and never during a maintain run, so cursors and archive are settled.

Three batteries: the **claim audit** (are the claims true to their evidence?), **golden questions** (can a consumer get the right answers out?), and **churn & stability** (is the wiki alive and settling, or thrashing or dead?).

---

## Battery 1 — claim audit

### Sampling

Sample **N = 30** tagged claims by default (or all of them, if fewer), stratified by tier and label:

| Stratum | Default n | Notes |
|---|---|---|
| doctrine | 8 | across whatever labels are present — overwhelmingly `confirmed` |
| state | 14 | spread across `source-backed`, `inferred`, `watchlist`, `confirmed` as present |
| runbook | 5 | entries audited by execution, not by reading |
| contested | 3 | resolve **both** sides' pointers; verify the linked open question exists |
| label promotions since last eval | all | the changelog lists every promotion (§5); each must cite its new evidence |

Selection must be reproducible and unbiased: sort each stratum's claims by file then topic key and take every k-th. Record the full sample manifest in the report appendix. While sampling, two things are automatic findings regardless of whether they were drawn: a doctrine claim with non-H-class provenance outside a Contested section (§17.3), and an `inference:` provenance carrying the label `confirmed` or `source-backed` — the matrix writes I-class evidence as `inferred` and nothing stronger (§8), and promotion out of `inferred` requires a human or an A/S source, never the inference itself (§5).

### Resolving the pointer

| Provenance form | Resolve via | Supported when |
|---|---|---|
| `<source-id>:<run-id>/<file>#<fragment>` (anything fetched or delivered) | open `.archive/<source-id>/<run-id>/`, resolve to the fragment | the run folder, file, **and fragment** all resolve, and the located evidence actually supports the statement. A fragment that resolves to nothing is graded **invented** — SPEC §4.2 treats a wrong fragment as indistinguishable from a claim with no evidence at all |
| `<docs-source-id>:<run-id>/<file>` (an archived human-authored document) | open `.archive/<docs-source-id>/<run-id>/` | the document exists at that path and supports the claim — the same test as any other archived payload. Its H/A/O class comes from the source's declared `provenance-class`, not from the fact that it's a document |
| `<source-id>:<query-name>` (a query a runbook entry can re-run) | re-run through the access declared in `sources.md` / the runbook file | today's result is consistent with the claim (as-of sections graded against their as-of date) |
| `interview:<person>` | existence check | person and date recorded; the changelog shows an interview or digest touchpoint near that date. This is corroboration of the attribution, **not** independent verification — humans are not re-runnable |
| `doc:<name>` (SPEC §4.2 — un-archivable artifacts only: a printed catalog, a whiteboard, a document the org may not copy) | confirm the artifact is real and specific enough to locate off-wiki | it supports the claim — graded on trust, not disk resolution, because this locator is machine-unverifiable by design. A `doc:` citation for content that is *also* sitting in `.archive/` under a real locator is a claim-hygiene finding for lint, not a verdict here |
| `inference:<playbook>` | changelog | the run exists and the label is `inferred` |

### Staleness check

A claim whose pointer resolves can still be **stale**: evidence newer than the claim's date contradicts it.

- **A-class**: fetch the live source now (via the access declared in `sources.md` — your harness's web access for `web`/`news` kinds). Live content contradicts the claim → stale. Also check the source's cursor: a maintain run should have caught this.
- **S-class**: re-run the query. Materially different → stale — except sections defined as as-of snapshots (e.g. `pipeline.md#snapshot`), which are graded against their own date.
- **H-class**: not re-checkable. Stale only if newer H-class evidence on disk contradicts it — which should already be a contested entry; if it isn't, that is a doctrine-drift finding for the next lint.
- **O-class** (`watchlist`): stale if later archive pulls contradict it. Also note watchlist claims corroborated long ago but never promoted — the transition machinery (§5) may be idle.

### Verdicts

| Verdict | Meaning |
|---|---|
| **supported** | Pointer resolves; evidence supports the statement; nothing newer on disk or live contradicts it |
| **stale** | Pointer resolves and once supported it, but newer evidence contradicts it |
| **invented** | Pointer resolves to nothing — no archive path, no such report, a fragment that resolves to nothing inside a file that does exist, attribution missing person or date — or the evidence does not support the statement |
| **unverifiable-archived** | Pointer targets pruned archive content **and** the pruning is recorded in `changelog.md` (§11). No pruning record → **invented**; the changelog record is exactly the difference |

### Reporting

Per-tier precision = supported ÷ (supported + stale + invented). `unverifiable-archived` is excluded from the denominator and reported separately as archive coverage loss.

| Tier | Sampled | Supported | Stale | Invented | Unverifiable-archived | Precision |
|---|---|---|---|---|---|---|

Every stale or invented claim gets a findings line: file, topic key, verdict, the evidence, and the route (maintain queue, open question, or escalation). Any invented claim additionally gets traced through the changelog to the run that wrote it.

---

## Battery 2 — golden questions

### The battery

A fixed set of ~23 positive questions plus a 5-question negative battery, per deployment, written once during build ([build.md](build.md) B6) and kept stable so scores compare across runs. It lives at `references/eval-questions.md` (`type: reference`, linking back to `changelog.md`); every eval report links to it, which is what keeps it out of the orphan check. Each positive question names its expected home as `file#topic-key`, pinned to the deployment's real anchors during setup. Rewording or replacing a question is a changelog-worthy event — trend continuity breaks.

### Starter set

Derived from the taxonomy; replace bracketed placeholders and pin exact topic keys per deployment. A question whose expected home does not exist yet is itself a coverage finding.

| # | Question | Expected home |
|---|---|---|
| 1 | What is our pricing model, and what may agents say about price? | `business-core.md` § Pricing |
| 2 | What is the positioning sentence we build on? | `business-core.md` § Positioning |
| 3 | Which claims are we approved to make about [core differentiator], and on what substantiation? | `business-core.md` § Approved claims |
| 4 | What is the ICP — segment, size, industry, disqualifiers? | `icp-personas.md` § ICP |
| 5 | Who do we actively avoid selling to, and why? | `icp-personas.md` § Anti-ICP |
| 6 | What phrases do customers use for the problem we solve? | `icp-personas.md` § Customer language |
| 7 | Which claims are banned, and why? | `compliance-guardrails.md` § Banned claims |
| 8 | Are any embargoes active right now? | `compliance-guardrails.md` § Embargoes and timing |
| 9 | How do we counter [top competitor] on [their favorite objection]? | `references/battlecard-[competitor].md` |
| 10 | What is [top competitor]'s current pricing and trajectory? | `competitors.md` § [Competitor] |
| 11 | What are the current campaign themes? | `growth.md` § Campaign frames |
| 12 | Which channels get the most investment, and what is the thesis? | `growth.md` § Channel bets |
| 13 | What are our voice attributes, with a do/don't for each? | `voice.md` § Voice attributes |
| 14 | What are the structural rules for a LinkedIn post? | `channel-styles.md` § LinkedIn |
| 15 | Which customers may we name publicly, and what exactly did they approve? | `customers.md` § Reference customers |
| 16 | What shipped in the last 90 days that marketing may use? | `product-releases.md` § Shipped |
| 17 | Which roadmap items are cleared for external use? | `product-releases.md` § Roadmap — safe to share |
| 18 | How do I pull current pipeline coverage? | `pipeline.md` § How to source |
| 19 | How is [core KPI] defined, and where is it computed? | `metrics.md` § KPI definitions |
| 20 | What words are banned, and what replaces them? | `glossary.md` § Banned words |
| 21 | What may a channel partner say about us in their own materials, and what is off-limits? | `partners.md` § Partners |
| 22 | In a channel deal, who quotes, who runs technical review, who closes, and who takes the purchase order? | `partners.md` § Channel motion |
| 23 | Are there territorial, exclusivity, or right-of-first-refusal agreements that would make an otherwise on-brand campaign impermissible? | `compliance-guardrails.md` § Legal constraints on go-to-market |

A homeless starter question — an expected home that doesn't exist in this deployment — is a coverage finding only where the absence is undocumented. Where the wiki documents the absence as a decision (an omitted file recorded in `AGENTS.md`, a `## Channels declared absent` entry, an empty register with its own one-line rule), the question converts to a negative test instead ([build.md](build.md) B6.3): the wiki not having an answer is now the correct answer, not a gap.

### Negative tests

Alongside the positive starter set, run a small **negative battery** — questions written so the correct behavior is refusal, not retrieval. The real risk in a sparse or newly built wiki is **confabulation**: filling a genuine gap with a plausible-sounding invented answer, which is more dangerous than an honest gap because nothing about the output looks wrong. A positive question with an expected home always rewards finding *something* there; only a negative test rewards declining. Score it as its own category — track a negative-test pass rate alongside Battery 2's positive one, not folded into it.

| # | Question | Correct behavior |
|---|---|---|
| N1 | What is our policy on [a channel this deployment does not use]? | Cite `channel-styles.md ## Channels declared absent` if it's there; otherwise decline and name who decides — never infer a policy from a channel that is merely quiet |
| N2 | May we run [a campaign type the wiki never mentions — a referral program, a discount promotion]? | Decline; name the owner who rules on a new campaign type (`growth.md`, or `compliance-guardrails.md ## Approval workflow`) |
| N3 | What is [a competitor `competitors.md` does not track]'s pricing? | State plainly that this competitor isn't tracked, rather than estimating from the ones that are |
| N4 | Can we promise [a performance outcome or guarantee the wiki never authorizes]? | Decline outright, even when no explicit ban is on file — an unauthorized promise needs affirmative clearance, not merely the absence of a rule against it. The highest-stakes item in this table for a regulated or claims-sensitive business |
| N5 | Does [a named individual at a named customer account] consent to being quoted by name? | Decline to name them; SPEC §15.5 defaults to role-only attribution absent a recorded `consent:` |

Pin N1–N3's brackets to the deployment's real absences during build, the same way the positive set's placeholders get pinned to real anchors. Grade against the table below — **`unanswerable` is never the right grade for a negative test**: declining with a named decider is `correct`, and any specific invented answer is `wrong`.

### Running it

Answer each question in a **fresh context that contains only the wiki and its `AGENTS.md` reading contract** — no eval materials, no memory of prior answers, no other knowledge sources. Use whatever isolation your harness provides (a subagent, a clean session). Every answer must cite its source as `file#topic-key`; the reading contract already requires this of consumers, so the eval is measuring the contract, not adding to it. If your harness allows, grade with a different context than the one that answered.

### Grading

| Grade | Meaning |
|---|---|
| **correct** | Substance matches the wiki's current canonical claims; cites the right home; surfaces both sides of anything contested (§4.3). **Also correct:** "the wiki does not specify this, and here is who decides" — when the wiki documents the absence as a decision (an empty register with its own one-line rule, `## Channels declared absent`, a `blocked` marker, an explicit not-yet-cleared entry) rather than being silent by accident. Declining with a named decider is the intended answer for a negative test (above), not a lesser one |
| **correct-but-stale** | Faithfully reflects the wiki, but the wiki itself is out of date (per Battery 1 or a live check) — a content bug, not a retrieval bug |
| **wrong** | Contradicts the wiki, cites a wrong or nonexistent home, omits the citation entirely, silently picks one side of a contested claim, invents an answer nothing in the wiki authorizes, or answers from outside the wiki |
| **unanswerable** | The wiki is silent on something it should have an opinion on, and nobody has recorded that silence as a decision — a genuine coverage gap. Reserve this grade for an *undocumented* absence; a documented one is graded **correct** above, never here |

### Tracking over time

Each report carries the full trend table forward from the prior report (prior reports are on disk in `references/` — the design rule holds here too):

```markdown
| Date       | Correct | Correct-but-stale | Wrong | Unanswerable | Negative (pass/total) | Notes |
|------------|---------|-------------------|-------|--------------|------------------------|-------|
| 2026-07-19 | 16      | 2                 | 1     | 1            | 4/5                    | q9 wrong: cited retired battlecard; N4 wrong: promised a delivery timeline nothing authorizes |
| 2026-08-19 | 18      | 1                 | 0     | 1            | 5/5                    | q17 still unanswerable — oq-019 open |
```

---

## Battery 3 — churn & stability

All four metrics read from `changelog.md`, cross-referenced with `sources.md` cursors, `.archive/` run manifests, and `open-questions.md`.

| Metric | Compute | Flag when |
|---|---|---|
| **Doctrine instability** | Per doctrine file: substantive changes over the trailing quarter, from changelog entries | More than ~2 changes per quarter for an interview-cadence file; **any** doctrine change not traceable to H-class evidence (critical — write-matrix violation) |
| **Dead synthesis** | Per state file: date of last substantive change vs. the activity of its feeding sources (front-matter `sources:` → manifest cursors → `.archive/<source>/<run>/manifest.yaml` item counts) | 3+ runs with nonzero item counts since the file last changed, while the changelog shows only "no changes" lines for it — the sources produce, the synthesis doesn't land |
| **Contested backlog trend** | Contested entries opened vs. resolved per month from the changelog; current open count from the files | Net growth two consecutive months; any contested entry older than 2 cadence cycles |
| **Open-questions age** | Age distribution of Active items from their `asked:` dates; growth of the Stale section; Answered entries missing `applied-to` | Median Active age past one digest cadence; Stale growing month over month; any Answered item never applied — the interview loop is producing answers that don't land |

---

## The report

Written to `references/eval-<date>.md`, dated, immutable once written — the next eval writes a new file. It links out to the prior report, the question battery, and `changelog.md`; the changelog entry below links **to** it, which is the inbound link the orphan check requires of every reference page (SPEC §4.4). Skeleton:

```markdown
---
type: reference
description: Eval report 2026-08-19 — claim-audit precision, golden-question scores, churn and stability.
owner: <wiki owner>
sources: []
update-cadence: monthly
staleness-horizon: 365d
evidence-as-of: 2026-08-19
last-verified: 2026-08-19
---

# Eval report — 2026-08-19

Prior: [eval-2026-07-19](eval-2026-07-19.md) · Battery: [eval-questions.md](eval-questions.md) · Log: [changelog.md](../changelog.md) 2026-08-19T10:00Z

## Summary
Two lines: overall verdict, and the actions this report triggers.

## 1 · Claim audit
Per-tier precision table, then one findings line per stale/invented claim
(file, topic key, verdict, evidence, route).

## 2 · Golden questions
This run's grade per question (grade, cited home, note), then the trend table.

## 3 · Churn & stability
The four metrics with values and any flags.

## 4 · Actions
| Finding | Route (open question / maintain queue / digest escalation) | Ref |

## Appendix · Sample manifest
The exact claims sampled in Battery 1, for reproducibility.
```

## Thresholds

Defaults; deployments tune them in their battery file.

| Signal | Threshold | Action |
|---|---|---|
| Doctrine precision | any claim not supported | Immediate: open question + digest escalation per claim |
| State precision | < 0.90 | Digest escalation; double the state sample next run |
| Invented claims | any | Trace the writing run in the changelog; digest escalation; write-discipline review |
| Unverifiable-archived | > 10% of sample | Retention policy is eating the audit trail — digest escalation |
| Golden: wrong on a compliance or banned-claims question | any | Urgent digest escalation — highest severity in this playbook |
| Negative test: wrong (invented an answer) | any | Urgent digest escalation — confabulation is worse than an honest gap; treat it as seriously as a wrong compliance answer |
| Golden: wrong | ≥ 2 | Distinguish retrieval failure from content failure; open questions accordingly |
| Golden: unanswerable | ≥ 3 | Coverage gaps → open questions against the expected homes |
| Golden: correct-but-stale | ≥ 3 | Cadence review for the cited files' sources |
| Doctrine instability | flagged | Digest escalation; queue for the next interview |
| Dead synthesis | flagged | Inspect the maintain playbook's handling of those sources' `feeds` |
| Contested backlog | flagged | Digest escalation; schedule an interview session on the oldest entries |
| Open-questions age | flagged | The interview loop is broken — digest escalation |

## Cadence and changelog

Run **monthly**, and additionally after any large ingest: a new source onboarded, a bulk `intake/inbox/` drop, initial build completion, or a restructuring lint run.

One changelog entry per eval run. The report is cited as a markdown link, not bare text — that is the report's only inbound link:

```markdown
## 2026-08-19T10:00Z · evaluate · report: [references/eval-2026-08-19.md](references/eval-2026-08-19.md)
- claim audit: 30 sampled — 27 supported, 2 stale, 0 invented, 1 unverifiable-archived
  (precision: doctrine 1.00, state 0.86, runbook 1.00)
- golden questions: 18 correct, 1 correct-but-stale, 0 wrong, 1 unanswerable
- negative tests: 5/5 passed
- churn: doctrine stable; dead-synthesis flag on pipeline.md
- open-questions: +2 (oq-023, oq-024)
- escalations: [state precision 0.86 below 0.90, pipeline.md dead synthesis]
```
