---
type: state
description: How Acme's sales team is resourced against accounts — coverage model, which role owns which segment, and the handoff rules marketing routing must respect.
owner: Priya Shah (VP Sales)
sources: [crm-hubspot, interviews]
update-cadence: monthly
staleness-horizon: 60d
evidence-as-of: 2026-08-15
last-verified: 2026-08-19
---

# Account ownership

Role and team granularity only. No individual quota or performance data enters this wiki, and no personal contact data (SPEC §15.5) — the account list itself is CRM data, queried per [crm.md](crm.md#standard-queries). What marketing needs from this file is routing and timing: who owns a given account, and what marketing must not do while they own it.

## Coverage model

- Sales is 6 AEs, 4 SDRs, and 2 CSMs under Priya Shah. There are no geographic territories: the split is segment plus the named-account list. [confirmed | interview:priya-shah | 2026-07-20] ^coverage-shape
- Named accounts: the 400-account list ([growth.md](growth.md#target-accounts)) is divided into two SDR pods by segment, roughly 100 accounts per SDR. Pod assignment follows the list refresh, so an account can change hands monthly. [confirmed | interview:priya-shah | 2026-07-20] ^named-account-split
- Inbound is routed by employee count rather than by source, which is why a self-serve trial from a 900-person company lands with an AE and not in nurture. [confirmed | interview:priya-shah | 2026-07-20] ^inbound-routing-basis

## Ownership map

| Segment / list | Owner (role) | What marketing must respect |
|---|---|---|
| Named accounts (400) | SDR pods A and B, split by segment | No marketing email to a named account inside an active sequence window — the pod owner's sequence wins |
| Inbound, 100–400 employees | Mid-market AE pod | Standard MQL handoff; the demo CTA is "See it on your data" ([channel-styles.md](channel-styles.md#web)) |
| Inbound, 400–1,000 employees | Upper-mid AE pod | Security review shows up early in these deals ([pipeline.md](pipeline.md#snapshot)); lead with SOC 2 Type II in the first touch |
| Inbound, under 100 employees | SDR triage with an ICP-floor check | The floor is contested ([icp-personas.md](icp-personas.md#icp-employee-floor)) — triage, do not auto-reject |
| Existing customers | CSM, expansion motion | Retention and expansion copy follows the patterns in [customers.md](customers.md#churn-signals) |
| Partner referrals | AE pod by segment, partner-sourced flag set | Partner rules in [partners.md](partners.md#partner-referral); a referred account is never also outbounded |

[source-backed | crm-hubspot:report-2026-08-owner-map | 2026-08-15] ^ownership-map-current

12% of named accounts had no owner in the 2026-08-15 pull. Unowned accounts fall to the SDR queue, ops is reconciling, and no sequence may assume an owner field is populated.
[source-backed | crm-hubspot:report-2026-08-owner-map | 2026-08-15] ^unowned-named-accounts

## Handoff rules

- Lifecycle: subscriber → lead → MQL → SQL → opportunity. Marketing owns everything through MQL. The MQL definition itself is a KPI definition ([metrics.md](metrics.md#kpi-definitions)), not a marketing preference to be adjusted campaign by campaign. [confirmed | interview:priya-shah | 2026-07-20] ^handoff-lifecycle
- SLA: SDR first touch within one business day of MQL. Nurture pauses while an account sits in an active SDR sequence — this is the dedup rule every outbound agent checks before sending, and the most common way marketing steps on sales. [confirmed | interview:priya-shah | 2026-07-20] ^handoff-sla
- Named accounts never enter the self-serve nurture. They get the 4-touch outbound sequence and then exit ([channel-styles.md](channel-styles.md#email)); re-entry requires a new trigger ([growth.md](growth.md#target-account-definition)). [confirmed | interview:morgan-lee | 2026-07-30] ^handoff-named-accounts
- Recycled accounts return to nurture 30 days after sequence exit, and only into educational sends — no promotional sequence follows a failed outbound run. [confirmed | interview:morgan-lee | 2026-07-30] ^handoff-recycle
- Closed-lost re-entry is a sales decision, not a marketing trigger: a lost account re-enters outbound only when the AE names the new trigger. [confirmed | interview:priya-shah | 2026-07-20] ^handoff-closed-lost

## Contested

None currently. A restructure appears here only once it is visible in the CRM (S-class); a plan stated in a meeting is an open question until then. Collisions land here the day they appear, each with a resolution path into [open-questions.md](open-questions.md#active).
