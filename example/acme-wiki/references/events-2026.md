---
type: reference
description: Detail archive for Acme's 2026 events — the pre-wiki H1 record reconstructed at build time, and where each month's detail lands once the 90-day log window drops it.
owner: Dana Okafor (CMO)
sources: [inbox-docs, interviews, crm-hubspot]
update-cadence: monthly
staleness-horizon: rolling — appended at month close, never revised
evidence-as-of: 2026-08-19
last-verified: 2026-08-19
---

# Events — 2026 detail archive

Parent: [events.md](../events.md#roll-ups). That file keeps a rolling 90-day / 100-entry window with a one-paragraph roll-up per closed month (SPEC §13). This file is where the individual entries land once the window drops them, so the roll-up stays short and the detail stays retrievable.

**This page is mostly empty on purpose, and that is the current, correct state.** The wiki was built on 2026-06-12; the oldest entry still in the live log is 2026-06-04, and the window does not reach back past it until 2026-09-02. Nothing has aged out yet.

## How entries arrive here

| When | What moves | What stays in `events.md` |
|---|---|---|
| A month closes | nothing yet — the entries stay in the live log while they are inside the window | the month's one-paragraph roll-up |
| The 90-day window passes an entry | the full entry, verbatim, with its claim tag and topic key intact | the roll-up only |
| An entry is superseded | nothing — supersession is recorded where the claim lives, not by moving it | the corrected claim |

Moving an entry is a restructure, not an edit: claims arrive here with their labels, provenance, dates, and topic keys unchanged. A claim that would need rewording to fit this page is a claim that should not be moved.

Next scheduled move: **2026-09-02**, when the June entries leave the window ([events.md](../events.md#rollup-2026-06) already carries their roll-up).

## H1 2026 — the pre-wiki record

Reconstructed at build time from a human-written recap and one interview, because the wiki did not exist while these happened. Thinner than anything the live log will produce, and deliberately not backfilled beyond what a source actually supports.

#### 2026-05-14 · First paid webinar experiment, retired

A gated webinar promoted entirely through LinkedIn Ads: 62 registrants, 19 live, no opportunities within the quarter. Retired rather than iterated — the finding that mattered was that paid distribution does not fix a format problem, which is part of why the Teardown relaunch in June led with format instead of spend.
[confirmed | doc:2026-h1-marketing-recap.md | 2026-06-10] ^ev-2026-05-paid-webinar

#### 2026-04-22 · Category language settled on "revenue attribution"

The decision that became doctrine. Recorded here as the event; the ruling itself lives in [business-core.md](../business-core.md#category) and [glossary.md](../glossary.md#terms-we-use), which are the canonical homes.
[confirmed | interview:dana-okafor | 2026-06-20] ^ev-2026-04-category-decision

#### 2026-03-05 · "Attribution models, explained" published

The post that turned into infrastructure — now roughly 38% of blog sessions on its own and the voice exemplar every other piece is measured against ([voice.md](../voice.md#exemplar-models-post)). Current traffic and status are tracked in [content-assets.md](../content-assets.md#models-post-traffic), not here.
[confirmed | doc:2026-h1-marketing-recap.md | 2026-06-10] ^ev-2026-03-models-post

#### 2026-02-11 · Brightpath HR case study published

The first and still the only customer story with numbers approved for public use. Approval scope and expiry are in [customers.md](../customers.md#reference-approvals); the claim wording is governed by [business-core.md](../business-core.md#claim-brightpath-cpo).
[confirmed | doc:2026-h1-marketing-recap.md | 2026-06-10] ^ev-2026-02-brightpath-published

## Gaps in this record

Stated rather than quietly filled, because an archive that looks complete when it is not is worse than one that admits its edges.

- January and the first half of February 2026 have no record at all. No recap document covers them and nobody has been asked. [inferred | inference:maintain | 2026-08-19] ^ev-2026-h1-gap-january
- The H1 recap is a single human-written document, so these four entries share one provenance and one author's memory. Anything load-bearing that traces only to here should be re-confirmed before it reaches copy. [inferred | inference:maintain | 2026-08-19] ^ev-2026-h1-single-source
