---
type: state
description: "TBD (write for retrieval): upcoming and recent field and market events, and why marketing cares about each"
owner: TBD
sources: []
update-cadence: per-run
staleness-horizon: 90d   # rolling capped log: 90d / 100 entries, monthly roll-ups
evidence-as-of:
last-verified: 2026-08-19
---

# Events

*State — the running log of field events and market events, capped at 90 days / 100 entries with monthly roll-ups (SPEC §13).*

## Upcoming

*What goes here: a dated list of conferences, webinars, and launches we're attached to.*

## Log

*What goes here: newest-first entries — `#### 2026-08-14 · <event>` with 2–3 lines on what happened and why marketing cares. Append-open: consumer agents may add entries here directly (SPEC §9). Product launches get one line linking to [product-releases.md](product-releases.md), which owns the detail; competitor events go to [competitors.md](competitors.md).*

## Roll-ups

*What goes here: monthly summaries of aged-out entries; detail beyond the window archives to `references/events-<year>.md`.*
