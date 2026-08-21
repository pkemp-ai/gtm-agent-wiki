# The Canonical Taxonomy

**Version 0.2 — companion to [SPEC.md](SPEC.md)**

This document defines every file in a deployed GTM wiki: its purpose, tier, typical sources, internal schema, freshness policy, and boundaries. The builder playbook creates these files; the interview question bank is organized around them; the maintainer's write rules key off each file's tier.

Two rules frame everything here, followed by the conventions every file inherits:

- **The top level is a starting place.** These files are the default root set. Depth and growth go into `references/` unless the SPEC §3 ladder fails. A deployment may omit files that don't apply (recorded in `AGENTS.md`), reinterpret a file whose name doesn't fit, or add a top-level file with a taxonomy entry in `AGENTS.md` (purpose, tier, schema, boundary vs the nearest home). An undeclared root file is a lint failure.
- **One canonical home per concept.** Every boundary note below exists to prevent the same fact living in two files. When in doubt, the fact goes in the file whose *consumers* need it most, and other files link to it. A new root file that duplicates an existing home is the expensive failure; the §3 boundary line exists to stop that.

Front-matter defaults given per file below (`cadence`, `staleness-horizon`) are starting points; deployments tune them in each file's front matter.

**Four dispositions.** A canonical file that doesn't fit a deployment, or a concept that has no home yet, has four legitimate outcomes, and picking the wrong one loses content:

