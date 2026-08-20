---
type: doctrine
description: What marketing agents may never say or do — banned claims, competitor conduct, trademark rules, embargoes with expiry, and data rules for outbound. Read before any content task.
owner: Dana Okafor (CMO)
sources: [interviews]
update-cadence: interview
staleness-horizon: 90d
evidence-as-of: 2026-08-11
last-verified: 2026-08-19
---

# Compliance guardrails

Prohibitions only, so the signal stays sharp. What agents *may* claim lives in [business-core.md](business-core.md#approved-claims). Every content task reads this file — no exceptions. Ask the origin story of every hard prohibition.

## Legal constraints on go-to-market

No territorial exclusivity, no right of first refusal, no OEM or white-label obligation. The only hard commercial constraint on *who we may sell to* is the anti-ICP line: we do not white-label, and we do not take B2C. That is a go-to-market constraint, not just a qualification rule — an agency asking for a white-label motion is a no, not a later.
[confirmed | interview:sam-whitfield | 2026-08-11] ^legal-no-whitelabel

## Approval workflow

Dana Okafor signs every customer-facing claim, embargo exception, and comparison page. Morgan Lee signs security wording and HubSpot-listing copy. Turnaround is two business days for claims and five for comparison pages; first-pass rejection on comparison pages has been high enough that we budget the extra cycle rather than hoping. Nothing ships on a founder's verbal "looks fine."
[confirmed | interview:dana-okafor | 2026-07-16] ^approval-workflow

## Banned claims

| Banned | Why |
|---|---|
| "The most accurate attribution" — or any accuracy superlative | Unsubstantiable; attribution accuracy has no agreed benchmark, and we won't pretend it does |
| "Guaranteed pipeline lift" / "guaranteed ROI" | Results depend on the customer's spend decisions; we report, they act |
| "Eliminates the need for a data team" | Overclaim. The approved scope is attribution without a data team ([business-core.md](business-core.md#claim-no-data-team)) — nothing wider |
| "AI-powered" as a headline claim | Describes nothing and points at Attribia's lane; name the actual function instead |
| Any revenue or pipeline number for a named customer without a matching approval in [customers.md](customers.md) | Customer approval is per-number, not per-logo |
| "GDPR compliant" / "makes you compliant" | We support customers' compliance work; we do not confer compliance |

[confirmed | interview:dana-okafor | 2026-07-09] ^banned-claims

## Regulated constraints

- Security wording: "SOC 2 Type II," and where space allows "audited annually." Never "certified" (SOC 2 is an attestation, not a certification); never "bank-grade" or "military-grade." [confirmed | interview:morgan-lee | 2026-07-30] ^soc2-wording
- Data residency: never promise EU data residency. It is not offered; prospects who need it get a straight no. [confirmed | interview:sam-whitfield | 2026-07-02] ^no-residency-promises
- Customers in regulated industries (e.g. Corvid Security, Brightpath HR): never imply Acme performs or automates their regulatory obligations. [confirmed | interview:dana-okafor | 2026-07-09] ^regulated-customers

## Competitor conduct

- Naming: competitors may be named in comparison pages and battlecards — never in ad copy or social posts. [confirmed | interview:dana-okafor | 2026-07-16] ^naming-policy
- Comparisons state facts with dated evidence from the competitor's own materials — pricing, implementation claims, feature presence. Nothing about their customers, funding, or internals, regardless of what we've heard. Evidence base: [competitors.md](competitors.md) and [references/battlecard-metricflow.md](references/battlecard-metricflow.md). [confirmed | interview:dana-okafor | 2026-07-16] ^comparison-rules
- Never engage Attribia bait threads on LinkedIn. Their motion runs on manufactured controversy; ours does not. [confirmed | interview:sam-whitfield | 2026-07-16] ^attribia-no-engage

## Trademark and naming

- Our mark: "Acme Analytics" on first use, "Acme" after. Never "AcmeAnalytics," "ACME," or a ™/® in copy. Full casing rulings: [glossary.md](glossary.md#product-names-and-capitalization). [confirmed | interview:morgan-lee | 2026-07-30] ^our-marks
- Their marks: MetricFlow, DashForge, Attribia, HubSpot, Salesforce, Gong — rendered exactly as the owner renders them, no abbreviations. [confirmed | interview:morgan-lee | 2026-07-30] ^their-marks

## Embargoes and timing

| Embargoed | Rule | Expires |
|---|---|---|
| Bidirectional Salesforce sync (internal name "Twinbridge") | No public mention anywhere — including "coming soon" hints, sales decks that leave the building, and roadmap answers on calls — until the launch post is live | 2026-09-10 |

[confirmed | interview:sam-whitfield | 2026-08-11] ^embargo-twinbridge

Expired embargoes are removed by the maintainer with a changelog entry. If an expiry date here is in the past, check [changelog.md](changelog.md) before assuming the embargo lifted.

## Data and privacy in outbound

- No individual names, quotes, or title-plus-company combinations from CRM records or call recordings in external copy without the approval trail in [customers.md](customers.md). [confirmed | interview:dana-okafor | 2026-08-05] ^no-unapproved-individuals
- No screenshots of real customer dashboards; demo assets come from the seeded demo org only. [confirmed | interview:morgan-lee | 2026-07-30] ^demo-org-only
- Outbound personalization is limited to: first name, company, stack signals, and publicly stated facts. Nothing mined from Gong. [confirmed | interview:dana-okafor | 2026-08-05] ^personalization-limits

## Contested

*(empty by decision — no contested guardrails, 2026-08-19)*
