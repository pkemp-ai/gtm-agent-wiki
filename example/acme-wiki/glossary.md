---
type: doctrine
description: Canonical terminology — product names and casing, the words we use and avoid for key concepts, customer-vocabulary mappings, and banned words with replacements.
owner: Morgan Lee (marketing ops)
sources: [interviews, gong]
update-cadence: per-run
staleness-horizon: 180d
evidence-as-of: 2026-07-30
last-verified: 2026-08-19
---

# Glossary

The smallest doctrine file. Anything needing a paragraph of explanation lives elsewhere, with a line here linking to it.

## Product names and capitalization

| Name | Ruling |
|---|---|
| Acme Analytics | Full name on first use, "Acme" after. Never "AcmeAnalytics," "ACME," or "AA" |
| Model Lab | Two words, both capitalized — the attribution-model workspace in Scale and Enterprise |
| Acme Sync for HubSpot | Full name in docs and web copy; "the HubSpot sync" is fine in body text |
| Journeys | Capitalized when naming the feature; lowercase when describing a buyer's journey |

[confirmed | interview:morgan-lee | 2026-07-30] ^product-names

## Terms we use

| Concept | We say | We avoid | Why |
|---|---|---|---|
| The category | revenue attribution | marketing analytics, MMM | Deliberate category decision — [business-core.md](business-core.md#category) |
| What we measure | pipeline created | leads generated, MQLs driven | Pipeline is the unit the board trusts |
| The method | multi-touch (hyphenated) | multitouch, "MTA" in customer-facing copy | Acronyms hide the meaning |
| Getting started | implementation | onboarding journey, activation | Plain word, no euphemism |

[confirmed | interview:dana-okafor | 2026-07-30] ^terms-we-use

## Terms customers use

Customer vocabulary mapped to ours. The phrases-as-evidence live in [icp-personas.md](icp-personas.md#customer-language); this table is the ruling on how we translate them in copy.

| Customers say | We write |
|---|---|
| "spreadsheet hell" | manual attribution |
| "flying blind" | no revenue visibility |
| "which half of the budget works" | channel-level attribution |

[confirmed | interview:dana-okafor | 2026-07-30] ^customer-term-map

### Dark social — no ruling ^term-dark-social

**No ruling yet:** customers say "dark social" for touches that surface as direct traffic. Until a human rules, neither their word nor a replacement for it is ours to write — quote the customer or leave the subject alone. The proposed wording sits with the question, not here: [open-questions.md#oq-021](open-questions.md#oq-021).

## Banned words

| Banned | Use instead |
|---|---|
| revolutionary, game-changing | (cut — state the number) |
| seamless | name the actual integration behavior |
| leverage (as a verb) | use |
| solution | product, platform |
| best-in-class, world-class | the specific comparison, sourced |
| unlock, supercharge, turbocharge | (cut) |

[confirmed | doc:2026-voice-guide.md | 2026-06-30] ^banned-words

The posture behind these bans: [voice.md](voice.md#never). Claim-level prohibitions: [compliance-guardrails.md](compliance-guardrails.md#banned-claims).
