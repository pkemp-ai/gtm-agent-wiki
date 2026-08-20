---
type: reference
description: The MetricFlow battlecard — where they genuinely win, where they are weak, the landmines to plant early, verbatim objection responses, and the win/loss record behind all of it.
owner: Dana Okafor (CMO)
sources: [web-metricflow, crm-hubspot, gong, reviews-web, interviews]
update-cadence: per-run
staleness-horizon: 45d
evidence-as-of: 2026-08-19
last-verified: 2026-08-19
---

# Battlecard — MetricFlow

Parent: [competitors.md](../competitors.md#metricflow). Read [compliance-guardrails.md](../compliance-guardrails.md#competitor-conduct) before any of this reaches a prospect: MetricFlow may be named in comparison pages and this card, never in ads or social posts, and every comparison cites their own dated materials and nothing about their customers, funding, or internals.

**How we win** and the landmines are decisions, not observations — doctrine-in-exile, H-class only. The maintainer may annotate them from external evidence and may never rewrite them.

## Who they are, in one paragraph

The enterprise incumbent in revenue attribution. Sales-led, aimed at 1,000+ employee organizations, with an attribution suite plus a services arm; their own implementation guide describes a six-week guided rollout.
[source-backed | web-metricflow:2026-07-14/implementation-guide.html | 2026-07-14] ^bc-mf-profile

Since August they also market FastStart, a fixed-scope three-week package for their entry tier; the evidence for it, and what it does to our timeline argument, sit under weaknesses below.

## Where they genuinely win

Naming these accurately is what makes the rest of the card credible. A rep who cannot say where MetricFlow is better will not be believed about where it is worse.

| They win when | Why |
|---|---|
| The buyer has a data team and wants warehouse-native custom models | Their modeling layer is deeper and they will build to spec. We lose these and should — it is the stated limit on our own right to win ([business-core.md](../business-core.md#right-to-win)) |
| Procurement wants a single vendor for attribution plus services | They sell the implementation as part of the deal; we sell a product that a customer's own ops lead runs |
| The org is 1,000+ employees with a central analytics function | Their reference base and security posture are built for that buyer; ours is built for the 100–1,000 band |
| The evaluation is run by a consultancy on a scorecard | Feature-count scorecards favor suites. Speed and ops ownership do not score well on a matrix |

[confirmed | interview:priya-shah | 2026-08-15] ^bc-mf-where-they-win

## Where they are weak

- **Implementation lift lands on the customer.** Six weeks guided, and FastStart's three weeks still assumes a data team on the customer side. [source-backed | web-metricflow:2026-08-04/blog/faststart.html | 2026-08-04] ^bc-mf-weak-implementation
- **A $10k implementation fee on every tier, list floor $2,500/mo billed annually.** The all-in first-year number is the part mid-market buyers do the arithmetic on themselves. [source-backed | web-metricflow:2026-08-10/pricing.html | 2026-08-10] ^bc-mf-weak-pricing
- **Configuration is a services engagement, not an ops task.** Model changes route back through their team, which is exactly the dependency a marketing ops lead is trying to escape ([persona-morgan.md](persona-morgan.md)). [confirmed | interview:morgan-lee | 2026-07-30] ^bc-mf-weak-config
- **Attention is moving upmarket.** Three of their last four published case studies are enterprise. Single-signal reading of their own publishing pattern — tracking, not asserting. [watchlist | web-metricflow:2026-08-10/case-studies.html | 2026-08-10] ^bc-mf-weak-upmarket

## Landmines to plant

Questions we want the prospect asking MetricFlow, planted early and neutrally. Never phrased as an attack — a loaded question loses the room and violates the disparagement rule.

| Plant | What it surfaces |
|---|---|
| "Who configures the model after go-live — your team or ours?" | Services dependency |
| "What is the all-in first-year cost including implementation?" | The $10k fee on every tier |
| "Can our marketing ops lead change the attribution window without a ticket?" | Ops ownership |
| "How many of your last ten case studies are companies our size?" | The upmarket drift, in their own materials |
| "What happens in week seven if the numbers still look wrong?" | Who owns the outcome after the engagement closes |

[confirmed | interview:dana-okafor | 2026-08-15] ^bc-mf-landmines

## Objection responses

Verbatim-ready. Each answers the objection and then moves the conversation to methodology or ownership, where we win.

**"MetricFlow is the category standard — nobody gets fired for buying them."**
> True for a 3,000-person org with an analytics team. You are a 40-person marketing team with one ops lead. The question is not which tool is safer to buy, it is which one still works in month four when nobody has a services engagement open. Ask both of us who configures the model after go-live.

[confirmed | interview:dana-okafor | 2026-08-15] ^bc-mf-obj-standard

**"Their model is more sophisticated than yours."**
> On custom warehouse-native modeling, that is fair, and if you have a data team who wants to own the model, they are the better fit. Our models are prebuilt and ops-configurable, which is a different bet: fewer knobs, and the person who owns the number can turn them.

[confirmed | interview:sam-whitfield | 2026-07-02] ^bc-mf-obj-sophistication

**"They quoted us three weeks with FastStart — same as your four days plus setup."**
> Compare the same thing. Our median is four business days from signature to a dashboard your team saved, across 61 implementations ([business-core.md](../business-core.md#claim-ttfd)). Their three weeks is a fixed-scope package, per their own materials, and it assumes someone on your side does the data work. Ask what your team is responsible for in each of those three weeks.

[confirmed | interview:dana-okafor | 2026-08-15] ^bc-mf-obj-faststart

**"We already have MetricFlow. Switching is too expensive."**
> Then do not switch on our word. Run one quarter of one channel in parallel and compare what each model credits. If the answers agree, keep them — we would rather lose that way than argue about it.

[confirmed | interview:priya-shah | 2026-08-15] ^bc-mf-obj-switching

**"Are you cheaper?"**
> We publish our prices and they publish theirs; do the first-year arithmetic yourself. But price is not the argument — if it were, DashForge would win. The argument is who runs the model after go-live.

[confirmed | interview:dana-okafor | 2026-08-15] ^bc-mf-obj-price

## Win/loss evidence

- Named in 44% of H1 2026 competitive deals. Our H1 win rate against them was 58%, rising above 70% when the buyer has no data team. [source-backed | crm-hubspot:report-2026-h1-winloss | 2026-07-28] ^bc-mf-winloss-rate
- The losses cluster in two shapes: buyers with an analytics team who wanted warehouse-native models, and consultancy-run scorecard evaluations. Neither is a messaging failure, and the first is a qualification success. [inferred | inference:build | 2026-08-19] ^bc-mf-loss-shapes
- Where we won, the deciding moment was consistently the prospect asking MetricFlow who configures the model after go-live. Read across five closed-won competitive deals, not a measured cause. [inferred | inference:build | 2026-08-19] ^bc-mf-win-moment
- One prospect described their MetricFlow evaluation as "a project before it was a tool." Single call, quoted because the phrasing is usable. [source-backed | gong:call-8677 | 2026-07-31] ^bc-mf-quote-project

## How we counter

Speed-to-value and ops ownership. **Never price.** FastStart still assumes a data team on the customer side, so the wedge is the four-day median and marketing-ops-owned configuration, not weeks-versus-weeks arithmetic.
[confirmed | interview:dana-okafor | 2026-08-15] ^bc-mf-counter

Doctrine's competitive frame still says "six-week implementations" ([business-core.md](../business-core.md#competitive-frame)). FastStart may date that phrasing; the comparison page already hedges to "three to six weeks, per their own materials," and the framing itself is a decision awaiting a human → [open-questions.md#oq-024](../open-questions.md#oq-024).

Whether their reps discount 30–40% in our segment is contested and unresolved — copy cites their published list price only until it settles ([competitors.md](../competitors.md#metricflow-discounting), [open-questions.md#oq-016](../open-questions.md#oq-016)).
