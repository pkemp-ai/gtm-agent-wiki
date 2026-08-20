---
type: state
description: Acme's partners — relationship type, integration depth, and exactly what co-marketing each one permits — plus where Acme sits in the CRM ecosystem.
owner: Sam Whitfield (founder/CEO)
sources: [web-hubspot, crm-hubspot, interviews, inbox-docs]
update-cadence: monthly
staleness-horizon: 90d
evidence-as-of: 2026-08-19
last-verified: 2026-08-19
---

# Partners

Every **allowed co-marketing** line below is doctrine-in-exile: it records a decision, so it requires H-class provenance, and the maintainer may annotate it from external evidence but never rewrite it. A partner's own published rules are separate — those are A-class facts about them and may be updated silently.

## Partners

### HubSpot ^partner-hubspot

- Relationship: certified app partner, listed in the App Marketplace since 2024. The deepest integration we have and the one the positioning sentence leans on.
- Integration: native bidirectional sync — the differentiator recorded in [business-core.md](business-core.md#claim-hubspot-sync).
- Allowed co-marketing: marketplace listing copy, one co-authored post per quarter reviewed by their partner team, and the phrase "certified HubSpot app." Never "official HubSpot partner," never their logo in paid creative. [confirmed | interview:dana-okafor | 2026-08-14] ^hubspot-comarketing
- Their listing rule, not ours: certified apps must document a two-way data flow and publish a support SLA. [source-backed | web-hubspot:2026-08-03/app-partner-requirements.html | 2026-08-03] ^hubspot-listing-requirements

  *Requirements updated 2026-08-03 — the prior version asked only for a documented one-way flow. A-class self-fact about the publishing entity, superseded silently per SPEC §7.2; see [changelog.md](changelog.md).*

### Salesforce ^partner-salesforce

- Relationship: an AppExchange listing and nothing else — no partner tier, no partner manager.
- Integration: one-way today. This is the honest limit in [business-core.md](business-core.md#right-to-win) and the passage ratified as on-voice in [voice.md](voice.md#exemplars); it is stated before the pitch, not after.
- Allowed co-marketing: none. No joint content, no tier claims, no "Salesforce partner" in any asset. [confirmed | interview:sam-whitfield | 2026-08-11] ^salesforce-comarketing
- Nothing about future sync capability may be said to Salesforce, to prospects, or in the listing while the embargo in [compliance-guardrails.md](compliance-guardrails.md#embargoes-and-timing) stands. That includes partner conversations, which are not a private channel.

### Gong ^partner-gong

- Relationship: integration partner, listed in their marketplace. No co-marketing agreement signed; a joint webinar was proposed in June and remains unsigned.
- Integration: call activity lands as attribution touchpoints, so sales conversations show up in the journey view instead of vanishing between form fill and closed-won.
- Allowed co-marketing: nothing beyond the marketplace listing until an agreement exists. Do not name Gong in campaign assets on the strength of the integration alone. [confirmed | interview:dana-okafor | 2026-08-14] ^gong-comarketing
- Separate rule, easy to conflate: call recordings are evidence for this wiki and never material for outbound personalization ([compliance-guardrails.md](compliance-guardrails.md#personalization-limits)).

### Referral partners ^partner-referral

- Three signed RevOps consultancies: Ridgeline RevOps, Two Rivers Consulting, and Harborlight — whose status is contested, below.
- Terms: referral only. 15% first-year fee, no reselling, no white-label, no co-branded product surface. The anti-ICP line on white-label agencies ([icp-personas.md](icp-personas.md#anti-icp)) is a partnership rule, not just a qualification rule. [confirmed | interview:sam-whitfield | 2026-08-11] ^referral-terms
- Allowed co-marketing: partners may say they implement Acme and may use our logo on a services page. We do not publish partner directories, case studies about partners, or joint lead magnets — none exist and none are planned this half. [confirmed | interview:sam-whitfield | 2026-08-11] ^referral-comarketing
- Referred opportunities route by segment with the partner-sourced flag set; the routing itself is in [account-ownership.md](account-ownership.md#ownership-map).
- Partner-sourced deals are 9% of open pipeline as of 2026-08-15 — small, and concentrated in two consultancies. [source-backed | crm-hubspot:report-2026-08-partner-referrals | 2026-08-15] ^referral-pipeline-share

## Channel motion

Acme does not sell through a distributor or reseller sales force. The two motions that look like "through" are:

1. **HubSpot App Marketplace.** A prospect finds the listing, starts a trial, and an AE picks them up on the ordinary inbound SLA. Nobody at HubSpot quotes, demos, or takes a PO for us. Enablement is the listing copy and the documented two-way data flow — not a partner kit.
2. **Referral consultancies.** The partner introduces; an Acme AE owns the demo, the technical review, and the purchase order. The partner does not quote, does not sit in the technical review unless the prospect asks, and does not take the PO. Enablement is a one-pager plus the right to use our logo on a services page — no demo kit, no certification roster, no co-branded product surface.

[confirmed | interview:sam-whitfield | 2026-08-11] ^channel-motion-direct

## Ecosystem position

- The HubSpot App Marketplace listing is the second-largest inbound source after the blog: 18% of H1 2026 inbound trials. [source-backed | crm-hubspot:report-2026-08-inbound-sources | 2026-08-15] ^eco-marketplace-inbound
- Salesforce is the structural gap. One-way sync keeps us off the AppExchange tiers that carry co-marketing, which is a plausible reason upper-mid deals arrive with an integration question already loaded — the pattern-read, not a measured cause. [inferred | inference:maintain | 2026-08-19] ^eco-salesforce-gap
- No reseller or white-label motion exists and none is planned. Agencies asking for one are anti-ICP, not pipeline, and the answer is a straight no rather than a "not yet." [confirmed | interview:sam-whitfield | 2026-08-11] ^eco-no-whitelabel
- Marketplace presence is distribution, not endorsement: a listing never becomes a proof point in copy ([compliance-guardrails.md](compliance-guardrails.md#banned-claims)). [confirmed | interview:dana-okafor | 2026-08-14] ^eco-listing-not-proof

## Contested

### Is Harborlight a referral partner or a competitor? ^harborlight-status

- Referral agreement signed 2026-07-31; two opportunities sent since. [source-backed | crm-hubspot:report-2026-08-partner-referrals | 2026-08-15]
- "They're productizing their internal attribution tool. Treat them as a competitor." [confirmed | interview:priya-shah | 2026-08-15]
- An H-versus-S collision (SPEC §7.4) — recency decides nothing here, and both readings can be true at once. Until it resolves: no asset names them, the referral flow stays open, and the watchlist entry in [competitors.md](competitors.md#wl-harborlight) stands. Resolution path: ask them directly at the Q3 partner review. → [open-questions.md#oq-027](open-questions.md#oq-027)
