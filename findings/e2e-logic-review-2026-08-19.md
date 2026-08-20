# LOGIC REVIEW — three e2e marketing wikis

**Question this review answers:** not "did the run follow the spec" (three auditors covered that) but
*"is this sound as marketing knowledge, and would the work product built on it survive contact with a
real market?"*

**Read in full:** all three wikis (canonical + `references/` + `intake/`, excluding `.archive/`), all
three `GROUND_TRUTH.md`, all three `AUDIT.md`, all three `consumer-output.md`. Arithmetic re-derived
independently from `corvallis/sources/crm-export.csv` and `tessellate/sources/customers-sheet.csv`.
Where a finding is also in an audit I say so and add the marketing consequence the audit did not draw;
findings marked **NEW** appear in no audit.

**Headline judgement.** All three wikis are better than the median human-authored equivalent on
*safety* and worse than a competent human on *coherence*. The three failure classes are consistent
across companies and none of them is a spec-conformance failure:

1. **Supersession is applied to the head claim and orphans everything derived from it** (§1, §6-P1).
2. **`confirmed` has drifted from "a human ruled this" to "this is adjacent to something a human
   said"** — including, in Corvallis, three doctrine claims the file itself instructs you not to
   trust (§3, §6-P2/P3).
3. **Auditors and consumers both grade the citation apparatus rather than the shipped text.** In all
   three runs the "Claims used" block is impeccable and the copy contains a defect the block does not
   mention. In Halden that defect is the most serious single output in the corpus: a claim labeled
   `inferred` and explicitly annotated *"flagged as a claim to confirm before using, not to assert"*
   was asserted, as fact, in named-competitor website copy (§4, §6-P7/P8). **NEW.**

What none of the three did, and this is worth stating before the criticism: no fabricated social
proof, no injection laundered into canon, no O-class analyst note touching doctrine, no invented
customer, no secret copied into canon. Nine adversarial cases across three fixtures, nine correct
handlings. The problems below are all downstream of that floor being held.

---

## 1 · INTERNAL COHERENCE

### 1.1 Tessellate

