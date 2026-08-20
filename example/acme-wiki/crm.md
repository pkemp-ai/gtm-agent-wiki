---
type: runbook
description: How agents reach Acme's CRM, which fields in it can be trusted, the objects marketing actually uses, and the standard pulls — customer list, target accounts, win/loss, ownership — with their verification stamps.
owner: Morgan Lee (marketing ops)
sources: [crm-hubspot, interviews, slack-gtm]
update-cadence: monthly
staleness-horizon: 60d
evidence-as-of: 2026-08-17
last-verified: 2026-08-17
---

# CRM

Runbook: every access pattern below carries a `verified:` stamp from actually running it, and a pattern that fails is marked **broken** with its error rather than deleted (SPEC §8). What the pipeline currently *shows* is [pipeline.md](pipeline.md#snapshot); who owns which accounts is [account-ownership.md](account-ownership.md#ownership-map); what each number *means* is [metrics.md](metrics.md#kpi-definitions). This file is only how to reach the data and what not to trust when you get there.

## System of record

HubSpot is the system of record for contacts, companies, deals, and marketing email. There is no data warehouse and no reverse-ETL layer — the CRM is the end of the line, which is the honest reason our own read-only warehouse export is still a beta roadmap item ([product-releases.md](product-releases.md#roadmap-warehouse-export)).
[confirmed | interview:morgan-lee | 2026-07-30] ^system-of-record

Administration: Morgan Lee owns the portal, property definitions, and report library. Sales ops changes to deal stages go through Priya Shah. Nobody else creates properties — a run that needs a field it cannot find files an open question rather than adding one.
[confirmed | interview:morgan-lee | 2026-07-30] ^crm-admin

Acme's own product is connected to this portal as a customer of itself: attribution fields and campaign costs write back into HubSpot through the certified app ([partners.md](partners.md#partner-hubspot)). That means some CRM properties are *derived by our product*, not entered by a human — the hygiene table below marks which.
[confirmed | interview:morgan-lee | 2026-07-30] ^self-hosted-attribution

### Field hygiene — what to trust ^field-hygiene

The single most useful section of this file. A number is only as good as the property under it.

| Property | Trust | Why |
|---|---|---|
| Deal amount, stage, close date | High | Priya Shah reviews the board weekly; stage discipline is enforced |
| Company employee count | High on inbound, medium on outbound | Enriched on form fill; hand-entered on some named accounts |
| Lifecycle stage | High | Automated; the MQL definition in [metrics.md](metrics.md#kpi-mql) is implemented as a workflow, not a manual flag |
| Original source | Medium | Correct at first touch, but it is a *first-touch* field — never read it as an attribution answer |
| Attribution fields (multi-touch credit) | High | Written back by our own product; recomputed, so a value can change without a human editing it |
| Campaign cost | High since 2026-06-30 | Write-back shipped then; earlier periods are spreadsheet-era and should not be compared like-for-like |
| Seat count on closed-won | **Low — 38% empty** | The blocker behind the broken cycle-length report and the contested sales-cycle number |
| Deal owner on named accounts | **Low — 12% empty at the last pull** | Unowned accounts fall to the SDR queue; no sequence may assume this field is populated |
| Competitor field on deals | Medium | Populated on competitive deals, left blank when the rep forgets — presence is meaningful, absence is not |

[source-backed | crm-hubspot:report-2026-08-field-hygiene | 2026-08-17] ^field-hygiene-table

Two consequences worth stating plainly, because both have already produced wrong answers: absence in the competitor field is not evidence of no competitor, and a segmentation by seat band is not a small-sample problem, it is an empty-property problem ([metrics.md](metrics.md#pitfall-seat-count-empty)).

## Access

How agents connect. Credentials appear here by **environment-variable name only** — never a value, never a fragment of one (SPEC §15.3).

| What | How | Credential |
|---|---|---|
| Saved-report reads, object search | The tool declared for `crm-hubspot` in [sources.md](sources.md) | `HUBSPOT_PRIVATE_APP_TOKEN` |
| Portal identity for report URLs | Same connection | `HUBSPOT_PORTAL_ID` |
| Bulk CSV export (quarterly recomputes) | Portal UI export, run by a human, dropped in `intake/inbox/` | none — human-mediated |
| Fallback when the connection is down | Ask ops for a CSV export; do not screen-scrape the portal | none |

[source-backed | crm-hubspot:report-2026-08-access-check | 2026-08-17] ^access-verified

Scopes are read-only: `crm.objects.contacts.read`, `crm.objects.companies.read`, `crm.objects.deals.read`, `crm.lists.read`. Marketing agents have no write scope to the CRM, deliberately — a wiki-driven agent that could edit deal records would be a new and much worse category of problem than a stale wiki.
[confirmed | interview:morgan-lee | 2026-07-30] ^readonly-scopes

The credential lives in the ops vault at `vault://gtm/hubspot/marketing-wiki-reader` and is injected into runs as the env var above. Rotation is quarterly; a run that gets a 401 marks the source broken in [sources.md](sources.md) with its cursor held and escalates in the digest — it does not retry with another credential.
[confirmed | interview:morgan-lee | 2026-07-30] ^credential-location

## Core objects and fields

Only what marketing agents actually touch. The full property list is in the portal and does not belong in a wiki.

| Object | Fields marketing uses | Gotchas |
|---|---|---|
| Contact | email, lifecycle stage, original source, associated company, MQL date | A contact can be an MQL without its company being in the ICP — always read the company, not just the contact |
| Company | name, employee count, industry, CRM-in-use, paid-channel count, named-account flag, target-list refresh date | The named-account flag is rewritten monthly by the list refresh, so historical membership is not recoverable from this field |
| Deal | amount, stage, close date, competitor, seat count, partner-sourced flag, attribution credit | Seat count and competitor are the two fields most often empty; see hygiene above |
| List (`Named Accounts — current`) | membership | The list is the target-account definition made concrete ([growth.md](growth.md#target-accounts)); it is regenerated, not edited |
| Marketing email | send, open, reply, sequence membership | Sequence membership is the dedup signal every outbound run must check ([account-ownership.md](account-ownership.md#handoff-sla)) |

[confirmed | interview:morgan-lee | 2026-07-30] ^core-objects

PII discipline: agents may read contact-level records to answer questions, and may write **business-context facts only** into the wiki — companies, roles, deal facts. No names, emails, or title-plus-company combinations enter wiki files (SPEC §15.5), and nothing from here reaches outbound copy beyond the personalization fields whitelisted in [channel-styles.md](channel-styles.md#email).
[confirmed | interview:dana-okafor | 2026-08-05] ^crm-pii-discipline

## Standard queries

The five pulls the rest of the wiki depends on. Pipeline reports are not duplicated here — they live with the snapshot they produce, in [pipeline.md](pipeline.md#sourcing-reports).

| Question | Report | Status |
|---|---|---|
| Who are our customers, by tier and segment? | "Customer Base — active by tier" → [customers.md](customers.md#base-shape) | verified: 2026-08-15 |
| What is on the named-account list right now? | List `Named Accounts — current`, membership export → [growth.md](growth.md#target-accounts) | verified: 2026-08-15 |
| Which competitors show up, and how do we fare? | "H1 2026 Win/Loss — Competitor" → [competitors.md](competitors.md#metricflow-winloss) | verified: 2026-07-28 |
| Who owns which segment? | "Owner Map — segment and list" → [account-ownership.md](account-ownership.md#ownership-map) | verified: 2026-08-15 |
| What predicts churn and expansion? | "Retention by data-source count" and "H1 Churn — champion tenure" → [customers.md](customers.md#churn-signals) | verified: 2026-07-28 |

[source-backed | crm-hubspot:report-2026-08-owner-map | 2026-08-15] ^standard-queries-verified

Conventions for running these:

- **Never widen a pull to "everything".** Each report is scoped; a run that needs a different scope adds a report rather than exporting the object. [confirmed | interview:morgan-lee | 2026-07-30] ^query-scope-discipline
- **Archive before reasoning.** The CSV export of every run is written to `.archive/crm-hubspot/<run-id>/` before any synthesis, even though claim locators cite the report name rather than the file — the report is re-runnable, the export proves what it returned on the day (SPEC §11). [confirmed | interview:morgan-lee | 2026-07-30] ^archive-before-reasoning
- **Report renames break locators.** Renaming a saved report orphans every claim citing it. Renames go through Morgan and get a changelog line. [confirmed | interview:morgan-lee | 2026-07-30] ^report-rename-rule
