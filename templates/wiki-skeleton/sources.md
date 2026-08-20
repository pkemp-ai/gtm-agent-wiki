---
type: system
description: "The source manifest — every input this wiki pulls from, how it is reached, what it feeds, and its freshness cursor"
owner: TBD
sources: []
update-cadence: per-run
staleness-horizon: n/a
evidence-as-of:
last-verified: 2026-08-19
---

# Sources

*This file IS the integration layer — the wiki declares its inputs here and hardcodes no connectors. The maintain run iterates this manifest and uses whatever `access` each entry declares. A source whose access fails is marked broken here and surfaced in the digest, never silently skipped (SPEC §10).*

```yaml
# Schema (SPEC §10) — one block per source:
#
# - id: <kebab-case id — claim tags cite it as <id>:<locator>>
#   kind: internal-chat | crm | analytics | call-recordings | interview |
#         community | stakeholder-docs | email | web | news | social |
#         reviews | manual   # kind may be a list
#   access: <how THIS deployment reaches the source — an MCP tool, an API, a CLI,
#            or "manual: ...". Declare the actual tool name here; playbooks refer
#            to it only as "the tool declared in sources.md">
#   provenance-class: H | A | S | O | I
#     # or structured, when class depends on who wrote the item:
#     # provenance-class:
#     #   default: O
#     #   by-author:
#     #     <author-key>: H
#   feeds: [<canonical files this source may touch — scopes each run>]
#   cadence: per-run | daily | weekly | monthly
#   cursor:
#     last-run: <ISO timestamp of the last pull, or null>
#     marker: <source-native cursor — timestamp, since_id, page cursor, HEAD — or null;
#              sources without native cursors use time windows>
#   status: ok | pending-access | broken   # pending-access is onboarding, not an outage
#   consent: none | named-individuals-ok   # inherited by claims citing this source (SPEC 15.5)
#   filename-pattern: <glob for manual drops, when kind includes stakeholder-docs>
#   decision-channel: true   # optional; a principal issues rulings in this channel
#   archive: default | <path override for .archive/>
#   notes: <trust rules, per-channel class rules, gotchas>

- id: intake-inbox
  kind: [manual, stakeholder-docs]
  access: "manual: stakeholder drops exports and documents in intake/inbox/"
  provenance-class: H
  feeds: [business-core, icp-personas, voice, channel-styles, compliance-guardrails, glossary, growth]
  # ^ tune during build: list the files stakeholder drops typically feed
  cadence: weekly
  cursor:
    last-run: null    # stamped by the first maintain run
    marker: null      # manual source — no native cursor; each run processes what it finds
  status: ok
  consent: none
  filename-pattern: "*.md"
  decision-channel: false
  archive: default
  notes: Every deployment starts with this source — a wiki with no integrations is
    still valid (SPEC §3). Human-authored strategy docs dropped here are H-class
    and cite `intake-inbox:<run-id>/<file>`, not `doc:<file>`. Forwarded external
    material is O-class and must not land in doctrine. Raw drops are archived to
    .archive/intake-inbox/<run-id>/ before synthesis, like any other pull.
```
