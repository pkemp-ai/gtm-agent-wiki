# Observations — consumer intake buffer

Append-only. Consumer agents never edit canonical files (SPEC §9); anything learned mid-run lands here as an entry. The maintainer consumes this file on every run — each entry is promoted into canon per the write matrix, converted to an open question, or discarded with a changelog note — and removes processed entries (the changelog keeps the audit trail). The test for writing here: *would someone who wasn't on this run need this?*

One discrete observation per entry. Three statements are three entries. Never edit or remove an entry that is already here, including your own.

<!-- Entry format (SPEC §9) — append below:

## 2026-08-19T15:42Z · <agent or session label>
- observation: <one actionable statement>
- suggested-target: <canonical file, e.g. competitors.md>
- evidence: <source-id>:<locator> — or interview:<person> / doc:<filename>, or a plain
  description of where you saw it when you have no pointer
-->

## 2026-08-19T14:05Z · outbound-draft agent · named-account sequence, HubSpot-install trigger

- observation: A prospect reply on the named-account sequence said they chose DashForge for a 40-seat pilot specifically because our Growth tier caps at 5 data sources and they run 7 paid channels. That is a packaging objection, not a multi-touch-depth objection, and it does not match how the DashForge counter-position is currently framed.
- suggested-target: competitors.md
- evidence: crm-hubspot:deal-11842 — the reply is on the deal record's email thread; no call, so no Gong locator
