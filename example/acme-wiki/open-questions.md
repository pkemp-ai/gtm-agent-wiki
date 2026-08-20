---
type: system
description: Acme's standing interview backlog — the questions only a human can answer, what each one blocks, where the answer will land, and the answers already applied.
owner: Dana Okafor (CMO)
sources: []
update-cadence: per-run
staleness-horizon: n/a
evidence-as-of: 2026-08-05
last-verified: 2026-08-19
---

# Open questions

The seam between what the wiki can work out and what only a person can decide. Producers: the build interview, every maintain run, and consumer agents (appending here is allowed — SPEC §9). Consumer: the drip interview, which carries 2–3 Active items into each weekly digest.

Ids are allocated sequentially and never reused. Gaps in the numbering are questions that were answered and aged out of the Answered section — the changelog keeps their trail.

Ten Active is above where this backlog should sit. Six of the ten are contested-claim resolutions, which is the load-bearing number: every one of them is a place where copy currently has to hedge.

## Active

### oq-014 · Is the 45-day sales cycle real above 20 seats? ^oq-014
- kind: gap
- owed-by: Priya Shah
- why-it-matters: pricing page copy and SDR sequencing both assume 45 days
- target: business-core.md#sales-cycle-length
- origin: contested claim, crm-hubspot:report-2026-q2-pipeline vs interview:priya-shah
- asked: 2026-08-12 (digest) — awaiting answer
- note: the report that would answer this without a human is broken on empty seat-count data ([pipeline.md#broken-cycle-by-seat](pipeline.md#broken-cycle-by-seat)), so this is a decision question until the hygiene backfill lands

### oq-016 · Does MetricFlow discount in our segment, and may we say so? ^oq-016
- kind: gap
- owed-by: Dana Okafor
- why-it-matters: the comparison page and every competitive deal desk cite their list price; if reps are seeing 30–40% off, our price argument is aimed at a number that does not exist
- target: competitors.md#metricflow-discounting
- origin: contested claim, interview:priya-shah vs web-metricflow:2026-08-10/pricing.html — an H-versus-A collision
- asked: 2026-08-15 (Q3 partner and competitive review) — awaiting answer
- draft-answer: track the pattern internally, keep copy on their published list price only

### oq-018 · Is the 100-employee ICP floor still the floor? ^oq-018
- kind: gap
- owed-by: Dana Okafor
- why-it-matters: SDR triage auto-deprioritizes sub-100 accounts, and 9 of 41 H1 wins were between 60 and 99 employees with normal onboarding times
- target: icp-personas.md#icp-employee-floor
- origin: contested claim, interview:dana-okafor vs crm-hubspot:report-2026-h1-wins
- asked: 2026-08-05 (digest) — awaiting answer
- blocked-on: two-quarter retention of the sub-100 cohort is not readable until 2026-10; a floor change is Dana Okafor's call, not a trend line's

### oq-021 · What is our answer on untracked touches — "dark social"? ^oq-021
- kind: gap
- owed-by: Dana Okafor
- why-it-matters: raised in 6 of the last 14 discovery calls; there is no doctrinal answer, so no asset can be written and reps are improvising
- target: icp-personas.md#objection-dark-social, glossary.md#term-dark-social
- origin: inferred pattern, inference:maintain 2026-08-12, corroborated across gong calls
- asked: 2026-08-12 (digest) — awaiting answer
- draft-answer: we model them as untracked touches and say so plainly; we do not claim to resolve them, and "dark social" stays a quoted customer phrase rather than our own word
- parked-draft: "Prospects keep asking whether we capture dark social — touches that surface as direct traffic. We model them as untracked touches and say so; we do not claim to resolve them, and 'dark social' stays a quoted customer phrase rather than our own word." Removed from icp-personas.md and glossary.md at delivery (SPEC §8 / §17.3); recoverable here until Dana rules.

### oq-024 · Does MetricFlow's FastStart date our six-week framing? ^oq-024
- kind: gap
- owed-by: Dana Okafor
- why-it-matters: the competitive frame in doctrine says six-week implementations; FastStart advertises three weeks for their entry tier, and our comparison page already hedges to "three to six weeks, per their own materials"
- target: business-core.md#competitive-frame
- origin: maintain run 2026-08-10, web-metricflow:2026-08-04/blog/faststart.html — A-class evidence against a doctrine claim, so annotation only
- asked: 2026-08-15 (digest) — awaiting answer
- draft-answer: keep the wedge on ops ownership rather than weeks, since FastStart still assumes a data team on the customer side

### oq-025 · Is the Model Lab template library GA or beta? ^oq-025
- kind: gap
- owed-by: Sam Whitfield
- why-it-matters: copy currently says neither, which costs us the strongest sentence in the Ops-owns-the-model narrative
- target: product-releases.md#model-lab-ga-status
- origin: contested claim, slack-gtm:2026-07-09/dump.json#msg-4802 vs webflow:2026-08-17/pages.json — two authoritative reads of our own state
- asked: 2026-08-19 (digest) — awaiting answer
- resolution-path: product confirms status, then either the docs page or the announcement gets corrected

### oq-026 · Which model defines "marketing-sourced pipeline"? ^oq-026
- kind: gap
- owed-by: Dana Okafor
- why-it-matters: 61% on the multi-touch overlay, 48% on last touch. Both are defensible, neither may be used, and the KPI has no definition until someone picks
- target: metrics.md#kpi-marketing-sourced, pipeline.md#marketing-sourced-share
- origin: contested claim, crm-hubspot:report-2026-q3-source-mix vs doc:q2-2026-qbr-deck.md
- asked: 2026-08-19 (digest) — awaiting answer
- note: nothing else in the backlog blocks as much. It blocks a board chart, a KPI definition, and the honest version of our own positioning

### oq-027 · Is Harborlight a referral partner or a competitor? ^oq-027
- kind: gap
- owed-by: Sam Whitfield
- why-it-matters: they are signed as a referral partner and have sent two opportunities, while sales is calling them a competitor. No asset may name them either way until this settles
- target: partners.md#harborlight-status
- origin: contested claim, crm-hubspot:report-2026-08-partner-referrals vs interview:priya-shah
- asked: 2026-08-15 (Q3 partner and competitive review) — awaiting answer
- resolution-path: ask them directly at the Q3 partner review; both readings can be true at once

### oq-028 · Do ops-led deals really close better than CMO-led deals? ^oq-028
- kind: gap
- owed-by: Priya Shah
- why-it-matters: if ratified, outbound message ordering flips to Morgan-first; until then the current Dana-first ordering is a habit nobody has defended
- target: pipeline.md#trend-ops-champion
- origin: inferred pattern across three quarters, inference:maintain 2026-08-19
- asked: not yet — queued for the 2026-08-26 digest
- falsifier: which recent deal contradicts this, and why

### oq-029 · Do we want a DashForge comparison asset? ^oq-029
- kind: gap
- owed-by: Dana Okafor
- why-it-matters: DashForge was named in 19% of H1 competitive deals and 4 of 63 currently open ones, concentrated in the band we sell into, and reps have nothing to send
- target: content-assets.md#gap-dashforge-comparison
- origin: inferred gap, inference:maintain 2026-08-19
- asked: not yet — queued for the 2026-08-26 digest
- note: publishing a comparison page is also a decision about attention. The counter-position in doctrine is to qualify rather than compete on price, and a comparison page argues with that

## Partially answered

<!-- A ruling landed and did not cover every named target. Keep the entry
     here until applied-to matches target:. None currently. -->

## Delegated

<!-- Rerouted to a different human with standing. owed-by: updates; asked: resets.
     oq-011's reroute is recorded on the Stale entry itself — that is the
     disposition, not a second live queue. -->

## Answered

### oq-009 · Do we lead with SOC 2 in enterprise outreach? ^oq-009
- kind: gap
- owed-by: Dana Okafor
- answer: Yes, always in first touch. [confirmed | interview:dana-okafor | 2026-08-05]
- applied-to: [channel-styles.md#email-soc2-first-touch](channel-styles.md#email-soc2-first-touch), [compliance-guardrails.md#soc2-wording](compliance-guardrails.md#soc2-wording)
- follow-on: the wording constraint came with it — "SOC 2 Type II," never "certified" — which is why the answer landed in two files rather than one

## Stale

Unanswered past two cadence cycles. Each gets exactly one of: re-asked once and smaller, rerouted to a different human with standing, or proposed for dropping.

### oq-011 · What is the ACV floor below which we walk away? ^oq-011
- kind: gap
- owed-by: Priya Shah
- why-it-matters: [business-core.md](business-core.md#pricing) records tiers but no floor, so nothing in the wiki tells an agent when a deal is too small to pursue; SDR triage currently uses employee count as a proxy for price
- target: business-core.md#pricing
- origin: build interview gap, 2026-06-20
- asked: 2026-07-08 (digest), re-asked 2026-07-29 (digest) — no answer either time
- disposition: reroute to Priya Shah at the Q3 review rather than re-asking Dana a third time. Standing risk while it sits here: the wiki is silent on a question sales answers ad hoc, and silence means agents may not assert a floor at all
