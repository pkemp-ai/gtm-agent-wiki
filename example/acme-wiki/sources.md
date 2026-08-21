---
type: system
description: The source manifest — every input Acme's wiki pulls from, how this deployment reaches it, what it feeds, its trust class, and its freshness cursor.
owner: Morgan Lee (marketing ops)
sources: []
update-cadence: per-run
staleness-horizon: n/a
evidence-as-of: 2026-08-19
last-verified: 2026-08-19
---

# Sources

*This file IS the integration layer: fourteen declared inputs, no connector code anywhere in the deployment. Each maintain run iterates these blocks, uses whatever `access` declares, and advances the cursor it actually consumed. A source whose access fails is marked `broken:` here with its cursor held, and surfaced in the digest — never silently skipped (SPEC §10).*

Reading the classes: `provenance-class` is what the *channel* confers, never what the content claims about itself. A Slack message from Sam Whitfield is H-class because he speaks for the org in that channel; the same claim quoted inside a competitor's page is A-class about them and nothing about us.

Locator conventions, because two kinds appear in claim tags across this wiki:

| Locator shape | Example | Resolves to |
|---|---|---|
| `<run-id>/<file>` | `web-metricflow:2026-08-10/pricing.html` | a raw payload in `.archive/web-metricflow/2026-08-10/` |
| `<report or object id>` | `crm-hubspot:report-2026-08-owner-map` | a re-runnable report in the system itself, per [crm.md](crm.md#standard-queries) |

Both satisfy SPEC §17.2. The second shape is used where the query is deterministic and repeatable; the run's CSV export is archived alongside it anyway, so an auditor never has to trust that the report still returns what it returned.

```yaml
# Schema (SPEC §10) — one block per source:
#
# - id: <kebab-case id — claim tags cite it as <id>:<locator>>
#   kind: internal-chat | crm | analytics | call-recordings | interview |
#         community | stakeholder-docs | email | web | news | social |
#         reviews | manual   # kind may be a list
#   access: <how THIS deployment reaches the source>
#   provenance-class: <H | A | S | O | I — or a by-author rule>
#   feeds: [<canonical files this source may touch — scopes each run>]
#   cadence: per-run | daily | weekly | monthly
#   cursor: {last-run, marker}
#   status: ok | pending-access | broken
#   consent: none | named-individuals-ok
#   filename-pattern: <glob for manual drops, when kind includes stakeholder-docs>
#   decision-channel: true   # optional; a principal issues rulings in this channel
#   broken: {since, error}   # present only while access is failing
#   archive: default | <path override>
#   notes: <trust rules, gotchas>

# ── Human channels ────────────────────────────────────────────────────────

- id: interviews
  kind: manual
  access: "manual: stakeholder sessions and digest replies, transcribed into .archive/interviews/<run-id>/session-notes.md by the interview playbook"
  provenance-class: H
  feeds: [business-core, icp-personas, voice, channel-styles, compliance-guardrails, glossary, growth, competitors, customers, events, product-releases, partners, account-ownership, pipeline, content-assets, metrics, crm, gtm-tools]
  cadence: weekly
  cursor:
    last-run: 2026-08-17T15:00:00Z
    marker: "session:2026-08-17-morgan-lee"
  status: ok
  consent: none
  decision-channel: true
  archive: default
  notes: The only source that may write doctrine. Claim tags cite the person, not this id — interview:dana-okafor, interview:sam-whitfield, interview:priya-shah, interview:morgan-lee. Digest replies count as sessions.

- id: inbox-docs
  kind: manual
  access: "manual: humans drop exports, decks, and strategy docs in intake/inbox/; each run archives them and empties the folder"
  provenance-class: H-when-human-authored, O otherwise
  feeds: [business-core, voice, channel-styles, growth, customers, events, product-releases, partners, pipeline, content-assets]
  cadence: weekly
  cursor:
    last-run: 2026-08-19T09:00:00Z
    marker: null
  status: ok
  consent: none
  filename-pattern: "*.md"
  decision-channel: false
  archive: default
  notes: Human-authored strategy docs dropped here are H-class and cite `inbox-docs:<run-id>/<file>` once archived. `doc:<filename>` survives only for artifacts this trimmed example did not archive (the voice guide, the H2 growth plan). Empty inbox is a meaningful no-op signal (SPEC §10) — it was empty at the last run. Forwarded external material is O-class.

- id: slack-gtm
  kind: internal-chat
  access: "mcp: <workspace chat search tool> — channels #gtm, #product-launches, #wins"
  provenance-class: H when an exec or a function owner posts inside their own domain; A for release announcements in #product-launches — our own official record of what shipped; O for anything relayed from outside the org
  feeds: [events, product-releases, gtm-tools, crm]
  cadence: daily
  cursor:
    last-run: 2026-08-19T09:00:00Z
    marker: "ts:1787130000"
  archive: default
  notes: Daily pulls, so a run-id and the message dates inside it line up. Standing is by domain — Sam Whitfield and Dana Okafor on strategy, Priya Shah on sales, Morgan Lee on ops and tooling — and it does not travel: the same person relaying news from outside the org is O-class. The release account posting in #product-launches is not a person and confers no H; its announcements are A-class about our own product, which is what the source-backed entries in product-releases.md cite. Pinned messages are treated as current, not historical.

# ── Internal systems ──────────────────────────────────────────────────────

- id: crm-hubspot
  kind: crm
  access: "mcp: <CRM read tool> — saved reports and object search, read-only scopes; token in env HUBSPOT_PRIVATE_APP_TOKEN"
  provenance-class: S
  feeds: [business-core, icp-personas, competitors, customers, events, partners, account-ownership, pipeline, content-assets, metrics, crm, gtm-tools]
  cadence: weekly
  cursor:
    last-run: 2026-08-17T09:00:00Z
    marker: "hs-lastmodified:2026-08-17T09:00:00Z"
  archive: default
  notes: System of record for pipeline, ownership, and the customer base. Field-level trust is not uniform — see the hygiene table in crm.md before citing any property. Report exports are archived per run even though claim locators name the report.

- id: gong
  kind: call-recordings
  access: "mcp: <call-recording search tool> — transcripts and call metadata, no recording downloads; token in env GONG_ACCESS_KEY"
  provenance-class: S for the transcript as a record; H when an Acme exec states a decision on the call; O for anything a third party asserts inside it
  feeds: [icp-personas, glossary, competitors, pipeline]
  cadence: weekly
  cursor:
    last-run: 2026-08-13T09:00:00Z
    marker: "call-id:9188"
  archive: default
  notes: Verbatim customer phrasing is the point — quote exactly into icp-personas customer language, where the claim is that the phrase was said (the transcript as a record, S) and never that what the customer said is true. Call content is evidence for this wiki and never material for outbound personalization (compliance-guardrails.md).

- id: ga4
  kind: analytics
  access: "mcp: <web analytics report tool> — read-only property access; service-account key path in env GA4_CREDENTIALS_PATH"
  provenance-class: S
  feeds: [content-assets, metrics, gtm-tools]
  cadence: weekly
  cursor:
    last-run: 2026-08-17T09:00:00Z
    marker: "window-end:2026-08-17"
  archive: default
  notes: The reporting UI default lookback changed from 90 to 30 days on 2026-08-12, so every pull states its window explicitly rather than accepting the default. Session and pageview numbers here will not match CRM-side attribution — that disagreement is mapped in gtm-tools.md data flows.

- id: webflow
  kind: web
  access: "mcp: <CMS inventory tool> — page and collection listing plus published HTML; token in env WEBFLOW_API_TOKEN"
  provenance-class: A for published page content — our own publication about ourselves; S for the CMS inventory read
  feeds: [product-releases, content-assets, metrics, gtm-tools]
  cadence: weekly
  cursor:
    last-run: 2026-08-17T09:00:00Z
    marker: "cms-updatedAt:2026-08-17T06:12:00Z"
  archive: default
  notes: Our own site is authoritative about what we currently claim in public, which is exactly why it can collide with an internal announcement — see the GA-versus-beta contested entry in product-releases.md.

# ── Competitor and partner publications (A-class) ──────────────────────────

- id: web-metricflow
  kind: web
  access: "your harness's web access — fetch pricing, implementation guide, case studies, and blog index; no login, no crawling beyond those paths"
  provenance-class: A
  feeds: [competitors]
  cadence: monthly
  cursor:
    last-run: 2026-08-10T09:00:00Z
    marker: "content-hash:pricing=9f2c1b,case-studies=4ad0e7"
  archive: default
  notes: A-class about themselves, so pricing and stated implementation timelines may supersede our snapshot silently with a changelog line (SPEC §7.2). Their claims about us are O-class and enter as watchlist at most.

- id: web-dashforge
  kind: web
  access: "your harness's web access — fetch pricing page and product blog; self-serve signup pages are out of scope"
  provenance-class: A
  feeds: [competitors]
  cadence: monthly
  cursor:
    last-run: 2026-08-10T09:00:00Z
    marker: "content-hash:pricing=b71e08"
  archive: default
  notes: Public pricing changes often and is the single most useful field on this source. Feature depth claims on their site are theirs to make; whether the feature does what the word implies is a reviews-web question, not this one.

- id: web-attribia
  kind: web
  access: "your harness's web access — fetch homepage, pricing, and docs index"
  provenance-class: A
  feeds: [competitors]
  cadence: monthly
  cursor:
    last-run: 2026-08-10T09:00:00Z
    marker: "content-hash:index=3c55da,pricing=e0918f"
  archive: default
  notes: No public pricing — the pricing page routes to a form, and that absence is itself the tracked fact. Their marketing copy is aimed partly at us; it is evidence about their positioning, never about our product.

- id: web-hubspot
  kind: web
  access: "your harness's web access — fetch app-partner program requirements and marketplace listing policy pages"
  provenance-class: A
  feeds: [partners]
  cadence: monthly
  cursor:
    last-run: 2026-08-03T09:00:00Z
    marker: "content-hash:app-partner-requirements=5d21c4"
  archive: default
  notes: Platform rules bind what we may say about the relationship, so a change here can invalidate approved co-marketing language overnight. What we are allowed to say remains an H-class decision in partners.md; only their published rules update silently.

# ── Third-party signal (O-class, watchlist only) ───────────────────────────

- id: news-web
  kind: news
  access: "your harness's web access — trade-press search for tracked competitor and category terms, results window bounded by the cursor"
  provenance-class: O
  feeds: [competitors, events]
  cadence: weekly
  cursor:
    last-run: 2026-08-15T09:00:00Z
    marker: "since:2026-08-08"
  archive: default
  notes: Enters as watchlist and can never touch doctrine (SPEC §8). Funding, headcount, and internals stay out of copy entirely regardless of label (compliance-guardrails.md). A second independent source promotes to source-backed; volume of coverage never does.

- id: reviews-web
  kind: reviews
  access: "your harness's web access — public review pages for Acme and the three tracked competitors, paginated by the cursor"
  provenance-class: O
  feeds: [competitors, customers, content-assets]
  cadence: monthly
  cursor:
    last-run: 2026-08-08T09:00:00Z
    marker: "review-id:3312"
  archive: default
  notes: Single reviews are anecdotes with a claim tag. The rule of three applies: a pattern becomes an open question at the third independent mention, not the first. Reviewer names and employers are never copied into the wiki.

- id: social-linkedin
  kind: social
  access: "your harness's web access — public company-page posts and job listings for tracked competitors"
  provenance-class: O
  feeds: [competitors]
  cadence: weekly
  status: broken
  broken: {since: 2026-08-14, error: "saved session expired; public post listing returns an interstitial instead of content"}
  cursor:
    last-run: 2026-08-11T09:00:00Z
    marker: "post-id:li-88214"
  archive: default
  notes: Cursor held at the last good pull and retried every run per SPEC §10 — escalated in the 2026-08-19 digest. Our own founder-brand posting is a channel decision in channel-styles.md, not an input; this source only watches competitors.
```

## How to change this file

Adding a source is a build-or-interview decision, not a maintain-run decision: a new input changes what the wiki can know, which files it can touch, and who is accountable for the access. Adding a **file** is a different decision — SPEC §3, maintainer-only, recorded reason. Neither is the other. Cursors, `broken:` markers, and recovery lines are the maintainer's to write on every run. If evidence clearly bears on a file outside a source's `feeds:`, widen `feeds:` in the same run and changelog it — never leave a known-false `confirmed` claim standing on a scoping technicality (SPEC §10).
