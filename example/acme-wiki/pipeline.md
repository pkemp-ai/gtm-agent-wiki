---
type: state
description: The pipeline picture agents may cite — coverage, stage mix, notable movements as of the last refresh — the multi-period trend reads, and the exact reports that produce all of it.
owner: Priya Shah (VP Sales)
sources: [crm-hubspot, gong, interviews, inbox-docs]
update-cadence: weekly
staleness-horizon: 30d
evidence-as-of: 2026-08-19
last-verified: 2026-08-19
---

# Pipeline

Internal numbers. Nothing in this file is a customer-facing claim — the claims agents may make in public live in [business-core.md](business-core.md#approved-claims), and they are a different, much shorter list. Deal-level detail stays in the CRM; what any of this *means* for strategy goes to [growth.md](growth.md) through an open question, never by direct edit.

## How to source <!-- tier: runbook -->

The reports that produce pipeline truth, in the order a refresh runs them. Access mechanics — connection, credential locations, object gotchas — are in [crm.md](crm.md#access); the attribution model each report uses is defined in [metrics.md](metrics.md#reporting-conventions). A report that runs stamps `verified`; one that fails is marked **broken** with its error and is never deleted.

| What it answers | HubSpot report name | Status |
|---|---|---|
| Coverage against the quarter's new-ARR target | "Q3 2026 — Pipeline Coverage (marketing view)" | verified: 2026-08-17 |
| Stage mix across open deals | "Deal Stage Distribution — rolling 90d" | verified: 2026-08-17 |
| Marketing-sourced share by channel | "Pipeline by Original Source (multi-touch overlay)" | verified: 2026-08-17 |
| Competitive presence in open and closed deals | "H1 2026 Win/Loss — Competitor" | verified: 2026-07-28 |
| Partner-sourced share | "Partner Referrals — sourced pipeline" | verified: 2026-08-15 |
| Cycle length by seat band | "Cycle Length by Seat Band" | **broken** — attempted 2026-08-17 |

[source-backed | crm-hubspot:report-2026-q3-coverage | 2026-08-17] ^sourcing-reports

**Broken:** "Cycle Length by Seat Band" returns a population too small to read — the seat-count property is empty on 38% of closed-won deals, so the segmentation buckets are unusable. This is the report that would resolve the contested sales-cycle number ([business-core.md](business-core.md#sales-cycle-length)); the resolution path is a data-hygiene task, not an analysis task. Do not substitute the unsegmented 45-day figure while this is broken.
[source-backed | crm-hubspot:report-2026-08-cycle-by-seat-band | 2026-08-17] ^broken-cycle-by-seat

## Snapshot

**As of 2026-08-15.** Replaced wholesale at each refresh — this section is defined as "current as-of," which is the one place recency legitimately wins. If the as-of date above is more than two weeks old, cite nothing from here without re-running the coverage report.

- Open pipeline is $1.72M against a $480k Q3 new-ARR target: 3.6× coverage, against a 3.0× floor. [source-backed | crm-hubspot:report-2026-q3-coverage | 2026-08-15] ^snap-coverage
- 63 open opportunities, median open deal size $27k — consistent with the blended ACV band in [business-core.md](business-core.md#acv-bands). [source-backed | crm-hubspot:report-2026-q3-coverage | 2026-08-15] ^snap-deal-count
- Stage mix: 44% discovery, 31% evaluation, 18% proposal or security review, 7% contracting. [source-backed | crm-hubspot:report-2026-08-stage-mix | 2026-08-15] ^snap-stage-mix
- Marketing-sourced share of open pipeline is 61% on the multi-touch overlay — a number that is itself contested, see below. Partner-sourced is 9% ([partners.md](partners.md#referral-pipeline-share)). [source-backed | crm-hubspot:report-2026-q3-source-mix | 2026-08-15] ^snap-source-mix
- Notable movements: two upper-mid deals entered security review in the first half of August, and DashForge is named in 4 of the 63 open deals — the encroachment tracked in [competitors.md](competitors.md#dashforge-encroaching), now visible in current open pipeline rather than only in H1 win/loss. [source-backed | crm-hubspot:report-2026-08-stage-mix | 2026-08-15] ^snap-movements

## Trends

Multi-period reads. These are agent synthesis across refreshes — `inferred` until a human ratifies them, and not usable in copy or in sequencing logic while they carry that label.

- Deals where the champion is the marketing ops lead close more often than deals championed by the CMO — roughly 1.4× across the last three quarters. If it holds, the Morgan-first message ordering in outbound is right and the Dana-first ordering is a habit. [inferred | inference:maintain | 2026-08-19] ^trend-ops-champion

  → awaiting ratification: [open-questions.md#oq-028](open-questions.md#oq-028)

- Pipeline creation clusters in the first three weeks of each month, tracking the Teardown webinar cadence ([events.md](events.md#log)). Correlation only: the webinar is also when the outbound sequences run, and nothing here separates the two. [inferred | inference:maintain | 2026-08-19] ^trend-teardown-cadence
- Security review is arriving before procurement in upper-mid deals, not after it — which makes the SOC 2 first-touch rule ([channel-styles.md](channel-styles.md#email-soc2-first-touch)) a pipeline mechanic rather than a courtesy. One call states it outright (gong:call-8934, 2026-08-06); the rest is a read across the last three refreshes and the two deals now in review, so the reading stays unratified. [inferred | inference:maintain | 2026-08-19] ^trend-early-security-review
- Q3 is tracking above the coverage floor for the first quarter in three; the honest caveat is that two upper-mid deals account for 31% of open value, so the floor is one slip away. [inferred | inference:maintain | 2026-08-19] ^trend-coverage-concentration

## Contested

### Is marketing-sourced pipeline 61% or 48%? ^marketing-sourced-share

- 61%, from "Pipeline by Original Source" with the multi-touch overlay applied. [source-backed | crm-hubspot:report-2026-q3-source-mix | 2026-08-15]
- 48%, the figure Priya presented in the Q2 QBR, using last touch on the opportunity record. [confirmed | doc:q2-2026-qbr-deck.md | 2026-07-24]
- Both numbers are correct for their model, which is the whole argument we sell — and precisely why we may not pick one quietly. An H-versus-S collision (SPEC §7.4): resolution requires naming one model for the "marketing-sourced" KPI in [metrics.md](metrics.md#kpi-definitions), not choosing the friendlier figure. Until then, neither number appears in a board deck, a post, or a plan. → [open-questions.md#oq-026](open-questions.md#oq-026)
