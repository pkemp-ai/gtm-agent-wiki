---
type: doctrine
description: What Acme Analytics sells, how it is positioned, what it costs, and the exact performance claims agents may make about it.
owner: Dana Okafor (CMO)
sources: [interviews, inbox-docs, crm-hubspot]
update-cadence: interview
staleness-horizon: 120d
evidence-as-of: 2026-07-23
last-verified: 2026-08-19
---

# Business core

## Company facts

Acme Analytics is a privately held B2B SaaS company, founded in 2022 in Chicago, with roughly 45 people across the US. English is the only language we sell and write in. There is no outside board; Sam Whitfield (founder/CEO) and Dana Okafor (CMO) are the two people with standing to change doctrine. We plan in halves, not in years.
[confirmed | interview:sam-whitfield | 2026-07-02] ^company-facts

## Product

Acme Analytics is a revenue attribution platform for B2B marketing teams: it connects ad platforms, the website, and the CRM, and shows which marketing touches actually create pipeline and revenue.
[confirmed | doc:2026-positioning-memo.md | 2026-06-14] ^what-it-is

The three jobs customers hire it for, in their order of urgency:

1. Show which channels and campaigns create pipeline — channel, campaign, and account level, not just last click.
2. Give the CMO revenue numbers credible enough for a board deck.
3. Keep attribution running without a data team — marketing ops owns it end to end.

[confirmed | interview:dana-okafor | 2026-06-20] ^jobs-to-be-done

## Positioning

Category: **revenue attribution**. We say "revenue attribution," never "marketing analytics" — the category decision is deliberate (ruling in [glossary.md](glossary.md#terms-we-use)).
[confirmed | doc:2026-positioning-memo.md | 2026-06-14] ^category

The positioning sentence agents build on:

> For B2B SaaS marketing teams on HubSpot or Salesforce, Acme Analytics shows which marketing actually creates pipeline — multi-touch attribution live in days, without a data team.

[confirmed | interview:dana-okafor | 2026-06-20] ^positioning-sentence

The competitive frame: MetricFlow sells the same promise to enterprises with six-week implementations; DashForge sells a cheaper, shallower version to SMBs; Attribia sells the AI story. We own the middle — teams big enough to need real attribution, too small to staff it. Current competitor state: [competitors.md](competitors.md). MetricFlow's FastStart announcement (three weeks for their entry tier) is A-class evidence against the six-week framing and is annotated only — doctrine is unchanged until Dana rules. → [open-questions.md#oq-024](open-questions.md#oq-024)
[confirmed | interview:dana-okafor | 2026-06-20] ^competitive-frame

Who we sell to is defined in [icp-personas.md](icp-personas.md). Where growth comes from is defined in [growth.md](growth.md).

## Right to win

| Advantage | Substance | Honest limit |
|---|---|---|
| Time to first dashboard | Median 4 days across the 61 implementations Jan–Jun 2026 | Assumes a reasonably clean CRM; messy Salesforce orgs run 2–3 weeks |
| Multi-touch without a data team | Prebuilt models on every tier, plus Model Lab from Scale up, configurable by marketing ops, no SQL | We lose deals that want warehouse-native custom models — and should |
| Native bidirectional HubSpot sync | Certified two-way app; attribution fields write back into HubSpot | Salesforce sync is one-way today (launch timing: see [compliance-guardrails.md](compliance-guardrails.md#embargoes-and-timing)) |

[confirmed | interview:sam-whitfield | 2026-07-02] ^right-to-win

Against MetricFlow specifically, speed and implementation lift are the wedge; the full argument lives in [references/battlecard-metricflow.md](references/battlecard-metricflow.md).

## Pricing

| Tier | Price | Contract | Built for |
|---|---|---|---|
| Growth | $1,200/mo | monthly or annual | up to 8 users, 5 data sources |
| Scale | $3,000/mo | annual only | unlimited users and sources, Model Lab, SSO |
| Enterprise | custom | annual only | security review, custom retention, dedicated support |

[confirmed | doc:2026-positioning-memo.md | 2026-06-14] ^pricing-tiers

What agents may say about price: list prices are public and may be quoted exactly. Never state or imply discounts in public copy — discounting is a sales conversation, not a marketing claim. There is no ratified ACV floor below which we walk away; SDR triage currently uses employee count as a proxy, which is a standing risk. → [open-questions.md#oq-011](open-questions.md#oq-011)
[confirmed | interview:dana-okafor | 2026-07-09] ^pricing-copy-rule

## Approved claims

The only performance claims agents may make. Wording may flex; the substance and the numbers may not. The prohibitions that bracket these live in [compliance-guardrails.md](compliance-guardrails.md). **Lead claim:** ^claim-ttfd — it heads a capability announcement; the others support it.

### "Median time to first dashboard: 4 days." ^claim-ttfd
- Substantiation: onboarding timestamps, 61 implementations, January–June 2026. Recomputed quarterly by marketing ops; if the recompute moves the median, this claim changes here before it changes anywhere else.
- [confirmed | interview:dana-okafor | 2026-07-09]

### "Multi-touch attribution without a data team." ^claim-no-data-team
- Substantiation: qualitative but defensible — prebuilt models, ops-configurable, no SQL required. Scope it to attribution only; the wider version is a banned overclaim ([compliance-guardrails.md](compliance-guardrails.md#banned-claims)).
- [confirmed | interview:dana-okafor | 2026-07-09]

### "Native bidirectional HubSpot sync." ^claim-hubspot-sync
- Substantiation: certified HubSpot app, two-way field sync. Do not extend this claim to Salesforce.
- [confirmed | interview:morgan-lee | 2026-07-09]

### "Brightpath HR cut cost per opportunity 31% in two quarters." ^claim-brightpath-cpo
- Substantiation: customer-approved case study numbers. Approval facts in [customers.md](customers.md); the asset itself in [content-assets.md](content-assets.md).
- [confirmed | interview:dana-okafor | 2026-07-23]

## Sales motion facts

- ACV: Growth lands at $14.4k, Scale at $36k; blended median ACV was $26k in H1 2026. [confirmed | interview:priya-shah | 2026-07-20] ^acv-bands
- Expansion motion: land on Growth, expand to Scale when the team adds a second CRM-connected motion; roughly a third of Growth accounts expand within a year. [confirmed | interview:priya-shah | 2026-07-20] ^expansion-motion
- Sales cycle length: **contested — do not cite a number** in copy or sequencing logic until oq-014 resolves. See below. ^sales-cycle-pointer

## Contested

### Average sales cycle length ^sales-cycle-length
- 45 days [source-backed | crm-hubspot:report-2026-q2-pipeline | 2026-07-01]
- "Closer to 90 days for anything above 20 seats" [confirmed | interview:priya-shah | 2026-07-20]
- Resolution path: segment the Q2 pipeline report by seat count; if the split confirms two populations, doctrine records two numbers, not an average. → [open-questions.md#oq-014](open-questions.md#oq-014)
