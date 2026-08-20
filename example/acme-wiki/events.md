---
type: state
description: Acme's event calendar and the running log of field and market events — what happened, when, and what marketing is supposed to do about it.
owner: Dana Okafor (CMO)
sources: [slack-gtm, crm-hubspot, news-web, interviews, inbox-docs]
update-cadence: per-run
staleness-horizon: rolling — 90d / 100 entries, monthly roll-ups
evidence-as-of: 2026-08-19
last-verified: 2026-08-19
---

# Events

A capped log: rolling 90-day / 100-entry window with monthly roll-ups (SPEC §13). Product launches get one line here and their detail in [product-releases.md](product-releases.md); competitor moves belong in [competitors.md](competitors.md), not here.

`## Log` is **append-open** — consumer agents may add entries to it directly (SPEC §9). Everything else in this file is maintainer-written.

## Upcoming

| Date | Event | Type | Why marketing cares |
|---|---|---|---|
| 2026-08-27 | Attribution Teardown #7 | webinar | The Teardown frame ([growth.md](growth.md#campaign-frames)); consenting company confirmed, unnamed until air date |
| 2026-09-10 | Launch window — item embargoed | launch | Nothing public before the launch post is live; the rule and expiry are in [compliance-guardrails.md](compliance-guardrails.md#embargoes-and-timing) |
| 2026-09-16 – 09-17 | RevPath Summit, Chicago | conference | Booth plus Priya Shah's stage session; the follow-up sequence is named-account outbound, not a badge-scan blast |
| 2026-09-24 | Attribution Teardown #8 | webinar | Slot open — the Teardown pipeline needs a consenting company by 2026-09-05 |
| 2026-10-01 | Board-Ready Q4 kickoff | campaign | Q4 board season; the Q3 template pack must be refreshed first ([content-assets.md](content-assets.md#lead-magnets-and-campaign-assets)) |

[confirmed | interview:dana-okafor | 2026-08-14] ^upcoming-q3-q4

38 of the 400 named accounts have a registered attendee at RevPath Summit — the list is loaded in HubSpot and is the reason the booth budget survived review.
[source-backed | crm-hubspot:report-2026-08-event-overlap | 2026-08-15] ^revpath-account-overlap

## Log

#### 2026-08-15 · Trade press: view-through window deprecation rumor

A trade outlet reports that a major ad platform will retire 90-day view-through windows in Q4. Single external signal with no platform announcement behind it — tracked, not used. Nothing goes in copy until the platform says it itself.
[watchlist | news-web:2026-08-15/view-through-window.html | 2026-08-15] ^ev-view-through-rumor

#### 2026-08-14 · Attribution Teardown #6

214 registrants, 97 live, 41% of registrants from named accounts — the best named-account share the series has had. The "which half of the budget" framing drew the most questions; a Devon-shaped audience, not a Dana-shaped one.
[source-backed | crm-hubspot:report-2026-08-webinar-registrants | 2026-08-14] ^ev-teardown-6

Recording cataloged in [content-assets.md](content-assets.md#evergreen-assets).

#### 2026-08-12 · GA4 shortened its default reporting lookback

Morgan Lee flagged in #gtm that GA4's reporting UI now defaults to a 30-day lookback where it used to default to 90. Read as a content trigger, not a product problem: it is exactly the "your tools disagree with each other" tension the Channel Answers series exists for.
[confirmed | slack-gtm:2026-08-12/dump.json#msg-5120 | 2026-08-12] ^ev-ga4-lookback

Any post about the change cites Google's own release note, not this entry — an unsourced number does not run ([voice.md](voice.md#never-unsourced-numbers)).

#### 2026-08-11 · Board Pack export shipped

One line by boundary rule; detail and marketing angle in [product-releases.md](product-releases.md#shipped).
[source-backed | slack-gtm:2026-08-11/dump.json#msg-5098 | 2026-08-11] ^ev-board-pack-ship

#### 2026-07-30 · Board-Ready Q3 template pack went out

The quarterly Board-Ready push ([growth.md](growth.md#campaign-frames)) landed ahead of the July board cycle and outperformed every other lead magnet in the library. Download numbers, status, and the Q4 refresh deadline stay with the asset, by the same boundary rule releases follow: [content-assets.md](content-assets.md#board-ready-conversion).
[source-backed | crm-hubspot:report-2026-08-lead-magnets | 2026-08-15] ^ev-board-ready-q3

#### 2026-07-16 · Attribution Teardown #5 · Fernhill Logistics rebuilt live

Fernhill's setup was rebuilt on air — the first Teardown to produce a usable customer story. What happened next, what may be said about it, and the full-session-only rule for the recording are in [customers.md](customers.md#story-fernhill).
[confirmed | interview:morgan-lee | 2026-08-17] ^ev-teardown-5

#### 2026-07-09 · Model Lab template library shipped

One line by boundary rule; detail in [product-releases.md](product-releases.md#shipped).
[source-backed | slack-gtm:2026-07-09/dump.json#msg-4802 | 2026-07-09] ^ev-model-lab-ship

#### 2026-06-25 · RevPath Summit session accepted

Priya Shah's session — "What your CRM says about your sales cycle, and what it leaves out" — was accepted for the September program. The talk sits directly on the contested sales-cycle question ([business-core.md](business-core.md#sales-cycle-length)); the abstract deliberately promises a method, not a number.
[confirmed | doc:revpath-2026-acceptance.md | 2026-06-25] ^ev-revpath-accepted

#### 2026-06-18 · Attribution Teardown #4 · relaunched format

First Teardown in the current format — one company, live rebuild, no slides. 148 registrants against a 90-registrant average for the old format. This is the entry that made the series the trust engine the growth plan now leans on.
[source-backed | crm-hubspot:report-2026-06-webinar-registrants | 2026-06-30] ^ev-teardown-4

#### 2026-06-04 · Ridgeline RevOps signed as the first referral partner

The referral motion's opening move; terms and the rest of the partner picture are in [partners.md](partners.md#partner-referral).
[confirmed | slack-gtm:2026-06-04/dump.json#msg-4180 | 2026-06-04] ^ev-ridgeline-signed

## Roll-ups

A roll-up is written when a month closes: it is the summary that survives after that month's individual entries leave the 90-day window and their detail archives to [references/events-2026.md](references/events-2026.md) (SPEC §13). August 2026's roll-up lands at month close.

### July 2026

Three Teardown-frame beats and one product moment. Teardown #5 rebuilt Fernhill Logistics live and produced the most-reused sales asset of the quarter; the Model Lab template library shipped; the Board-Ready Q3 pack went out ahead of board season. Webinar registration was the month's largest single source of new named-account contacts — the pattern the September calendar is built around.
[inferred | inference:maintain | 2026-08-19] ^rollup-2026-07

### June 2026

The Teardown series relaunched in its current format and the referral motion opened with one signed consultancy. Detail entries stay in the log until 2026-09-02, when the window drops them.
[inferred | inference:maintain | 2026-08-19] ^rollup-2026-06
