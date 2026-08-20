---
type: state
description: Current evidence on MetricFlow, DashForge, and Attribia — pricing snapshots, trajectory readings, recent moves, win/loss data — plus the watchlist of not-yet-competitors.
owner: Dana Okafor (CMO)
sources: [web-metricflow, web-dashforge, web-attribia, news-web, reviews-web, social-linkedin, crm-hubspot, gong, interviews]
update-cadence: per-run
staleness-horizon: 45d
evidence-as-of: 2026-08-15
last-verified: 2026-08-19
---

# Competitors

What agents may *say* about competitors in public copy is governed by [compliance-guardrails.md](compliance-guardrails.md#competitor-conduct): facts with dated evidence from the competitor's own materials, nothing about their customers, funding, or internals. This file may track more than copy may use.

Each **How we counter** line is doctrine-in-exile: it records a decision, requires H-class provenance, and the maintainer may annotate it from external evidence but never rewrite it.

## Tracked competitors

### MetricFlow

The enterprise incumbent. Sales-led motion aimed at 1,000+ employee orgs; attribution suite plus a services arm; their own implementation guide describes a six-week guided rollout.
[source-backed | web-metricflow:2026-07-14/implementation-guide.html | 2026-07-14] ^metricflow-profile

Pricing snapshot: list floor $2,500/mo billed annually, plus a $10k implementation fee on every tier.
[source-backed | web-metricflow:2026-08-10/pricing.html | 2026-08-10] ^metricflow-pricing

*Pricing updated 2026-08-10 — the floor was $2,200/mo since first tracked. A-class self-fact, superseded silently per SPEC §7; see [changelog.md](changelog.md).*

Trajectory: MetricFlow appears to be moving upmarket; three of their last four case studies are enterprise.
[watchlist | web-metricflow:2026-08-10/case-studies.html | 2026-08-10] ^metricflow-upmarket

Recent moves:

- Announced "FastStart," a fixed-scope implementation package promising three weeks for their Essentials tier. Aimed squarely at our wedge. [source-backed | web-metricflow:2026-08-04/blog/faststart.html | 2026-08-04] ^metricflow-faststart
- Doctrine's competitive frame still cites their six-week implementations ([business-core.md](business-core.md#positioning)); FastStart may date that framing. Annotation only — raised as [open-questions.md#oq-024](open-questions.md#oq-024). The public comparison page already hedges to "three to six weeks, per their own materials."

Win/loss: named in 44% of H1 competitive deals; our H1 win rate against them was 58%, and rises above 70% when the buyer has no data team.
[source-backed | crm-hubspot:report-2026-h1-winloss | 2026-07-28] ^metricflow-winloss

**How we counter:** speed-to-value and ops ownership, never price. FastStart still assumes a data team on the customer side; our argument is the 4-day median and marketing-ops-owned configuration ([business-core.md](business-core.md#right-to-win)).
[confirmed | interview:dana-okafor | 2026-08-15] ^counter-metricflow

Full battlecard — strengths, landmines, objection responses, win/loss detail: [references/battlecard-metricflow.md](references/battlecard-metricflow.md).

### DashForge

Cheap self-serve attribution for SMB: freemium plus a $299/mo paid tier, credit-card checkout, no sales team. Historically last-click only.
[source-backed | web-dashforge:2026-08-10/pricing.html | 2026-08-10] ^dashforge-profile

They launched a "multi-touch beta" on 2026-07-21, per their own announcement.
[source-backed | web-dashforge:2026-07-21/blog/multi-touch-beta.html | 2026-07-21] ^dashforge-mt-beta

Early review-site chatter characterizes the beta as reweighted last-click rather than path modeling. Single external signal — tracking, not citing.
[watchlist | reviews-web:2026-08-08/dashforge-reviews.json#rev-3312 | 2026-08-08] ^dashforge-mt-quality

Trajectory: creeping into our band. Named in 19% of H1 competitive deals, up from 9% in Q1, concentrated in the 100–300 employee segment.
[source-backed | crm-hubspot:report-2026-h1-winloss | 2026-07-28] ^dashforge-encroaching

No comparison asset covers them yet — flagged in [content-assets.md](content-assets.md#gaps).

**How we counter:** never on price. Qualify on multi-touch depth and CRM write-back; a prospect who only needs last-click is DashForge's customer, not ours, and we say so.
[confirmed | interview:priya-shah | 2026-07-20] ^counter-dashforge

Battlecard (thin stub until they justify more): [references/battlecard-dashforge.md](references/battlecard-dashforge.md).

### Attribia

AI-native newcomer, founded 2024. Loud founder-led LinkedIn presence; positions attribution as a modeling problem solved by AI, with "10-minute setup, no ops work" as the recurring promise on their site.
[source-backed | web-attribia:2026-08-10/index.html | 2026-08-10] ^attribia-profile

No public pricing — the site routes everything to "talk to us."
[source-backed | web-attribia:2026-08-10/pricing.html | 2026-08-10] ^attribia-pricing

Recent signals, all single-source and tracked as such:

- Trade-press report of a $12M Series A. Tracking only — funding never appears in our copy per [compliance-guardrails.md](compliance-guardrails.md#competitor-conduct). [watchlist | news-web:2026-07-29/attribia-series-a.html | 2026-07-29] ^attribia-funding
- Three enterprise AE job postings visible on their LinkedIn page — a sales-led turn would contradict their self-serve story. [watchlist | social-linkedin:2026-08-11/attribia-jobs.json | 2026-08-11] ^attribia-hiring
- A reviewer reports numbers shifting week-to-week without explanation ("the model changed under us"). Matches the unproven-data-model read; needs a second source before it informs anything. [watchlist | reviews-web:2026-08-08/attribia-reviews.json#rev-1108 | 2026-08-08] ^attribia-model-drift

**How we counter:** never engage their LinkedIn threads ([compliance-guardrails.md](compliance-guardrails.md#competitor-conduct)). In deals, invite the prospect to ask both vendors to explain the model behind the numbers — we win when the conversation reaches methodology.
[confirmed | interview:sam-whitfield | 2026-07-16] ^counter-attribia

Battlecard (thin stub): [references/battlecard-attribia.md](references/battlecard-attribia.md).

## Watchlist

Entities not yet tracked as full competitors. Promotion to a section above happens on CRM evidence — the entity appearing in competitive fields of real deals — not on news volume.

- Signalpost — B2C attribution vendor; announced a "B2B module" on their blog. Not yet seen in a deal. [watchlist | news-web:2026-08-06/signalpost-b2b.html | 2026-08-06] ^wl-signalpost
- Harborlight — RevOps consultancy reportedly productizing an internal attribution tool; one prospect mentioned evaluating it on a discovery call. [watchlist | gong:call-9188 | 2026-08-13] ^wl-harborlight

## Contested

### Does MetricFlow discount in our segment? ^metricflow-discounting
- "MetricFlow reps are discounting 30–40% to hold renewals whenever we're in the deal" [confirmed | interview:priya-shah | 2026-08-15]
- Their pricing page states list pricing and markets a no-negotiation policy [source-backed | web-metricflow:2026-08-10/pricing.html | 2026-08-10]
- H vs. A collision (SPEC §7.4) — neither side wins by recency. Resolution path: collect Q3 win/loss notes from deals where MetricFlow was the incumbent. Until resolved, copy may cite their list prices only. → [open-questions.md#oq-016](open-questions.md#oq-016)