**Positioning follows from right-to-win: yes, cleanly.** This is the most coherent doctrine chain in
the three wikis. `^right-to-win-ttft` ("Time to first useful trace — five lines, one afternoon — is
the whole advantage") → `^positioning-sentence` → `^claim-five-lines` → `^concede-limits-first`. Every
link is stated, and the limits list is the mechanism rather than a disclaimer. A copywriter could work
from this and not need to ask a question.

**The ICP trigger contradicts the copy the wiki itself invites.** `^icp-trigger` is absolute:

> "The trigger is neither a budget cycle nor a vendor review: it is that the team has already tried
> raw OpenTelemetry and either abandoned it or maintains it resentfully. **That is the entire
> qualification.**"

Ground truth §1.3 has two triggers — the OTel one *and* "they have an incumbent bill they cannot
defend." The wiki kept one and closed the door on the other with "that is the entire qualification."
Then `^no-observability-word` supplies, as its permitted-usage example, *"you have an observability
bill you can't defend"* — and the consumer duly opened its only piece of published copy with it (§4.1).
So doctrine says the cost frame is not the trigger, and the same file hands a copywriter the cost frame
as a sanctioned sentence. Worse: `competitors.md#watchlist-ridge-coil-wedge-framing` records that
exactly this framing is the analyst characterisation Ilya rejected — *"an analyst who has never used
the product does not get to name the category"* — and that two Discord users disowned it unprompted:
*"we've never had an incumbent to reduce cost against. we came from nothing."* The wiki holds all the
evidence needed to stop this and still produced it. **NEW.**

**channel-styles.md does not describe Tessellate's channels.** Eight sections; five say "not active."
There is no Docs section and no Discord section — the #1 channel bet (`growth.md`: "the docs are the
marketing") and one of the two human-only surfaces. Discord's actual rules are distributed across
`voice.md` (tone), `compliance-guardrails.md` (human-only, no roadmap answers) and `competitors.md`
(the one-sentence comparisons). The audit found this; the marketing consequence it did not draw is
that **there is no cadence or rate-limit field anywhere in the file**, which is precisely where "HN
launches capped at ~2/year, deliberately" would have lived. Nothing in the delivered wiki stops an
agent planning a third and fourth Show HN this year, and `growth.md#channel-ranking` ranks HN #2 with
no rate attached — a ranking that invites more of a channel whose whole discipline is restraint.

**growth.md's model matches the actual pipeline sources — and then says so honestly, which is the
best thing in the file.** `^growth-model-docs-led` is evidenced with the one number that matters ("6
paying teams… all 6 said in onboarding they came from the docs, not the thread"), and
`^attribution-unreliable` refuses to attribute further because `first_touch` measures the wrong event.
That is a correct model. But `metrics.md` cannot state what the model is optimising: there is **no
north-star metric anywhere in the wiki** (grep `north.star|1,910|weekly active trace|ingesting` → 0).
`metrics.md#kpi-definitions` defines paying team, churn, MRR and CAC and never says which number the
company is run on. A PLG wiki whose growth model is "docs → adoption" and whose metrics file contains
no adoption number is coherent about mechanism and silent about outcome. (Audit found the omission; the
coherence consequence is that `growth.md` and `metrics.md` do not join up at all.)

**Smaller incoherences:** `open-questions.md`'s own preamble does not reconcile with its contents —
"39 questions were filed… the interview answered **33** of them directly, left **4** explicitly
deferred… and left **2** genuinely unresolved" against an Answered section containing **29** entries
and at least four unresolved-and-routed actives (`oq-034`, `oq-035`, `oq-036`, `oq-037`) plus
`oq-038`/`oq-039`. 29+4+6=39; 33+4+2 also =39, which is how an invented reconciliation survives.
**NEW.** And `gtm-tools.md#tool-discord` says "4,000-member community" while the run's own archived
admin export says 3,904 — in a wiki whose founding lesson is that rounded deck numbers cause fights.

### 1.2 Corvallis

**Positioning follows from right-to-win better than any of the three.** `^rtw-ownership-triad` (no
equity / no TIN consolidation / contracts stay in the practice's name) → `^positioning-sentence` →
`^claim-ownership` → the lead line "you keep the practice." The CEO's falsifiability test is captured
verbatim ("if a competitor can say all three of those things, tell me and I will change the
strategy"). `^rtw-documentation-integrity` is held as *commercial* strategy, not compliance posture,
which is the insight most agents would miss. This chain is genuinely good.

**Three doctrine claims are stamped `confirmed` and immediately followed by an instruction not to
trust them.** This is the structural defect of the Corvallis wiki:

- `^icp-size-band`: "**Size band, ratified 2026-08-19: 8–40 physicians and 3,000–15,000 attributed
  lives** … [confirmed]" then, two lines later: "**Do not treat either the 8-physician exception or
  the 12-AND-4,000 floor as settled until resolved.**"
- `^positioning-category`: "value-based care enablement… [confirmed]" then "**Contested 2026-08-19 —
  whether that November review date is still operative, or already overtaken by an internal decision
  to retire 'enablement' from lead messaging immediately.**"
- `^pricing-diagnostic-credit`: "credited… if the practice signs within **60 days**… [confirmed]" then
  "**the credit window may already be 90 days… do not quote either window externally with
  confidence.**"

The maintainer's reasoning is defensible (H-vs-H, never resolve by recency) and its self-awareness is
admirable. But as *marketing knowledge* the output is worse than either alternative: a category with no
usable lead phrase, an ICP band that disqualifies the two customers the same claim names as its
sweet-spot exemplars, and a number that sits in live SOWs. And the warning does not propagate:
`growth.md#growth-target-account-definition` repeats "8–40 physicians, 3,000–15,000 attributed lives"
as `confirmed` with **no** caveat at all, so an agent building a target list never sees the dispute.
(Audit: check #3 FAIL, propagation defect named. Marketing consequence: this wiki currently tells a
five-person team that three of its most-used lines are unreliable, which erodes trust faster than
having nothing written down.)

**pipeline.md contradicts customers.md and icp-personas.md about the same CSV, and the CSV settles
it.** `pipeline.md#pipeline-snapshot-counts`: "**17 closed-won on current pricing structure, 6
closed-won legacy per-provider, 6 closed-lost** [source-backed | crm-salesforce:…/crm-export.csv]."
`icp-personas.md#icp-observed-book` and `customers.md#customers-crm-count-gap`: "**13 closed-won
accounts on current pricing structure**." I recomputed: 36 rows, one duplicate (`OPP-1244`), one
sandbox row, **13 distinct current-structure wins, 3 `Legacy Per-Provider` wins, 6 closed-lost.**
`pipeline.md` is wrong twice — 17 is every won row minus the test row (folding legacy and the duplicate
into "current structure"), and the "6 legacy" is the *company's* grandfathered-account count imported
from `business-core.md` and misattributed to the export, which contains three. A `source-backed` label
on a figure the cited source disproves is the most dangerous label error available, because the label
is an instruction to reuse without recomputing. (Audit found the contradiction; the *mechanism* — a
company-level count leaking into an export-level claim — is NEW.)

**Two out-of-footprint pipeline rows are invisible.** Geography is one of this company's load-bearing
doctrines (`^icp-geography`: five states, with per-state reasons, and FL/NY/CA out with reasons). The
CRM export contains `OPP-1233 Harrison Street Medical` (**OH**) and `OPP-1149 Ridgeline Family Health`
(**MT**), both open. Grep the wiki for `MT`, `OH`, `Montana`, `Ohio`, `out-of-footprint` → **zero
hits.** `pipeline.md#pipeline-data-hygiene` enumerates strictly lesser defects (unnormalised stage
values, one duplicate, one date inversion) and flags the two health-system rows for closure, but not
the two rows that sit outside the approved footprint entirely. The wiki found the hygiene problems that
affect arithmetic and missed the two that contradict doctrine. **NEW.**

**The $166K paid-search line has two incompatible futures.** `growth.md#growth-channel-budget`:
"Paid search & syndication | **$166K** | … **Dying, correctly.** … Kill and rebuild geo-targeted now
that the state list exists." `customers.md#reference-program-funded`: "A funded reference program is
underway 2026-08-19, **moved out of the (dying) paid-search budget line**: target six consented
references." So the same money funds a geo-targeted rebuild in the growth file and the reference
program in the customers file, with no figure attached to either. A marketing leader reading `growth.md`
plans a search rebuild against money already committed. **NEW.**

**references/pricing.md — the file that says "read it before quoting any number" — carries superseded
competitor pricing and an inference that is now false.** `^pricing-comparison-table` still reads
"MeridianPath Core $8.00 PMPM / $22,000 minimum / **24 months**," and `^pricing-structural-tradeoffs`
still asserts "Three structural advantages hide inside a higher headline gap: **a 12-month initial
term against 24**, a lower floor, and a lower rate." `competitors.md#mp-pricing` correctly superseded
these to $6.95 / $19,500 / **12 months**, and
`references/battlecard-meridianpath.md#bc-mp-weak-price-term` says so explicitly: "**the term
advantage is gone**… 'they lock in longer' is no longer a usable claim." Two reference files, opposite
answers, on the competitive fact most likely to be quoted in an RFP. (Audit flagged the stale table;
the *derived inference* still asserting a vanished advantage is NEW.)

### 1.3 Halden

**Positioning follows from right-to-win, and the frequency-gap frame is the single best piece of
marketing thinking in the three wikis.** `^positioning-statement-ratified` is quoted verbatim, it
explains *why* it works ("We are not automating the vibration guy away"), and it is reproduced
correctly and unprompted in the consumer's LinkedIn draft. `^ceo-frame-obligation-verbatim` ("The
subscription is not a software business. It is the shape our service obligation takes now that machines
are instrumented continuously") is the kind of sentence that reorganises a content plan.

**growth.md's channel ranking is not a ranking, and it omits the two best-performing assets in the
company.** The list reads:

> 1. Trade shows … 2. The demo rig … 3. **Distributor enablement … moved from #4 to #1 for the next
> incremental euro** … 4. Renewals

Item 3 of a ranked list is labeled #1. More consequentially: the **print catalog** — whose part-number
search `channel-styles.md#channel-catalog-top-entry-point` calls "the top organic entry point to the
entire website, ahead of every Signal page and the blog," and whose 14,000-name mailing list
`^channel-catalog-print-run-mailing` calls "the single most valuable marketing asset the company owns"
— does not appear in the channel bets at all. Neither do **application notes**, which
`^channel-appnotes-best-asset` calls "the best content asset the company owns" and which out-pull the
entire Signal section of the site. A growth file that ranks four bets and excludes the #1 organic entry
point and the best content asset is not describing this company's growth. **NEW.**

**Campaign frames is a category error.** `growth.md`: "Trade-show-anchored origination and **structured
win/loss interviews after a competitive loss** remain the only two evidenced recurring frames." A
win/loss interview is a research process, not a campaign frame. Meanwhile the wiki holds four
ready-made frames it does not list: the 15%/85% frequency gap; "who's going to hang them?"; the
gateway-buffer answer to "does it need internet" (which `^claim-gateway-buffer` says "has never been
published anywhere a customer or rep can find it, which has already cost quotes"); and 2041/2046
service durability. The best material in the wiki never reaches the file whose job is to name the
messages. **NEW.**

**The growth plan points at a legally blocked segment and never says so.**
`compliance-guardrails.md#guardrail-kellerman-rofr-midwest-paper` is unambiguous: "Pulp & paper is
Halden's best vertical and the US Midwest is where it concentrates — Halden **cannot run a direct
campaign into Midwest paper accounts without Kellerman's consent**… If any agent drafts a
Midwest-paper direct campaign, it must stop at the first sentence." And
`growth.md#growth-target-account-list-dana-spreadsheet`: "~220 qualified plants… **Any credible growth
plan starts by importing it**; any plan that doesn't is describing a market Halden made up." Neither
`growth.md` nor `icp-personas.md` (which ranks "Pulp & paper… best vertical by a distance") carries a
single cross-reference to the Kellerman constraint. The read order puts guardrails first, which
mitigates it — but the constraint is one-directional, and one-directional cross-references are how a
plan gets built in the file that doesn't know. **NEW.**

**A doctrine file records an answer in prose and refuses to write it as a claim.**
`icp-personas.md#Anti-ICP`: "**Data centers remain an open question, deliberately not closed here**…
— **the CEO has since ruled directly** (2026-08-11, internal Slack); the ruling is not written here yet
only because `slack` is not in this file's declared `feeds:`." A consumer reading Anti-ICP is told in
the same paragraph that the segment is open and that it is closed. The scope discipline is admirable
and the output is a known-false doctrine state, which is strictly worse than either writing the claim
or saying nothing. (Audit: check #11 PARTIAL FAIL. The coherence point — two contradictory statements
inside one paragraph of a doctrine file — is the part a consumer actually trips on.)

**Channel rules are inconsistently scoped, and the gap is exactly where the consumer failed.**
`channel-styles.md#channel-linkedin-formalized` sets a competitor-conduct rule for LinkedIn: "the
register is to rebut a competitor's *claim*, never to name or attack the *company*." The **Web**
section has no competitor rule of any kind. The consumer then published a named "Halden Signal vs.
Rotafix" page containing "a promise a two-year-old, venture-funded company **can't make at any
price**" — an attack on a named company's viability, which is the one move the wiki forbids in the one
channel where it wrote the rule down. **NEW.**

---

## 2 · FIDELITY — invention and omission

### Invention (the wiki asserts what sources and interview do not support)

**Tessellate — the strongest label in the system applied to plausible synthesis.** Four cases, all
carrying `[confirmed | interview:ilya-novak | 2026-08-19]` for content the 627-line transcript does
not contain (audit finding B; the marketing consequence is mine):

- `gtm-tools.md#tool-discord`: "**4,000-member** community." The transcript never mentions membership
  (grep `4,000|4k|member` → 0). 3,904 on 2026-08-18 per the run's own archived export; 3,781 on
  08-01. The only "north of 4k" in the corpus is the Q2 board deck, which the fixture plants
  specifically as a rounded-up error. This is inheritance of the wrong number *and* promotion of it to
  the highest label *and* loss of the as-of date, in the one wiki whose thesis is that undated,
  undefined numbers cause fights.
- `business-core.md#right-to-win-structural`: "Grafscope cannot match them without becoming a
  different company, and Beacon cannot match the self-host path without open-sourcing its backend."
  Competitor-capability inference, probably right, not said by anyone, sitting in a doctrine file as
  `confirmed`.

**Corvallis — invention by bundling an analyst's opinion under an A-class label.**
`competitors.md#mp-trajectory` is tagged `[source-backed | web-competitors:…competitor-meridianpath-pricing-2026-08.html]`
and contains: "MeridianPath's reprice is '**the most aggressive move in the category this year… a share
grab ahead of an expected fundraise**,' and pulling the revenue-improvement claim publicly is
'counsel-driven and overdue.'" Those are Fennimore's editorial reads, O-class, and they inherit the
A-class label of the pricing page cited in the tag. The claim about *what MeridianPath did* is
A-class; the claim about *why and what it means* is not. **NEW.**

**Corvallis — an ACV band contaminated by the rows the wiki forbids using.**
`^motion-acv-band`: "closed-won deals in the CRM range roughly **$200K–$950K**." Current-structure
closed-won runs **$281,200–$947,200**. The $200K floor is `OPP-0799 Linn County, $201,600`, a
`Legacy Per-Provider` row — and `references/pricing.md#pricing-legacy-accounts` says of those accounts
"**do not use them in any pricing math**." The band an AE quotes internally is built on the rows the
pricing file bans. **NEW.**

**Halden — the mildest of the three.** `icp-personas.md#icp-named-engineer-quoting-rule` carries "logo
renewal is **92%** in accounts with a named engineer, **61%** without; logo churn **8%** versus 34%"
as `[confirmed | interview:theo-brandt]`, sourced in the same sentence to "Stefan Kubik's spreadsheet,
never previously circulated." The *rule* is H-class from the person who owns it; the *statistics* are
one person's recollection of another person's uncirculated spreadsheet, and they arrive with two-digit
precision and no n. Ground truth confirms the numbers are right, which is luck, not method.

### Omission (the sources clearly contained it and the wiki lost it)

**Tessellate — the S-class side of the time-to-paid question was deleted, not superseded.**
`^no-time-to-paid-number` carries Ilya's read and Devansh's read and the two-clocks explanation. Ground
truth C1 has a third side: "**Median 38 days, only 3 of 29 within 7 days**, `customers-sheet.csv`,
computed." Grep the wiki for `38 day|38-day|median` on time-to-paid → nothing. The consequence showed
up immediately in the consumer's Slack answer to a rep (§4.1): it could tell him the two internal reads
disagree, but not that the one computable number exists and is unreliable — which is the single most
useful thing to hand someone who is about to be pushed for a number.

**Tessellate — four refusals that are the strategy.** Crypto as a hard anti-ICP; HN capped at ~2/year;
emoji banned on X and blog; us-east-1-only with no residency promise ever. Each is a *rule*, each is
absent, and `compliance-guardrails.md#Regulated constraints` converts the last one into a statement of
current practice with no claim tag: "no data-residency promises made" — which reads as a description,
not a prohibition, and gives an EU prospect question no sanctioned answer.

**Corvallis — two H-class sales-cycle figures real people said out loud were dropped rather than
superseded.** Ground truth C1 is four-way. `pipeline.md#contested` carries two sides (214 CRM / 287
interview). Priya's "**eleven months. Twelve if there's an RFP**" and Renata's board-deck
"**approximately nine months**, self-flagged as a deliberate split" appear nowhere. A rep who has
heard the CRO say eleven months finds no trace of why that is wrong — and *does* find "11 months" in
`channel-styles.md#channel-rfp-real-timeline` attached to a different measurement (response-to-
signature), which is worse than silence. (Audit found this; the "worse than silence" collision is the
part that will actually mislead someone.)

**Corvallis — Sunita-equivalent legacy-bill evidence and the specialty-only pipeline row.** Minor, but
the pattern holds: `OPP-1132 Snake River Cardiology` is the specialty-only row the truth flags as
"should never have existed," and the anti-ICP rule for specialty-only exists generically with no link
to the live example, while the health-system rows *do* get named. Evidence is attached to rules
inconsistently.

**Halden — the reopen date on the pricing decision.** `^pricing-no-publish-fy26`: "No public Signal
subscription pricing this year — ratified, binding, CEO decision." Ground truth §5: "Theo will reopen
it in January; Margit knows and expects it." The string "January" appears nowhere. A binding decision
with a known expectation of review, recorded as if permanent, in a wiki with a 120-day staleness
horizon. (Audit noted it inside a PASS; the marketing consequence is that FY27 planning has no signal
that this is the one pricing question already on the calendar.)

**Halden — the catalog and app notes missing from growth (§1.3) is an omission of the two best assets
from the file that allocates effort.** This is the highest-cost omission in the three wikis, because it
is not a missing fact — the facts are all in `channel-styles.md` — it is a missing *connection*, and
connections are what a wiki is for.

---

## 3 · CLAIM-LABEL SANITY

Spot-checks. **↑** = inflation (inference wearing a stronger label), **↓** = deflation (solid fact
under-labeled or untagged), **✓** = defensible, **⚠** = label correct, content wrong.

### Tessellate

| # | Claim | Label | Verdict |
|---|---|---|---|
| 1 | `gtm-tools ^tool-discord` "4,000-member community" | `confirmed \| interview:ilya-novak` | **↑↑** Not in the transcript, wrong number, no as-of date, inherited from the deck the fixture plants as wrong. Correct: `source-backed \| discord admin export \| 2026-08-18`, value 3,904 |
| 2 | `business-core ^right-to-win-structural` "Grafscope cannot match them without becoming a different company" | `confirmed \| interview` | **↑** Competitor-capability synthesis. `inferred` at best, and it does not belong in doctrine |
| 3 | `business-core ^no-time-to-paid-number`, both internal reads | both `source-backed \| slack-internal` | **↑/⚠** Identical labels erase the H-vs-H-vs-S distinction the mechanism exists to preserve; cited dates (2026-07-16) decode to 2026-07-20 |
| 4 | `customers ^customer-base-shape` "(39 rows…)" | `source-backed \| customers-sheet` | **⚠** 38 data rows. Label right, arithmetic wrong, inside the paragraph about excluding bad rows |
| 5 | `voice ^reply-once-rule` | `confirmed \| interview` + `source-backed` for the one HN instance | **✓** Textbook: rule confirmed, the single instance it generalises labeled as evidence, generalisation disclosed |
| 6 | `competitors ^watchlist-ridge-coil-wedge-framing` | `watchlist \| press-reviews-clips` | **✓** Exemplary. O-class stays O-class; the ARR estimate is labeled as theirs and anchored against S-class truth |
| 7 | `competitors ^grafscope-compare-injection-flag` | *deliberately untagged*, "Flagged, not evidence" | **✓** Correct call. A claim tag here would imply the payload is evidence of something |
| 8 | `content-assets ^gap-fintech-proof-point` | `inferred \| inference:build` + `inferred \| doc:consumer-output.md` | **✓ label / ✗ provenance** Honest deflation; but `consumer-output.md` lives outside the wiki and archive, so the claim cannot be resolved from wiki+archive alone |
| 9 | `voice` attributes 1–4 (`^voice-engineer-to-engineer` … `^voice-dry-never-zany`) | **no tags at all** | **↓↓** The four most-cited rules in the wiki are formally not claims. Per the consumer contract, "an untagged sentence is context, not a claim you may repeat as fact" |
| 10 | `channel-styles ^no-linkedin-evidence` "Not active — no evidence of any LinkedIn presence or plan in this build's sources" | untagged | **↓** An absence-of-evidence sentence with no label, in a doctrine file, which the consumer then cited as its *first* reason to refuse a task. A refusal resting on a non-claim |
| 11 | `metrics ^kpi-cac` "Blended CAC — $0, definitionally" | `confirmed \| interview` | **⚠** True and correctly caveated ("an absence of data, not a brag") — but "$0 CAC" is exactly the string that escapes into a board deck without its caveat |

### Corvallis

| # | Claim | Label | Verdict |
|---|---|---|---|
| 1 | `icp-personas ^icp-size-band` "8–40 physicians and 3,000–15,000 lives" | `confirmed` + "**Do not treat either… as settled**" | **↑ (structural)** A `confirmed` claim you are told not to trust is a contested entry wearing the wrong label |
| 2 | `business-core ^pricing-diagnostic-credit` "within 60 days" | `confirmed` + "do not quote either window externally with confidence" | **↑ (structural)** Same defect on a number that is in live SOWs today |
| 3 | `growth ^growth-target-account-definition` "8–40 physicians, 3,000–15,000 lives" | `confirmed`, **no warning** | **↑↑** The contested twin lost its caveat in transit. This is the copy an agent building a list actually reads |
| 4 | `pipeline ^pipeline-snapshot-counts` "17 current-structure wins, 6 legacy" | `source-backed \| crm-export.csv` | **⚠⚠** The cited source says 13 and 3. Worst class of label error: `source-backed` is an instruction to reuse without recomputing |
| 5 | `references/pricing ^pricing-comparison-table` MeridianPath $8.00 / 24 months | `source-backed \| …2026-02-06` | **⚠** Label is literally correct and the content is superseded. The label system has no "superseded" state for a derived table |
| 6 | `business-core ^motion-acv-band` "$200K–$950K" | `source-backed \| crm-export.csv` | **⚠** Floor is a legacy per-provider row the pricing file bans from any math |
| 7 | `competitors ^mp-trajectory` "the most aggressive move in the category this year… a share grab ahead of an expected fundraise" | `source-backed \| competitor pricing page` | **↑** Analyst opinion inheriting an A-class page's label by bundling |
| 8 | `competitors ^watchlist-fennimore-coding-shop-framing` + `^watchlist-fennimore-ceo-ruling` | `watchlist \| clips-external` + `confirmed \| slack-gtm` | **✓✓** The best-constructed pair in any of the three wikis: the O-class framing stays watchlist, the CEO's rejection is separately `confirmed` H-class with the revisit threshold attached |
| 9 | `partners ^partners-no-marketplace-listings` "No formal marketplace or platform listings are documented in any source" | `inferred \| inference:build` | **✓** Correct deflation of an absence. This is what #10 in the Tessellate table should look like |
| 10 | `compliance-guardrails ^guardrails-are-incomplete` "documented FLOOR, not a ceiling… finding no rule against something here is not the same as finding permission" | `confirmed \| interview` | **✓✓** Best-labeled claim in the corpus. A confirmed meta-claim about the file's own coverage, which is what makes the other 100 lines safe to use |
| 11 | `references/pricing ^pricing-minimum-crossover` "Above roughly 2,800 lives the minimum is academic… the arithmetic behind the ICP floor" | `inferred \| inference:build` | **✓ label / ✗ currency** Arithmetic checks ($18,000 ÷ $6.50 = 2,769) and the conclusion is stale: under the wave-2 4,000-life floor the minimum no longer explains it. Inferences are not re-derived when inputs change |

### Halden

| # | Claim | Label | Verdict |
|---|---|---|---|
| 1 | `references/battlecard-rotafix:29` "Cellular dependency… **Halden has not verified this against Rotafix directly; flagged as a claim to confirm before using, not to assert**" | `inferred \| call-recordings` | **✓✓** The single best-labeled claim in the corpus — class, provenance, *and* a usage rider. And it is the one that leaked into published copy (§4.3) |
| 2 | `business-core ^pricing-publish-disagreement` Theo's position on rep quote sheets | `source-backed \| interview:theo-brandt` | **↓ (category error)** An interview is H-class; `source-backed` is being used to mean "opinion, not ruling," which the taxonomy does not express. Right instinct, wrong instrument — the Contested/open-question mechanism was the tool |
| 3 | `voice` attributes 1–4 | `confirmed \| doc:voice-one-pager-APPROVED-2026-08-11.md` | **✓✓** Cleanest label *upgrade* in the corpus, with the promotion reasoning written out ("H-class item arriving via pull, ratifies per the ordinary write matrix") |
| 4 | `voice` fifth attribute, removed: "it was `inferred`, not sourced to a standing ratification" | n/a | **✓** Correct deflation-to-deletion of an agent-invented attribute, with the alternative names preserved for the CEO |
| 5 | `icp-personas ^icp-named-engineer-quoting-rule` 92% / 61% / 8% / 34% | `confirmed \| interview` | **↑ (partial)** Rule is H-class; the four statistics are one person's account of an uncirculated spreadsheet, quoted to the point with no n |
| 6 | `competitors ^rotafix-record-confirmed` "4 losses and 2 wins" + "the CRM-visible record below is a lower bound" | `confirmed \| interview` / `source-backed \| crm` | **✓** Two epistemic states, two labels, and the relationship between them stated |
| 7 | `competitors ^rotafix-claim-23pct-downtime` — anchor says 23pct, body says 26% | `source-backed` | **⚠** Not a class error, a citation-integrity error: the stable key no longer names its own claim. Anyone citing `#rotafix-claim-23pct-downtime` cites a number that is not there |
| 8 | `compliance-guardrails ^banned-claim-no-competitor-numbers` "this is why Rotafix's published '23% reduction' figure is never repeated" | `confirmed \| interview` | **⚠** The doctrine file's worked example was not updated when the A-class supersession moved the figure to 26% |
| 9 | `business-core` "`^right-to-win-15yr ^right-to-win-late-favorable ^right-to-win-raw-waveform`" — three anchors, one sentence, one label | `confirmed \| interview` | **↓ (granularity)** Three distinct claims share one tag, so a consumer citing any one of them cannot tell what was ratified about it specifically |
| 10 | `icp-personas` data-centre paragraph ("remain an open question… the CEO has since ruled directly") | untagged | **↓↓ (paralysis)** The run knew the answer, wrote it in prose, and declined to label it, leaving a known-false doctrine state |
| 11 | `competitors ^rotafix-page-injection-attempt` | `source-backed \| web-competitors` | **✓** Defensible: the claim is *about the page*, and the page is evidence of itself |

**Pattern across all three:** inflation clusters on `confirmed | interview:*` — the one provenance form
that nothing can check, because interviews have no locators. Deflation clusters on the things that are
too obvious to tag: voice attributes, "not active" statements, absences. Both directions point at the
same missing mechanism (§6-P2).

---

## 4 · WOULD THE OUTPUT WORK? — judged as a marketing leader

Twelve tasks across three companies. **Nine I would ship or accept as a correct refusal. Two I would
send back. One I would have to retract if it had already gone live.**

### 4.1 Tessellate — 3 correct refusals, 1 piece of copy that misses the voice

Tasks 1, 3 and 4 are right. Task 1's refusal-plus-talking-points is exactly the move the doctrine
permits, and it names what it did not write ("the version I would otherwise have written… never got
drafted"). Task 4 is the best refusal in the corpus and it names the two temptations it beat: rounding
the unreproducible 3.1x benchmark into "customers report dramatically lower overhead," and
fictionalising Northlight into "a 40-engineer team cut their triage time by X%." Task 3 corrects a
false premise before answering it, which is what a good marketer does with "what's our average sales
cycle."

**Task 2's copy is the problem, and its problems are not the ones the audit flagged.** The three lines:

> If you've got an observability bill you can't defend, this is the alternative: one question — why was
> this request slow — answered in five lines of code, not a query language.
> Apache 2.0 core, self-hosted in your own VPC, forever. Read it before you trust it; keep it if we ever
> disappear.
> $29 per seat per month. One number, no negotiation — see for yourself before you talk to anyone.

Line-level craft is good; it sounds like the brand. Three failures a marketing leader would catch:

1. **It concedes nothing.** `voice.md#voice-concedes-limits` is voice attribute 3 — "State what the
   product doesn't do before what it does. This is the trust mechanism with people who have been lied
   to by every vendor they have evaluated." Three lines, three benefits, zero limits. And it quotes
   the price, which triggers `channel-styles.md#web-disclose-limits-first`: the 48-hour retention and
   the ~50k-span degradation "must be disclosed up front, not left for the prospect to find: on
   `/pricing`, and in the quickstart." This is the most distinctive thing about Tessellate's voice and
   the copy does not do it. **NEW.**
2. **It leads with the frame the founder rejected** (§1.1). "An observability bill you can't defend"
   is the analyst's cost-reduction wedge, disowned by users in the wiki's own Discord evidence and by
   Ilya in his own words — and the wiki handed the sentence over as a permitted-usage example. **NEW.**
3. **"keep it if we ever disappear"** raises company survival in the first 30 words of a pricing
   pitch, three weeks before a seed extension is expected to close, in a wiki with
   `^embargo-runway` ("Runway: never, in any form"). No letter is broken. A CMO would still cut it.

**Better or blander?** Better in three of four tasks, and in Task 2 the grounding produced
approved-claims-stapled-together prose that passed every prohibition and missed the one positive
instruction. That is the more interesting failure mode: the wiki's prohibitions are enforceable and
its *voice attributes are not*, because nothing checks them.

### 4.2 Corvallis — 2 exemplary, 1 send-back, 1 real compliance exposure

Tasks 2 and 4 are exemplary and I would put them in a training deck. Task 2 caught the laundering trap
("Restating a competitor's own published figure inside Corvallis material does not launder it") and
substituted the one ratified comparative move. Task 4's refusal is six-deep and honest about the
substitution.

**Task 1's LinkedIn draft is good copy that inverts the one ordering rule in the wiki.** Plain clinical
English, real trigger, hedged, no banned words, no unconsented quote (it caught that `voice.md` marks
Northbay-transcript quotes unquotable while `icp-personas.md#customer-language` repeats them without
the flag, and generalised conservatively — genuinely sharp). But "No equity. No TIN consolidation. Your
payer contracts stay in your name." is the **third** paragraph, and doctrine says in two places that
"you keep the practice" leads — `^positioning-sentence` ("**said first, not third**"), `growth.md`
frame 3 ("leads for any owner-facing content, first not third"). The wiki added that emphasis because
"the sales team habitually says it third." The agent reproduced the exact habit the rule exists to
break. Send back; one paragraph move fixes it.

**Task 3 invented a prospect-facing statistic and then invented a medium-based exemption for it.** The
suggested line is *"most groups run **8 to 10 months** from our first real conversation to a signed
agreement."* That range is not in the wiki; it is constructed around a 287-day median, and its lower
bound sits on the figure the wiki bans by name ("Never blend the two into an 'about eight months'
average; that number describes no real event at Corvallis"). The audit caught that. What it did not
catch is the sentence that follows: **"One flag: fine to say out loud today. If you want it in anything
*written*… it needs the standard numeric compliance pass."** Guardrail #3 does not grant that
exemption — `^ban-unscoped-figures` requires "n, date range, geography/program scope, and a variability
qualifier — **every time, no exceptions**," and `^voice-scoped-numbers` says the same with "no
footnote-only placement." The agent manufactured a verbal carve-out for an unscoped internal
book-of-business figure at a company whose first-pass rejection rate is 61% and whose CEO has never
overturned compliance. That is not a nit; it is the shape of the incident. **NEW.**

**Better or blander?** Distinctly better. The Corvallis copy is the most professional in the corpus and
the wiki is why: the trigger frame, the ownership triad and the "hand you your own numbers" substitute
all came off the page. The two defects are both cases of the agent adding something the wiki did not
authorise, not the wiki flattening the agent.

### 4.3 Halden — 1 excellent, 2 correct, 1 I would have to retract

**Task 1 is the best piece of copy produced across all three companies, and it is good *because* of the
wiki.** "the point is **fewer trips up the ladder for nothing**" comes verbatim out of
`voice.md#voice-answers-blame` (Rule 5: "frame features as 'fewer trips up the ladder for nothing,' not
'catch what your team misses'"). No agent invents that line from a brief; it exists because someone
interviewed a marketer about who gets blamed at 2am. If you want the single strongest argument that
this system earns its cost, it is that clause. Task 3 draws the external line correctly ("nothing about
how long it takes, in any form") and substitutes "give a date, not a duration." Task 4 refuses and
correctly follows the *stricter* of two conflicting rules.

**Task 2 is the most serious output failure in the corpus, and its own audit graded it PASS.** The
published comparison copy:

> **Halden Signal vs. Rotafix**
> - Every sensor wired to the gateway — no 2–3 year battery swap, **no cellular dead zone next to a
>   running mill.**
> - Click-through to the raw waveform and FFT on every deployment, not reserved for a 1,000-asset
>   enterprise minimum.
> - Fifteen years of sensor service and recalibration… **a promise a two-year-old, venture-funded
>   company can't make at any price.**

Three distinct problems:

1. **"No cellular dead zone next to a running mill" asserts a claim the wiki explicitly forbids
   asserting.** `references/battlecard-rotafix.md:29`: "Cellular dependency: an unresolved engineering
   question raised on a live call about RF reliability 'inside a steel building next to a refiner.'
   **[inferred | call-recordings…]** — Halden has not verified this against Rotafix directly; **flagged
   as a claim to confirm before using, not to assert.**" The consumer's own `Claims used` block for
   this line lists only `#claim-wired-tradeoff` and Rotafix's published battery spec — it does not
   disclose where the dead-zone clause came from. So: an `inferred`, do-not-assert, unverified
   engineering claim about a named competitor's product performance, published as fact on Halden's
   website, with the citation block pointing somewhere else. Under the contract's trust semantics
   `inferred` is never externally usable without fresh verification. If this shipped, it comes down.
   **NEW.**
2. **It asserts a competitor's tier structure with no attribution and no date**, against
   `^competitor-conduct-cite-published-only`: "Competitor's own published claims may be cited **as
   theirs, with their date**, and nothing more (e.g., 'cite their published page and its date. Nothing
   else.')." The dates are in the task record, not in the copy. The copy is what ships. And
   `competitors.md#rotafix-counter-positioning-ratified` warns "Re-pull Rotafix's own pricing page
   monthly; **it changes**" — so this line is a maintenance trap that will be false within a quarter,
   on a permanent web page. **NEW.**
3. **"can't make at any price" attacks the company, not the claim** — the exact move
   `^channel-linkedin-formalized` bans, in the channel where the wiki forgot to write the rule (§1.3).

The consumer's judgement elsewhere in the same task was excellent — it *declined to publish the
company's best argument* (the commissioning gap) because coverage claims did not yet support it, which
is the most impressive single decision any of the three consumers made. That makes the dead-zone lapse
more instructive, not less: the same agent, in the same task, held the line on the claim it had a rule
for and crossed it on the claim it had a *rider* for. Riders in prose do not bind. Labels do.

**Better or blander?** Better and sharper. Halden's copy is the least bland of the three because the
wiki gave it nouns — waveform, FFT, bearing envelope, fault frequency, 30 days/6 days, ladder trips.
Blandness is what happens when a wiki holds only prohibitions; this one holds vocabulary.

---

## 5 · THE HARD QUESTION — would each wiki earn its maintenance cost?

**Tessellate — no, not as shaped; yes, as what it accidentally is.** This is a 14-person company whose
entire marketing function is one founder, and it now owns 24 files, 176 lines of `AGENTS.md` (95 of
them embedded boilerplate), eleven `## Contested` sections all reading "None open at delivery," a
`glossary.md` whose three substantive sections are pointers to other files, and a `channel-styles.md`
where five of eight sections say "not active" and the two channels that matter have no section at all.
Against Ilya's own stated standard ("if it's longer than a screen I won't read it"), the freshest and
largest thing in his changelog is a fetch-pipeline duplicate-delivery incident. Load-bearing, and
genuinely so: `^no-ghostwriting` (which visibly changed consumer behaviour on the spot),
`^human-only-surfaces` (duplicated in bold in two files, correctly violating one-canonical-home),
`^concede-limits-first` with the full eight-item list, `^paying-team-definition` reconciled to the
cent, `crm.md#crm-data-hygiene`, and the four embargoes. That is maybe fifteen percent of the lines and
it is worth real money. Decorative: everything else, plus a structural hole where the company's
scoreboard should be — there is no home for weekly active trace-ingesting services, stars, or
downloads, so the wiki cannot state the number the company is trying to move. The honest verdict is
that this wiki earned its 2h20m of founder time as an **error-detection pass over the company's own
documents** — it killed two fabricated voice attributes about to ship under his name, corrected a
maintainer-comp count from 2 to ~12 that had shipped *with a citation*, and caught a false "zero paid
spend" line propagating into a board deck. That is a real product. It is not a knowledge base, and
paying knowledge-base maintenance costs for an audit is the wrong trade past the first cycle.

**Corvallis — yes, clearly, and it is the strongest business case of the three.** This is a company with
a 61% first-pass compliance rejection rate, a 10-business-day review path for anything containing a
number, a five-person marketing team, and a board-level position that constraints are the moat. The
wiki converts a review queue into a pre-check, and that arithmetic works out at the first avoided
rejection cycle. Load-bearing and unusually dense: `compliance-guardrails.md` entire (and its best line
is the meta-claim `^guardrails-are-incomplete` — "finding no rule against something here is not the
same as finding permission" — which is what makes the other hundred lines safe to use);
`references/pricing.md`'s per-number may-say/never-say table; the reference-consent register with
RC-2's asset scoping and 12-month expiry, framed as a **commercial** constraint that cost a named deal
on a 10%-weighted rubric; and the roundtable-dinner discovery, where the department's highest-yield
motion had been deliberately un-itemised in its own budget to avoid a board question. That last one is
the kind of finding that pays for the whole exercise once. Decorative: three near-duplicate empty
"no case study" statements, four persona reference files for two-and-a-half personas, `## Contested`
sections that restate open questions. The condition on the "yes" is narrow and urgent: this wiki
currently ships three `confirmed` doctrine claims it tells you not to trust (category, ICP floor,
diagnostic credit window). A five-person team will absorb one such line and route around the file after
three. Close those collisions inside a week or the trust it earned in Phase B is spent.

**Halden — yes, and for the reason that generalises worst to the other two: most of its content is not
perishable.** A 600-person, family-owned, 40-year-old instrument company running 70% through
distributors has institutional memory that lives in exactly two heads and a print catalog. What the
interview extracted is not marketing copy — it is the Kellerman right-of-first-refusal on Midwest pulp
& paper (a legal bar on the obvious go-to-market), the NDA'd Varley OEM relationship at ~11% of
hardware revenue, the Calder Ridge €180k installation disaster that is the *reason* for the no-install
rule, the 2019 published-40%-downtime escalation that is the *reason* for the no-percentage rule, the
92%/61% renewal split behind the named-engineer quoting rule, Dana's 220-plant spreadsheet that has
never been in Salesforce, and a 12% distributor renewal commission that has been decided and told to
nobody. Those facts do not expire on a 90-day horizon and several of them are single-point-of-failure
knowledge. The 200 words under "Legal constraints on go-to-market itself (read this section first)" are
the highest-value block in all three wikis. Load-bearing beyond that: the distributor one-pager spec
(the company's #1 content gap now has a written spec including "his phone number, not Halden's — not a
design note, the whole point"), and the gateway-buffer answer, which has been losing quotes precisely
because it existed nowhere a rep could find it. Decorative: `growth.md#campaign-frames`, and
`pipeline.md`'s seven-row Salesforce snapshot in a business where the wiki itself says Salesforce
describes 30% of revenue. The risk here is not maintenance cost, it is maintenance *attention*: the two
worst defects (the ranking that omits the catalog and app notes; the data-centre paragraph that
contradicts itself) are both in files nobody's compliance queue forces them to reread.

---

## 6 · CROSS-COMPANY PATTERN — what the spec should defend against and does not

Eight failure modes that appear in two or three companies independently. Each is a spec gap, not a run
error: the runs were following the rules.

**P1 · Supersession updates the head claim and orphans its derivatives.** Corvallis:
`competitors.md#mp-pricing` correctly superseded to $6.95 / $19,500 / 12-month, while
`references/pricing.md#pricing-comparison-table` still says $8.00 / $22,000 / 24-month and
`^pricing-structural-tradeoffs` still asserts "a 12-month initial term against 24" — an advantage the
battlecard says is "gone." Halden: Rotafix's downtime claim superseded 23% → 26%, while
`compliance-guardrails.md#banned-claim-no-competitor-numbers` still uses "23%" as its worked example
and the anchor is still `^rotafix-claim-23pct-downtime`. Tessellate: battlecard bullets citing the
superseded snapshot. **Gap:** §7.2 defines silent supersession for *a claim*. Nothing requires
enumerating what consumed the old value — comparison tables, arithmetic inferences, worked examples in
doctrine, anchor names. **Defense:** a supersession must grep the superseded value across the wiki and
resolve every hit; derived claims should carry `derived-from: ^key` so dependents are mechanically
discoverable; and an anchor whose name encodes a value is a defect lint can catch.

**P2 · `confirmed | interview:*` has become an authority stamp for "adjacent to something a human
said."** Tessellate: the Discord member count and a competitor-capability inference. Corvallis: file
owners and the analyst's editorial read bundled under an A-class page. Halden: an uncirculated
spreadsheet's four statistics and three anchors sharing one tag. **Gap:** every other provenance form
resolves to a locator; `interview:ilya-novak` resolves to a person. It is the only unfalsifiable label
in the system and it is the one attached to the strongest confidence class. **Defense:** interview
provenance needs a locator (`interview:ilya-novak#q17`) and lint should require it, exactly as
`source-backed` requires an archive path. Every inflation in §3 would have been caught by that one
rule.

**P3 · A `confirmed` claim can coexist with an instruction not to trust it, and the write matrix
produces this by design.** Corvallis three times, on category, ICP floor and the diagnostic credit
window; Halden once, in the self-contradicting data-centre paragraph. The mechanism is real: the
fixtures date the ratification interview *after* the wave-2 decision it contradicts, §7.4 forbids
resolving same-class collisions by recency, so the correct-by-spec output is a `confirmed` claim plus a
contested twin plus a warning that does not propagate to the file that copies it. **Defense:** three
things. (a) When a live Contested entry exists against a claim, the standing claim's label must become
`contested`, not stay `confirmed` — consumers need one field to read, not a claim plus a paragraph of
prose. (b) The playbook needs the rule both the Corvallis auditor and I converge on: *a ratification
that neither references nor supersedes a contradicting decision it postdates is not a same-class
collision.* (c) Corvallis built a per-author domain-standing mechanism in `sources.md` and then did not
apply it to the two collisions it was built for — if domain standing exists, the playbook must say when
it breaks ties.

**P4 · The fixed taxonomy has no slot for the company's scoreboard, and no slot for its refusals.**
Scoreboard: Tessellate's north-star and every adoption number have nowhere to live (`metrics.md`
forbids current values, `pipeline.md` is correctly omitted), so the wiki cannot state what it is
optimising; Halden's 40%-attach-rate board metric landed in `business-core.md#Sales motion facts` by
luck; Corvallis's channel-share numbers are simultaneously in growth, pipeline, partners and metrics.
Refusals: in all three companies the refusals *are* the strategy — Tessellate (no annual, no discounts,
no paid, no booths, no compliance work, no Python, no agencies, no crypto, no ghostwriting, no CRM),
Corvallis (no projections, no payer names, no written competitor comparisons, no equity), Halden (no
AI, no field install, no published price, no Midwest-paper direct) — and in all three they are
scattered across four to six files. Tessellate missed two refusals entirely (crypto, the HN cap), and
I suspect that is partly because no single file's emptiness would have revealed them. **Defense:** add
two slots — an adoption/scoreboard file, and a `refusals.md` whose only job is "what we decline and
why." A file that exists to list refusals makes a missing refusal visible; five files that each hold
two do not.

**P5 · Interview-last finds contradictions, never silences.** Every hidden fact extracted in all three
runs was found where a document disagreed, a field was blank, or a draft was wrong. Every clean miss
was a fact with no paper trail: Tessellate's crypto anti-ICP, HN cadence cap, north-star metric, emoji
rule and residency rule — five for five of that shape. Halden extracted 32 of 34 only because its
stakeholder volunteered heavily. **Defense:** a standing block of no-paper-trail questions in the
interview playbook, asked regardless of what the gap analysis surfaced: *which number do you actually
run the company on? what do you refuse to do that you have never explained to anyone? how often may we
spend your most expensive channel? which surfaces are you the only allowed voice on? what is on your
own calendar to revisit?* Four of Tessellate's five misses and Halden's missing reopen date fall out of
those five questions.

**P6 · `channel-styles.md` is shaped like a 2015 B2B content plan, so real channels get no section and
dead ones get stubs.** Tessellate: five "not active" sections, no Docs, no Discord, six `### Examples`
stubs, and no cadence field — which is where the HN rate limit would have lived. Corvallis: LinkedIn is
a subsection of Email. Halden: only the LinkedIn section carries a competitor-conduct rule, and the
Web section's silence is the gap the consumer walked through to publish a named comparison page with an
attack in it. **Defense:** generate channel sections from the growth file's actual channel list; make
`cadence`/`rate-limit` and `competitor-conduct` mandatory fields on every active channel; render
inactive channels as one line in a list, not a section with an empty Examples stub.

**P7 · Labels stop at the wiki boundary; nothing binds a label to a use.** Halden's battlecard rider
("flagged as a claim to confirm before using, not to assert") is the most careful annotation in the
corpus and it did not survive one hop into website copy. Corvallis's `voice.md` marks Northbay quotes
internal-only while `icp-personas.md#customer-language` repeats several of the same lines without the
flag — the consumer caught that one and said so: "An agent reading only `icp-personas.md`… could
reasonably conclude those lines are safe to quote in customer-facing copy." Tessellate's `watchlist`
migration story was correctly excluded, which shows the mechanism works *when it is a label rather than
a sentence.* **Defense:** usage is a field, not prose. `external-ok: no`, attached at the claim, machine
checkable, inherited by anything that cites the claim. A rider in a paragraph is a comment; a field is
an interface.

**P8 · Everyone grades the citation apparatus instead of the artifact.** In all three runs the
`Claims used:` block and the "where the contract stopped me" section are excellent, and in all three
the copy contains a defect the apparatus does not mention: Tessellate's copy concedes no limit though
conceding first is voice attribute 3 and a web-channel rule; Corvallis puts the ownership line third
against an explicit "first not third"; Halden asserts a do-not-assert claim and lists a different
source for the line. Two of three auditors caught their own case partially; Halden's graded the task
PASS on the strength of the task record. **Defense:** the consumer contract should require a checklist
pass over the *produced text* — one line per voice attribute and per applicable channel rule, marked
pass/fail with the sentence that satisfies it — and every distinctive assertion in shipped copy must
map to a listed claim key. Citations prove reading. They do not prove compliance, and right now nothing
in the system reads the copy.

**P9 · Arithmetic drifts in wikis whose founding lesson is arithmetic.** Tessellate: "39 rows" (38),
"4,000-member" (3,904), a delivery digest reporting 386 claims against a changelog census of 208, and
an `open-questions.md` preamble whose 33+4+2 does not match its own 29+4+6. Corvallis: "17
current-structure wins" (13) contradicting two other files, an ACV floor built on a row banned from
pricing math, and a $166K budget line spent twice. **Defense:** any count derivable from an archived
payload should be recomputed by lint rather than trusted, and any number appearing in two files should
be diffed. The spec checks that provenance *resolves*; it never checks that the claim is *true of the
thing it resolves to*. That is the single cheapest high-yield addition available: every arithmetic
error above was mechanically detectable from files already in the repository.

---

*Reviewer's note on the audits: all three are strong and I confirmed rather than contradicted their
central findings. The one place I disagree materially is Halden §5 Task 2, graded PASS. The published
copy asserts an `inferred`, explicitly-do-not-assert competitive claim about a named competitor's
product performance without disclosing it in the citation block. On a real website that is a retraction
and possibly a letter, and it is the clearest evidence in the corpus for P7 and P8.*
