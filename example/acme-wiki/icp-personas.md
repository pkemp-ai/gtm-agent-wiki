---
type: doctrine
description: Who Acme sells to and refuses to sell to, what each buying persona cares about and objects to, and the words customers actually use.
owner: Dana Okafor (CMO)
sources: [interviews, crm-hubspot, gong]
update-cadence: interview
staleness-horizon: 120d
evidence-as-of: 2026-08-06
last-verified: 2026-08-19
---

# ICP and personas

## ICP

A qualified account matches all five criteria:

| Criterion | Definition |
|---|---|
| Segment | B2B SaaS |
| Size | 100–1,000 employees |
| Marketing team | 5+ people, with a dedicated ops function or clear intent to hire one |
| CRM | HubSpot or Salesforce |
| Channel mix | 3+ paid channels running concurrently |

[confirmed | interview:dana-okafor | 2026-06-20] ^icp-definition

Highest-intent stack signal we know: HubSpot plus Gong plus a paid-social pixel. Target-list construction rules live in [growth.md](growth.md#target-accounts).
[confirmed | interview:dana-okafor | 2026-06-20] ^icp-stack-signals

## Anti-ICP

We decline or deprioritize these outright — history says they churn or consume support:

| Who | Why we avoid them |
|---|---|
| B2C and ecommerce | The data model is B2B-pipeline-shaped; retrofitting it for cart economics fails, and they churn inside two quarters |
| Companies under 20 employees | No ops function to own the tool; onboarding stalls and never recovers |
| Agencies seeking white-label | No white-label offer exists and none is planned; saying yes creates support debt and channel confusion |

[confirmed | interview:dana-okafor | 2026-06-20] ^anti-icp

## Personas

Persona names are internal shorthand for buyer archetypes, not real people. Three of them collide with the first names of Acme colleagues, so the reading convention across this wiki is: a bare first name — Dana, Morgan, Devon — is the persona; an Acme colleague is written in full (Dana Okafor, Morgan Lee, Devon Park).

### Dana — data-driven CMO (economic buyer) ^persona-dana

- Cares about: numbers that survive a board meeting; defending the budget with revenue evidence.
- Pains: every channel reports its own flattering numbers; the CFO trusts none of them.
- Triggers: a board question she couldn't answer; planning season; a new CFO.
- Objections: "Is this another dashboard my team ignores?" — answered with CRM write-back and board-deck exports, not features.
- What convinces: her own pipeline on screen in the first call; the Brightpath HR numbers ([business-core.md](business-core.md#claim-brightpath-cpo)).

[confirmed | interview:dana-okafor | 2026-06-27] ^persona-dana-profile

### Morgan — marketing ops lead (champion, power user) ^persona-morgan
<!-- primary: true -->

- Cares about: implementation lift, data hygiene, not being blamed when numbers disagree.
- Pains: maintaining attribution spreadsheets by hand; being the human API between systems.
- Triggers: a botched attribution report; a CRM migration; being told to "just fix the numbers."
- Objections: "Who maintains this when it breaks?" — answered with the 4-day implementation median and ops-owned configuration.
- What convinces: a sandbox with their own CRM fields; a reference call with another ops lead.

[confirmed | interview:morgan-lee | 2026-06-27] ^persona-morgan-profile

Deep dive — demo script, objection handling, onboarding sequence: [references/persona-morgan.md](references/persona-morgan.md).

### Devon — demand-gen manager (daily user) ^persona-devon

- Cares about: channel-level answers this week, not model philosophy.
- Pains: reallocating budget on gut feel; last-click undercounting the channels Devon runs.
- Triggers: a channel that "stopped working" with no explanation; quarterly budget reviews.
- Objections: "Will this contradict the numbers I already reported?" — acknowledge it directly: it usually will, and that is the point.
- What convinces: one of their own campaigns shown multi-touch next to its last-click number.

[confirmed | interview:dana-okafor | 2026-06-27] ^persona-devon-profile

Morgan is the **primary** persona: outbound, demo scripts, and one-asset copy default to her unless the brief names Dana (economic buyer) or Devon (daily user) instead. There is no channel persona — Acme sells direct, not through a partner sales force.

### Dark social / untracked touches — no ruling ^objection-dark-social

**Not doctrine, deliberately absent:** prospects keep asking whether we capture "dark social" — touches that surface as direct traffic. There is no ratified answer, so no persona above carries this objection and no copy may answer it. The call evidence, the frequency, and the proposed wording all sit with the question: [open-questions.md#oq-021](open-questions.md#oq-021). Interim handling in a live call — acknowledge, say what the model does, take the question back — is ratified in [references/persona-morgan.md](references/persona-morgan.md#pm-obj-untracked-touches).

## Customer language <!-- tier: state -->

Verbatim phrases from calls, usable in copy. The terminology rulings derived from them live in [glossary.md](glossary.md#terms-customers-use); these are the phrases as evidence — which is why this section is marked `state` inside a doctrine file (SPEC §6): each claim asserts that a phrase *was said*, the transcript as a record, and not that what the customer said is true ([sources.md](sources.md)).

- "We're flying blind between HubSpot and the board deck." [source-backed | gong:call-7743 | 2026-07-08] ^cl-flying-blind
- "Spreadsheet hell, every first week of the quarter." [source-backed | gong:call-8102 | 2026-07-22] ^cl-spreadsheet-hell
- "I can't tell which half of the paid budget is doing anything." [source-backed | gong:call-8467 | 2026-08-06] ^cl-paid-budget

## Contested

### Is the 100-employee ICP floor real? ^icp-employee-floor
- The floor is 100 employees; below that there is no ops function to own the tool [confirmed | interview:dana-okafor | 2026-06-20]
- 9 of 41 H1 2026 closed-won accounts were between 60 and 99 employees, and their onboarding times match the median [source-backed | crm-hubspot:report-2026-h1-wins | 2026-07-28]
- Resolution path: check two-quarter retention of the sub-100 cohort; a floor change requires Dana Okafor's ratification, not a trend line. → [open-questions.md#oq-018](open-questions.md#oq-018)
