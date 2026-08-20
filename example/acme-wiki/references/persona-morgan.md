---
type: reference
description: Deep dive on Morgan, the marketing ops lead — the champion's real job, the objection sequence in order, the demo script that works, the onboarding path, and the words to avoid with them.
owner: Dana Okafor (CMO)
sources: [interviews, gong, crm-hubspot]
update-cadence: interview
staleness-horizon: 120d
evidence-as-of: 2026-08-17
last-verified: 2026-08-19
---

# Persona deep dive — Morgan, marketing ops lead

Parent: [icp-personas.md](../icp-personas.md#persona-morgan). The summary profile lives there; this page is the operating detail — what Morgan's week actually looks like, the objections in the order they arrive, and the demo and onboarding paths built around them.

Morgan is the champion and the power user. Dana signs ([icp-personas.md](../icp-personas.md#persona-dana)), Devon uses it daily ([icp-personas.md](../icp-personas.md#persona-devon)), and Morgan decides whether it survives month four. Deals where Morgan is the champion close roughly 1.4× more often than deals championed by the CMO — an unratified read, not yet usable in sequencing logic ([pipeline.md](../pipeline.md#trend-ops-champion), [open-questions.md#oq-028](../open-questions.md#oq-028)).

## What the job actually is

Morgan is the human API between the CRM, the ad platforms, and the spreadsheet the CMO shows the board. The work is not analysis — it is reconciliation, and it is invisible until it breaks.
[confirmed | interview:morgan-lee | 2026-06-27] ^pm-job-shape

- **The quarterly reconciliation.** First week of every quarter, rebuilding the same attribution spreadsheet by hand. This is the single most reliable pain to name out loud, and to name in the customer's words rather than ours — "spreadsheet hell, every first week of the quarter," which carries its own call provenance in [icp-personas.md](../icp-personas.md#cl-spreadsheet-hell). [confirmed | interview:morgan-lee | 2026-06-27] ^pm-quarterly-reconciliation
- **Being the person blamed when two dashboards disagree.** Morgan usually knows *why* they disagree and has no authority to make either one wrong. Naming the disagreement as a modeling difference rather than a data error is the moment trust arrives. [confirmed | interview:morgan-lee | 2026-06-27] ^pm-blame-position
- **Maintenance debt from the last tool.** Whatever is in place, Morgan inherited part of it and cannot fully explain part of it. Nobody wants to say that in a group call. [confirmed | interview:morgan-lee | 2026-06-27] ^pm-inherited-debt

## Triggers

| Trigger | What to lead with |
|---|---|
| A botched attribution report that reached leadership | The reconciliation, not the features — "how long did the rebuild take?" |
| A CRM migration, in progress or announced | Implementation lift and field mapping; do not pitch models yet |
| Being told to "just fix the numbers" | Model transparency: the numbers are not broken, the model is unnamed |
| A new CMO arriving with board reporting expectations | Board Pack export and the four-chart convention ([metrics.md](../metrics.md#convention-board-charts)) |
| Paid spend crossing roughly $60k/month | Channel-level answers are now worth someone's job |

[confirmed | interview:morgan-lee | 2026-06-27] ^pm-triggers

## Objections, in the order they arrive

Morgan's objections are sequential, not a menu. Answering the third one first reads as evasion of the first.

1. **"Who maintains this when it breaks?"**
   > You do, and that is the design. Models are configurable from the ops side without SQL and without a ticket to us. The honest version: the first configuration is ours, everything after is yours.

   [confirmed | interview:morgan-lee | 2026-06-27] ^pm-obj-maintenance

2. **"How much of my time does implementation take?"**
   > Median four business days from signature to a dashboard your team saved, across 61 implementations ([business-core.md](../business-core.md#claim-ttfd)). Your part is CRM access and a conversation about campaign naming. If your Salesforce org is messy, it is two to three weeks and we will say so in week one, not week three.

   [confirmed | interview:morgan-lee | 2026-07-30] ^pm-obj-implementation-time

3. **"What happens to the numbers I already reported?"**
   > They will change, and that is the point — but you get to see exactly why. We can show last-click and multi-touch side by side on the same quarter so you can walk leadership from the old number to the new one instead of announcing a discontinuity.

   [confirmed | interview:morgan-lee | 2026-06-27] ^pm-obj-existing-numbers

4. **"Does this write back into the CRM, or is it another dashboard?"**
   > Bidirectional with HubSpot: attribution fields and campaign costs land on the records ([business-core.md](../business-core.md#claim-hubspot-sync)). Salesforce is one-way today. If write-back to Salesforce is a hard requirement, we are probably not your tool yet.

   [confirmed | interview:morgan-lee | 2026-07-09] ^pm-obj-writeback

5. **"What about the touches we cannot see?"**
   > No doctrinal answer yet — do not improvise one. Acknowledge the question, say what the model does with untracked touches, and take the question back. This is the live gap ([icp-personas.md](../icp-personas.md#objection-dark-social), [open-questions.md#oq-021](../open-questions.md#oq-021)).

   Interim handling ratified while the doctrinal answer is missing: acknowledge, describe what the model does, take the question back. Do not fill the gap in the room.
   [confirmed | interview:dana-okafor | 2026-08-14] ^pm-obj-untracked-touches

## The demo script that works

Twenty minutes, Morgan-shaped. The structure matters more than the wording.

| Minutes | Move | Why |
|---|---|---|
| 0–3 | Ask what last quarter's reconciliation took, in hours | Establishes the problem in their number, not ours |
| 3–8 | Their own CRM fields on screen in a sandbox — not the demo org, their field names | The single highest-signal moment; the CTA is "See it on your data" for this reason ([channel-styles.md](../channel-styles.md#web-cta-language)) |
| 8–13 | One campaign, last-click next to multi-touch, with the delta explained | Turns the scary discontinuity into a controllable comparison |
| 13–17 | Model Lab: change the attribution window live, without SQL | Proves ops ownership rather than asserting it |
| 17–20 | Name one limit before they find it — Salesforce write-back, or the untracked-touch question | Limits-first is on-voice and it is what makes the rest believable ([voice.md](../voice.md#exemplar-limits)) |

[confirmed | interview:morgan-lee | 2026-07-30] ^pm-demo-script

Never open with the model philosophy, and never show the seeded demo org to Morgan — it invites "but our data is messier than that," which is both true and unanswerable in a demo. Real customer dashboards are prohibited outright ([compliance-guardrails.md](../compliance-guardrails.md#demo-org-only)); a sandbox with their own field names is the middle path.
[confirmed | interview:morgan-lee | 2026-07-30] ^pm-demo-antipatterns

## What convinces, and what closes

- **A reference call with another ops lead**, not with a CMO. Morgan wants to ask the maintenance question of someone who has lived it. Fernhill Logistics and Brightpath HR both have ops leads willing to take these calls; the approval fact and how to arrange one live in [customers.md](../customers.md#reference-calls). [confirmed | interview:dana-okafor | 2026-08-14] ^pm-reference-call
- **The migration guide, read alone, before any call.** "Out of the Spreadsheet" is the asset that does the most unattended work on this persona ([content-assets.md](../content-assets.md#evergreen-inventory)). [confirmed | interview:morgan-lee | 2026-08-17] ^pm-migration-guide
- **An Attribution Teardown recording** where someone else's setup gets rebuilt live. It is proof by demonstration and it costs Morgan nothing to watch ([growth.md](../growth.md#campaign-frames)). [confirmed | interview:morgan-lee | 2026-08-17] ^pm-teardown-proof

## Onboarding path

The first thirty days, because they determine retention. Accounts that never connect a second data source inside 60 days churn at roughly 3× the base rate, and Morgan is the person who either connects it or does not ([customers.md](../customers.md#churn-single-source)).

| Day | Milestone |
|---|---|
| 0–1 | CRM connected, campaign naming reviewed |
| 2–4 | First dashboard saved by someone at the customer — the moment the time-to-first-dashboard clock stops ([metrics.md](../metrics.md#kpi-ttfd)) |
| 5–10 | Second data source connected. This is the retention milestone, not a nice-to-have |
| 10–20 | One model configured by Morgan without our help, deliberately unassisted |
| 20–30 | First reconciliation-free reporting cycle; Morgan shows the numbers to Dana |

[confirmed | interview:morgan-lee | 2026-07-30] ^pm-onboarding-path

Build a second champion inside the account before day 60. Champion departure precedes churn in most of the accounts we have lost, and flattering the first champion is not a retention strategy ([customers.md](../customers.md#churn-champion-departure)).
[confirmed | interview:dana-okafor | 2026-08-14] ^pm-second-champion

## Words to avoid with this persona

Beyond the standing bans in [glossary.md](../glossary.md#banned-words):

| Avoid | Say instead | Why |
|---|---|---|
| "single source of truth" | "the model your CRM uses" | Morgan has been promised this before, by the tool they are currently maintaining |
| "set it and forget it" | "configurable by you, without SQL" | Reads as a claim they will personally be left holding |
| "easy" | the actual number of days, with the messy-CRM caveat | Morgan's job exists because it is not easy |
| "insights" | the question the number answers | Insight is what Morgan is expected to produce; a tool claiming it is competing with them |

[confirmed | interview:morgan-lee | 2026-07-30] ^pm-words-to-avoid
