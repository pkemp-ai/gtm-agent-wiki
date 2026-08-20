---
type: state
description: The catalog of Acme's marketing assets — what exists, where it lives, whether it is safe to send today — and the known holes in the library.
owner: Morgan Lee (marketing ops)
sources: [webflow, ga4, crm-hubspot, reviews-web, interviews, inbox-docs]
update-cadence: weekly
staleness-horizon: 60d
evidence-as-of: 2026-08-19
last-verified: 2026-08-19
---

# Content assets

The catalog: status, location, fitness for use. An asset's *substance* — the story, the numbers, what the customer approved — lives in [customers.md](customers.md); this file never restates a number, it points at the one canonical home for it.

Status vocabulary, used the same way in every table below:

| Status | Meaning |
|---|---|
| current | Safe to send today, as-is |
| aging | Accurate but shows an old UI or a superseded framing; usable with a caveat, due for revision |
| blocked | Complete or near-complete, but an approval or legal gate is not cleared — do not distribute |
| deprecated | Do not send, do not link; kept only so agents recognize it in the wild |

[confirmed | interview:morgan-lee | 2026-08-17] ^status-vocabulary

## Case studies

| Asset | Customer / industry | Result claim | Status | Location |
|---|---|---|---|---|
| Brightpath HR case study | Brightpath HR · HR tech | Cost per opportunity, per [business-core.md](business-core.md#claim-brightpath-cpo) | current | Webflow › /customers/brightpath-hr |
| Lumastone case study | Lumastone · analytics tooling | Board reporting time, per [customers.md](customers.md#story-lumastone) | blocked | Drive › Marketing › Case Studies › lumastone-2026-08 |
| Enterprise security-review one-pager | anonymized · security | Review passed in three weeks, unnamed customer | current | Drive › Sales Assets › security-review-onepager |
| Attribution Teardown #5 recording | Fernhill Logistics · logistics | Narrative only — no written numbers approved | current | Webinar platform, gated page in Customer.io |

[confirmed | interview:morgan-lee | 2026-08-17] ^case-study-inventory

Fitness notes that matter more than the table:

- Brightpath is the only case study whose numbers may appear in public copy, and its approval expires at their 2027-01 renewal ([customers.md](customers.md#reference-approvals)). Diary it; do not discover it. [confirmed | interview:dana-okafor | 2026-08-14] ^brightpath-approval-expiry
- The Lumastone asset is finished writing and blocked on their legal sign-off. It may not be sent to a prospect, attached to a sequence, or linked internally in a way that leaks — blocked means blocked. [confirmed | interview:dana-okafor | 2026-08-14] ^lumastone-blocked
- The Teardown #5 recording may only be shared as the full session. No clips, no GIFs, no pulled quotes — the approval covers the session, not its parts ([customers.md](customers.md#story-fernhill)). [confirmed | interview:morgan-lee | 2026-08-17] ^teardown5-full-session-only

## Evergreen assets

| Asset | What it is for | Status | Location |
|---|---|---|---|
| "Attribution models, explained" | The flagship educational post; the voice exemplar in [voice.md](voice.md#exemplars) | current | Webflow › /blog/attribution-models-explained |
| MetricFlow comparison page | The only competitor comparison we publish | aging | Webflow › /compare/metricflow |
| Sales one-pager (limits-first) | The Salesforce-limits passage, stated before the pitch | current | Drive › Sales Assets › acme-onepager |
| SOC 2 security overview | Enterprise first touch ([channel-styles.md](channel-styles.md#email-soc2-first-touch)) | current | Drive › Sales Assets › security-overview |
| "Out of the Spreadsheet" migration guide | The always-on migration frame ([growth.md](growth.md#campaign-frames)) | current | Webflow › /guides/out-of-the-spreadsheet |
| Attribution Teardown library, #1–#6 | Proof-by-demonstration for the Teardown frame | #1–#3 aging, #4–#6 current | Webinar platform, index page in Webflow |
| HubSpot App Marketplace listing copy | Marketplace distribution surface ([partners.md](partners.md#partner-hubspot)) | current | HubSpot partner portal |

[confirmed | interview:morgan-lee | 2026-08-17] ^evergreen-inventory

- "Attribution models, explained" is 38% of blog sessions on its own and is the entry point for most first-touch journeys we can see. Treat it as infrastructure: it gets maintained, not rewritten. [source-backed | ga4:2026-08-17/blog-pages.csv | 2026-08-17] ^models-post-traffic
- The MetricFlow comparison page is marked aging for one reason: their FastStart announcement dates our implementation-timeline framing. The page already hedges to "three to six weeks, per their own materials" ([competitors.md](competitors.md#metricflow-faststart)), which holds until [open-questions.md#oq-024](open-questions.md#oq-024) resolves. [confirmed | interview:dana-okafor | 2026-08-15] ^comparison-page-hedge
- One review-site comment says our comparison page overstates MetricFlow's implementation timeline. A single unverified external signal that happens to agree with the hedge already in place — tracked, not acted on. [watchlist | reviews-web:2026-08-08/acme-reviews.json#rev-2104 | 2026-08-08] ^asset-comparison-stale-signal
- Teardown recordings #1–#3 show the pre-Model Lab interface. They are still true and still useful in a nurture; they are not usable in a demo-adjacent context. [confirmed | interview:morgan-lee | 2026-08-17] ^teardown-library-aging

## Lead magnets and campaign assets

| Asset | Attached to | Status | Location / gate |
|---|---|---|---|
| Board-Ready Q3 template pack | Board-Ready frame | current, Q4 refresh due 2026-09-24 | Webflow landing page, Customer.io form |
| Last-click vs. multi-touch delta calculator | Channel Answers series, Devon-facing | current | Webflow › /tools/delta-calculator, ungated |
| Attribution Teardown application form | Teardown frame — the series' supply engine | current | Webflow › /teardown, ungated |
| Named-account outbound sequences (2) | Triggers: new CMO, HubSpot install detected | current | Customer.io, 4-touch cap per [channel-styles.md](channel-styles.md#email) |
| LinkedIn Ads creative set, Q3 | Distribution for proof assets | current, 6 variants | LinkedIn Ads, one approved claim per variant |

[confirmed | interview:morgan-lee | 2026-08-17] ^campaign-asset-inventory

- The Board-Ready pack is the highest-converting lead magnet in the library: 340 downloads in its first week, 61% from accounts already in the CRM (the July send is logged at [events.md](events.md#ev-board-ready-q3)). Its Q4 refresh is the single most load-bearing production task of September. [source-backed | crm-hubspot:report-2026-08-lead-magnets | 2026-08-15] ^board-ready-conversion
- The delta calculator is ungated on purpose: it is a trust asset, and gating it would cost more in reach than it returns in emails. [confirmed | interview:dana-okafor | 2026-08-14] ^calculator-ungated

## Gaps

Known holes. Inferred entries are welcome here — a gap is a read, not a fact, until someone decides to fill it.

- No comparison asset covers DashForge, though they were named in 19% of H1 competitive deals and are concentrated in the 100–300 employee band we sell into ([competitors.md](competitors.md#dashforge-encroaching)). The gap is the reason reps improvise on that call. [inferred | inference:maintain | 2026-08-19] ^gap-dashforge-comparison

  → [open-questions.md#oq-029](open-questions.md#oq-029)

- No case study covers logistics or supply-chain SaaS, the fastest-growing slice of the base — 6 of the last 15 closed-won ([customers.md](customers.md#base-segments)). The story exists (Fernhill); what is missing is written approval, so this is an approvals task, not a production task. [inferred | inference:maintain | 2026-08-19] ^gap-logistics-story
- Nothing in the library answers the untracked-touches question prospects keep raising ([icp-personas.md](icp-personas.md#objection-dark-social)). Blocked upstream: there is no doctrinal answer yet, and writing the asset first would invent one. [inferred | inference:maintain | 2026-08-19] ^gap-untracked-touches
- Three landing pages in the site inventory have no campaign attached and no inbound links — orphaned assets that still collect form fills into no sequence. [source-backed | webflow:2026-08-17/pages.json | 2026-08-17] ^gap-orphan-landing-pages
- No enterprise asset names a customer. Corvid Security is anonymized-only ([customers.md](customers.md#reference-approvals)), which caps how far the security-review one-pager can carry an upper-mid deal. [confirmed | interview:priya-shah | 2026-08-04] ^gap-named-enterprise-reference

## Contested

None currently. Collisions here are usually a status disagreement — an asset a rep calls current that this file marks aging — and they land here the day they appear with a resolution path into [open-questions.md](open-questions.md#active).
