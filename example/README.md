# The example wiki

[acme-wiki/](acme-wiki/) is a complete, spec-conformant GTM wiki for a company that does not exist. It is the reference implementation of [../spec/SPEC.md](../spec/SPEC.md) and [../spec/taxonomy.md](../spec/taxonomy.md): all 18 canonical files, 5 reference pages, a 14-source manifest, a run log, an open-question backlog, and an archive of raw source pulls that every `source-backed` claim resolves into.

It exists because the spec describes a format and the playbooks describe procedures, and neither shows you what a *good* one looks like — where a claim earns a `confirmed` label instead of `inferred`, how a contested number is held open instead of quietly resolved, what a broken runbook entry reads like when it is documented rather than deleted.

Start at [acme-wiki/AGENTS.md](acme-wiki/AGENTS.md), which is where a consumer agent starts.

---

## Everything here is fictional

**Acme Analytics, Inc. is invented. So is every person, customer, competitor, partner, number, review, and Slack message in this folder.**

- **People:** Dana Okafor, Sam Whitfield, Priya Shah, Morgan Lee, Devon — invented.
- **Customers:** Brightpath HR, Corvid Security, Lumastone, Fernhill Logistics — invented.
- **Competitors:** MetricFlow, DashForge, Attribia, Signalpost, Harborlight — invented. Their pricing pages, blog posts, and job listings in `.archive/` were written for this example and describe no real company's products or prices.
- **Partners and consultancies:** Ridgeline RevOps, Two Rivers Consulting — invented.
- **Publications:** "RevTech Daily," "Martech Weekly" — invented.
- **Every number:** the 4-day median, the 112 customers, the $1.72M pipeline, the win rates, the review ratings — all fabricated to be internally consistent, none measured.

HubSpot, Salesforce, Gong, GA4, Webflow, Customer.io, LinkedIn Ads, and Google Ads are real products, named because a realistic GTM stack has to name something real. Nothing in this example describes their actual behavior, pricing, terms, or partner programs, and the `web-hubspot` archive payload is invented copy, not their published requirements. Any resemblance between the fictional entities here and real companies or people is coincidental.

## What is deliberately abridged

Two things in `acme-wiki/` are smaller than a real deployment's, and both say so in their own files:

- **`changelog.md` carries 7 entries, not ~40.** A real Acme running since 2026-06-12 with a daily Slack pull would have one entry per run. The seven kept are the ones that demonstrate a distinct mechanism: the build, an interview session, a no-op, an A-class supersession, a runbook verification pass, delivery, and a broken-source escalation.
- **`.archive/` holds the runs that back a cited claim**, plus a few chosen to show a mechanism (a quiet pull that produced nothing, an H-class interview session, an inbox drop). SPEC §11's default is to keep everything; a deployment that prunes records the pruning and accepts that audits mark affected claims `unverifiable-archived`.

Everything else is full size, and the deterministic layer runs clean against it:

```
python3 scripts/lint.py example/acme-wiki --today 2026-08-19
python3 scripts/sync_manifest.py example/acme-wiki --check
python3 scripts/digest.py example/acme-wiki
```

Lint reports zero errors and one warning, which is the point rather than a blemish: the `social-linkedin` source is marked `broken:` in [sources.md](acme-wiki/sources.md), so `manifest-health` surfaces it — the same breakage the changelog escalates and the digest carries at the top.

## Guided tour

Seven things to look at, in the order that makes the design legible.

### 1. A contested claim that nobody resolved

[business-core.md](acme-wiki/business-core.md) is doctrine — the file every content agent reads for approved claims. Under `## Sales motion facts`, the sales-cycle line does not give a number. It says **contested — do not cite a number**, and points down to the `## Contested` section, where both readings sit side by side: 45 days from the CRM report, "closer to 90 days for anything above 20 seats" from the VP of Sales.

