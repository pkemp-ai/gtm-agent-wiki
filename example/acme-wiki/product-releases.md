---
type: state
description: What Acme shipped and its marketing angle, the narratives current releases support, and the only roadmap items cleared for external use.
owner: Dana Okafor (CMO)
sources: [slack-gtm, webflow, interviews, inbox-docs]
update-cadence: per-run
staleness-horizon: rolling — 90d, monthly roll-ups
evidence-as-of: 2026-08-19
last-verified: 2026-08-19
---

# Product releases

A capped log on the same terms as [events.md](events.md): rolling 90-day window, monthly roll-ups (SPEC §13). What a release *implies* for positioning is never written into [business-core.md](business-core.md) from here — it goes to [open-questions.md](open-questions.md#active) first and waits for a human.

## Current release themes

The narratives current releases support. Three, deliberately — a fourth would mean we are shipping without a story.

1. **Ops owns the model.** Everything that moves configuration from engineering to marketing ops. This is the theme Morgan buys ([icp-personas.md](icp-personas.md#persona-morgan)) and the one that substantiates the approved no-data-team claim. [confirmed | interview:dana-okafor | 2026-08-14] ^theme-ops-owns-model
2. **Board-ready by default.** Export, reporting, and rounding-that-survives-scrutiny work. Dana's theme; it feeds the Board-Ready campaign frame ([growth.md](growth.md#campaign-frames)). [confirmed | interview:dana-okafor | 2026-08-14] ^theme-board-ready
3. **The CRM is the destination, not just the source.** Write-back depth. In public copy this theme is HubSpot-only ([business-core.md](business-core.md#claim-hubspot-sync)) — the Salesforce half is not sayable. [confirmed | interview:dana-okafor | 2026-08-14] ^theme-crm-destination

## Shipped

Newest first: what shipped, the marketing angle in one line, and the announcement of record.

#### 2026-08-11 · Board Pack export

Exports the revenue view as a slide-ready pack. Angle: the board section without the manual rebuild — the product half of the Board-Ready frame.
[source-backed | slack-gtm:2026-08-11/dump.json#msg-5098 | 2026-08-11] ^rel-board-pack

Announcement: <https://acme-analytics.example/changelog/board-pack-export>. Log line: [events.md](events.md#log).

#### 2026-07-28 · Journeys: seat-band filters

Journeys can now be filtered by seat band. Angle for Devon and Morgan: "does this hold for our bigger deals?" becomes a filter instead of a CSV export. Internally it is the unblock path for the contested sales-cycle number ([business-core.md](business-core.md#sales-cycle-length)) — but only once the CRM seat field is populated, which is why the report that would answer it is still broken ([pipeline.md](pipeline.md#broken-cycle-by-seat)).
[source-backed | slack-gtm:2026-07-28/dump.json#msg-4977 | 2026-07-28] ^rel-seat-band-filters

Announcement: <https://acme-analytics.example/changelog/journeys-seat-bands>.

#### 2026-07-09 · Model Lab template library

Six prebuilt attribution models, each configurable by marketing ops without SQL. Angle: the approved claim "multi-touch attribution without a data team" now has a concrete referent to point at ([business-core.md](business-core.md#claim-no-data-team)) — scope it to attribution and no wider.
[source-backed | slack-gtm:2026-07-09/dump.json#msg-4802 | 2026-07-09] ^rel-model-lab-templates

Announcement: <https://acme-analytics.example/changelog/model-lab-templates>. GA-versus-beta wording is contested — see below before writing about it.

#### 2026-06-30 · HubSpot sync: campaign-cost write-back

Campaign costs now write back into HubSpot alongside attribution fields. Angle: substantiates the bidirectional-sync claim with a third object instead of an adjective ([business-core.md](business-core.md#claim-hubspot-sync)).
[source-backed | slack-gtm:2026-06-30/dump.json#msg-4703 | 2026-06-30] ^rel-hubspot-cost-writeback

Announcement: <https://acme-analytics.example/changelog/hubspot-campaign-costs>.

#### 2026-06-12 · Dashboard rebuild

No marketing angle — infrastructure. Logged because the review chatter about dashboards slowing dates from just after this release ([customers.md](customers.md#churn-perf-chatter)). That is a single unverified signal, tracked there; it is not something copy answers, and support owns the reply if a customer raises it.
[source-backed | slack-gtm:2026-06-12/dump.json#msg-4551 | 2026-06-12] ^rel-dashboard-rebuild

## Roll-ups

Same convention as [events.md](events.md#roll-ups): written at month close, and what remains once the month's detail leaves the window.

### July 2026

Two releases, both under **Ops owns the model**. The Model Lab template library is the one marketing leads with and the one that made the no-data-team claim demonstrable rather than rhetorical; seat-band filters matter more internally — they are the lever on the sales-cycle question — than in any external message.
[inferred | inference:maintain | 2026-08-19] ^rollup-2026-07

## Roadmap — safe to share

Only items a human has explicitly cleared for external use, each with its clearance and an expiry. Uncleared items do not appear at all: absence is the guardrail.

### Spend anomaly alerts ^roadmap-anomaly-alerts
- Cleared for: sales conversations and roadmap slides, phrased as "on the roadmap for Q4." Never in ads, web copy, or posts.
- Expires: 2026-10-01.
- [confirmed | interview:sam-whitfield | 2026-08-11]

### Read-only warehouse export (beta) ^roadmap-warehouse-export
- Cleared for: naming to Scale and Enterprise prospects who ask about data-team workflows. Describe as beta; never attach a date.
- Expires: 2026-09-30.
- [confirmed | interview:sam-whitfield | 2026-08-11]

Expiry means the clearance lapses, not that the item shipped: past an expiry date, the item is unsayable again until a human re-clears it.

One further item is under embargo and deliberately absent from this table. Its rule and expiry live in [compliance-guardrails.md](compliance-guardrails.md#embargoes-and-timing) — agents deciding whether something is sayable read that file, never this one.

## Contested

### Is the Model Lab template library GA or beta? ^model-lab-ga-status

- Announced as generally available in the product channel. [source-backed | slack-gtm:2026-07-09/dump.json#msg-4802 | 2026-07-09]
- The published docs page still labels the template library "beta." [source-backed | webflow:2026-08-17/pages.json#docs-model-lab | 2026-08-17]
- Two authoritative reads of our own state disagree, so neither wins (SPEC §7.4) and recency decides nothing. Until it resolves, copy says neither "GA" nor "beta": it names the six models and what each does. Resolution path: product confirms the status and the docs page or the announcement gets corrected. → [open-questions.md#oq-025](open-questions.md#oq-025)
