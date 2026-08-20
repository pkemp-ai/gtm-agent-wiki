---
type: runbook
description: "TBD (write for retrieval): which CRM is the system of record, how agents access it, core objects and fields, standard queries"
owner: TBD
sources: []
update-cadence: monthly   # verification cadence
staleness-horizon: 60d
evidence-as-of:
last-verified: 2026-08-19
---

# CRM

*Runbook — verified by execution: every access pattern carries a `verified: <date>` stamp from actually running it; failures are marked **broken** with the error, never deleted (SPEC §8).*

## System of record

*What goes here: which CRM, who administers it, and the data-hygiene reality — which fields to trust.*

## Access

*What goes here: how agents connect — the tool declared in [sources.md](sources.md), an API, or an export path — and credential LOCATIONS (env-var names, vault paths), never values (SPEC §15.3).*

## Core objects and fields

*What goes here: the objects and fields marketing agents actually use, with gotchas.*

## Standard queries

*What goes here: customer list, pipeline report, target accounts, win/loss pulls — each with a verified stamp. What the pipeline currently SHOWS lives in [pipeline.md](pipeline.md); who owns which accounts in [account-ownership.md](account-ownership.md).*