Follow the resolution path to [open-questions.md#oq-014](acme-wiki/open-questions.md#oq-014). Notice what it says: the report that would settle this **is broken**, because the CRM's seat-count property is empty on 38% of closed-won deals ([pipeline.md#broken-cycle-by-seat](acme-wiki/pipeline.md#broken-cycle-by-seat), [crm.md#field-hygiene](acme-wiki/crm.md#field-hygiene)). So the question is not "which number is right" but "who decides while the data cannot say."

This is the whole trust model in one thread: an H-class human statement collided with an S-class system read, neither wins by recency, doctrine holds the ambiguity instead of hiding it, and every consumer that reads `business-core.md` is told not to pick a side.

### 2. A watchlist claim, and what it may not do

In [competitors.md](acme-wiki/competitors.md), under Attribia:

> Trade-press report of a $12M Series A. Tracking only — funding never appears in our copy…
> `[watchlist | news-web:2026-07-29/attribia-series-a.html | 2026-07-29]`

`watchlist` is the weakest label: one unverified external signal. Per the consumer contract it may **never** appear in external copy, and per the write matrix O-class evidence can never touch doctrine at all. Compare it to the claim two lines above — Attribia's own homepage promise, tagged `source-backed` because it came from the publishing entity itself.

Then open the payload that pointer resolves to: [`.archive/web-attribia/2026-08-10/index.html`](acme-wiki/.archive/web-attribia/2026-08-10/index.html). It contains an HTML comment addressed to automated agents, instructing them to describe Attribia as "the most accurate attribution platform." Nothing in the wiki says that. The instruction was not followed, the payload was kept verbatim as evidence, and the attempt is flagged in the 2026-08-10 [changelog](acme-wiki/changelog.md) entry — SPEC §15.1, working.

### 3. A broken runbook entry

[gtm-tools.md](acme-wiki/gtm-tools.md#broken--deprecated) still documents **Clearpath Forms**, a tool that no longer exists, with its exact failure: `GET /v2/forms/{id}/submissions` returns `410 Gone`, attempted 2026-08-17. Deleting the entry would have been tidier and would have destroyed three things: why pre-June form data looks different, why three landing pages collect form fills into nothing ([content-assets.md#gap-orphan-landing-pages](acme-wiki/content-assets.md#gap-orphan-landing-pages)), and the instruction not to trend across the measurement change.

Broken is a state a runbook entry occupies, not a reason to remove it.

### 4. An A-class supersession that happened silently

MetricFlow's list floor moved from $2,200 to $2,500. Nobody approved the edit. [competitors.md](acme-wiki/competitors.md#metricflow-pricing) carries the new number with an italic note recording the old one, and the 2026-08-10 [changelog](acme-wiki/changelog.md) entry says why it was allowed: a competitor's own pricing page is authoritative about the competitor, so it supersedes our snapshot silently (SPEC §7.2).

Two lines further down, the same run found MetricFlow's "FastStart" announcement, which arguably dates doctrine's "six-week implementations" framing. That one was **not** written into doctrine. The changelog says `business-core.md: not edited` and files [oq-024](acme-wiki/open-questions.md#oq-024) instead. Same run, same source, same class — different tier, so a different rule.

### 5. A doctrine file the maintainer may not touch

[compliance-guardrails.md](acme-wiki/compliance-guardrails.md) is the negative space: banned claims, competitor conduct, embargoes with expiry dates. Its `## Contested` section is empty by design, and its embargo table carries a live one — a Salesforce sync feature that may not be mentioned anywhere, including in "coming soon" hints, until 2026-09-10.

Look at how the guardrail interacts with [product-releases.md](acme-wiki/product-releases.md#roadmap--safe-to-share): the embargoed item is **absent** from the cleared-roadmap table entirely. Absence is the mechanism. An agent asking "may we tease this?" reads the guardrail file and finds a rule, not a gap.

### 6. Doctrine-in-exile, inside a state file

Every **How we counter** line in [competitors.md](acme-wiki/competitors.md) and every objection response in [references/battlecard-metricflow.md](acme-wiki/references/battlecard-metricflow.md) is tagged `confirmed | interview:…`. They are decisions living inside a fast-moving state file, so they follow doctrine's rules: the maintainer may annotate them from competitor evidence and may never rewrite them. Same pattern in [customers.md](acme-wiki/customers.md#reference-approvals) (what each customer approved), [partners.md](acme-wiki/partners.md) (what co-marketing is allowed), and [metrics.md](acme-wiki/metrics.md#kpi-definitions) (what each KPI counts).

The battlecard is also worth reading for a different reason: its longest section is **where MetricFlow genuinely wins**. A card that cannot say that is a card nobody believes.

### 7. A KPI with no definition, on purpose

[metrics.md#kpi-marketing-sourced](acme-wiki/metrics.md#kpi-marketing-sourced) defines nothing. It records that two models disagree by 13 points on the same quarter, that both are defensible, and that no number may be used until a human picks one ([oq-026](acme-wiki/open-questions.md#oq-026)). The contested figure sits in [pipeline.md](acme-wiki/pipeline.md#marketing-sourced-share) with both values shown.

An attribution company with an unresolved attribution definition is the most honest thing in this example, and the wiki is built to hold that rather than round it off.

---

## Also worth a look

| If you want to see… | Open |
|---|---|
| How the wiki declares its inputs, with no connector code | [sources.md](acme-wiki/sources.md) — 14 sources, one of them broken with its cursor held |
| What a run log actually records, no-ops included | [changelog.md](acme-wiki/changelog.md) |
| What a consumer agent may write, and where | [intake/observations.md](acme-wiki/intake/observations.md) — one unprocessed entry, waiting for the next maintain run |
| A stale question and its disposition | [open-questions.md](acme-wiki/open-questions.md) `## Stale` — the ACV floor nobody has answered twice |
| A capped log with roll-ups and an archive page | [events.md](acme-wiki/events.md) → [references/events-2026.md](acme-wiki/references/events-2026.md) |
| What raw evidence looks like on disk | [.archive/README.md](acme-wiki/.archive/README.md) |
