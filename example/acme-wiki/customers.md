---
type: state
description: Who Acme's customers are, which may be named publicly and with what approvals, which success stories are usable, and the churn patterns retention copy should know.
owner: Dana Okafor (CMO)
sources: [crm-hubspot, interviews, inbox-docs, reviews-web]
update-cadence: weekly
staleness-horizon: 60d
evidence-as-of: 2026-08-17
last-verified: 2026-08-19
---

# Customers

Business-context facts only, per SPEC §15.5: companies, roles, deal facts. Individual contact data stays in the CRM — query patterns in [crm.md](crm.md). Customer approval is per-number, not per-logo ([compliance-guardrails.md](compliance-guardrails.md#banned-claims)).

## Customer base

112 active customers as of 2026-08-15: 71% Growth, 26% Scale, 3% Enterprise.
[source-backed | crm-hubspot:report-2026-08-customer-base | 2026-08-15] ^base-shape

HR tech and security together are 38% of the base; logistics and supply-chain SaaS is the fastest-growing slice — 6 of the last 15 closed-won.
[source-backed | crm-hubspot:report-2026-08-customer-base | 2026-08-15] ^base-segments

Notable logos: Brightpath HR, Corvid Security, Lumastone, Fernhill Logistics. Public-use rules per logo below — the logo list is not blanket permission.
[confirmed | interview:dana-okafor | 2026-08-14] ^base-logos

## Reference customers

What each customer has approved for public use. Approval facts are H-class; nothing beyond the listed scope may be used, whatever other evidence exists.

| Customer | Logo | Quote | Numbers | Case study | Limits |
|---|---|---|---|---|---|
| Brightpath HR | yes | yes | the 31% cost-per-opportunity claim only ([business-core.md](business-core.md#claim-brightpath-cpo)) | published | re-approve numbers at the 2027-01 renewal |
| Corvid Security | integrations page only | no | anonymized only — "a mid-market security vendor" | no | regulated customer: [compliance-guardrails.md](compliance-guardrails.md#regulated-constraints) |
| Lumastone | yes | the board-deck quote in the case draft | not yet — pending their legal review | in production | nothing publishes before written sign-off lands in intake/inbox/ |
| Fernhill Logistics | yes | verbal only — not usable in writing | no | no | Teardown #5 recording reuse approved, full session only, no clipped excerpts |

[confirmed | interview:dana-okafor | 2026-08-14] ^reference-approvals

Reference calls are not public use, so they are not in the table: Brightpath HR and Fernhill Logistics each have an ops lead willing to take one, arranged through the AE and never offered in writing to a prospect list. Used in the Morgan motion → [references/persona-morgan.md](references/persona-morgan.md#pm-reference-call).
[confirmed | interview:dana-okafor | 2026-08-14] ^reference-calls

## Success stories

One entry per usable story: the result, its substantiation, and where the asset lives ([content-assets.md](content-assets.md) is the catalog; this file is the substance).

### Brightpath HR — 31% lower cost per opportunity in two quarters ^story-brightpath
- The flagship story and the only customer numbers approved for public copy. Exact claim wording is governed by [business-core.md](business-core.md#claim-brightpath-cpo).
- Mechanism: moved spend from two channels that created clicks into three that created pipeline — the ratified phrasing lives in [voice.md](voice.md#exemplars).
- Asset: published case study → [content-assets.md](content-assets.md#case-studies).
- [confirmed | interview:dana-okafor | 2026-07-23]

### Lumastone — board reporting from 9 days to 2 ^story-lumastone
- Consolidated five reporting tools into one; time from quarter close to board-ready numbers fell from 9 days to 2. Customer-verified in the case-study draft; not publishable until their legal sign-off.
- [confirmed | doc:lumastone-case-draft-2026-08.md | 2026-08-07]
- Asset: case study in production → [content-assets.md](content-assets.md#case-studies).

### Corvid Security — enterprise security review passed in 3 weeks ^story-corvid
- Useful in enterprise outreach, where SOC 2 leads the first touch ([channel-styles.md](channel-styles.md#email)). Anonymized use only: "a mid-market security vendor," never named with numbers.
- [confirmed | interview:priya-shah | 2026-08-04]

### Fernhill Logistics — the live Teardown story ^story-fernhill
- Attribution Teardown #5 (2026-07-16) rebuilt their setup on air; they reallocated Q3 paid budget two weeks later. Verbal results only — no written numbers approved, so the story runs as narrative, not claims.
- [confirmed | interview:morgan-lee | 2026-08-17]
- Asset: recording approved for reuse, full session only → [content-assets.md](content-assets.md).

## Churn signals <!-- tier: state, sensitive --> ^churn-signals

Patterns worth knowing when writing retention and expansion copy. Never used externally in any form.

- Accounts that never connect a second data source inside 60 days churn at roughly 3× the base rate — onboarding follow-through is the retention lever. [source-backed | crm-hubspot:report-2026-q2-retention | 2026-07-10] ^churn-single-source
- Champion departure precedes churn: in 7 of 11 H1 churned accounts, the ops power user left first. Expansion copy should build a second champion, not flatter the first. [source-backed | crm-hubspot:report-2026-h1-churn | 2026-07-28] ^churn-champion-departure
- Two reviews this quarter mention dashboards slowing after the June update. Single-signal review chatter — tracking only; becomes an open question if a third signal lands. [watchlist | reviews-web:2026-08-08/acme-reviews.json#rev-2091 | 2026-08-08] ^churn-perf-chatter

Retention of the sub-100-employee cohort is the live test for the ICP floor — contested at [icp-personas.md](icp-personas.md#icp-employee-floor), tracked as [open-questions.md#oq-018](open-questions.md#oq-018).

## Contested

None currently. A collision here — say, an approval a rep remembers more generously than this file records — goes contested the day it appears and links into [open-questions.md](open-questions.md#active). Until then, this file's scope wins.
