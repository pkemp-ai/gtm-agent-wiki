---
type: state
description: "TBD (write for retrieval): shape of the customer base, approved reference customers, usable success stories, churn signals"
owner: TBD
sources: []
update-cadence: weekly
staleness-horizon: 60d
evidence-as-of:
last-verified: 2026-08-19
---

# Customers

*State — who the customers are and which stories are usable. PII minimization applies (SPEC §15.5): companies, roles, and deal facts only — personal contact data stays in the CRM, which [crm.md](crm.md) tells agents how to query.*

## Customer base

*What goes here: the shape of the base — count, segments, notable logos — S-class from CRM queries.*

## Reference customers

*What goes here: customers approved for public reference, with exactly what they approved (logo? quote? case study?). Approval facts are H-class — never infer permission from usage.*

## Success stories

*What goes here: one entry per usable story — customer, result with numbers and their substantiation, and where the full asset lives → [content-assets.md](content-assets.md). The substance lives here; that file is only the catalog.*

## Churn signals <!-- tier: state, sensitive -->

*What goes here: patterns worth knowing when writing retention and expansion copy. Sensitive — keep at pattern level; named at-risk accounts never enter the wiki. Omit `## Contested` until a real collision exists.*