1. **Keep** — the normal case.
2. **Omit** — the underlying need genuinely does not exist. Delete the file (don't ship a stub) and record the omission in `AGENTS.md` deployment notes with the reason.
3. **Retain with reinterpreted scope** — the file's *name* assumes a shape this company lacks, but the underlying need is real. Keep the file, state its local reading at the top, and record it as a local taxonomy change. A PLG company with no CRM still has a customer system of record and still needs "which fields to trust"; a services company with no product releases still launches service lines. Reaching for *omit* when the answer is *reinterpret* is the most common way a deployment loses something important.
4. **Add** — no existing file, section, or `references/` page can hold the concept as a consumer starting point. New top-level file, SPEC §3 protocol, recorded as a local taxonomy addition. Restoring a previously omitted file is this disposition in reverse: the motion now exists.

**`## Contested` is omitted when empty.** Only include the section when a real collision exists — an empty heading with placeholder text is noise in every file, and repeated across eighteen files it is a meaningful tax on readers. The single exception is `compliance-guardrails.md`, where the section is always present and reads `*(empty by decision — no contested guardrails, <date>)*`, because for guardrails "we checked and there are none" is materially different from "nobody looked."

**Spell out "and" in prescribed headings.** Never `&` — it slugs to a double hyphen (`## Trademark & naming` → `#trademark--naming`), which silently breaks every anchor written the natural way.

**Designated evidence sections.** Three doctrine sections exist to hold evidence *in its own words*, and they keep their evidence's true provenance class permanently. This is SPEC §17.3(b), and it survives delivery — it is not the bootstrap exception in disguise:

| Section | Holds | Class it keeps |
|---|---|---|
| `icp-personas.md ## Customer language` | verbatim customer phrasing | O, or whatever the source is |
| `voice.md ## Exemplars` | on-voice passages, ours or borrowed | H / A / O as sourced |
| `channel-styles.md ### Examples` | links to strong past pieces | S / A |

A claim in one of these sections is illustration, never a decision: it may never be the only tag under an assertion a consumer would act on as doctrine. Everything else in a doctrine file is H-class or it does not belong there.

**Two more sections any doctrine file may carry.** `## Contested` for evidence conflicts (SPEC §4.3, omitted when empty) and `## Live tensions` for a decision the org has not made and marketing may not make for it (SPEC §8.2). They are different surfaces and neither substitutes for the other: contested is "the evidence disagrees," a live tension is "two people with standing disagree and nobody has ruled."

**The `blocked` marker.** Some constraints are neither prohibitions, nor decisions, nor open questions — they are drafting freezes. Any section may carry one, and it names its owner and the condition that lifts it:

```markdown
> **blocked** — no partner-facing collateral until the Tri-County agreement is countersigned.
> owner: Margo · unblocks: countersignature, expected September
```

Prose emphasis and hope are not a mechanism. An agent reading a rich partner section needs the freeze to be structurally visible, or the single most important fact — that it may not write a word of this today — is carried by tone. Freezes on a specific asset live beside the asset in `content-assets.md`; freezes on a whole motion live in the file describing the motion; freezes imposed by the review process live in `compliance-guardrails.md ## Approval workflow`.

**Optional files.** `pipeline.md`, `account-ownership.md`, `product-releases.md`, and `glossary.md` (when the vocabulary is thin) are optional — omit or reinterpret them without ceremony. Deployments with no agent-reachable systems collapse the three runbook files into one; the runbook section below states what must survive that merge.

---

## The manifest — `AGENTS.md`

**Tier:** system · **Cadence:** per-run (regenerated sections) · **Horizon:** n/a

The wiki's front door, named per the [agents.md](https://agents.md) convention so that agent harnesses (Claude Code, Codex, Cursor, Gemini CLI) load it automatically when working in the wiki directory. It contains, in order:

1. **The company in three sentences.** What the org sells, to whom, and why it wins. Hand-written during build, doctrine-sourced.
2. **File inventory table** — one row per root file with parseable front matter: name, tier, `description` (pulled from front matter), `evidence-as-of`, `last-verified`. Taxonomy order first, then local additions alphabetically. Both dates, because a consumer deciding whether to trust a file needs to know how old the evidence is *and* when a human last looked (SPEC §4.1). *Machine-generated by `scripts/sync_manifest.py`; never hand-edited.*
3. **Read order** — which files a consumer reads for common tasks (e.g. "writing outbound copy → voice, channel-styles, compliance-guardrails, icp-personas, glossary; anything customer-facing → compliance-guardrails always").
4. **The reading contract** — the consumer rules (trust semantics, citation discipline, write-back rules), embedded from [consumer/AGENTS.md](../consumer/AGENTS.md).
5. **Deployment notes** — omitted files and why, local taxonomy additions (purpose, tier, schema, boundary vs the nearest canonical home), storage adapter in use, digest recipient and cadence. The inventory table is generated; the taxonomy entry is hand-written prose in this section, which is what lint's `top-level-growth` check reads.

**Boundaries:** no knowledge lives here. The three-sentence summary cites `business-core.md`; everything else is navigation and rules.

---

## Doctrine files

Decisions the org has made. H-class provenance required to change (SPEC §8). Small, read whole by every consumer. Doctrine staleness produces open questions ("is this still true?"), never silent edits.

### `business-core.md`

**Tier:** doctrine · **Cadence:** interview / quarterly · **Horizon:** 120d

What the company sells and why it wins. Sections, in order:

- `## Company facts` — founding, ownership and capital structure, headcount, geography and languages, decision horizon. The flat premises everything else is downstream of. It goes first because it is short, because a consumer answering "who are these people" should not have to infer it, and because doctrine that contradicts it is usually wrong: *"no outside capital, no board seats sold, we optimise for twenty years — everything conservative is downstream of that"* was extracted in an interview's second sentence and evaporated, because no section owned it. That is the largest single content loss recorded in the end-to-end test
- `## Product` — what it is, in customer language; the 2–3 jobs it does. An org with several lines or services gives each a `### <line>` subsection carrying its own buyer, price, and motion — one undifferentiated `## Product` for five service lines is how two of them ended up named nowhere in the wiki
- `## Positioning` — category, for-whom statement, differentiated value; the positioning sentence agents build on
- `## Right to win` — the honest structural advantages (and their limits)
- `## Pricing` — model, tiers, floors, discount policy; what agents may say about price. Carry the actual numbers, not only the permissions — a file with pricing doctrine and no prices is a common and expensive miss <!-- if pricing is complex, fan out to references/pricing.md -->
- `## Approved claims` — the exact claims agents may make, each with its substantiation `^claim-<key>`, plus a **lead claim** pointer naming which one heads a capability announcement. A flat numbered list makes every consumer rank the claims itself, and consumers rank them differently
- `## Sales motion facts` — cycle length, ACV bands, expansion motion. Section name and anchors here are **illustrative**: an org with no sales motion omits the section rather than reshaping itself to fit it. Naming a sales cycle in a company that has none summons one
- `## Contested`

**Boundaries:** banned claims live in `compliance-guardrails.md` (the un-missable file), not here. Contracts that constrain who may be sold to → `compliance-guardrails.md ## Legal constraints on go-to-market`. Persona-specific value props live in `icp-personas.md`. Strategy and channel bets live in `growth.md`.

### `icp-personas.md`

**Tier:** doctrine · **Cadence:** interview / quarterly · **Horizon:** 120d

Who we sell to, who we don't, and how they talk. Sections:

- `## ICP` — firmographic definition: segment, size, industry, stack signals, disqualifiers
- `## Anti-ICP` — who we actively avoid and why (churn history, support cost, mission mismatch), including the disqualifiers nobody has written down
- `## Personas` — per persona: role, pains, triggers, objections, what convinces them; one subsection each, fan out to `references/persona-<name>.md` when deep. **Exactly one persona carries a `primary: true` marker**, or the section carries a per-channel default map ("web and catalog default to the reliability engineer; LinkedIn to the plant manager"). Without it a consumer writing one asset has to rank the personas itself: two of three test consumers guessed, one by cross-referencing an unrelated file's authorship convention
- `## Channel personas` — for orgs selling through distributors, resellers, or platforms: the partner rep is an audience with his own pains, incentives, and objections, marketed **to** in order to sell **through**. Mark the section `<!-- not a buyer: we market THROUGH them -->`, fan out to `references/persona-<name>.md`, and point the fan-out's parent link at `partners.md`. Omit where no channel motion exists. The deployment whose distributor reps carried 70% of revenue shipped with no entry for them anywhere, because there was no slot and the placement question went to a stakeholder who correctly refused to answer it
- `## Customer language` — verbatim phrases customers use for their problem and our solution (mined from calls/reviews; each phrase cites its source and **keeps that source's provenance class** — a designated evidence section, SPEC §17.3(b)). Attribute quotes by role, never by name, unless the source carries a `consent:` record (SPEC §15.5)
- `## Contested`

**Boundaries:** the current customer *list* is state → `customers.md`. Persona-targeted channel tactics → `growth.md`. The channel *motion* the channel persona sits inside → `partners.md ## Channel motion`.

### `voice.md`

**Tier:** doctrine · **Cadence:** interview / semiannual · **Horizon:** 180d

How the brand talks, everywhere. Sections:

- `## Voice attributes` — 3–5 named attributes, each with a one-line definition and a do/don't pair
- `## Tone by context` — how voice flexes: educational vs. promotional vs. support vs. crisis
- `## Never` — constructions, cliches, and postures the brand never uses
- `## Exemplars` — 3–5 short passages of on-voice writing, with why they work. A designated evidence section (SPEC §17.3(b)): an exemplar keeps its source's provenance class, and a borrowed passage is not a decision about our voice — the surrounding note is
- `## Contested`

**Boundaries:** per-channel mechanics (lengths, formats, hashtags, CTAs) → `channel-styles.md`. Word-level rules (capitalization, banned words, product names) → `glossary.md`.

### `channel-styles.md`

**Tier:** doctrine · **Cadence:** interview / quarterly · **Horizon:** 120d

Prescriptive per-channel rules — one section per channel the org actually uses.

**The channel list is illustrative, not prescriptive.** Sections are added and deleted freely to match the real channel set, with no taxonomy entry, no deployment note, and no open question required. Read as a fixed set, this file was the worst fit in all three test companies at once: each carried several inactive sections while its single most important channel — a community server, a trade-show booth and demo rig, a print catalog — had no section at all.

Illustrative sections, to pick from and extend:

| Section | Covers |
|---|---|
| `## LinkedIn` / `## X` | post length, structure, link and hashtag policy, what performs |
| `## Blog` | structure, depth, SEO conventions, internal linking, bylines |
| `## Email` | outbound vs. newsletter rules, subject lines, length, sign-offs |
| `## Web` | page-copy conventions, headline patterns, CTA language |
| `## Paid` | ad-copy constraints per platform |
| `## Field and events` | booth copy, demo-rig rules, who staffs, what collateral travels |
| `## Print` | catalog and spec-sheet conventions, imagery rules, lead times |
| `## Channel collateral` | what a distributor is given, what it may alter, what it may not |
| `## Community` | a company-hosted server or forum: who may post, reply-once rules, whether agents may post at all |
| `## Docs` | where documentation is simultaneously product, channel, and voice exemplar |
| `## Webinars` | abstract conventions, registration copy, follow-up sequence |
| `## RFP and proposal responses` | structure, what may be promised, who signs off |

Required regardless of the channel set:

- `## Channels declared absent` — channels the org deliberately does not use, one line each with the reason. "Absent" and "undocumented" are different facts, and this section is what stops an agent inventing an email sequence for a company that has never sent one.
- A **cadence / rate limit** line in every active channel section: how often this channel may be used, and the ceiling. "≤2 launch posts per year, deliberately — you get two, then you're that guy" is a rate limit, not a strategy note; `growth.md ## Channel bets` carries ranking and thesis but no rate, so an agent with no ceiling plans a third launch and burns the channel permanently.
- `### Examples` at the end of each section, linking to strong past pieces in `content-assets.md`. A designated evidence section (SPEC §17.3(b)).
- `## Contested`

**Boundaries:** voice attributes live in `voice.md` — this file assumes them and adds channel mechanics. Channel *strategy* (which channels, how much, why) → `growth.md`. What happened at a specific event → `events.md`. One trade show splits three ways; see the coverage map.

### `compliance-guardrails.md`

**Tier:** doctrine · **Cadence:** interview / quarterly · **Horizon:** 90d — the strictest file in the wiki

The negative space: what marketing agents may never do or say. Kept separate from `business-core.md` so it cannot be missed — the read-order rule is that *every* content task reads this file. Sections, in reading order (the first two bind hardest):

- `## Legal constraints on go-to-market` — agreements that constrain **who may be sold to or marketed to**: territorial rights, rights of first refusal, exclusivity, OEM and white-label obligations, service-coverage limits, NDA'd relationships. Read first, because these make an otherwise excellent campaign unlawful rather than merely off-brand. A right of first refusal over one vertical makes "go direct" legally unavailable in the best market a company has, and a wiki that does not carry it will authorize that campaign cheerfully. In the test corpus this was the miss that would have caused real damage, and it landed in this file only by luck
- `## Approval workflow` — who approves what, on what turnaround, in what sequence, and where a draft waits. Include the rejection rate if it is known. Where a principal personally clears every catalog page and wordmark use on a 48-hour turn, or where first-pass rejection runs at 61%, the gate *is* the operating rhythm and asset lead times are set by it — that is canonical content, not reference depth. Drafting freezes (the `blocked` marker) live here or beside the asset. Operational detail fans out to `references/compliance-review-workflow.md`
- `## Banned claims` — claims we must not make (unsubstantiated superlatives, forbidden comparisons), each with why. Past roughly ten entries, fan the permission matrix out to `references/say-matrix.md` (speaker × medium × claim → allowed?)
- `## Regulated constraints` — industry rules that bind copy (financial promotion rules, health claims, anti-kickback and referral rules, data residency promises…). A statutory analysis requirement belongs here, not under a privacy heading
- `## Competitor conduct` — disparagement policy, naming policy, comparison rules
- `## Trademark and naming` — our marks, their marks, usage rules
- `## Embargoes and timing` — what cannot be discussed publicly yet (entries carry expiry dates)
- `## Data and privacy in outbound` — what customer data may never appear in marketing
- `## Contested` — always present in this file; when empty it carries `*(empty by decision — no contested guardrails, <date>)*` (SPEC §4.3). A contested guardrail is an urgent open question

**Boundaries:** approved claims → `business-core.md`. This file holds prohibitions, the contracts that create them, and the gate that enforces them — nothing positive about the offer, so its signal stays sharp. Ask the origin story of every hard prohibition: rules without their stories get relaxed by the next person in the job.

### `glossary.md`

**Tier:** doctrine · **Cadence:** per-run additions, interview ratification · **Horizon:** 180d

Canonical terminology. Mechanical, cheap to maintain, extremely high hit-rate. Sections:

- `## Product names and capitalization` — exact renderings, forbidden abbreviations
- `## Terms we use` — our word for each key concept (and the words we deliberately avoid for it)
- `## Terms customers use` — mapping customer vocabulary → our vocabulary (mined; overlaps `icp-personas.md#customer-language` by design: that file holds phrases-as-evidence, this file holds the ruling)
- `## Banned words` — with replacements

**Boundaries:** the smallest doctrine file; anything needing a paragraph of explanation belongs elsewhere with a glossary line linking to it.

### `growth.md`

**Tier:** doctrine · **Cadence:** interview / quarterly · **Horizon:** 90d

The growth strategy — where growth comes from and where effort goes. Sections:

- `## Model` — how the company grows (inbound, outbound, PLG, partner-led — the actual mix, not aspiration)
- `## Channel bets` — active channels ranked by investment, each with thesis and current verdict
- `## Target accounts` — how the target list is defined and where it lives (the list itself is CRM data → runbook pointer)
- `## Campaign frames` — recurring campaign types/themes and what each is for <!-- active in-flight campaign state may fan out to references/campaigns-active.md -->
- `## Contested`

**Boundaries:** pipeline *results* → `pipeline.md` (state). Sales-team account assignments → `account-ownership.md`. Persona definitions → `icp-personas.md`.

---

## State files

Facts about the world. Written freely by the maintainer with confidence labels per SPEC §8; contradictions go contested; A-class self-facts may supersede silently. Staleness horizons short.

### `competitors.md`

**Tier:** state · **Cadence:** per-run (external monitoring) · **Horizon:** 45d

Per-competitor summaries, battlecard-ready. One section per tracked competitor:

- `### <Competitor>` — who they are, motion, pricing snapshot, trajectory reading, recent moves (each claim tagged; A-class from their own site, O-class from news/reviews, `watchlist` until corroborated)
- Deep dives fan out: `references/battlecard-<competitor>.md` (strengths/weaknesses, landmines to plant, objection responses, win/loss evidence)
- `## Watchlist` — entities not yet tracked as full competitors
- `## Contested`

**Boundaries:** *our counter-positioning* against a competitor is a decision → those claims require H-class provenance even inside this file (doctrine-in-exile, SPEC §8.1: the builder sources it from interviews, and the maintainer may only annotate it from external evidence, never rewrite it). Win/loss *data* → S-class from CRM, lives here.

### `customers.md`

**Tier:** state · **Cadence:** weekly · **Horizon:** 60d

Who the customers are and which stories are usable. Sections:

- `## Customer base` — shape of the base (count, segments, notable logos), S-class from CRM
- `## Reference customers` — customers approved for public reference, with what they've approved (logo? quote? case study?) — approval facts are H-class (doctrine-in-exile, SPEC §8.1)
- `## Success stories` — one entry per usable story: customer, result (with numbers and their substantiation), where the full asset lives → `content-assets.md`
- `## Churn signals` <!-- tier: state, sensitive --> — patterns worth knowing when writing retention/expansion copy; individual figures that must not leave the org carry `!internal` (SPEC §4.2)
- `## Contested`

**Boundaries:** PII minimization per SPEC §15.5 — quotes included: a named individual at a named account is attributed by role unless the source carries a `consent:` record. Consent is declared once at the source (SPEC §10) and inherited by every claim citing it, never repeated per quote. How to *query* the customer list → `crm.md`.

### `events.md`

**Tier:** state · **Cadence:** per-run · **Horizon:** rolling — cadence-relative log window (SPEC §13: at least two of the org's channel cycles, minimum 90 days, declared as `log-window:`)

The running log of field events and market events. Sections:

- `## Upcoming` — dated list: conferences, webinars, launches we're attached to
- `## Log` — newest-first entries: `#### 2026-08-14 · <event>` with 2–3 lines of what happened and why marketing cares. *Append-open: consumer agents may add entries here directly (SPEC §9).*
- `## Roll-ups` — monthly summaries of aged-out entries; detail archives to `references/events-<year>.md`

Set `log-window:` from the org's real event cadence, not the default: a biennial trade-show calendar needs two years, because a 90-day window can never hold a show *and* its outcome. On a first build the window is usually already expired — the delivered sources are months old — so an empty `## Log` at delivery is normal and says so in one line, with the substance in the roll-ups and the year reference page.

**Boundaries:** product launches get one line here linking to `product-releases.md`, which owns the detail. Competitor events → `competitors.md`.

### `product-releases.md`

**Tier:** state · **Cadence:** per-run · **Horizon:** rolling — cadence-relative log window (SPEC §13; declared as `log-window:`)

What shipped and what's coming that marketing may use. The single biggest driver of wiki freshness. Sections:

- `## Current release themes` — the 2–3 narratives current releases support
- `## Shipped` — newest-first: feature, date, one-line marketing angle, link to official announcement (A/S-class from release notes, product channel)
- `## Roadmap — safe to share` — only entries a human has explicitly cleared for external use (H-class required, doctrine-in-exile per SPEC §8.1, each with clearance provenance and expiry)
- `## Contested`

**Boundaries:** roadmap items *not* cleared for external use do not appear at all — absence is the guardrail. Positioning implications of a release → proposed as open questions against `business-core.md`, not written directly.

### `partners.md`

**Tier:** state · **Cadence:** monthly · **Horizon:** 90d

The partner and ecosystem picture. Sections:

- `## Partners` — per partner: relationship type, integration, what co-marketing is allowed (allowed-use facts are H-class)
- `## Channel motion` — where the org sells *through* partners: the sequence end to end. Who quotes, who joins the technical review, who closes, who takes the purchase order, and what enablement the partner gets (certification roster, demo kit, co-branded collateral rules). Where the channel carries a large share of revenue this is the most-queried content in the file, and in the one deployment that needed it the sequence was described nowhere end-to-end while the certified-technician roster fragmented across three files — and the update landed in only one of them. Omit where no channel motion exists
- `## Ecosystem position` — marketplaces, platforms, and alliances that shape distribution
- `## Contested`

**Boundaries:** omit this file for orgs without a partner motion (record in `AGENTS.md`). Co-marketing *rules* and the PO rule are H-class doctrine-in-exile (SPEC §8.1), same pattern as battlecard counter-positioning. The partner *rep* as an audience → `icp-personas.md ## Channel personas`; his collateral mechanics → `channel-styles.md ## Channel collateral`; the channel *thesis* → `growth.md`. A distributor's own sales report is A-class about itself and O-class about the end customer (SPEC §7.7).

### `account-ownership.md`

**Tier:** state · **Cadence:** monthly · **Horizon:** 60d

How the sales team is resourced against accounts — what marketing agents need to route and personalize correctly. Sections:

- `## Coverage model` — SDR/BDR/AE structure, named-account vs. territory split
- `## Ownership map` — segment/territory → owner (S-class from CRM; keep at role/team granularity, fan out only if agents genuinely need per-account routing)
- `## Handoff rules` — MQL→SDR→AE flow as marketing needs to understand it
- `## Contested`

**Boundaries:** individual quota/performance data never enters the wiki. The account *list* → `crm.md` query patterns.

### `pipeline.md`

**Tier:** state (with a runbook section) · **Cadence:** weekly · **Horizon:** 30d

The pipeline picture agents may cite, and how to refresh it. Sections:

- `## How to source` <!-- tier: runbook --> — the exact queries/reports that produce pipeline truth (verified-by-execution stamps)
- `## Snapshot` — as-of-dated: coverage, stage distribution, notable movements (S-class, replaced wholesale each refresh — snapshot replacement is the one place recency legitimately wins, because the section is defined as "current as-of")
- `## Trends` — multi-period readings; `inferred` labels for agent pattern-reads until a human ratifies
- `## Contested`

**Boundaries:** deal-level detail stays in the CRM. Growth strategy interpretation → `growth.md` via open questions.

### `content-assets.md`

**Tier:** state · **Cadence:** weekly · **Horizon:** 60d

Inventory of existing marketing assets — the "do we already have a case study for X?" file. Sections:

- `## Case studies` — per entry: customer, industry, result claim, status (current/aging/deprecated), location
- `## Evergreen assets` — one-pagers, decks, whitepapers, webinar recordings: what each is for, status, location
- `## Lead magnets and campaign assets` — what exists, what it's attached to
- `## Gaps` — known holes (`inferred` entries welcome — "no case study covers fintech despite 40% of wins")
- `## Contested`

**Boundaries:** an asset's *substance* (the story, the numbers) → `customers.md`; this file is the catalog: status + location + fitness-for-use.

---

## Runbook files

How agents access and operate systems. Verified by execution, in the four states SPEC §8³ defines: `verified: <date>` from running the access pattern; `verified: <date> (against archive: <locator>)` where there is no live access but the query ran against an archived payload and reproduced the figure; `unverified: {since, reason, question}` for an entry never executed; `broken: {since, error}` for one that ran and failed, kept with its error and never deleted. `broken` is an entry state, never a claim-tag label.

**Zero-access deployments collapse these three files into one.** Where no system is agent-reachable — the state of all three test deployments — `metrics.md`, `crm.md`, and `gtm-tools.md` become a single `gtm-tools.md` answering four questions: what systems exist, who owns each, what marketing needs from each, and who to ask for access. Record the collapse in `AGENTS.md`. Three files of query patterns nobody can run exist because the taxonomy has three slots, not because there are three things to say.

**What must survive the merge is the data-hygiene layer** — which fields to trust, which rows to exclude, which columns are mislabelled. It is the highest-value content in the tier because it is what stops a wrong number reaching a public page. And "no CRM" never means "no system of record": a hand-maintained sheet plus a payments dashboard *is* the customer record, agents will quote from it, and it is the least trustworthy source in the wiki — which is exactly why that file earns its place.

### `metrics.md`

**Tier:** runbook · **Cadence:** monthly verification · **Horizon:** 60d

KPI definitions and how to compute them. Sections:

- `## KPI definitions` — per KPI: exact definition, owner, why it's defined this way (definitions are H-class doctrine-in-exile, SPEC §8.1; the *queries* are runbook)
- `## Where data lives` — system → what's authoritative there
- `## Query patterns` — per KPI: the query/report/tool call that produces it, last-verified stamp, known pitfalls
- `## Reporting conventions` — periods, attribution model, the charts leadership expects

**Boundaries:** current *values* belong in a dated snapshot, not in the query patterns above — a number written beside its definition rots invisibly. Put them in `pipeline.md`'s snapshot where that file exists; where it is omitted, add a `## Snapshot` section here (marked `<!-- tier: state -->`, as-of dated, replaced wholesale each refresh) rather than leaving the org's headline numbers homeless. A PLG deployment's downloads, stars, community size, and weekly-active counts are exactly the numbers agents ask for most, and they have nowhere else to live.

Also required: `## North star` — the one metric the company actually runs on, named by a human. It is a decision, so it needs H-class provenance, and it is frequently *not* any of the metrics on the dashboard. Without it a wiki full of KPI definitions lets agents optimize a vanity metric in good faith.

### `crm.md`

**Tier:** runbook · **Cadence:** monthly verification · **Horizon:** 60d

Where and how the CRM is maintained, and how agents access it. Sections:

- `## System of record` — which CRM, who administers it, data-hygiene reality (what fields to trust)
- `## Access` — how agents connect (MCP tool names / API / export path), credential *locations* (env-var names, never values)
- `## Core objects and fields` — the objects and fields marketing agents actually use, with gotchas
- `## Standard queries` — customer list, pipeline report, target accounts, win/loss pulls — each with verified stamps

**Boundaries:** what the pipeline currently *shows* → `pipeline.md`. Who owns which accounts → `account-ownership.md`.

### `gtm-tools.md`

**Tier:** runbook · **Cadence:** monthly verification · **Horizon:** 90d

Inventory of the GTM stack. Sections:

- `## Stack` — per tool: what it's for, who owns it, how agents access it (or "no agent access"), verified stamp
- `## Data flows` — which tool feeds which (the map that explains why numbers disagree)
- `## Broken / deprecated` — tools going away, access that no longer works

**Boundaries:** deep per-tool usage guides fan out to `references/tool-<name>.md` only when an agent workflow genuinely depends on one.

---

## System files

Defined normatively in SPEC §12; taxonomy notes only:

- **`open-questions.md`** — the interview backlog, batched by `owed-by:`. Active / Partially answered / Answered / Delegated / Stale, ordered by priority rather than id (SPEC §12.1). Every contested entry everywhere links here; the wiki's own housekeeping never does.
- **`changelog.md`** — append-only run log, newest first, no-ops included. The digest and the eval both read from it.
- **`sources.md`** — the source manifest: access declarations, cursors, per-author provenance classes, `consent:`, `status:`, and delivery routing (SPEC §10). This file *is* the integration layer; there is no connector code in a deployment.
- **`intake/observations.md`**, **`intake/inbox/`** — consumer append buffer and human drop folder (SPEC §9).
- **`references/`** — fan-out pages. Every page front-matters `type: reference` and links back to its canonical parent. Named pages below.
- **`.archive/`** — raw pulls per run (SPEC §11). Not markdown, not part of the readable wiki, required for audits.
- **`outbox/`** — artifacts sent to humans, dated, exempt from orphan and front-matter checks (SPEC §3).

### `references/` naming

A deployment may add pages, but where one of these exists it uses this name. What failed in testing was never the fan-out mechanism — it absorbed every homeless concept in all three runs — it was that nothing *named* the destination, so each page was invented once and its placement filed as a question to a stakeholder who correctly refused to answer it. These names are the default home (SPEC §3 rung 3). Promote one to a root file only when consumers need it as a starting point and the parent would hide it — the community-as-primary-GTM case in SPEC §3 is that exception, not a second naming convention.

| Page | Holds | Parent |
|---|---|---|
| `battlecard-<competitor>.md` | strengths, weaknesses, landmines, objection responses, win/loss evidence | `competitors.md` |
| `persona-<name>.md` | one persona in depth — buyer or channel rep | `icp-personas.md` (channel personas: `partners.md`) |
| `events-<year>.md` | aged-out log detail | `events.md` |
| `pricing.md` | tier, floor, and discount detail too long for doctrine | `business-core.md` |
| `tool-<name>.md` | per-tool usage guide where a workflow depends on one | `gtm-tools.md` |
| `campaigns-active.md` | in-flight campaign state | `growth.md` |
| `community.md` | **Default depth** for a company-hosted community that is a channel, not the GTM. **Promote to a root file** (SPEC §3) when the community *is* the motion — maintainer comps, contributor credit, issue triage as marketing, the support answer that is the funnel. Discord *mechanics* (length, cadence, reply-once) stay in `channel-styles.md ## Community` either way; do not keep the motion in both places | `channel-styles.md ## Community` while this stays a reference page; after promotion, the root file is the motion's home |
| `say-matrix.md` | speaker × medium × claim → allowed? Required once `## Banned claims` passes ~10 entries; for a regulated seller it is the most-queried table there is | `compliance-guardrails.md` |
| `owned-audiences.md` | lists the org owns — catalog mailing list, newsletter, user group — with size, consent basis, and what may be sent. An audience is not a channel convention, and a 14,000-name engineer list buried in a print-mechanics section is the company's most valuable marketing asset filed as a formatting note | `growth.md` |
| `buying-committee.md` | who votes, in what order, on what calendar — the reason a cycle runs 287 days. Neither persona (who) nor pipeline (results) | `icp-personas.md` |
| `compliance-review-workflow.md` | the review process in operational detail: queues, turnarounds, rejection reasons | `compliance-guardrails.md ## Approval workflow` |
| `refusals.md` | what the org refuses to do and why — no discounts, no booths, no paid, no ghostwriting. Where refusals *are* the strategy they should sit in one place, so that a gap in the list is visible; scattered across five files, two of them were missed entirely | `business-core.md` |

---

## Coverage map — "where does X go?"

| You learned… | It goes in… |
|---|---|
| The CMO redefined the ICP in Slack | `icp-personas.md` (H-class — write it), changelog |
| Competitor raised prices (their site) | `competitors.md` (A-class, may supersede silently) |
| A reviewer says our onboarding is slow | `competitors.md`/`customers.md` as `watchlist`; open question if it recurs |
| Gong calls keep surfacing a new objection | `icp-personas.md` objections as `inferred` + open question to ratify |
| A query in `metrics.md` now 404s | mark the entry `broken: {since, error}` in `metrics.md` (an entry state, never a claim label — SPEC §8³), digest escalation |
| Sales restructured territories | `account-ownership.md` (S-class from CRM once visible there) |
| We shipped a feature | `product-releases.md` + one line in `events.md` |
| Exec said "stop calling it a dashboard" | `glossary.md` banned words (H-class), `voice.md` if it reflects posture |
| An agent drafting a post found a stat it couldn't verify | `intake/observations.md` (it may not write canon) |
| New embargo on the funding announcement | `compliance-guardrails.md` embargoes (H-class, with expiry) |
| **"We ran a trade show"** | **three files.** Mechanics (booth copy, demo rig, who staffs, what collateral travels) → `channel-styles.md ## Field and events`; what happened → `events.md ## Log`; whether it was worth repeating → `growth.md ## Channel bets`. Sending all three to one file is the most common filing error in an event-led business |
| A distributor rep needs different collateral than the end buyer | the rep as an audience → `icp-personas.md ## Channel personas`; the sequence he sits in → `partners.md ## Channel motion`; what he may alter → `channel-styles.md ## Channel collateral` |
| We're launching a new service line | `business-core.md ## Product` gains a `### <line>` subsection (buyer, price, motion); its sequencing and the bet behind it → `growth.md`; clearance to mention it externally → `product-releases.md ## Roadmap — safe to share` (H-class, with expiry) |
| Marketing is forbidden from producing something until a condition clears | the `blocked` marker beside the asset in `content-assets.md`, or in `compliance-guardrails.md ## Approval workflow` — never prose emphasis alone |
| The hosted community **is** the GTM (comps, credit, triage-as-funnel) | root `community.md` (doctrine), SPEC §3 — `references/community.md` fails rung 3 because it hides a starting point. Discord length/cadence/reply-once stay in `channel-styles.md ## Community` |
| A concept none of the 18 can hold as a consumer starting point | SPEC §3 ladder: reinterpret, then a section, then `references/`. Rung 3 fails when the named reference page would hide a starting point, not when the filename exists in the naming table. A new root file only if all three fail, with the complete write. Never an interview question about the filename |
