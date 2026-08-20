---
type: runbook
description: How Acme defines each number leadership watches, which system is authoritative for it, the exact report that produces it, and the reporting conventions a board-facing chart must follow.
owner: Morgan Lee (marketing ops)
sources: [crm-hubspot, ga4, webflow, interviews]
update-cadence: monthly
staleness-horizon: 60d
evidence-as-of: 2026-08-17
last-verified: 2026-08-17
---

# Metrics

Two different kinds of content live here, and they are governed differently. **KPI definitions are decisions** — doctrine-in-exile, H-class only, and the maintainer may annotate but never rewrite them. **Query patterns are runbook** — they are verified by running them, and a pattern that fails is marked **broken** with its error rather than deleted (SPEC §8).

No current metric *values* appear in this file. Values rot; definitions and queries do not. Pipeline numbers as of the last refresh live in [pipeline.md](pipeline.md#snapshot); anything else an agent needs, it derives by running the pattern below and dating its own output.

## North star

**Pipeline created** — opportunities created in the period, counted at creation date. It is the unit the board trusts, the number the channel bets are judged against, and the thing we are willing to be wrong about in public if the definition is honest. It is not MQLs, not trials, and not "marketing-sourced pipeline" (which has no definition until [open-questions.md#oq-026](open-questions.md#oq-026) lands).
[confirmed | interview:dana-okafor | 2026-07-16] ^north-star

## KPI definitions

Per KPI: what counts, who owns the definition, and why it is drawn where it is drawn.

### MQL ^kpi-mql

A contact who has (a) submitted a form on a gated asset or requested a demo, **and** (b) matches the ICP filter in [icp-personas.md](icp-personas.md#icp-definition) on employee count and CRM presence. Both halves are required — a demo request from a 12-person agency is not an MQL, it is a disqualification.

Owner: Morgan Lee. Why here: sales works MQLs on a one-business-day SLA ([account-ownership.md](account-ownership.md#handoff-sla)), so a definition that inflates volume spends AE time rather than earning it.
[confirmed | interview:morgan-lee | 2026-07-30] ^kpi-mql-def

### Pipeline created ^kpi-pipeline-created

Sum of opportunity amount for opportunities **created** in the period, counted at creation date and never restated when a deal's amount later changes. Open and closed both count; the metric measures generation, not outcome.

Owner: Priya Shah. Why here: it is the unit the board trusts, which is why we say "pipeline created" and not "leads generated" ([glossary.md](glossary.md#terms-we-use)).
[confirmed | interview:priya-shah | 2026-07-20] ^kpi-pipeline-created-def

### Marketing-sourced pipeline ^kpi-marketing-sourced

**Definition unresolved.** Two models are in use and they disagree by 13 points on the same quarter: the multi-touch overlay on original source, and last touch on the opportunity record. Naming one model here is the resolution path for the contested figure in [pipeline.md](pipeline.md#marketing-sourced-share) — and until a human names it, this KPI has no definition and no number of it may appear in a board deck, a post, or a plan.
→ [open-questions.md#oq-026](open-questions.md#oq-026)

That an attribution vendor has an unresolved attribution definition is not embarrassing, it is the product thesis stated inward: the model is a choice, and choosing it is a decision, not a query.

### Cost per opportunity ^kpi-cpo

Paid spend in the period divided by opportunities created in the period, attributed on the multi-touch model, with no lag adjustment. Spend comes from the ad platforms via campaign-cost write-back ([product-releases.md](product-releases.md#rel-hubspot-cost-writeback)), not from a spreadsheet.

Owner: Morgan Lee. Why here: this is the metric behind the only customer number we may publish ([business-core.md](business-core.md#claim-brightpath-cpo)), so its definition has to survive a customer's own finance team checking it.
[confirmed | interview:morgan-lee | 2026-07-30] ^kpi-cpo-def

### Time to first dashboard ^kpi-ttfd

Business days from contract signature to the first customer-configured dashboard being saved by a user at the customer, excluding dashboards created by our own implementation staff. Reported as a **median**, never a mean — the mean is dragged by a handful of messy Salesforce migrations and would overstate the typical case.

Owner: Morgan Lee, recomputed quarterly. Why here: it is the substantiation for our headline claim. The claim and its current value are governed in [business-core.md](business-core.md#claim-ttfd) — this file owns how it is computed, that file owns what we are allowed to say. If a recompute moves the median, doctrine changes there first.
[confirmed | interview:morgan-lee | 2026-07-30] ^kpi-ttfd-def

### Blog-assisted trials ^kpi-blog-assisted

Trials whose journey contains at least one blog pageview before the trial start, counted on the multi-touch model. Deliberately "assisted" and not "sourced": the blog rarely closes anything on its own, and a sourced framing would let us claim credit the model does not support.

Owner: Dana Okafor. Why here: it is the number the SEO channel bet is judged on ([growth.md](growth.md#channel-bets)).
[confirmed | interview:dana-okafor | 2026-07-16] ^kpi-blog-assisted-def

## Where data lives

Which system is authoritative for what, and where the second-best copy will disagree. The full stack and the flows between tools are mapped in [gtm-tools.md](gtm-tools.md#data-flows).

| Question | Authoritative system | Not authoritative, and why |
|---|---|---|
| Pipeline, deal amounts, stages, owners | CRM (HubSpot) | Our own product's revenue view is a *model* over CRM data; it never overrides the CRM's own totals |
| Paid spend by campaign | The ad platforms, written back into the CRM as campaign cost | Platform UIs restate spend after the fact; the write-back snapshot is what our reports used |
| Sessions, pageviews, on-site behavior | GA4 | The CRM sees only sessions it can stitch to a known contact — always a subset |
| Which touches a journey contains | Our own product (Journeys) | GA4 last-click will disagree by design; that disagreement is the thing we sell |
| Page and asset inventory | Webflow CMS | The asset catalog in [content-assets.md](content-assets.md) is the fitness-for-use ruling, not the inventory |
| Call content and customer phrasing | Call recordings (Gong) | Rep notes in the CRM are a summary written by an interested party |

[confirmed | interview:morgan-lee | 2026-07-30] ^where-data-lives

## Query patterns

Each pattern names the report or tool call that produces the number, the connection it needs (declared for its source in [sources.md](sources.md), credentials by env-var name only), and its last successful execution. A pattern that fails is marked **broken** here with the error and stays on the list.

| KPI | Pattern | System | Status |
|---|---|---|---|
| MQL volume | Saved report "MQL Volume by Week — ICP-filtered" | CRM | verified: 2026-08-17 |
| Pipeline created | Saved report "Pipeline Created — by period, creation-dated" | CRM | verified: 2026-08-17 |
| Cost per opportunity | Saved report "CPO — spend over opportunities, multi-touch" | CRM | verified: 2026-08-17 |
| Time to first dashboard | Onboarding-timestamp export, quarterly recompute in the ops workbook | CRM export | verified: 2026-07-31 |
| Blog-assisted trials | GA4 landing-page report joined to the trial list on email hash | GA4 + CRM | verified: 2026-08-17 |
| Blog page performance | GA4 report "Blog pages — sessions and entrances" | GA4 | verified: 2026-08-17 |
| Marketing-sourced share | *no pattern* — the definition is unresolved, see above | — | blocked on [open-questions.md#oq-026](open-questions.md#oq-026) |

[source-backed | crm-hubspot:report-2026-08-kpi-verification | 2026-08-17] ^query-patterns-verified

Pipeline-specific reports — coverage, stage mix, source mix, win/loss — are not duplicated here. They live with the snapshot they produce, in [pipeline.md](pipeline.md#sourcing-reports), which is also where the one currently broken pipeline report is recorded. Access mechanics, object gotchas, and the field-hygiene table are in [crm.md](crm.md#access).

Known pitfalls, in the order they have actually bitten:

- **The GA4 window.** The reporting UI default lookback moved from 90 days to 30 on 2026-08-12 ([events.md](events.md#ev-ga4-lookback)). Every GA4 pull states its window explicitly; a report that accepted the default silently changed meaning mid-August. [source-backed | ga4:2026-08-17/blog-pages.csv | 2026-08-17] ^pitfall-ga4-window
- **Creation-dated versus close-dated.** Pipeline created is dated at creation; anything comparing it to revenue must re-window, not reuse the same period. Mixing the two produced the discrepancy behind the Q2 QBR figure. [confirmed | interview:priya-shah | 2026-07-20] ^pitfall-date-basis
- **Seat count is 38% empty on closed-won.** Any segmentation by seat band is unreadable until the hygiene backfill lands ([crm.md](crm.md#field-hygiene)); this is why the cycle-length-by-seat report is broken and why the sales-cycle number stays contested ([business-core.md](business-core.md#sales-cycle-length)). [source-backed | crm-hubspot:report-2026-08-cycle-by-seat-band | 2026-08-17] ^pitfall-seat-count-empty
- **Median, not mean.** Time to first dashboard and cycle length are both reported as medians. A mean on either invites a single migration to move the headline number. [confirmed | interview:morgan-lee | 2026-07-30] ^pitfall-median-only

## Reporting conventions

- Periods are calendar quarters, and the fiscal year is the calendar year. Monthly views exist for operating rhythm only and never appear in a board deck. [confirmed | interview:dana-okafor | 2026-07-16] ^convention-periods
- The default attribution model for every marketing report is the multi-touch model configured in Model Lab. When a report uses anything else, the model is named in the chart title — not in a footnote. [confirmed | interview:dana-okafor | 2026-07-16] ^convention-model-named
- Every number leadership sees carries its as-of date and its model. A number without both is not board-ready, and "board-ready by default" is a release theme we are supposed to live by ([product-releases.md](product-releases.md#theme-board-ready)). [confirmed | interview:dana-okafor | 2026-08-14] ^convention-asof-and-model
- The four charts leadership expects, in this order: pipeline created against target, coverage ratio against the 3.0× floor, channel contribution on the multi-touch model, and cost per opportunity trended over four quarters. [confirmed | interview:dana-okafor | 2026-07-16] ^convention-board-charts
- Rounding: whole percentages, dollar figures to the nearest thousand below $1M and to two significant figures above it. Never round a number in a direction that improves it. [confirmed | interview:morgan-lee | 2026-07-30] ^convention-rounding
