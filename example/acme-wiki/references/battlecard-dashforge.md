---
type: reference
description: The DashForge battlecard — a thin card on purpose: where the qualification line sits, the three objections that actually come up, and why we do not compete on price.
owner: Dana Okafor (CMO)
sources: [web-dashforge, reviews-web, crm-hubspot, interviews]
update-cadence: per-run
staleness-horizon: 45d
evidence-as-of: 2026-08-15
last-verified: 2026-08-19
---

# Battlecard — DashForge

Parent: [competitors.md](../competitors.md#dashforge). Conduct rules: [compliance-guardrails.md](../compliance-guardrails.md#competitor-conduct).

**This card is deliberately thin.** DashForge is mostly a qualification question, not a competitive fight — the counter-position is to find out fast whether the prospect needs multi-touch at all, and to say so honestly when they do not. There is no comparison asset and creating one is an open decision, not an oversight ([open-questions.md#oq-029](../open-questions.md#oq-029)).

## Who they are

Cheap self-serve attribution for SMB: a free tier plus $299/mo paid, credit-card checkout, no sales team. Historically last-click only; a multi-touch beta was announced 2026-07-21.
[source-backed | web-dashforge:2026-08-10/pricing.html | 2026-08-10] ^bc-df-profile

Early review chatter characterizes the beta as reweighted last-click rather than path modeling. One external signal — tracked, never cited to a prospect.
[watchlist | reviews-web:2026-08-08/dashforge-reviews.json#rev-3312 | 2026-08-08] ^bc-df-beta-quality

## Where they win, and where the line sits

| They win when | Our move |
|---|---|
| The team needs last-click reporting and nothing more | Say so. They are DashForge's customer, not ours |
| Under 20 employees, no ops function | Anti-ICP for us ([icp-personas.md](../icp-personas.md#anti-icp)) — decline cleanly |
| Budget is the entire decision and $299 is the ceiling | We do not have a $299 answer and are not building one |
| The buyer wants to self-serve without talking to anyone | Our product needs a CRM connection before it shows value; that is a real gap, not a positioning problem |

[confirmed | interview:priya-shah | 2026-07-20] ^bc-df-where-they-win

Where the line sits, stated as a question a rep can ask in the first ten minutes: *does more than one touch need to get credit for the same deal, and does the answer have to survive your CFO?* Two yeses and DashForge cannot serve them. One yes and it is genuinely close.
[confirmed | interview:priya-shah | 2026-07-20] ^bc-df-qualifying-question

## Where they are weak

- **Multi-touch depth.** Their own announcement calls it a beta; whether the model does path attribution is not established by anything we can cite. Argue depth only from our own capability, never from a claim about theirs. [source-backed | web-dashforge:2026-07-21/blog/multi-touch-beta.html | 2026-07-21] ^bc-df-weak-depth
- **No CRM write-back.** Attribution that stays inside the reporting tool never reaches the deal record, so the number never survives a board conversation. This is the argument that lands ([business-core.md](../business-core.md#claim-hubspot-sync)). [confirmed | interview:morgan-lee | 2026-07-30] ^bc-df-weak-writeback
- **No implementation support.** Fine at 15 employees, structurally hard at 300 with three paid channels and a messy CRM. [confirmed | interview:priya-shah | 2026-07-20] ^bc-df-weak-implementation

## Objection responses

**"DashForge does this for $299."**
> For last-click, yes, and if last-click answers your question you should buy it. What it will not do is write credit back into your CRM, so the number stays in a reporting tool and never shows up on the deal. If your CFO has to be able to check the number, that is the difference you are paying for.

[confirmed | interview:priya-shah | 2026-07-20] ^bc-df-obj-price

**"They just shipped multi-touch too."**
> They announced a beta in July — that is their word for it, and I would ask them what the model actually does before treating it as settled. I would rather you test both on one channel for a quarter than take either of our word for it.

[confirmed | interview:dana-okafor | 2026-08-15] ^bc-df-obj-multitouch

**"We started on DashForge and outgrew it."**
> That is the common path and the migration is straightforward — the data you want is in your CRM and your ad platforms, not in their tool. The one thing to check first is whether your CRM has clean campaign data, because that determines whether you are four days out or three weeks out.

[confirmed | interview:morgan-lee | 2026-07-30] ^bc-df-obj-outgrew

## Win/loss evidence

- Named in 19% of H1 2026 competitive deals, up from 9% in Q1, concentrated in the 100–300 employee segment. [source-backed | crm-hubspot:report-2026-h1-winloss | 2026-07-28] ^bc-df-winloss-rate
- Now visible in current open pipeline too: named in 4 of 63 open deals. Encroachment is no longer a historical read ([pipeline.md](../pipeline.md#snap-movements)). [source-backed | crm-hubspot:report-2026-08-stage-mix | 2026-08-15] ^bc-df-open-deals

Not yet evidence, but worth reading before the next competitive call: an unprocessed entry in [intake/observations.md](../intake/observations.md) reports a prospect choosing DashForge for a 40-seat pilot on data-source limits in our Growth tier — a packaging objection rather than a depth objection, which is not how this card frames the fight. It becomes a claim, an open question, or nothing at the next maintain run. Consumers may not cite it in the meantime.

## How we counter

Never on price. Qualify on multi-touch depth and CRM write-back; a prospect who only needs last-click is DashForge's customer, not ours, and we say so out loud.
[confirmed | interview:priya-shah | 2026-07-20] ^bc-df-counter
