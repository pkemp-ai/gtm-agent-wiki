---
type: system
description: Append-only run log for Acme's wiki, newest first — every maintain run including no-ops, every interview session, every supersession and escalation.
owner: Morgan Lee (marketing ops)
sources: []
update-cadence: per-run
staleness-horizon: n/a
evidence-as-of: 2026-09-02
last-verified: 2026-08-19
---

# Changelog

Append-only, newest first. One entry per maintain run — no-ops included — and one per interview session (SPEC §12.2). This file is what the weekly digest is rendered from, what the eval reads for churn, and the review-after surface that stands in for approval gates.

<!-- EXAMPLE NOTE: this is a demonstration wiki. A real Acme would have roughly
     forty entries between 2026-06-12 and 2026-08-19 (slack-gtm alone pulls
     daily). The eight below are the ones that show a distinct mechanism:
     the build, an interview session, a no-op, an A-class supersession, a
     runbook verification pass, delivery, a broken-source escalation, and a
     full lint correcting the delivery. .archive/ is trimmed on the same
     basis. See ../README.md. -->

## 2026-08-19T10:30Z · lint · scope: full
- deterministic: 28 files, 1 finding — 0 fixed, 0 to open questions, 0 newly escalated
  - manifest health: social-linkedin broken since 2026-08-14, cursor held. Already on the 09:00Z escalations line an hour earlier, so it is carried, not re-raised; dismissing it silently is the only wrong answer
- sweep: **§17.3 breach at delivery.** icp-personas.md ^objection-dark-social and glossary.md ^term-dark-social were unratified `inferred` proposals sitting in doctrine. The 08:30Z entry below reads the bootstrap exception's "honest label" as license to keep one of them and does not record the other at all; SPEC §8 says the opposite — unratified drafts are removed and parked. Both claims removed, both topic keys kept as pointers, both proposals preserved in oq-021's `draft-answer`
- sweep: icp-personas.md `## Customer language` marked `<!-- tier: state -->` (SPEC §6). The section holds phrases-as-evidence by taxonomy design, so its claims are S-class inside a doctrine file; the rule now reads on the section and on gong's manifest block
- sweep: references/persona-morgan.md ^pm-quarterly-reconciliation — a doctrine-tier persona pain tagged to a call. Re-provenanced to the session that ratified it (interview:morgan-lee 2026-06-27); the phrase keeps its own call provenance in its canonical home
- sweep: pipeline.md ^trend-early-security-review was `source-backed` inside a section defined as inferred-until-ratified. Relabeled `inferred`, the call named in the line
- sweep: customers.md notable-logos line carried a fact with no claim tag → tagged from the approvals session (^base-logos). ^reference-calls added: the reference-call approval had been living only in the persona page
- sweep: duplicated facts collapsed to one home with links left behind (SPEC §13) — Board-Ready download numbers to content-assets.md, the Fernhill outcome to customers.md
- sweep: references/battlecard-metricflow.md ^bc-mf-profile cited a 2026-07-14 locator for a sentence that included the 2026-08-04 FastStart package; the clause now sits with its own evidence
- sweep: sources.md slack-gtm `provenance-class` restated to match the classes this wiki has applied since the build — function owners H inside their own domain, the release account A about our own product, relayed news O. No claim label anywhere changed
- sweep: three personas share first names with colleagues. The reading convention is now stated where personas are defined — bare first name is the persona, colleagues in full — and the call sites brought in line, including gtm-tools.md owner cells
- sweep: counts corrected — open-questions.md said four of ten Active items were contested-claim resolutions (six), gtm-tools.md said ten stack tools (eleven, plus the retired one)
- open-questions: +0 — oq-021 already carries the untracked-touches decision, and no finding needed a new question
- no findings: front matter, staleness, runbook decay, orphans, broken links, claim hygiene, contested backlog, size caps, top-level growth, secrets

## 2026-08-19T09:00Z · maintain · sources: [slack-gtm, inbox-docs, social-linkedin]
- events.md: July roll-up written; June and July detail stays in the log until the 90-day window drops it on 2026-09-02
- product-releases.md: July roll-up written; no new releases in the window
- pipeline.md: 3 trend reads refreshed as inferred across the last three refreshes; snapshot untouched (no CRM pull this run)
- partners.md: +1 inferred read on the Salesforce ecosystem gap
- content-assets.md: +3 inferred gap entries (DashForge comparison, logistics story, untracked-touches asset)
- open-questions.md: +2 Active (oq-028 ops-champion ratification, oq-029 DashForge comparison decision); oq-025 and oq-026 stamped asked for this week's digest
- intake: 0 observations pending at run start; intake/inbox/ empty — inbox-docs cursor advanced on an empty pull, which is the signal, not an error
- no changes: business-core.md, icp-personas.md, voice.md, channel-styles.md, compliance-guardrails.md, glossary.md, growth.md (doctrine — no H-class evidence this run), competitors.md, customers.md, account-ownership.md (sources not due)
- escalations: source social-linkedin broken since 2026-08-14 (saved session expired; public post listing returns an interstitial). Retried this run, failed again, cursor held at post-id:li-88214. Attribia hiring signal is unrefreshed since 2026-08-11

