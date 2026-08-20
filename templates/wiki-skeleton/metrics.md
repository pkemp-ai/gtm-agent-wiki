---
type: runbook
description: "TBD (write for retrieval): KPI definitions, where the data lives, verified query patterns, reporting conventions"
owner: TBD
sources: []
update-cadence: monthly   # verification cadence
staleness-horizon: 60d
evidence-as-of:
last-verified: 2026-08-19
---

# Metrics

*Runbook — verified by execution: every access pattern carries a `verified: <date>` stamp from actually running it; failures are marked **broken** with the error, never deleted (SPEC §8).*

## North star

*What goes here: the one metric the company actually runs on, named by a human. It is a decision, so it needs H-class provenance, and it is frequently not any of the metrics on the dashboard. Without it a wiki full of KPI definitions lets agents optimize a vanity metric in good faith.*

## KPI definitions

*What goes here: per KPI — the exact definition, its owner, and why it's defined this way. Definitions are H-class doctrine-in-exile; only the queries below are runbook.*

## Where data lives

*What goes here: system → what's authoritative there. The full stack map lives in [gtm-tools.md](gtm-tools.md).*

## Query patterns

*What goes here: per KPI — the query, report, or tool call that produces it, its last-verified stamp, and known pitfalls. Current metric VALUES never live here (they rot). Put them in [pipeline.md](pipeline.md)'s snapshot where that file exists; where pipeline is omitted, add a `## Snapshot` section here (marked `<!-- tier: state -->`, as-of dated) rather than leaving headline numbers homeless.*

## Reporting conventions

*What goes here: periods, attribution model, the charts leadership expects.*
