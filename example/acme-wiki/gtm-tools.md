---
type: runbook
description: Acme's GTM stack — what each tool is for, who owns it, whether agents can reach it and how, the data flows that explain why two tools disagree, and what has stopped working.
owner: Morgan Lee (marketing ops)
sources: [slack-gtm, interviews, crm-hubspot, ga4, webflow]
update-cadence: monthly
staleness-horizon: 90d
evidence-as-of: 2026-08-17
last-verified: 2026-08-17
---

# GTM tools

Runbook: each row's `verified` stamp comes from actually exercising the access, and access that stops working moves to [Broken / deprecated](#broken--deprecated) with its error rather than being deleted (SPEC §8). Credentials appear as environment-variable names only (SPEC §15.3).

Eleven tools, plus one retired that stays on the record. The useful part of this file is not the list — it is the flow map underneath it, which is what to read when two numbers disagree.

## Stack

| Tool | What it is for | Owner | Agent access | Verified |
|---|---|---|---|---|
| HubSpot | CRM and system of record; marketing email lives here too | Morgan Lee | Read-only, per [crm.md](crm.md#access) — `HUBSPOT_PRIVATE_APP_TOKEN` | 2026-08-17 |
| Acme Analytics (own product) | Attribution model and the Journeys view; writes attribution fields and campaign cost back into HubSpot | Morgan Lee | Read via the HubSpot write-back fields; no separate agent connection | 2026-08-17 |
| Gong | Call recording and transcripts; the source of customer phrasing | Priya Shah | Read-only transcript search — `GONG_ACCESS_KEY` | 2026-08-13 |
| Slack | Where GTM decisions get announced before they get documented | Sam Whitfield | Read-only search over `#gtm`, `#product-launches`, `#wins` | 2026-08-19 |
| GA4 | Sessions and on-site behavior | Morgan Lee | Read-only reporting — `GA4_CREDENTIALS_PATH` | 2026-08-17 |
| Webflow | Website and blog CMS; all public pages and forms | Morgan Lee | Read-only page and collection listing — `WEBFLOW_API_TOKEN` | 2026-08-17 |
| Customer.io | Lifecycle email, nurture, and the named-account sequences | Devon Park | **No agent access.** Sequence changes are human-only, on purpose — an agent that can send is an agent that can send twice | 2026-08-17 |
| LinkedIn Ads | Paid social; distribution for proof assets | Devon Park | **No agent access.** Spend reaches the wiki through campaign-cost write-back into HubSpot | 2026-08-17 |
| Google Ads | Paid search; branded and high-intent category terms | Devon Park | **No agent access.** Same write-back path as LinkedIn Ads | 2026-08-17 |
| Google Drive | Sales assets, decks, one-pagers, case-study drafts | Dana Okafor | **No agent access.** Humans drop what the wiki needs into `intake/inbox/` | 2026-08-17 |
| Webinar platform | Attribution Teardown delivery and recordings | Devon Park | **No agent access.** Registration data reaches the CRM via a native sync | 2026-08-14 |

[source-backed | crm-hubspot:report-2026-08-access-check | 2026-08-17] ^stack-verified

Three notes that matter more than the table:

- **"No agent access" is a decision, not a gap.** Every send-capable and spend-capable tool is deliberately outside agent reach. An agent may draft a sequence and hand it to a human; it may not own the button. [confirmed | interview:dana-okafor | 2026-08-14] ^no-send-access-by-design
- **The declared connections are the only connections.** Access this file does not list does not exist for agents, whatever a harness happens to have available. The manifest in [sources.md](sources.md) is the authority on what may be reached and how often. [confirmed | interview:morgan-lee | 2026-07-30] ^declared-access-only
- **Our own product is in the stack and is not authoritative over the CRM.** It models CRM data; when the model and the CRM totals disagree, the CRM wins on totals and the model wins on credit ([metrics.md](metrics.md#where-data-lives)). [confirmed | interview:morgan-lee | 2026-07-30] ^own-product-not-authoritative

## Data flows

Read this before believing any two numbers should match. Arrows are "feeds", and every arrow is a place where a definition can change.

```text
LinkedIn Ads ─┐
Google Ads ───┼─► campaign cost ──► HubSpot ◄── Webflow forms
              │                       ▲  │
GA4 ◄─ site ──┘                       │  └─► Customer.io (sequences, nurture)
                                      │
Gong (call activity) ─────────────────┤
                                      │
Webinar platform (registrations) ─────┘
                                      │
                          Acme Analytics (model)
                                      │
                    attribution credit + cost ──► back into HubSpot
```

The four disagreements this map explains, each of which has cost someone an afternoon:

| Symptom | Cause |
|---|---|
| GA4 sessions far exceed CRM-visible sessions | The CRM only sees sessions it can stitch to a known contact. The gap is anonymous traffic, not lost data |
| GA4 and our own Journeys view credit different channels | GA4 is last-click by default; Journeys is the configured multi-touch model. Both are correct for their model — this is the product thesis, not a bug ([voice.md](voice.md#exemplar-models-post)) |
| Spend in the ad platform UI differs from campaign cost in the CRM | The write-back snapshots spend at sync time; platforms restate spend afterwards. Reports use the snapshot |
| Webinar registrant counts differ between the platform and the CRM | The native sync drops registrants whose email does not resolve to a contact or company record |

[confirmed | interview:morgan-lee | 2026-08-17] ^flow-disagreements

One flow change worth knowing about even though it is not ours: GA4's reporting UI default lookback moved from 90 days to 30 on 2026-08-12, so any GA4 pull that accepted the default silently changed meaning ([events.md](events.md#ev-ga4-lookback), pitfall recorded in [metrics.md](metrics.md#pitfall-ga4-window)).
[confirmed | slack-gtm:2026-08-12/dump.json#msg-5120 | 2026-08-12] ^flow-ga4-lookback

## Broken / deprecated

Entries move here and stay. A deleted entry destroys the record of what used to work and why the data before a certain date looks different.

### Clearpath Forms — **BROKEN**, retired ^broken-clearpath-forms

The legacy landing-page and form builder Acme used before the site moved to Webflow. Retired by the vendor on 2026-07-31; the account is closed and the API is gone.

- **Failure note:** attempted 2026-08-17 — `GET /v2/forms/{id}/submissions` returns `410 Gone` with body `{"error":"account_closed"}`. Retried once on the same day with the same result. Credential `CLEARPATH_API_KEY` has been removed from the ops vault; do not restore it, and do not re-add this tool to [sources.md](sources.md).
- **What is lost:** form-fill records created before 2026-06-01 exist only as the contacts they created in HubSpot. The submission-level detail — which variant, which referrer — is not recoverable from anywhere.
- **What this explains:** the three landing pages with no campaign attached and no inbound links ([content-assets.md](content-assets.md#gap-orphan-landing-pages)) are Clearpath pages that were migrated as HTML and never rewired. They still collect form fills into no sequence. Fixing them is a Webflow-and-Customer.io task, not a Clearpath one.
- **Do not** compare pre-June and post-June form conversion rates as a trend. The measurement changed, not the performance.

[confirmed | slack-gtm:2026-08-12/dump.json#msg-5117 | 2026-08-12] ^clearpath-retirement-note

### Deprecated, still reachable ^deprecated-still-reachable

- **HubSpot "Original Source" as an attribution answer.** Not broken — deprecated *as a use*. It is a first-touch field and reading it as attribution is how the two marketing-sourced numbers came to disagree ([pipeline.md](pipeline.md#marketing-sourced-share)). Read it as first touch or not at all. [confirmed | interview:morgan-lee | 2026-07-30] ^deprecated-original-source
- **The pre-Model-Lab demo org.** Still exists, still loads, shows the old interface. Demo assets come from the current seeded demo org only ([compliance-guardrails.md](compliance-guardrails.md#demo-org-only)). [confirmed | interview:morgan-lee | 2026-07-30] ^deprecated-old-demo-org