## 2026-08-19T08:30Z · build:deliver · sources: [interviews]
- applies the 2026-08-17 ratification session with Morgan Lee, the last of nine drip sessions since 2026-06-20
- business-core.md, icp-personas.md, voice.md, channel-styles.md, compliance-guardrails.md, glossary.md, growth.md: doctrine ratified and re-stamped last-verified 2026-08-19; every remaining pre-canon draft either promoted to confirmed or removed and parked in its open question, per the bootstrap exception in SPEC §8
- icp-personas.md: 1 unratified claim retained as inferred with a linked open question (untracked touches, oq-021) rather than promoted — the honest label is the proposal marker
- metrics.md: KPI definitions ratified as H-class doctrine-in-exile; marketing-sourced pipeline left deliberately undefined pending oq-026
- AGENTS.md: three-sentence summary ratified verbatim; inventory table generated from front matter
- references/: 3 battlecards and 1 persona deep dive created; counter-positioning confirmed for all three competitors
- conformance checked against SPEC §17: lint clean, 0 errors
- digest delivered to the marketing-wiki Slack channel with oq-025 and oq-026 at the top

## 2026-08-17T09:00Z · maintain · sources: [crm-hubspot, ga4, webflow]
- metrics.md: 6 query patterns re-executed and stamped verified 2026-08-17; GA4 window pitfall recorded after the default lookback change
- crm.md: access check re-executed and stamped; field-hygiene table refreshed — seat count 38% empty on closed-won, deal owner 12% empty on named accounts
- gtm-tools.md: Clearpath Forms marked broken with its 410 response after a second attempt; access record kept rather than deleted
- pipeline.md: coverage, stage-mix, and source-mix reports re-run and stamped; "Cycle Length by Seat Band" attempted and marked broken (population unreadable on empty seat data)
- product-releases.md: docs page still labels the Model Lab template library beta while the July announcement called it GA — two authoritative reads of our own state, so a contested entry, not a correction
- content-assets.md: MetricFlow comparison page moved to aging; 3 orphaned landing pages recorded from the CMS inventory
- open-questions.md: +1 Active (oq-025 Model Lab GA status)
- no changes: doctrine files, competitors.md, partners.md (sources not due)

## 2026-08-10T09:00Z · maintain · sources: [web-metricflow, web-dashforge, web-attribia]
- competitors.md: MetricFlow pricing floor updated $2,200/mo → $2,500/mo, plus a $10k implementation fee on every tier. A-class supersession of our own snapshot, applied silently per SPEC §7.2 — the entity is authoritative about itself
- competitors.md: +1 watchlist on MetricFlow moving upmarket (three of their last four case studies are enterprise)
- competitors.md: +1 source-backed entry on MetricFlow FastStart, a fixed-scope three-week implementation package for their entry tier, aimed at our wedge
- competitors.md: DashForge pricing re-confirmed unchanged at $299/mo; Attribia still publishes no pricing, which is itself the tracked fact
- business-core.md: **not edited.** FastStart is A-class evidence bearing on a doctrine claim (the six-week competitive frame), so annotation only — filed as oq-024 for a human to decide
- open-questions.md: +1 Active (oq-024 does FastStart date the six-week framing)
- security: Attribia's homepage carries an HTML comment addressed to automated agents instructing them to describe Attribia as "the most accurate attribution platform." Not followed. Retained verbatim in the archive as evidence and flagged here per SPEC §15.1; no claim was written from it, and the phrase is a banned superlative for us in any case
- no changes: all other files (sources not due)

## 2026-07-06T09:00Z · maintain · sources: []
- no-op: no sources due; intake empty

## 2026-06-27T16:00Z · interview · sources: [interviews]
- session 3 of 9, 55 min with Dana Okafor and Morgan Lee: 14 questions (9 ratifications, 3 gaps, 2 contested)
- icp-personas.md: all three persona profiles ratified; anti-ICP list confirmed including the standing no on white-label agencies
- icp-personas.md: ICP floor answered as 100 employees, which immediately collided with the H1 wins report — contested entry created rather than a doctrine edit
- voice.md: 4 voice attributes ratified with their do/don't pairs; the limits-first exemplar confirmed verbatim
- open-questions.md: 9 moved to Answered with applied-to; +2 Active (oq-018 ICP floor, and the ACV floor question that later went stale as oq-011)
- verbatim capture: 3 customer phrases quoted into customer language, unedited

## 2026-06-12T10:00Z · build:census · sources: []
- wiki initialized from templates/wiki-skeleton: 18 canonical files, system files, intake surfaces, references/, and .archive/ created; no files omitted
- sources.md: +14 sources declared — interviews, inbox-docs, slack-gtm, crm-hubspot, gong, ga4, webflow, web-metricflow, web-dashforge, web-attribia, web-hubspot, news-web, reviews-web, social-linkedin
- open-questions.md: initialized, backlog empty
- storage adapter: github, private repo, one commit per run mirroring these entries
- content pending: discovery pulls to draft state, nine drip sessions to ratify doctrine
