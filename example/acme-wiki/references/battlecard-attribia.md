---
type: reference
description: The Attribia battlecard — what is actually established about them versus what is only signal, the one question that decides these deals, and the standing rule not to engage them publicly.
owner: Sam Whitfield (founder/CEO)
sources: [web-attribia, news-web, reviews-web, social-linkedin, interviews]
update-cadence: per-run
staleness-horizon: 45d
evidence-as-of: 2026-08-19
last-verified: 2026-08-19
---

# Battlecard — Attribia

Parent: [competitors.md](../competitors.md#attribia). Conduct rules: [compliance-guardrails.md](../compliance-guardrails.md#competitor-conduct).

**Thin by design, and unusually strict about evidence.** Most of what circulates about Attribia is O-class signal, and most of it is unusable in a deal. This card separates the two lines carefully, because the temptation to argue with them is the main risk they present.

## What is established

Founded 2024, AI-native positioning: attribution as a modeling problem solved by AI, with "10-minute setup, no ops work" as the recurring promise on their site.
[source-backed | web-attribia:2026-08-10/index.html | 2026-08-10] ^bc-at-profile

No public pricing — every pricing path routes to a form. The absence is the fact; do not infer a number from it.
[source-backed | web-attribia:2026-08-10/pricing.html | 2026-08-10] ^bc-at-pricing

## What is only signal

Everything here is single-source, `watchlist`, and **not usable in front of a prospect** — not as a hint, not as a question, not as a "we've heard." Carried here so reps recognize the signals rather than repeat them.

- Trade-press report of a $12M Series A. Funding never appears in our copy in any form, whatever its label.
  [watchlist | news-web:2026-07-29/attribia-series-a.html | 2026-07-29] ^bc-at-funding
- Three enterprise AE job postings on their company page — a sales-led turn would contradict their self-serve story. Unrefreshed since 2026-08-11 because that source is broken ([sources.md](../sources.md)).
  [watchlist | social-linkedin:2026-08-11/attribia-jobs.json | 2026-08-11] ^bc-at-hiring
- A reviewer reporting numbers shifting week-to-week — "the model changed under us." Matches the unproven-data-model read; needs a second independent source before it informs anything.
  [watchlist | reviews-web:2026-08-08/attribia-reviews.json#rev-1108 | 2026-08-08] ^bc-at-model-drift

## Where they win

- **The demo is genuinely fast and genuinely impressive.** Ten minutes to a chart beats four days to a dashboard in a room where nobody has asked yet where the numbers come from. [inferred | inference:build | 2026-08-19] ^bc-at-fast-demo
- **A buyer with an AI mandate.** When the evaluation criterion is "are we using AI," they win and no methodology argument reaches the room. [confirmed | interview:sam-whitfield | 2026-07-16] ^bc-at-ai-mandate
- **Prospects who have never had attribution at all.** No incumbent model to reconcile, so nothing about their answer looks wrong yet. [inferred | inference:build | 2026-08-19] ^bc-at-greenfield

## The one question that decides these deals

Every Attribia deal we have won turned on the same move: get the conversation to methodology. Invite the prospect to ask both vendors to explain the model behind the numbers — and to ask what changes when the model updates.
[confirmed | interview:sam-whitfield | 2026-07-16] ^bc-at-methodology-question

The follow-up that matters more than the first question: *if the number changes next month and nothing about my spend changed, what happened?* We can answer that ([metrics.md](../metrics.md#kpi-definitions) defines every number and names its model). A vendor whose model is the product often cannot answer it without saying "the AI improved."

## Objection responses

**"Attribia does this with AI and it takes ten minutes."**
> Setup speed and model quality are different things, and I would not argue with their ten minutes. What I would ask both of us is what the model actually does, and what happens to last month's numbers when the model updates. If your board saw a number in April, it should still be that number in July.

[confirmed | interview:sam-whitfield | 2026-07-16] ^bc-at-obj-ai-speed

**"Isn't your product AI too?"**
> Not as the headline, no. Our models are prebuilt and configurable by your ops lead, and you can read what each one does. We deliberately do not lead with "AI-powered" because it describes nothing about the answer you get ([compliance-guardrails.md](../compliance-guardrails.md#banned-claims)).

[confirmed | interview:dana-okafor | 2026-07-09] ^bc-at-obj-are-you-ai

**"They said your approach is outdated."**
> They may be right that prebuilt models are less exciting. Ask us both to show the same quarter on the same data and explain the difference. That is a checkable question, and I would rather answer it than argue about approaches.

[confirmed | interview:sam-whitfield | 2026-07-16] ^bc-at-obj-outdated

## Win/loss evidence

Not yet in the CRM in usable volume — Attribia appears in competitive fields too rarely for a rate to mean anything, which is itself the reason they are tracked as a competitor rather than treated as one. Revisit at the Q3 win/loss pull.
[inferred | inference:build | 2026-08-19] ^bc-at-winloss-thin

## How we counter

Never engage their LinkedIn threads ([compliance-guardrails.md](../compliance-guardrails.md#attribia-no-engage)). Their motion runs on manufactured controversy and ours does not; a reply is the only thing they need from us. In deals, invite the prospect to ask both vendors to explain the model behind the numbers — we win when the conversation reaches methodology.
[confirmed | interview:sam-whitfield | 2026-07-16] ^bc-at-counter
