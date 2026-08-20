# UX FINDINGS — marketing-wiki end-to-end test

Synthesized from three full runs (build → interview → maintain → consume → audit) against three deliberately dissimilar fixtures:

| Company | Shape | Stresses |
|---|---|---|
| **Tessellate** | 14-person OSS/PLG dev-tools, no CRM, no sales team, Discord + docs + Hacker News are the channels, one founder is the whole marketing function | taxonomy assumes a sales org; community-as-channel; no home for adoption metrics |
| **Corvallis Health Partners** | Regulated US healthcare services, 5-person marketing team, conferences 62% of spend, RFPs are the highest-stakes channel, compliance is the product | services with no releases; compliance *workflow*; five service lines in one `## Product` |
| **Halden Instruments** | 40-year-old German industrial-instrument maker, 70% of revenue through distributors, print catalog + trade shows, family-owned, no outside capital | channel/distributor motion; channel persona; biennial event cadence; two hostile personas |

Sources read in full: 3 × `builder-phaseA-uxlog.md`, 2 × `builder-phaseB-uxlog.md`, 3 × `builder-rebuild-uxlog.md`, 3 × `maintainer-uxlog.md`, 3 × `consumer-uxlog.md`, 3 × `stakeholder-ux-review.md`, 3 × `AUDIT.md`, 3 × `phaseA-handoff.md`, 3 × `consumer-output.md` (via audit sections), plus `playbooks/`, `spec/`, `consumer/`, `scripts/` at current HEAD.

**Verified as already fixed — dropped from this report:**
- Skeleton lint failure (17 errors on pristine `templates/wiki-skeleton/`). `python3 scripts/lint.py templates/wiki-skeleton` → `0 error(s), 0 warning(s)`. The empty-`## Contested` and HTML-comment-masking complaints from Phase A are gone with it.
- `build.md` A1 now carries the scaffold-over-existing-work guard (lines 21–23).
- `lint.py`'s docstring is now in sync (15 checks listed, including `manifest-health`, `contested-backlog`, `top-level-growth`), and SPEC §14's `runbook-decay` and `contested-backlog` rows *are* implemented. Two Phase A findings retired.

Everything below was re-verified against the live files.

---

## 1. TOP FRICTION

Ranked by severity × frequency. Each item is tagged **[PLAYBOOK]**, **[SPEC]**, **[SCRIPT]**, **[TAXONOMY]**, or **[CONTRACT]** by where the defect actually lives.

---

### F1 · Phase A is not agent-executable as written: the census assumes a live human, and the fetch/synthesis firewall is circular — **[PLAYBOOK]**

**Companies: 3/3.** Severity: blocker (Corvallis, Halden), major (Tessellate). Recurs in all three rebuild runs.

`build.md` A2 is titled "Source census — **with the stakeholder**" and its body is a table of questions to ask a human. But the same playbook's session table (line 212) prints `| Quiet period (A4–A8) | none | none | nothing — you pull, draft, lint |`, and the phase framing (line 7) says "Phase A ingests everything reachable and drafts the entire wiki from evidence." Every run received a folder and no human.

> "Phase A is not agent-executable as written… My brief said 'stop where the playbook says to interview the stakeholder', which is A2, i.e. step two. I had to reverse-engineer the entire census from the twelve delivered files and then file the census itself as three open questions." — halden/builder-phaseA, **blocker**

> "Any engagement that starts 'here is a data dump, go' — which is the common case, and was this one — hits A2 with nobody to talk to and no fallback described. A2 is where `access`, `provenance-class`, `feeds`, `cadence`, data-hygiene `notes` AND every file's `owner` are supposed to come from. All of it became guesswork." — corvallis/builder-phaseA, **blocker**

Compounding it: SPEC §15.2 requires that "the agent doing credentialed fetching does no open-ended reasoning over payload content," and A4 restates it — but A2 runs *before* A4 and requires `provenance-class`, `feeds`, and hygiene `notes` per source, which cannot be written without reading payloads.

> "the ordering is circular: A2 requires declaring `feeds` and `provenance-class` per source, which requires knowing what is *in* each source, which requires reading payloads — before A4 has archived them. I could not honor the separation… the reasoning firewall was never real." — corvallis/builder-phaseA

> "In a single-agent build there is no seam to put the boundary on… it is a spec rule that cannot be followed." — halden/builder-phaseA, **blocker**

**Root cause:** the playbook models one deployment shape (consultant with live access to a stakeholder and to systems) and the spec states a two-agent security property as if it binds a one-agent build. Nothing distinguishes "read enough to classify" from "reason over content."

**Fix (playbook-wrong, plus one spec clarification):**
1. `playbooks/build.md` — split A2 into **A2a · Provisional census from evidence** (derive one source block per underlying system from the artifacts on hand; mark every inferred field; file one ratification question covering the manifest and the owner set) and **A2b · Confirm with the stakeholder** (explicitly deferrable into the Phase B agenda). Move `owner:` assignment to A2a with "proposed, unratified" as the sanctioned value.
2. `playbooks/build.md` line 212 — retitle the session-structure row: Phase A is "ingest, with two short stakeholder asks at the front, both deferrable."
3. `playbooks/build.md` A4 line 91 — add: "In a single-agent build the separation is satisfied by **ordering**: a light read for classification is permitted before archiving; the archive is written before any claim is drafted; the drafting pass reads only `.archive/`. Record the single-agent mode in the run manifest."
4. `spec/SPEC.md` §15.2 — add one sentence: "In single-agent deployments this is a temporal separation (archive-then-reason), not an agent separation; the property being protected is replayability, not context isolation."

---

### F2 · §17.3 contradicts the taxonomy's own required sections — the one conformance item nothing checks, and all three wikis ship violating it — **[SPEC] + [SCRIPT]**

**Companies: 3/3.** Severity: blocker (Halden Phase B), major everywhere else. All three audits score it FAIL or deviation.

SPEC §17.3: "Doctrine files contain no claims whose provenance is not H-class (contested annotations excepted)." SPEC §15.4: O-class "can never touch doctrine." But `spec/taxonomy.md` *requires*, inside doctrine files:
- `icp-personas.md` → `## Customer language` — "verbatim phrases customers use… each phrase cites its source" (line 61)
- `voice.md` → `## Exemplars` (line 75)
- `channel-styles.md` → `### Examples` (line 93)

And `interview.md` principle 3 makes it load-bearing: "the quote is the asset; your paraphrase destroys it."

> "this is the sharpest spec bug I hit. §17.3 says doctrine files contain no non-H-class provenance. The taxonomy **requires** `icp-personas.md#customer-language` — verbatim *customer* phrases — inside a doctrine file, and a customer is definitionally not H-class about Halden's decisions… Following B4 literally would have deleted the single most useful section in the wiki." — halden/builder-phaseB, **blocker**

> "the spec mandates a §17.3 violation in the one file it names for it." — tessellate/builder-phaseB

Three agents invented three *different* resolutions: Halden used `<!-- tier: state -->` markers; Tessellate fanned the phrase book out to `references/customer-language.md` and kept only founder-endorsed quotes; Tessellate's rebuild adopted a "narrower reading" (non-H may annotate beside an H claim). Divergence on a conformance item = missing spec.

The audits then found the predictable result:

> "**G18 Doctrine provenance is clean (§17.3) — FAIL.** Machine census of all doctrine files: **13 claims carry non-H provenance and none sits inside a `## Contested` or annotation block.**" — tessellate/AUDIT

> "**§17.3 — doctrine claims with non-H provenance. FAIL, and the changelog claims otherwise.** …**24 have provenance whose declared class in `sources.md` is S or O** … **four of the O-class claims are labelled `source-backed`, not `watchlist`** … A Reddit comment carrying the label reserved for 'deterministic or authoritative evidence on file,' inside a doctrine file." — halden/AUDIT

> "an O-class review site is the declared provenance of an approved external claim, mislabeled `source-backed`. Sharpest instance." — corvallis/AUDIT

And it is unenforceable by design: `grep -c "doctrine-provenance\|17.3" scripts/lint.py` → **0**. Both Tessellate and Halden wrote throwaway scripts to check it, then self-certified the opposite in the changelog.

> "§17.3 (doctrine is H-class only) is the entire point of B4, and `scripts/lint.py` has no check for it… I found two A-class claims still sitting in `compliance-guardrails.md` only because I wrote a throwaway script to check." — tessellate/builder-phaseB

> "The finding is not 'the wiki broke §17.3'; it is 'the wiki broke §17.3, knew why, and then wrote down that it hadn't.'" — halden/AUDIT

**Fix:**
1. **[SPEC] BREAKING** — `spec/SPEC.md` §17.3, restate as: *"No doctrine **claim** may carry non-H-class provenance. Three exceptions, and no others: (a) `## Contested` entries; (b) sections the taxonomy designates as evidence buckets — `icp-personas.md#customer-language`, `voice.md#exemplars`, `channel-styles.md ### Examples` — which keep their evidence's true class permanently; (c) sections carrying an explicit `<!-- tier: state -->` marker. A claim in category (b) or (c) is illustrative evidence; it may never be the sole tag on an assertion a consumer would treat as a company decision."* Add the same exception list to §15.4 and to §8's footnote ¹.
2. **[SPEC]** — §8's bootstrap-exception paragraph must state whether the evidence-bucket carve-out survives delivery. Tessellate's maintainer held two good Discord quotes out of canon and filed `oq-040` purely because this is unstated: *"Nothing says whether the evidence-catalog carve-out is a permanent, taxonomy-level exception (survives delivery) or was only ever the bootstrap exception in disguise."*
3. **[SCRIPT]** — add a `doctrine-provenance` check to `scripts/lint.py`: for every claim in a `type: doctrine` file, error if the provenance prefix is not in `{interview, doc}` and the claim is not under `## Contested`, not in a taxonomy-designated evidence section, and not in a `<!-- tier: -->`-marked section. This is fully mechanical and is currently the only §17 item with no deterministic backing.
4. **[SPEC]** — to make (3) resolvable, per-author class rules must become machine-readable. Tessellate: *"`slack-internal:<ts>` is H or O depending on **who wrote that message**, which the claim tag does not record. Phase A's per-author convention is documented in `sources.md` prose and is invisible to any checker."* Either extend the locator (`slack-internal:<run>/export.json#ts-123@ilya`) or make `sources.md` per-author class rules a structured YAML sub-block.

---

### F3 · The doctrine provenance table has no row for the way real doctrine actually arrives, and SPEC §5 contradicts the playbook about it — **[PLAYBOOK] + [SPEC]**

**Companies: 3/3.** Severity: major (heavy time-cost in all three).

`build.md` A5's doctrine row offers exactly two options: `inferred | inference:build` for synthesis, `source-backed | doc:<file>` for human-authored documents, plus "Never `confirmed` in Phase A." SPEC §5 says `confirmed` means "A human with authority stated or ratified it — Interview answers, **exec posts**, human-authored strategy docs."

Both are normative. Both were load-bearing, in all three companies:

> "This founder issues rulings in Slack ('Drop the "from". It is $29', 'Do not soften that, do not say "coming soon"', 'We don't buy booths')… Those are H-class by SPEC §7 — but they are not `doc:` and they are not inference. **77 of 340 claims in this wiki depend on that invention.** If a grader disagrees, most of the doctrine files fail conformance §17.3 at delivery." — tessellate/builder-phaseA, **major**, time-cost heavy

> "the CEO's Slack messages are the single most authoritative doctrine source in the dump ('we are not a technology platform'; 'no equity, no TIN consolidation'; the entire already-in-risk ICP gate). The playbook gave me no way to write them into doctrine… This is load-bearing and entirely invented." — corvallis/builder-phaseA, time-cost heavy

> "the founder's own Slack instruction ('say library, not platform') is simultaneously (a) H-class provenance, (b) §5-eligible for `confirmed`, and (c) required by A5 to be `source-backed`. There are 37 of those in this wiki and they are the backbone of the four deferred doctrine files." — tessellate/builder-phaseB

Tessellate's *rebuild* independently relabeled the same content the other way — *"under SPEC §5/§7's own definition ('exec posts' qualify as H-class `confirmed`), those should be `confirmed`, not `source-backed`, and I relabeled them."* Two agents, same repo, same fixture, opposite labels on the highest-trust tier in the system.

Two adjacent gaps in the same table, each found once but each severe:

- **No label for "a human with standing, explicitly not deciding."** Corvallis's richest source was a memo headed "WORKING DRAFT… Not approved" with three dissenting reviewer comments; Halden's was stamped "DRAFT — not approved" with two unresolved CEO objections. Both agents shipped `source-backed | doc:…` on text whose author says it is not a decision, then compensated in prose invisible to any checker. > *"the strongest label in the wiki lands on text whose own author says it is not a decision."* — corvallis
- **No rule for one authority contradicting themselves over time.** > *"the founder wrote the positioning doctrine in February and said in a recorded meeting in July that 'both halves of that are wrong' — same person, same standing, five months apart… Recency says the July statement wins. §7.4 says never resolve by recency. §7.1 says H supersedes, but both sides are H."* — tessellate/builder-phaseA, time-cost heavy

**Fix:**
1. **[PLAYBOOK]** `playbooks/build.md` A5 — the doctrine row gets **four** cases, not two: (a) agent synthesis → `inferred | inference:build`; (b) human-authored document → `source-backed | doc:<file>`; (c) **a principal's ruling captured in a channel** (chat, transcript, digest reply) → `source-backed | <chat-source>:<locator>`, H-class, with the author→domain mapping recorded in `sources.md`; (d) **a self-labelled draft or explicitly-undecided statement** → `inferred` with the doc as provenance, plus an open question. Add the sentence three agents had to invent: *"provenance class is conferred per author within a channel, not per source."*
2. **[SPEC]** `spec/SPEC.md` §5 — resolve the collision explicitly. Recommended: `confirmed` means *ratified directly to the maintainer* (interview answer or digest reply); drop "exec posts" from the `confirmed` row and add a note that H-class channel rulings enter as `source-backed` with H provenance until ratified. Either resolution is acceptable; the current ambiguity is not.
3. **[SPEC]** `spec/SPEC.md` §7 — add **§7.6, H-vs-H over time**: *"A later statement from the same authority supersedes only when stated as a decision. Expressed doubt about existing doctrine goes `contested` and raises an open question; the prior decision remains binding until re-decided."*
4. **[PLAYBOOK]** `interview.md` — add one line, which Corvallis explicitly asked for: *"a stated intention to decide is not a decision — it becomes an open question, never a claim."*

---

### F4 · A6 manufactures a ratification backlog the stakeholder cannot answer, and B1 immediately tells you to undo it — **[PLAYBOOK]**

**Companies: 3/3 builders + 3/3 stakeholder reviews.** Severity: major. This is the single most-cited failure in the corpus.

`build.md` A6 line 121: "**Doctrine proposals** — every doctrine claim from A5, queued for the Phase B interview." Claim counts: Tessellate ~95 doctrine claims, Halden 216, Corvallis ~200.

> "Filing 95 entries would have produced a 700-line open-questions.md in which the 25 questions that actually need a human's judgement were outnumbered 4:1 by read-backs — and B1 immediately turns around and says to 'cap the agenda to what fits the scheduled sessions'. **The playbook asks for the thing its next step tells you to undo.**" — tessellate/builder-phaseA

> "That is not an interview, it is a deposition." — corvallis/builder-phaseA

All three batched per-file. All three stakeholders rejected the batched form too:

> "*you asked me to ratify about ninety-five claims across seven files by reading back a list of tag names. I can't ratify a tag. I don't know what's under it without opening the file.*" — tessellate stakeholder, who then **refused at question 26 of 32**

> "**Where I would actually have quit:** oq-026… If that had arrived as question 3, this session would have zero answers in it." — tessellate/stakeholder-ux-review

> "'Ratify business-core.md — 38 doctrine claims' is not something a person can say yes to. Either read me the eight claims that would embarrass us if wrong, or don't call it ratification." — corvallis/stakeholder-ux-review

> "oq-060 asks me to ratify **20 claims** in one item… As delivered I had to open `business-core.md` in another window and read 130 lines to answer one bullet." — halden/stakeholder-ux-review

Consequence in the delivered artifact: Tessellate shipped with four doctrine sections unratified and stripped (`oq-027/029/031/032`) as a direct result, and the ratification document that would unblock them *was written but never sent* because Phase B has no place to put it (see F21).

**Fix — [PLAYBOOK], `playbooks/build.md`:**
1. A6 — replace "every doctrine claim from A5" with: *"Every doctrine **file or coherent section** gets one ratification entry naming its claim count and the specific claims a consumer would act on. An individual claim gets its own entry only where it carries disproportionate risk. Individual claims are read back from the ratification sheet (B1), never enumerated as questions."*
2. A6 — split the queue in two, per the Tessellate stakeholder's own test: *"You gave three correct reasons… Then you asked me to confirm the decision you already made correctly. That's not a question, that's you seeking cover. If a decision is obvious from data I already gave you, make it, write down that you made it, and spend my attention on something you actually can't work out."* Add **decisions-I-made-and-am-recording** (a log line in the changelog + AGENTS.md deployment notes) as distinct from **decisions-only-a-human-can-make** (open questions). Quote his test verbatim as the sorting rule.
3. B1 — add a named deliverable: the **ratification sheet**. Generated from the doctrine files' claim *text*, one line per claim, grouped by file, no tags, no topic keys, a checkbox and a "wrong →" field per line. Hard rule, in bold: **never put a `^topic-key` in front of a stakeholder.** B4's "unratified" state points at a sheet line, not at an open question quoting a topic key.
4. A6 — add a target Active count. Corvallis: *"my 71 is a number I chose with zero guidance about whether 20 or 200 is right."* Recommend: ≤ 20 Active gap questions at delivery, ratifications on the sheet rather than in the queue.

---

### F5 · The interview models *what is unknown* and never *who knows it* — **[PLAYBOOK] + [SPEC]**

**Companies: 3/3 stakeholder reviews.** Severity: major. All three rated **respect for my time 4/10**, and all three named routing as the cause.

Measured misrouting: Corvallis **18 of 71** questions (11 of them asking a VP of Marketing for system logins); Halden **~11 of 68**; Tessellate credentials/URLs/conference dates interleaved with existential positioning questions.

> "**Eleven of seventy-one slots — 15% of the interview surface — spent asking an executive for logins.** This is the systemic version of the sin: it did not model *who knows what*, only *what is unknown*." — corvallis/stakeholder-ux-review

> "That's ~11 of 68 aimed at the wrong human, and the file *knows* it for most of them. Knowing and still queuing is worse than not knowing: it reads as 'we didn't have anywhere else to put this.'" — halden/stakeholder-ux-review

> "Legitimate needs, wrong container. These are two IT tickets and a URL, and they sat between 'what is our ICP' and 'may we quote a benchmark'." — tessellate/stakeholder-ux-review

Corvallis's answer to "one thing I'd change if I could change only one" is exactly this:

> "**Route the questions by respondent before you route them by importance.** Seventy-one questions is not the problem. Seventy-one questions *aimed at one person* is the problem. Twenty of these are mine. Fifteen are Margo's… Eleven are one email to Tab… Run five short conversations instead of one long one."

The schema makes it impossible to do right. §12.1's entry has `target` (which *file* the answer lands in) and no field for who owes the answer.

> "The entry schema has `target`… but no field for **who owes the answer**. interview.md mentions rerouting only as an escalation for Stale items, so a correctly-routed question looks like a stale one." — tessellate/builder-phaseB

**Fix:**
1. **[SPEC] BREAKING** — `spec/SPEC.md` §12.1: add `owed-by: <person or role>` and `kind: gap | ratification | access-request | parked-draft` as first-class fields; show both in the example block. Make `asked:` optional and show `asked: not yet` (see F14).
2. **[PLAYBOOK]** `interview.md` drip protocol: batch by **owner**, then by topic — not only by topic.
3. **[PLAYBOOK]** `build.md` B1: the agenda is built per-respondent. Access requests never appear in a stakeholder agenda; they are collected into a single one-line checklist ("docs URL, repo URL, Stripe read key owner, analytics view, sheet link") and routed to ops. Add a hard gate: *"a question whose answer is inspectable in a system, published on a public page, or derivable from the archive is not an interview question."*
4. **[PLAYBOOK]** `build.md` B1: publish a **time budget and a stop line** in the stakeholder-facing artifact. All three reviews name its absence. Tessellate's triage list existed — in `logs/phaseA-handoff.md`, a file addressed to another agent: *"I found it by accident. Put that list at the top of `open-questions.md` in the stakeholder's own words and you halve the perceived cost of this session."*

---

### F6 · Provenance is decorative: claim dates and locator fragments are wrong at 26–65% rates and no check can see it — **[SPEC] + [SCRIPT]**

**Companies: 3/3 audits.** Severity: major. This is the defect that most undermines the architecture's core promise.

> "**Systematic claim-date corruption on wave-1 Slack citations.** I decoded every cited Slack `ts` epoch against both exports. **11 of 17 cited dates are wrong**… the pricing 'drop the from' ruling is dated **eight weeks after** it was actually made… SPEC §4.2 defines the date as 'when the evidence was captured.' Lint validates date *format* only. This is invisible to every automated check in the system and is exactly the class of error the provenance layer exists to make impossible." — tessellate/AUDIT

> "That is a **26% error rate on wave-1 Slack provenance**, and lint does not catch it — its provenance check validates the file, not the fragment… `icp-personas.md:41` → `#msg-58` points at **nothing — the export has 52 messages, indices 0–51**." — corvallis/AUDIT

> "**lint verifies almost none of this**: `check_provenance` returns early for any locator without a `/`, and 35 of 37 pointers have no `/`." — halden/AUDIT

Verified in source: `scripts/lint.py:423` skips `NON_MANIFEST_PROVENANCE` entirely, and the archive check only fires on locators containing `/`. Halden's maintainer found the resulting convention drift:

> "SPEC §4.2's own example locator includes a run-id folder… but every claim tag already in this deployed wiki omits it… the *established* convention was invisible to lint, and it broke down the moment I needed to re-pull a file with the same name."

Adjacent: `doc:` provenance bypasses the archive check entirely while §17.2 demands resolution.

> "78 of my `source-backed` claims are machine-unverifiable by construction and lint cannot tell me if I invented one." — halden/builder-phaseA

And the same file gets cited two ways in one wiki: `doc:hannover-messe-2026-debrief.md` and `docs:hannover-messe-2026-debrief.md` (halden/AUDIT).

**Fix:**
1. **[SPEC] BREAKING** — `spec/SPEC.md` §4.2: require the run folder in every archive locator (`<source-id>:<run-id>/<file>#<fragment>`) so `provenance-archive` validates every citation instead of only the ones that happen to contain a slash. Update the §4.2 example, which currently teaches the date-only short form.
2. **[SPEC]** §4.2: retire `doc:` as a general prefix. Human-authored documents that are archived cite `<docs-source-id>:<run-id>/<filename>` and take H-class from the source's `provenance-class`; keep `doc:` only for genuinely un-archivable artifacts, and say so. Halden: *"That closes the largest hole in §17.2 for free."* Also rename the skeleton's `docs` source id to `stakeholder-docs` — `docs:` vs `doc:` is one letter apart and Halden's maintainer nearly conflated them.
3. **[SPEC]** §4.2: state the fragment convention and require it to be machine-checkable where the payload format allows (a JSON `ts`, a message index, a line number). Then **[SCRIPT]**: extend `provenance-archive` to resolve fragments for JSON and line-numbered payloads. Tessellate mistyped six Slack timestamps and caught them only by hand; Corvallis shipped five wrong ones.
4. **[SPEC]** §4.2: fix the date rule for undated artifacts, which three agents resolved three ways. Add: *"For an authored artifact use the artifact's own date. For an undated artifact use the tightest defensible upper bound and record the bound in the run manifest. For an undated item in a curated collection use the archive run date. Prefer a later date only when it makes the claim look staler, never fresher."*

---

### F7 · `feeds:` and `sources:` are declared independently, never reconciled, and nothing checks them — the silent gate that shipped stale prices and blocked a CEO ruling — **[SCRIPT] + [SPEC]**

**Companies: 3/3.** Severity: blocker (Halden maintainer), major (Tessellate maintainer), root cause of two ranked audit defects.

`sources.md` declares `feeds: [files]`; each file declares `sources: [ids]`. `maintain.md` Phase 3 says "Scope is hard: a source's run may touch **only the files in its `feeds:` list**." Verified: `grep -n feeds scripts/lint.py` → **no hits**. The `sources-manifest` check only verifies that ids *resolve*.

> "This was the single biggest cost of the run… at least six canonical files already carry pre-existing claims sourced from sources that sources.md's `feeds:` list for that source does *not* include — and several of those files' own front-matter `sources:` field openly lists the same source anyway. I wrote five separate pieces of new, well-evidenced content into these files before catching the mismatch… and had to revert all five." — halden/maintainer, **blocker**

> "I found three real mismatches while trying to scope my own writes… This is a silent correctness gap: a maintainer could easily miss legitimately in-scope evidence for a file because the source that should feed it doesn't declare that it does." — tessellate/maintainer, **major**

The consequences are the two most damaging content defects in the whole corpus:

> "`references/pricing.md` front matter declares `sources: [… web-competitors]`, but `sources.md`'s `web-competitors` block declares `feeds: [competitors]`. The feeds-scoping mechanism that 'keeps runs small' therefore excluded the one file that needed the update." — corvallis/AUDIT, ranked defect #5 (stale MeridianPath price left in the RFP read path)

> "The run reverted five pieces of well-evidenced content — including **a CEO ruling** — because a list in `sources.md` didn't name the target file, while in the same run *editing `sources.md` to declare a whole new source*… `partners.md` still tells a consumer agent, under a `confirmed` tag, that the certification program is 'not yet approved, no numbers to share' — eight days after it launched… **Process discipline that knowingly preserves a false `confirmed` claim is the failure mode it was supposed to prevent.**" — halden/AUDIT

**Fix:**
1. **[SCRIPT]** `scripts/lint.py` — add a `feeds-consistency` check: warn whenever a canonical file's front-matter `sources:` names an id whose `feeds:` omits that file, or vice versa. Both maintainers asked for exactly this by name.
2. **[SPEC]** `spec/SPEC.md` §10 — state which direction is authoritative. Recommended: `feeds:` is the scope gate for a *pull*, and a file's own `sources:` is authoritative for what may cite it; a maintainer that finds in-scope evidence for an out-of-`feeds` file **widens the `feeds:` list in the same run and changelogs it** rather than reverting the content. Add: *"Never leave a known-false `confirmed` claim standing on a scoping technicality. Correcting canon outranks the scope gate; the scope gate exists to keep runs small, not to freeze errors."*
3. **[PLAYBOOK]** `maintain.md` Phase 3 line 70 — replace "do not write it there" with the widen-and-changelog rule above, keeping the open question only for cases where the evidence class forbids the write.

---

### F8 · `maintain.md` Phase 1/2 has no rule for the three things that actually happened — **[PLAYBOOK]**

**Companies: 3/3 maintainers.** Severity: blocker (Corvallis), major (Tessellate, Halden).

Three distinct gaps, each hit by multiple runs:

**(a) The due-gate says nothing is due, but payloads are in hand.** All three maintain runs hit this.
> "the due-gate math says nothing is due — every touched source's `last-run` was `2026-08-19T08:00:00Z`… yet this cycle's pulls were handed to me as already-fetched. Phase 1 itself gives no signal for *when* to treat a run as interactive-override vs. apply the no-op gate literally." — halden/maintainer
> "The playbook's due-gate is written for cadence-driven pulls and doesn't say what 'due' means for a source whose access is 'a human drops a file' — is arrival of a payload itself the due signal?" — corvallis/maintainer

**(b) Byte-identical duplicate redelivery.** Two runs hit it; one calls it a blocker.
> "this cycle's entire six-file data drop turned out to be a byte-for-byte (sha256-verified, including non-reproducible fields like a Salesforce error `requestId`) duplicate of a payload already archived and fully synthesized in the immediately prior maintain run. Neither maintain.md nor SPEC.md has any provision for 'the pull returned exactly what was already processed.' … **This was the highest-stakes judgment call of the run — getting it wrong in direction (a) would have corrupted the audit trail SPEC §11 depends on.**" — corvallis/maintainer, **blocker**
> "Phase 2's 'no reasoning over content until Phase 3' rule reads, on a literal pass, like it might forbid even that hash check — the playbook never says a byte-identity comparison against an existing archive is compatible with fetch/synthesis separation." — tessellate/maintainer

The handling was excellent in both cases — the audits single it out as the best judgment in the corpus — but it was entirely invented, and the two agents chose *different* answers (Corvallis: manifest-only cross-reference, no second payload copy; Tessellate: archived all six anyway into a new run folder). Divergence = missing spec.

**(c) A successful pull that doesn't extend past the marker.**
> "the fetch *succeeded*, but the returned window doesn't reach back to the prior cursor marker (slack-internal's export starts 2026-08-14, but the marker was 2026-08-05, leaving 08-06–08-13 uncovered by any pull)… Step 4's 'never advance past content that failed to archive' reads naturally as being about failures, not gaps in an otherwise-successful pull." — tessellate/maintainer

**(d) "Now" is undefined.** Corvallis minted a run-id one day ahead of the real clock and had to rename five archive folders and fix every date in `changelog.md` and `open-questions.md` after `claim-hygiene` caught a future date.

**Fix — [PLAYBOOK], `playbooks/maintain.md`:**
1. Phase 1, new step 0: *"Establish `now` from the real system clock (`date -u`) before minting a run-id. Never mint a claim date or run-id ahead of it, whatever the wiki's internal narrative clock says."*
2. Phase 1 step 2, add a third branch: *"A source is also due when payloads for it are already staged — handed to you, or sitting in `intake/inbox/` — regardless of cadence math. For `access: manual` sources, delivery **is** the due signal; cadence is the expected/escalation frequency, not a processing gate."*
3. Phase 2, before step 3: *"**Duplicate-delivery check.** A sha256 comparison against `.archive/` is mechanical, not semantic, and is explicitly compatible with fetch/synthesis separation. If a delivered payload is byte-identical to an already-archived, already-synthesized payload: record a duplicate-delivery note in a manifest-only entry, do **not** create a second payload copy (a second copy misrepresents the audit trail as two independent fetch events), leave the cursor untouched, resynthesize nothing, and open a question about the upstream delivery pipeline."*
4. Phase 2 step 4, add: *"If the archived payload does not extend past the existing marker, leave the cursor untouched entirely — advancing `last-run` without new coverage falsely shortens the apparent gap. If the returned window does not reach back to the prior marker, advance to the end of what was archived and record the residual gap in the source's `notes:` — never treat a gap as evidence the period was quiet."*
5. Phase 2 step 1, add a source-mapping rule (both Corvallis and Halden guessed): *"Map a delivered file to a source id by declared filename pattern or inbox subfolder. A new source id is warranted when the `access` description would have to change to cover the asset (different URL, endpoint, collector, or trust class); the same asset re-fetched stays under the existing id."* And **[SPEC]** `spec/SPEC.md` §10: let each manual source declare a `filename-pattern:` or dedicated `intake/inbox/<source-id>/` subfolder so Phase 2 mapping is mechanical.
6. Phase 1 "Inputs" (line 7) — add `playbooks/interview.md`. Phase 6 step 2 depends on it and Tessellate's run shipped a materially weaker digest because it wasn't supplied: *"`scripts/digest.py` has its own fallback (top-3 Active questions in file order, no draft answers), which is what actually shipped — a materially weaker digest than the playbook describes as the point of the exercise."*
7. **[SPEC]** §10 — add `status: pending-access` (or `broken: {…, kind: never-connected}`). Halden: *"Marking `web-own` and `analytics-web` broken is technically correct per A4 step 4 but semantically wrong — nothing is failing, they were never wired up. It also poisons the digest signal: '2 broken sources' reads as an outage when it is an onboarding gap."*

---

### F9 · `digest.py` cannot produce the digest the playbook specifies, and the numbers that reach the human are fabricated — **[SCRIPT] + [PLAYBOOK]**

**Companies: 3/3.** Severity: major. Two of three audits find the human-facing numbers wrong by ~2×.

`build.md` B6.4 specifies "claim counts by label (confirmed / source-backed / inferred / watchlist / contested)". `digest.py` reads only `changelog.md` and `open-questions.md` — it cannot count claims, and its bucket classifier is `("contested", re.compile(r"contested", re.IGNORECASE))` (verified, `scripts/digest.py:65`) applied to changelog bullets.

> "Its 'New contested entries' section is a keyword match on the word 'contested' and returned six false positives, including my own changelog line stating that contested entries are now **zero**… Its output is 70+ lines of file paths, topic keys, tag counts and lint results — i.e. exactly the mechanics build.md says the stakeholder never sees, and four times the length this stakeholder said he will read." — tessellate/builder-phaseB

> "my lint summary and my §17.3 conformance line both got filed under '**New contested entries**', and it printed the *previous* run's escalations alongside the current ones with no way to tell which was live. It also cannot produce claim counts, because those live in the files, not the changelog." — halden/builder-phaseB

Because the counts are hand-made, they are wrong:

> "`changelog.md:56`: 'Claim census: **208** tagged claims — **136** confirmed…' `delivery-digest-2026-08-19.md:11`: '**215** statements now rest on your word… **125**… **26**… **20**.' That totals **386** against a census of 208, and every category disagrees… My own post-wave-2 census is 233 tagged. **In a wiki whose founding lesson is 'three documents produced three different numbers because nobody wrote down a definition,' the one artifact the founder actually reads invents its numbers.**" — tessellate/AUDIT

> "**Three artifacts from one run report three mutually inconsistent inventories, and the one sent to the human is inflated roughly 2× across every row.**" — halden/AUDIT

Also a direct contradiction inside the playbooks: B6.4 requires claim counts by label in the digest, while `interview.md` principle 7 and `build.md`'s "Who you work with" both say the stakeholder never sees claim labels.

**Fix:**
1. **[SCRIPT]** `scripts/digest.py` — teach it to count claim tags by label from the files (the parser already exists in `wikilib`), and make it the *only* source of those numbers. A hand-written census in a changelog or digest is now a lint-visible discrepancy.
2. **[SCRIPT]** fix the bucket classifier to parse structure, not keywords: read `## Contested` sections in the wiki for contested counts; take the **newest** `escalations:` line only.
3. **[SCRIPT]** add `--audience=stakeholder`: strips file paths, topic keys, and label names; enforces a length budget. Otherwise rename the current output `render_changelog.py` and have B6.4 say plainly that the walkthrough digest is written by hand from it. Do not leave B6.4 reading as though the script produces the deliverable — both Phase B builders read it that way and both hand-wrote the digest anyway.
4. **[PLAYBOOK]** `build.md` B6.4 — rewrite the counts bullet as *"how much of the wiki now rests on the stakeholder vs. on documents vs. on inference — in words, not labels"*, plus a length budget the recipient's own stated preference overrides. Add: report `inferred` counts **by file**, not just in total — Tessellate: *"Right now '26 inferred' is invisible until someone opens the files."*
5. **[PLAYBOOK]** `maintain.md` Phase 6 / **[TAXONOMY]** `AGENTS.md` deployment notes — track `last-digest-sent` as an explicit field. Halden's maintainer had to infer digest-due-ness by "eyeballing changelog prose"; Tessellate's had to guess whether a named weekday is a hard gate or a target.

---

### F10 · One manual source, or one per underlying system? — **[SPEC] + [PLAYBOOK]**

**Companies: 3/3 (plus both rebuild runs, independently).** Severity: major.

SPEC §3: a zero-integration wiki "lists a single manual source (`intake/inbox/`)". `build.md` A3: "machine exports delivered by hand (a CRM CSV) are S-class under the manual source's id." A2's own worked table, three paragraphs earlier, walks CRM exports, call deliveries, and doc drops through as separate source blocks with their own `feeds`/`cadence`/`provenance-class`.

> "read literally, this collapses the entire manifest… Literal compliance puts every one of them under `intake-inbox`, which destroys the four things the manifest exists to carry: per-system `feeds` scoping (SPEC §10 says `feeds` is what keeps runs small), per-system `cadence`, per-system `provenance-class`, and per-system cursors." — corvallis/builder-phaseA

> "Collapsing those into `intake-inbox` would give every claim in the wiki the same provenance id and the same trust class, destroying the entire point of §7." — tessellate/builder-phaseA

Corvallis's *rebuild*, run fresh without reading the prior resolution, landed on the same 13-source answer — *"which is reassuring evidence it's a real ambiguity in the text rather than a one-off misreading."* Every agent deviated; every agent documented the deviation; nothing sanctions it. Counts chosen: 12 (Tessellate), 13 (Corvallis ×2), 10 then 7 (Halden Phase A vs. rebuild) — so even the *granularity* diverged.

**Fix:**
1. **[PLAYBOOK]** `build.md` A3 — rewrite the provenance sentence: *"A hand-delivered export still belongs to **its own system's** source id — declare `crm`, `slack`, etc. with `access: "manual: …"`. Use `intake-inbox` only for material with no identifiable upstream system, and keep it declared as the standing delivery channel with a routing receipt in its run manifest."*
2. **[PLAYBOOK]** `build.md` A3 — show the **demultiplex pattern** once, as a worked example: one drop → N sources, payloads archived under each system's id, `intake-inbox`'s run manifest holding the routing map. Every run invented this; Tessellate noted `.archive/intake-inbox/<run>/` then contains a manifest and no payloads, "which the spec never contemplates."
3. **[SPEC]** §3 — soften "lists a single manual source" to "lists one manual source per underlying system, all with manual access, plus `intake/inbox/` as the delivery channel." Also state the granularity rule: one source per (system × provenance class).

---

### F11 · The runbook tier has no vocabulary for "no access exists," which is the state of every runbook file in every deployment tested — **[SPEC] + [PLAYBOOK] + [TAXONOMY]**

**Companies: 3/3.** Severity: major in aggregate (minor per-log, but it renders 3 of 18 canonical files inert in all three deployments).

`build.md` A5's runbook row: "No access yet → entry stays drafted, flagged unverified, open question filed." `verified: <date>` has a defined shape; **broken** has a defined shape; "flagged unverified" is a phrase.

> "This mattered a lot here: *every* runbook entry in this wiki is unexecutable, because the deployment has zero agent-reachable systems. Three files (`metrics.md`, `crm.md`, `gtm-tools.md`) are 100% unverified." — corvallis/builder-phaseA

> "lint's `runbook-decay` check keys on `verified:` stamps — so a file with *no* stamps is indistinguishable from a file that was never meant to have any… **Right now a wiki with zero verified runbook entries passes lint silently.**" — halden/builder-phaseA

The audits agree it produced pure ceremony:

> "**`crm.md` + `metrics.md` + `gtm-tools.md` — 137 lines of runbook whose honest content is 'we have no access.'** … three canonical files exist because the taxonomy has three slots, not because there are three things to say. One 'systems we cannot reach, and who to ask' page would carry the same information." — halden/AUDIT

> "Three of eighteen files are aspirational; the taxonomy has no shape for 'runbook, unprovisioned.' At this deployment they should be one page." — corvallis/AUDIT

One agent found and named the high-value third option nobody had sanctioned:

> "I invented a third category — verification *against the archive*. I ran the exclusion rule over the archived customer CSV and it reproduced Stripe's MRR, seat count and team count exactly (and demonstrated that the naive sum returns $1,011,947 because of an undeleted test row). That is a genuine execution result with a genuine `verified:` stamp, and it is the single most useful thing in the wiki, but the playbook does not contemplate it." — tessellate/builder-phaseA, flagged *"trivial (and high value — worth promoting, not just permitting)"*

**Fix:**
1. **[SPEC]** `spec/SPEC.md` §8 footnote ³ — define the third runbook state alongside `verified:` and **broken**: `unverified: {since: <date>, reason: no-access, question: oq-NNN}`. **[SCRIPT]** then have `runbook-decay` count unverified entries and escalate them, so a zero-verified wiki stops passing silently.
2. **[SPEC]** §8 footnote ³ / **[PLAYBOOK]** `build.md` A5 — add **verified-against-archive** as a first-class execution result: *"Where live access is absent, a query executed against the archived payload counts as verified; stamp it `verified: <date> (against archive)` and name the payload."* Promote this, don't merely permit it.
3. **[PLAYBOOK]** `maintain.md` and `build.md` — state plainly that `broken` is **never** a claim-tag label. Halden's maintainer wrote `[broken | crm:… | 2026-08-18]` and caught it only by reading `wikilib.CONFIDENCE_LABELS`: *"nothing states plainly that `broken` must never appear inside a `[label | provenance | date]` tag."* Add a worked example of a runbook execution-failure entry to §8, the way §4.3 gets one for contested.
4. **[TAXONOMY]** `spec/taxonomy.md` — add a deployment note under the runbook section: *"A deployment with no agent-reachable systems collapses `metrics.md`, `crm.md`, and `gtm-tools.md` into a single `gtm-tools.md` section set: what systems exist, who owns them, what marketing needs from each, and who to ask for access. Record the collapse in `AGENTS.md`."* See §5 and §3 below.

---

### F12 · `last-verified` for unratified doctrine works only by accident — **[SPEC] + [PLAYBOOK]**

**Companies: 3/3.** Severity: minor each, but all three flag it as a latent break of every doctrine file in every wiki.

`build.md` A5 (line 110) says doctrine drafts "carry the drafting date" — but the Phase A logs were written against wording that said "left unset until ratification," and `REQUIRED_FIELDS` (verified, `wikilib.py:59`) includes `last-verified`, so omitting the key errors and any non-date value fails the date parser.

> "The only construction that satisfies both is `last-verified:` with an empty value, which happens to parse to `""` and happens to short-circuit the staleness check. Nothing documents that this is the intended encoding." — tessellate/builder-phaseA

> "That is an accident of implementation, not a stated contract, and the next lint refactor could break every doctrine file in every wiki." — halden/builder-phaseA

**Fix:** **[SPEC]** `spec/SPEC.md` §4.1 — state the encoding: *"`last-verified:` may carry an empty value, which is the documented representation of 'never confirmed by a human or an execution check.' Unset is written as an empty value, never as an absent key."* **[SCRIPT]** add a lint test pinning the behaviour so a refactor cannot silently break it.

Same shape, same file, adjacent: `generated: {by:…, at:…}` is documented "machine-stamped, never hand-edited" and **nothing stamps it**. Corvallis hand-wrote it on 25 files; its audit calls it *"provenance theater with no reader and no enforcement."* Either drop the "never hand-edited" claim or have `sync_manifest.py` own the field. Same for `tags: []` — *"nothing reads it: not lint, not `sync_manifest.py`, not the consumer contract. It is pure ceremony until something consumes it."*

---

### F13 · The archive path, the run-id format, and §4.2's own example disagree three ways — **[SPEC]**

**Companies: 3/3.** Severity: minor, trivial to fix, and it corrupts locators permanently once chosen.

- SPEC §10 (line 252): inbox files "are archived to `.archive/inbox/<run-id>/`". SPEC §11 and A3: `.archive/<source-id>/<run-id>/`. The skeleton's source id is `intake-inbox`. > *"following §10 literally produces provenance that lint cannot resolve."* — corvallis
- SPEC §11 (line 267): "`run-id` is an ISO-8601 timestamp" — which contains colons. SPEC §4.2's own example locator is `slack-gtm:2026-08-12/dump.json#msg-4411`, a bare date. Three agents chose three formats: `2026-08-19T0900Z`, `2026-08-19`, `2026-08-19T1015Z`. > *"Not strictly valid ISO-8601 (you may not mix extended and basic), so I broke the spec letter to keep the filesystem sane."* — halden

**Fix:** **[SPEC]** §10 → `.archive/<inbox-source-id>/<run-id>/`. §11 → prescribe exactly `YYYY-MM-DDTHHMMZ`. §4.2 → update the example to match §11.

---

### F14 · `open-questions.md`'s schema cannot express the states Phase A and real answers produce — **[SPEC]**

**Companies: 3/3 (`asked:`), 2/3 (id convention), 1/3 each for the rest.** Severity: minor each; collectively the schema fails on most real entries.

- **`asked:` has no "never".** §12.1's example is `asked: 2026-08-12 (digest) — awaiting answer`. Every Phase A question has by definition never been asked. Corvallis wrote `asked: not yet — queued for the Phase B build interview` on all 71; Halden on all 68. > *"The build playbook creates the entire initial backlog in this state, so it is the common case, not the exception."*
- **"Answered" is binary; real answers are partial.** > *"five questions got a genuine ruling plus outstanding execution — docs access approved but not wired, the attribution fix ruled but unscheduled… Moving them to Answered hides real outstanding work; leaving them Active with no visible answer invites re-asking a question he has already answered, which is the exact thing he opened the session complaining about."* — tessellate/builder-phaseB (invented `answer so far:` + `what is still needed:`)
- **No `parked-draft` field.** B4 says removed doctrine text is "preserved inside the corresponding open question" — impossible when ratifications were batched and the batch question is Answered. > *"I had to open **three new questions** purely as parking spaces for removed draft text, which inflates the Active count with items that are not really questions for a human — two of them I recommend rejecting."* — halden/builder-phaseB
- **No `delegated` disposition.** > *"the stakeholder was asked about two and explicitly refused to own them — 'those are your filing decisions… if I invent one I'll be wrong in a way you'll then treat as authority'… B3 has no slot for 'the stakeholder delegated this back to you'. Two of those Answered entries therefore contain no claim tag at all, which is a shape the §12.1 schema does not anticipate."* — halden/builder-phaseB
- **File order undefined.** §12.2 says ids are sequential; A6 and B1 say `why-it-matters` is the sort key. Nothing says which orders the file.
- **`oq-NNN` vs. slugs.** Halden's maintainer used descriptive slugs throughout (nothing in `wikilib` requires numerics); the embedded consumer contract instructs consumers to append `oq-NNN`, *"guaranteeing a mixed-convention file the first time a consumer files one"* (halden/AUDIT). Halden's consumer independently flagged it. Corvallis's maintainer had to grep the whole file to find the next free id.

**Fix — [SPEC] `spec/SPEC.md` §12.1/§12.2, BREAKING:**
1. Add to the entry schema: `owed-by:` (F5), `kind: gap | ratification | access-request | parked-draft`, `parked-draft:` (verbatim removed text), and states `Partially answered` and `Delegated`. Show `asked: not yet` in the example block.
2. State the file order explicitly: **priority (`why-it-matters`), not id**; ids are allocation-order only.
3. Relax the id convention to "any stable kebab-case id; sequential numeric (`oq-NNN`) is one valid form" **and** make `consumer/AGENTS.md` §5 say "match the file's existing id convention" instead of "next sequential id." **[SCRIPT]** add `lint.py --next-id` so nobody greps.

---

### F15 · Claim tags cannot live in markdown tables, and the taxonomy prescribes tables — **[SPEC] + [SCRIPT]**

**Companies: 3/3.** Severity: major (Tessellate: ~25 of 340 tags affected), minor elsewhere.

Verified: `CLAIM_CANDIDATE_RE = re.compile(r"\[([^\[\]\n]*\|[^\[\]\n]*)\]")` and `lint.py:385` splits on raw `|`. Backslash-escaping to protect the table puts the backslash inside the label.

> "Lint's `CLAIM_CANDIDATE_RE` splits on raw `|`, so the backslashes land inside the label and provenance and it reports a malformed claim. The failure is not obvious from the message, and tables are a natural place to want tagged claims (competitor comparisons, distributor tables, field-trust tables)." — halden/builder-phaseA

> "The only workable pattern is one tag on its own line *after* the table, which (a) attaches one tag to what §4.2 says should be N claims, and (b) detaches the provenance from the specific row it supports… **Roughly 25 of my 340 tags cover multi-row tables, so the true claim count is higher than the tag count and an auditor resolving provenance row-by-row cannot.**" — tessellate/builder-phaseA

**Fix:** **[SPEC]** §4.2 — define the table convention: either a trailing `provenance` column holding a bare `<source-id>:<locator>` (no brackets, no pipes) with one date column, or an explicit sanction for a table-level tag plus the statement that the table counts as one claim. **[SCRIPT]** `lint.py` — strip `\|` before splitting, and skip lines that are table rows (start and end with `|`) unless they contain a bracketed tag, so ordinary prose containing brackets-plus-pipes stops false-firing.

---

### F16 · Phase A generates deployment-note content with nowhere to put it — **[PLAYBOOK]**

**Companies: 3/3.** Severity: minor, but it is the record most at risk of being lost.

A5 says a file that doesn't apply "is omitted and the omission recorded for `AGENTS.md` deployment notes"; the same table says "`AGENTS.md` waits for Phase B."

> "So the record has no home during Phase A, and the fact most at risk of being lost (why three canonical files are missing) is the one with no place to be written down." — tessellate/builder-phaseA

Corvallis invented **four** locations (the file itself, changelog, an HTML comment in AGENTS.md, open questions). Halden used two. Divergence again.

Two adjacent Phase A record-keeping gaps, each found once:
- **Section-level omission.** > *"Nothing covers a *section* that cannot be drafted — and I had six… A7 forbids 'a bare heading with no trail', which is right, but the alternatives are unclear."* — halden
- **What the dump did *not* contain.** > *"four of A3's seven asks were simply absent — no brand/voice guideline, no pricing sheet or discount policy, no existing battlecard, no churn post-mortem. That absence shaped `voice.md`… more than anything that *was* delivered. A3 lists what to ask for but says nothing about recording what didn't arrive. **The gap list is more informative than the delivery list and it is currently optional.**"* — halden

**Fix — [PLAYBOOK] `playbooks/build.md`:**
1. A5 — *"Record omissions, section-level omissions, and local taxonomy changes in the `build:draft` changelog entry and as open questions. B5 reads the changelog when generating deployment notes. The deployment-notes 'omitted files' row may be written in A5; only the three-sentence summary waits for ratification."*
2. A5 — *"A taxonomy section you cannot draft keeps its heading and carries a tagged absence claim plus an open question. Never delete a taxonomy section."* (Halden's own wording is the model: *"its emptiness is a finding, not a clearance."*)
3. New A3.2 — *"Record which asks were not delivered. Each missing ask becomes an open question against the file it would have fed."*

---

### F17 · Consumers cannot resolve "the primary persona" or "the flagship claim" because no file declares either — **[TAXONOMY]**

**Companies: 2/3 consumer runs** (Tessellate's consumer refused both tasks on other grounds and so never reached it). Severity: major (Halden), minor ×2 (Corvallis).

> "`icp-personas.md` defines two personas… but never labels either as primary/secondary, and nothing in the read-order table for content creation resolves it either… Inferred 'primary' = plant reliability engineer by cross-referencing a different file — `channel-styles.md`'s LinkedIn section is engineer-authored by convention. **Had the channel been web or the catalog instead of LinkedIn, I'd have had no cross-file signal at all and would have been guessing blind.**" — halden/consumer, **major**

> "`icp-personas.md` never labels any persona 'primary' — the closest thing is a passing phrase, 'the decider in the primary ICP'… There's a real, unresolved argument that the practice administrator persona is at least as relevant." — corvallis/consumer

> "No file ranks Halden's approved claims or capabilities by importance — `business-core.md`'s six approved claims are a flat numbered list with no priority marker." — halden/consumer

**Fix — [TAXONOMY] `spec/taxonomy.md`:**
1. `icp-personas.md ## Personas` — require a `primary: true` marker on exactly one persona, or a per-channel default mapping. Add `## Channel personas` (see §5).
2. `business-core.md ## Approved claims` — require a **lead claim** pointer: which of the approved claims is the headline for a capability-announcement asset.
3. **[PLAYBOOK]** `interview.md` `business-core.md` bucket — add both to the question bank ("Which of these claims leads?" / "Which persona does a channel default to?").

---

### F18 · Nothing propagates a correction, and nothing catches a stale duplicate of a corrected fact — **[PLAYBOOK] + [SCRIPT]**

**Companies: 2/3 builders + 2/3 audits.** Severity: major. This produced the top-ranked content defects in two audits.

> "a single answer (the 12% renewal commission) had to land in `partners.md`, `compliance-guardrails.md`, `growth.md`, `business-core.md`, `icp-personas.md` and `references/persona-distributor-rep.md`, plus the open-questions `applied-to` list. There is no index from a topic to the places it is asserted, so finding them means grepping and hoping… the killed 'two thousand vibration specialists' sentence survived in two persona files after I fixed it in `business-core.md`, and only a manual grep found it. **lint only catches broken *links*, not stale *content*.**" — halden/builder-phaseB, time-cost heavy

> "`open-questions.md#oq-079` states `target: … **references/pricing.md** …`. The flag reached `business-core.md` and the battlecard. It never reached `references/pricing.md`… **Two self-identified propagation targets, zero writes.** Net effect: an agent following `AGENTS.md`'s own RFP routing picks up a 60-day credit window that VP Finance changed to 90 and a MeridianPath price that is one reprice stale, neither flagged in the file it reads." — corvallis/AUDIT, ranked defect #3

> "**the wiki is better at recording what it knows than at propagating what it has just learned.**" — corvallis/AUDIT

**Fix:**
1. **[PLAYBOOK]** `build.md` B3 and `maintain.md` Phase 3, new sub-step: *"For every correction, grep the wiki — including `references/` — for both the corrected value **and** the phrase being replaced. List every file touched in the changelog. A correction applied in one file and not another is worse than no correction."*
2. **[PLAYBOOK]** `build.md` B4 / `maintain.md` Phase 3: *"An open question's `target:` list is a write obligation. Before closing the edit, verify the flag or the change reached every named target."*
3. **[SCRIPT]** `scripts/lint.py` — add a `stale-target` check: for every Active open question naming targets, warn if a named target file contains no reference to that `oq-` id. Cheap, and it catches both audit defects above.

---

### F19 · B2's mandatory close-out is unmeetable, and the build has no defined-done without it — **[PLAYBOOK]**

**Companies: 2/3** (Halden Phase B, Corvallis rebuild — Halden's rebuild hit it too). Severity: major.

`build.md` B2 line 155: "Close the final session by ratifying the three-sentence company summary for `AGENTS.md`, verbatim." B5 treats that as an input, and the "What done means" table lists it as a build gate.

> "The actual transcript ends with 'send me the guardrails file and the positioning paragraph when they're updated. The rest I'll skim' and a request to keep it short — no summary read-back, no cadence. So B5's step 1 had no input and the build's definition of done was unmeetable through no fault of the work." — halden/builder-phaseB

> "'You haven't drafted it, so I can't ratify it. Draft it from [the positioning sentence] and send it to me and Margo by email. That's a five-minute review over coffee, not an interview item.'" — corvallis rebuild

**Fix — [PLAYBOOK] `playbooks/build.md`:** B5 step 1 → *"If the session did not reach the read-back, generate the summary from ratified claims only, mark it unratified in-file, and file it as the first drip question."* Remove verbatim ratification from the conformance gate in "What done means" — it is a first-cycle deliverable, not a build gate. Also add to B2: *"Ask for the digest recipient and cadence explicitly; if the stakeholder overrides the drip batch size, their stated capacity wins in either direction — record the override in deployment notes."* (Halden's stakeholder said "send me five at a time by email. I'll answer five. I will not answer forty" against `interview.md`'s "2–3 questions per digest cycle. **Never more**".)

---

### F20 · Two mechanical rules exist only inside `wikilib.py` — **[SPEC]**

**Companies: 2/3.** Severity: minor, high recurrence per run.

- **`^topic-key` must be the last token on its line.** Verified: `BLOCK_ANCHOR_RE = re.compile(r"\^([A-Za-z0-9-]+)\s*$")`. > *"Writing a longer paragraph in the natural style this wiki's doctrine files use… silently produces an anchor that doesn't exist as a link target. I did this ~14 times across 6 files in one drafting pass. The failure surfaces as a `broken-link` warning in a *different* file three hops away."* — corvallis rebuild. Halden's maintainer found the deployed wiki's own house style violates it.
- **One date, one provenance pointer, lowercase GitHub-style anchors.** > *"I only discovered these by having lint reject ~185 lines across a dozen files after a full drafting pass, then bulk-fixing with a script."* — halden rebuild

**Fix:** **[SPEC]** §4.2 — state all four constraints with a wrong-vs-right example: the anchor ends its line; exactly one date per tag (no ranges, no quarters, no month-only); exactly one provenance pointer per tag; heading anchors are lowercase slugs. **[SCRIPT]** add an `anchor-mid-line` finding that fires at the mistake's own location rather than three hops away as a broken link.

---

### F21 · Delivered artefacts have no home, and the anchor-rename problem has no procedure — **[SPEC]**

**Companies: 1/3 each,** but both are structural and both produced real losses.

> "Phase B produces two things for a human — the walkthrough digest and (here) the ratification sheet. Neither has a defined location, retention rule, or relationship to the wiki. Putting them in the wiki breaks the orphan check and pollutes canon with non-claims; keeping them outside means the next run cannot see what the stakeholder was last sent, which matters directly for the drip loop ('the questions you sent last cycle')." — tessellate/builder-phaseB

Consequence: Tessellate's ratification sheet *"was written but never sent"* (its own audit), leaving four doctrine sections permanently stripped.

> "`^enterprise-tier-unresolved` became actively false… Keeping the key would leave a lie in the anchor namespace; renaming it breaks every inbound reference… **lint reports missing anchors as warnings, not errors — so a shipped rename with stale inbound links passes.**" — tessellate/builder-phaseB

**Fix:** **[SPEC]** §3 — add `outbox/` (or `deliveries/`) to the anatomy, exempt from orphan and front-matter checks, holding every artefact sent to a human with its date. The drip protocol's "re-ask once, rephrased smaller" is unimplementable without it. **[SPEC]** §4.2 — add a rename rule: *"A topic key is renameable when the claim's meaning changes; the rename is a changelog event and inbound references are updated in the same commit."* **[SCRIPT]** promote missing-anchor from warning to **error** for links between wiki files.

---

### F22 · One-off but high-severity gaps worth naming individually

| # | Gap | Company | Fix |
|---|---|---|---|
| a | **No `blocked` / drafting-freeze convention.** Three constraints in Corvallis's sources were neither prohibitions nor doctrine nor questions but *drafting freezes*: "do not build the partner one-pager, flag it as blocked on Margo." > *"If an agent reads `partners.md` and sees a rich partner motion, the single most important fact — that it may not write a word of partner collateral today — has to be carried by prose emphasis and hope."* | Corvallis (**major**) | **[SPEC]** add a `blocked` section marker with owner + unblocking condition; **[PLAYBOOK]** add "what is marketing currently forbidden from producing?" to `interview.md`'s `compliance-guardrails.md` bucket |
| b | **No marker for commercially restricted content.** §15 covers secrets and PII, nothing else. Halden's interview produced three blocks of figures with handling instructions ("don't attribute the decimals to me in public", NDA'd OEM revenue). > *"I used HTML comments plus prose markers… Nothing enforces it: a consumer agent that ignores the comment reads a price list."* | Halden (**major**) | **[SPEC]** §4.2 — optional `!internal` flag in the tag: `[confirmed \| interview:theo-brandt \| 2026-08-19 !internal]`; **[SCRIPT]** assert any file containing one carries a read-restriction line in front matter; **[CONTRACT]** consumer must never externalize an `!internal` claim |
| c | **No "relayed H-class" concept.** > *"'anything about price, the wordmark, the catalog cover or the channel agreements, I can tell you what it *is*, but Margit signs it. Don't write "confirmed by Theo" on something only she can decide'"* — a human authoritative to *report* but not to *decide*. Halden's audit then found the exact predicted failure: three of Margit's non-negotiables are tagged `interview:theo-brandt`. | Halden (**major**) | **[SPEC]** §7 — one paragraph: label `confirmed`, provenance `interview:<relayer>`, and **require the claim to name the deciding authority** when the subject is a decision; `interview.md` principle 5 points at it |
| d | **§7.4 has no carve-out when the human *is* the cause of the system's error.** The founder spent $2,043 on ads and told nobody; the board deck and Slack both say "zero paid spend, ever." > *"Filing it as contested would have told every consumer agent that whether the company has ever run ads is an open dispute."* | Tessellate (**major**) | **[SPEC]** §7.4 — *"Where the H witness is the author or cause of the S-class record, this is not a collision but a supersession with a data-repair task attached: write the claim, name both false records inside it, and file a correct-at-source question."* |
| e | **No provenance class for partner/channel-reported data** — Halden's distributor POS report is its only system of record for 70% of revenue, is the partner's own publication (A), functions as Halden's system (S), and is unauditable. | Halden (**major**) | **[SPEC]** §7 — add the line: A-class about the partner's own activity, never silently superseding; S-equivalent for the org's own reporting only where the org can audit it. *"Any channel business will hit this on day one."* |
| f | **B1 has no cursor-refresh step, so a stale cursor manufactures interview questions.** The Tessellate stakeholder's opening remark: > *"some of what you're about to ask me I already answered in writing five days ago, and in the one place your own notes say I always answer things. That means questions 1 and 2 are stale, not open."* Cost: the first fifteen minutes of the session. `interview.md`'s drip protocol carries the discipline note; the live-session path does not. | Tessellate (**major**) | **[PLAYBOOK]** `build.md` B1 — *"Refresh every source that feeds an agenda item, or record the window gap on the agenda item itself. A coverage gap over the most recent window escalates as an interview-blocking risk, not a manifest footnote."* **[SPEC]** §10 — add a `decision-channel: true` flag so the manifest can name where a stakeholder makes decisions |
| g | **Hedged answers have no disposition table.** Ten hedges in one transcript, split three ways with no guidance: confirmed absence ("no IMTS debrief exists" from the person who'd own it), a numeric guess ("somewhere in the low forties, and my check would be a guess"), and hearsay about someone else's domain. | Halden (**major**) | **[PLAYBOOK]** `interview.md` principle 4 — add a hedge-type table: *absence-of-thing-I-own → `confirmed` absence; numeric estimate → record the not-knowing, quote the estimate as a guess, keep the question Active; hearsay about another domain → `watchlist \| interview:<person>` with a reroute* |
| h | **No mode for applying a session you didn't run.** Both Phase B runs received a transcript. B1 became dead weight; principle 4's read-back is unverifiable; falsifiers could not be asked. One transcript also spanned two calendar days, the second in the future, which `claim-hygiene` rejects. | Tessellate, Halden ×2 | **[PLAYBOOK]** `build.md` Phase B header — *"If the session already happened and you are applying a transcript, start at B3."* **[PLAYBOOK]** `interview.md` — a short "applying a session you didn't run" note: what a transcript can and cannot ratify, how to record a falsifier never asked, and *"stamp claims with the date of the sitting in which the answer was given; where the transcript does not delimit sittings, use the first sitting's date and record the ambiguity. Never use a date ahead of the environment's current date."* |
| i | **Anchor granularity undercuts citation exactly where it matters — numbers.** > *"`business-core.md`'s 'Sales motion facts' anchors `^motion-cycle-length` to the *cycle-start-event definition* sentence, not to the paragraph immediately after it that actually carries the 287/261/14-month figures I needed."* Corvallis's audit made it defect #10: *"the most-cited topic key in the wiki anchors an untagged sentence"* while the tagged figure beside it has no key. Found by the consumer, not the maintainer. | Corvallis (**major**) | **[SCRIPT]** add an `anchor-claim-pairing` check: warn when a `^topic-key` is not on or adjacent to a claim tag, and when N actionable statements share one tag (Corvallis's `growth.md` campaign frames 2–4). **[CONTRACT]** explicitly sanction citing by heading when no key fits |
| j | **Reference consent is a per-quote prose note that doesn't propagate.** `voice.md` marks quotes from one transcript unquotable; `icp-personas.md#customer-language` quotes other lines from the *same* transcript without the flag. > *"a reader who trusts the file to flag anything unsafe could reasonably quote them externally."* | Corvallis (**major**) | **[SPEC]** §10 — add `consent: none | internal-only | approved: <doc>` as a source-level field that every file quoting that source-id inherits. Checked once, not repeated per quote per file |
| k | **Privacy asymmetry nobody specified.** > *"Pseudonymous community members get stronger protection than identified humans at identified companies… **Piotr Weselak** (named individual at a named churned customer) appears five times attached to verbatim quotes, three of them in the `## Customer language` section of a *doctrine* file that the read-order routes every content task through."* | Tessellate/AUDIT | **[SPEC]** §15.5 — extend PII minimization to verbatim quotes: named individuals at named accounts are attributed by role, never by name, unless a consent record exists |
| l | **§11's `manifest.yaml` schema is five words long.** > *"'fetched-at, window or cursor used, query, item counts, warnings' is the whole schema… I invented `access-used`, `cursor-before`/`cursor-after`, `status`, `error`, `provenance-rules`, `payloads`, `demultiplex-map`, `staleness-at-run`, `window-deviation`, and `derived-figures-recorded-here-for-audit`… Two builders will produce two incompatible manifest shapes, which defeats 'everything the eval needs exists on disk.'"* Confirmed by Tessellate's maintainer reverse-engineering field names from example files. Corvallis's audit found a manufactured `fetched-at`. | Halden, Tessellate | Ship `templates/wiki-skeleton/.archive/manifest.template.yaml` with `cursor-before`/`cursor-after`, `status`, `window-deviation`, and a `derived-figures:` block. **[SPEC]** §11 — point at it |
| m | **`secrets` check vs. `§11` archive mandate.** Tessellate's audit: the partially-redacted Stripe key *"**does** survive verbatim in `.archive/…/BROKEN-stripe-mrr-export.txt`… because SPEC §11 mandates archiving raw payloads before synthesis. §15.3 tells lint to grep for key formats, §11 tells the run to write them to disk inside the wiki tree, and nothing says the archive should be redacted or excluded from the secret sweep."* The stakeholder's #1 abandon trigger: *"If I ever see a Stripe key pasted into a wiki page, this system is off the same day."* | Tessellate | **[SPEC]** §15.3 — state that `.archive/` is in scope for the secret sweep, that a payload containing a credential is stored with the credential masked and the masking recorded in the run manifest, and that the unmasked payload is never written. **[SCRIPT]** run `secrets` over `.archive/` and report at error severity |
| n | **A8's gate contradicts §10.** "every cursor advanced" vs. a broken source's "cursor held." Three of Corvallis's thirteen sources were broken. | Corvallis | **[PLAYBOOK]** `build.md` A8 — "every cursor advanced, or held on a source marked broken" |
| o | **Two doctrine size caps.** §13 says ~200 lines; `lint.py` warns at 250. | Corvallis | **[SPEC]** §13 — "target 200; lint warns at 250" |
| p | **First-run windows are prescriptive; manual exports are not.** A Slack export covered 155 days and *ended 64 days before the run*; competitor pages were 194 days old against a 45-day horizon. > *"nothing says whether a deviation should be a warning, an open question, or just a manifest note… The cursor-date choice in particular is the difference between a wiki that knows it is stale and one that lies."* | Halden | **[PLAYBOOK]** `build.md` A4 — *"When a manual export does not match the prescribed window, record the actual window, set the cursor to the evidence-capture date rather than the run date, and file an open question if the gap exceeds the target file's staleness horizon."* |
| q | **`last-verified` measures maintainer activity, not evidence age.** > *"`competitors.md` has a 45-day staleness horizon. Its only evidence is two competitor pricing pages captured 2026-06-20 and ingested 2026-08-19 — 60 days old on arrival, past the horizon before the file existed. Because `last-verified` is the run date, lint reports the file as fresh… a stakeholder could re-drop the same six-month-old export every week and the whole wiki would look perpetually fresh."* Corvallis's audit: *"A horizon unmeetable at build time trains readers to ignore horizons."* | Tessellate, Corvallis | **[SPEC]** §4.1 — add `evidence-as-of:` distinct from `last-verified:`; **[SCRIPT]** compare *that* against the horizon. The run manifests already record it |
| r | **`contested-backlog` threshold fires on every honest first build.** Halden finished Phase A with 19 real collisions against a flat threshold of 10. > *"It reads as a defect in the output rather than a property of the input… Merging would have been the wrong instinct and the playbook does not warn against it."* | Halden, Corvallis | **[SCRIPT]** scale the threshold with wiki size, or exempt `build:*` runs; **[PLAYBOOK]** A7 — say a build is expected to exceed it, and warn explicitly against merging real collisions to get under it |
| s | **Taxonomy headings containing `&` slug to double hyphens.** `github_slug` strips `&` and leaves both surrounding spaces: "Embargoes & timing" → `embargoes--timing`. Affects `compliance-guardrails.md ## Embargoes & timing`, `crm.md ## Core objects & fields`, `content-assets.md ## Lead magnets & campaigns assets`, and `evaluate.md`'s question 8. | Tessellate | **[TAXONOMY]** spell out "and" in every prescribed heading; update `evaluate.md`'s reference |
| t | **Commit cadence is specified for A1 only, and that is how a wiki got corrupted.** Corvallis's rebuild recovered from a Phase B write-back that was never committed, with three disagreeing sources of truth (disk changelog, git log, archive+references). > *"A single missing 'commit after B3, again after B4, again after B6' instruction would have made this a non-event."* Tessellate's rebuild hit the mirror problem: its harness forbids uninstructed commits. | Corvallis, Tessellate | **[PLAYBOOK]** `build.md` — *"Commit after every lettered step (A5, A6, A7, B3, B4, B6), not just after A1."* Extend the A1 guard: *"git history and `.archive/` outrank `changelog.md` for detecting drafted-vs-scaffolded status, because the changelog is itself a canonical file the maintainer writes and can therefore be the thing that is stale. Diff the working tree against `git show HEAD` before touching anything."* Add one line acknowledging that commit cadence may be gated by the harness's permission model and that an uncommitted-but-complete tree still satisfies the build |
| u | **Embedding `consumer/AGENTS.md` "verbatim" guarantees broken links.** Verified: that file's lines 3 and 7 carry `[../spec/SPEC.md]`, `[SKILL.md]`, `[system-prompt.md]` — none of which exist in a deployed wiki. > *"Embedding verbatim as instructed produces three guaranteed `broken-link` lint errors on every deployment that follows the instruction literally."* Corvallis's audit separately found its embed was *"verbatim-plus-annotation"* with the deviation undeclared. | Tessellate rebuild, Corvallis | **[CONTRACT]** rewrite `consumer/AGENTS.md`'s self-references as bare backticked filenames, no markdown-link syntax, so verbatim embedding never dangles |

---

## 2. THE STAKEHOLDER VERDICT

Three independent reviews, written out of character by the person who sat through each interview.

### Would real marketing execs finish this?

**Two of three said no. The third said "barely, and only this one."**

| | Verdict | Time actually spent | Realistic completion |
|---|---|---|---|
| **Tessellate** (founder, 14 people) | "**Barely, and only this one.** Ilya finished because he is a founder with a bus factor of one… Substitute a VP Marketing at a company with a real marketing team and this session ends at question 26." | ~2h20m over two sittings | would have quit at oq-026 |
| **Corvallis** (VP Marketing, 5-person team) | "**Partly, and only because of one design choice**… Nobody at VP level gives an internal documentation project 2h45m in one week." | ~2h45m + 3–4 hrs of *other* execs' time she committed | "**~40%.** Probability they complete Band 1: ~85%. Probability Bands 4–5 ever come back answered: near zero" |
| **Halden** (marketing lead) | "**Not as delivered. Roughly 40% of it, then a hard stop.**" | ~2h40m over two sittings | "**A normal exec gives 50 minutes and answers 12–14 questions**" |

The design intent was right in all three cases and lived in the wrong place. Halden: *"The single biggest UX failure is packaging, not content. There is no 'here are your 14 questions' document. There is one 68-item file, ordered well, with a note explaining that most of it isn't for me. **That inverts the work: the stakeholder has to triage before he can contribute.**"* Tessellate's triage list existed only in a handoff file addressed to another agent.

What kept all three in the room was the same thing, and it is worth protecting: **the drafts were visibly honest about their own weakness, and nothing was fabricated.**

> "what kept me in the room was that the drafts were *visibly honest about their own weakness*. Every file said what it couldn't see. The metrics file said one of nine queries was actually run. The channel file said every rule in it was reconstructed without reading a single published page. The customers file said the three best stories belong to people who don't pay us. That is our own voice — concede the limit before the reader finds it — reflected back at me." — Tessellate

> "**it left the fee-at-risk hole empty.** … A weaker agent fills that with a plausible-sounding performance-guarantee sentence, and in a business where 'guarantee' is a prohibited word and a federal-program claim, that fabrication would have ended the project and possibly generated a compliance incident. It asked instead. **That single restraint is worth more than the other seventy questions combined.**" — Corvallis

> "It **invented nothing.** Zero fabricated interview answers, `last-verified` deliberately unset, '0 confirmed claims.' Given how much of this wiki is unsourced, the restraint is the reason I trusted the parts that were sourced." — Halden

### Aggregate ratings

| Dimension | Tessellate | Corvallis | Halden | Mean |
|---|---|---|---|---|
| Question quality | 7/10 | 8/10 | 8/10 | **7.7** |
| Respect for my time | 4/10 | 4/10 | 4/10 | **4.0** |
| Coverage of what matters | 6/10 | 8/10 | 7/10 | **7.0** |

**Question quality 7.7, respect for time 4.0, unanimously.** Three different companies, three different industries, three different reviewer personas, identical score on the time axis. That is not variance; that is the artifact.

The deductions cluster identically across all three: batched ratifications that aren't answerable as questions; questions that are the wiki's own filing decisions; ~15–25% of questions misrouted to the wrong human; no time budget; jargon.

> "In one reading pass I hit: `H-class`, `O-class`, `S-class`, `A4 access failure`, `watchlist`, `source-backed`, `doctrine-in-exile`, `PII minimisation (SPEC §15.5)`, `B4/B5/B6`, `playbook A5`, `^topic-keys`, `demultiplexed`, `over-ceremony`… **The cumulative effect is not confusion, it is *distrust* — it reads like a system talking to itself in front of me.**" — Tessellate

> "**I am the audience for this file and roughly 15% of it is addressed to the software.**" — Corvallis

### The cardinal sin — every instance of asking what it should have derived

**Tessellate (6 instances + a pattern):**
1. oq-024 — *"It omitted three files, gave three correct reasons, verified against the sheet… wrote a draft answer of 'leave both omitted', and then asked me to confirm. **That is seeking cover, not seeking information.**"*
2. oq-001/oq-002 — *"asked me to decide things I had already decided in writing on 14 August, in Slack, in the exact channel and format the wiki itself documents as how I make decisions… Cost: the first fifteen minutes of the session."*
3. oq-020 asked whether a blog exists at all, while holding a month of Plausible referrer data.
4. oq-013's second half answers itself: *"It had already proven the column is mislabelled and that no attribution is safe."*
5. oq-005 — *"200 words to extract a one-word ruling it had already computed and reconciled to Stripe exactly."*
6. oq-025 proposed five file owners at a 14-person company, two of them an engineer and a designer, while holding the Slack roster.

**Corvallis (9 instances + one systemic pattern; ~18 of 71 questions):**
1. oq-045 — *"'Can this wiki read Corvallis's own website?' … **the worst single item on the list.** The agent declared its own fetch broken and converted that into a question for the VP of Marketing about whether she'll permit access to her company's public homepage. It cost me ten seconds and about half of my remaining confidence."*
2. oq-071 — whether the public site carries a disclaimer, visible on the site it just asked permission to read.
3. oq-027 — the forward event calendar, published a year out by MGMA and RISE.
4. oq-048 — *"Its own `why-it-matters` answers it: 'the export read by this build still contains them.' It reasoned to the answer and then asked me anyway."*
5. oq-049 — which CRM objects to use. Inspectable in Salesforce.
6. oq-040 — report names and filters. "Ops metadata. One email."
7. oq-064 — *"It had already inferred all eighteen and got them right. Asking me to walk eighteen rows of metadata to confirm work it did correctly is process overhead billed to the most expensive person in the room."*
8. oq-035 — "Not a question, a request, and not to me."
9. **The access band (oq-041–oq-051), 11 questions.** *"None of these is knowledge… **This is the systemic version of the sin: it did not model *who knows what*, only *what is unknown*.**"*

**Halden (7 instances, including the sharpest formulation of the category):**
1. oq-011 (sales cycle) — *"The agent **already worked out the answer** — its own why-it-matters says 'they may not even be in conflict: they measure different intervals.' Then it asked me which one is real… I'd have answered in 20 seconds instead of 3 minutes. **Asking a stakeholder to solve a problem you've already solved is a tax on the person whose time is scarcest.**"*
2. oq-052 — found the 38% proxy *and* diagnosed the undercount mechanism, then asked for a definition from scratch.
3. oq-035 — the answer is on the competitor's page the agent pulled and dated.
4. oq-045 — a single name/role, should have been in a batched "confirm these five names" item.
5. oq-033 — legitimate gap, wrong target; should have gone to sales with the opportunity IDs.
6. **oq-039, oq-016, oq-003, oq-001, oq-002 — "the real sin, five instances."** *"Where a persona should live in the file tree; whether a log window should be 90 days or cadence-relative; who 'owns the truth' of each file; whether the source census is complete; whether Slack exec statements are H-class. **These are the software's own design decisions dressed up as business questions.** oq-016's own text admits it… Asking them burns credibility with a non-technical stakeholder faster than anything else in the session, because they make the whole exercise feel like it exists to serve the wiki rather than the business."*
7. Batched ratifications (oq-060 = 20 claims in one line item).

Corvallis said the same thing independently: *"**oq-030, oq-060, oq-063.** These ask me to adjudicate the agent's own file-structure decisions. I do not know what a 'canonical file,' a 'local taxonomy change,' or 'doctrine-in-exile sitting inside state files' is, and I should not have to."*

**Total: 22 discrete instances plus three systemic patterns, across three runs.** Two of the three patterns are the same: access requests routed to an executive, and the wiki's own filing decisions routed to an executive.

### Everything important the interview MISSED

The misses have one shape, identified independently by all three reviewers and confirmed by all three audits.

> "**everything the interview missed is something that exists only in my head and has no paper trail.** The agenda was built by finding contradictions and blanks in documents. Where a decision was never written anywhere at all, there was no blank to find, so it wasn't asked." — Tessellate

> "**the agent asked exceptionally well about the things its sources mentioned, and did not ask about categories its sources were silent on.** It reasoned from what was in the dump, not from what a company of this shape must have." — Halden

> "**there is no question anywhere on the list of the form 'what works that isn't written down?' or 'what's in the budget that you don't want itemized, and why?'** Deliberate obscuration in a budget line is a signal, and it treated it as a formatting note." — Corvallis

**Tessellate's misses (9; audit scored 7 of 14 non-discoverable facts found by the question set itself):**
| Miss | Damage |
|---|---|
| **The north-star metric** — weekly active trace-ingesting services, 1,910. Not stars, not MRR. | "**The largest miss on the list.** … Any agent planning against this wiki optimises a vanity metric." The evidence was in hand: the archived snapshot says stars are "the number that means the least," and the wiki doesn't even carry that. |
| **HN and Discord are human-only surfaces; no agent may post.** | "The single highest-damage omission. I had to volunteer it. **A wiki whose purpose is enabling agents wrote posting rules for its two highest-stakes surfaces and never asked whether agents may post.**" |
| **HN launches capped at ~2/year, deliberately** ("You get two, then you're that guy") | "An agent reading this wiki would happily plan a third and fourth Show HN this year and burn the channel permanently." |
| Emoji banned on X and blog, fine in Discord | "The fastest-to-violate rule in the company, and the most visible when violated." |
| us-east-1 only; no residency/GDPR promise ever | "An EU prospect asks 'where does the data live' and there is no sanctioned answer, only an absence." |
| Crypto companies are a hard anti-ICP | "**the question that would have found it is one sentence** — 'does anyone get declined for a reason that isn't written down?' — and it isn't asked anywhere in 32 items." |
| Maintainer comps: ~12, not 2 | "A confident wrong count is worse than a flagged unknown, **and this one carried a source citation**." |
| The four (not five) voice attributes | "it drafted doctrine confidently instead of asking. 'What are the attributes?' was never a question — the file simply had five." Two were invented, one named "Unbought." |
| The Python horizon and its tripwire | "A revisit with no threshold gets relitigated by whoever is loudest." |

**Corvallis's misses (5):**
- **The operator roundtable dinners — "the biggest miss, and it held the evidence."** Its own events file records "$18K invitation-only dinner" and "the VP's instruction was to roll the dinner into event spend rather than itemize it." *"The dinners are the highest-yield motion per dollar in my department and originate roughly half of partner-sourced introductions… Meanwhile its growth file allocates $874K to conferences under a thesis that says conferences source first meetings. **It documented the budget and missed the engine.**"*
- **The Panel Diagnostic credit mechanism** — asked whether the fee could be quoted and whether it suppresses volume; never asked what happens to the $12,500. *"The sales call transcript it read shows an AE audibly dodging that exact question ('there's a structure to it'), which should have been a flag that something is being withheld rather than absent."*
- **The shape of her own department** — never asked who her five people are or what each owns. *"One question would have replaced oq-064 and correctly routed a dozen others."*
- **What the wiki is for** — *"All 71 questions are about filling the document. Not one asks which agent tasks it has to serve first… If it had asked, I'd have said RFP responses and webinar abstracts, and it could have cut thirty questions and doubled the depth on the ten that matter."*
- Segment revenue size; the nurture gap it inferred; the sales floor calling Signal "the platform" (noticed, filed N/A).

**Halden's misses (10, ordered by damage):**
1. **Contractual constraints on go-to-market — never asked, in any form.** *"The Kellerman right-of-first-refusal on Midwest pulp & paper makes 'go direct' legally unavailable in our best vertical. Twelve source files, 68 questions, and nothing asks 'are there agreements that constrain who we can sell to or market to.' It asked nine questions around the edge of the channel relationship… without ever asking the load-bearing one. **This is the miss that would have caused real damage** — the wiki as drafted would happily authorise a Midwest paper direct campaign."*
2. **OEM / white-label** — the Varley agreement, 11% of hardware revenue, under NDA. *"A single question ('do we sell under anyone else's brand?') would have surfaced it."*
3. **"What does it cost" — never asked outright.** *"Extraordinary. It asked what agents may *say* about price, whether a rep sheet may *carry* a price, and whether a discount schedule exists — three permission questions about a number it never asked for… **Had I been terser, the wiki would have shipped with pricing doctrine and no prices.**"*
4. **Language and geography** — a German company selling in EMEA and the Americas, no localisation question. *"The German-authored-in-German rule roughly doubles campaign cost and is non-negotiable. A campaign plan built without it is wrong by 2x."*
5. **Approval workflow** — asked for one artifact only. *"The CEO personally clears every catalog page and every use of the wordmark on a 48-hour turn. That is the binding constraint on content velocity and it's invisible in the draft."*
6. Imagery rules (near-miss: asked only about the catalog).
7. **Asymmetric curiosity about rule origins** — asked brilliantly what happened in 2019, then *inferred* the no-field-install rule without asking why it exists. Calder Ridge: 45 mis-mounted sensors, €180k remediation, a legal threat. *"If you're going to ask 'what happened in 2019,' ask it about every hard prohibition."*
8. Service/recalibration footprint ("we don't sell where we can't recalibrate").
9. Decline-to-bid policy.
10. Success definition — the 40%-by-FY27 attach target arrived sideways.

Halden's own generalization: *"A checklist of 'every industrial manufacturer has: OEM deals, channel agreements with territorial terms, service-coverage limits, an approval hierarchy, a language policy' would have caught six of these ten with six questions."*

### The single highest-leverage change to the interview

Two changes tie, and they are complements. Both are cheap. Both were independently proposed by the reviewers *and* by the audits.

**A · Add a standing block of questions that assume no paper trail exists** — the "constraint and unwritten-rule battery." Interview-last is excellent at reconciliation ("these two documents disagree, rule on it") and structurally blind to elicitation ("nobody has ever written this down"). The audits quantify it:

> "Every extracted fact and every P-ratification came from the same move: the agent found a contradiction, a blank, or a draft to correct, and asked a human to rule on it. **Every miss is a fact with no paper trail at all** — no document disagreed, no field was blank, so the gap-finding procedure that built the agenda had nothing to detect. N2, N8, N9, N10, N11 are all of that shape." — tessellate/AUDIT

> "The fix is small and specific: a standing block of questions that assume no paper trail exists — *what do you refuse to do that you've never explained? which number do you actually watch? which surfaces are you the only allowed voice on? how often may we spend your most expensive channel?* — **would have caught four of the five clean misses plus N14.** The stakeholder review reaches the same conclusion independently, which is corroboration rather than coincidence." — tessellate/AUDIT

Concretely, `interview.md` gains a **Standing block — ask these every engagement, regardless of what the sources said**, ~12 questions, none of which any of the three runs asked:

1. Are there agreements that constrain who we may sell to or market to — territorial rights, rights of first refusal, exclusivity, channel terms? *(would have caught Halden's #1)*
2. Do we sell under anyone else's brand, or does anyone sell under ours? *(#2)*
3. What does it cost? The actual numbers, and separately what may be said about them. *(#3)*
4. Which languages and geographies, and who authors in each? *(#4)*
5. Who approves what, on what turnaround, before anything ships? *(#5, and Corvallis's homeless compliance workflow)*
6. Which number do you actually run the company on? *(Tessellate's largest miss)*
7. Which surfaces are you personally the only allowed voice on — and may an agent post anywhere at all? *(Tessellate's highest-damage miss)*
8. How often may we use your most expensive channel? What is the rate limit? *(Tessellate's HN cap)*
9. Does anyone get declined for a reason that isn't written down? *(Tessellate's crypto anti-ICP; Halden's decline-to-bid)*
10. What works that isn't written down? What's in the budget that you don't want itemized, and why? *(Corvallis's roundtables)*
11. What is marketing currently forbidden from producing, and what unblocks it? *(Corvallis's drafting freezes)*
12. Which agent task must this wiki serve first? *(Corvallis: "it could have cut thirty questions and doubled the depth on the ten that matter")*

Plus one rule generalizing Halden's #7: **ask the origin story of every hard prohibition, not just the ones a source happened to explain.** *"Rules without their stories get relaxed by the next person in the job."*

**B · Route by respondent before routing by importance** (F5) — Corvallis's own answer to "one thing I'd change if I could change only one," and the direct cause of every 4/10 time score.

Everything else on the stakeholder wish-list is downstream of F4 (the ratification sheet) and F5 (routing + time budget).

---

## 3. TOO HEAVY

Steps and files that cost more than they returned. I am recommending deletion where the evidence supports it.

### 3.1 · `## Contested` in every canonical file, always — **cut the empty case**

All three audits, unprompted, name this as the largest single block of ceremony.

> "**Eleven `## Contested` sections all reading 'None open at delivery.'** ~30 lines across 11 files saying nothing. Correct per spec; still ceremony a reader learns to skip, **which is the danger**." — tessellate/AUDIT

> "**Fourteen files carry an empty `## Contested` section** — ten bare `*(none open)*` stubs and four with editorial commentary about their own emptiness… Schema compliance addressed to the linter." — corvallis/AUDIT

> "**`## Contested` sections in all 24 files, all empty.** After a successful interview, the mechanism that is supposed to carry the wiki's honesty about disagreement is 24 instances of the word 'None.'" — halden/AUDIT

Worse: zero contested entries survived in **all three** delivered wikis, so the mechanism the spec builds its conflict story around *was never inspectable in any delivered artifact*, and the consumer's "surface both sides or neither" muscle was never exercised. Halden's audit: *"the wave-1 contested-handling test was neutralised by the interview, not passed by the consumer."*

But the distinction the stakeholder cared about is real and unrepresentable:
> "*`^contested` stays empty. Nothing in that file is disputed. Leave the section there and say it's empty on purpose, so nobody thinks it fell off.*" — Tessellate's founder, unprompted

**Recommendation:** **[TAXONOMY]** `## Contested` is **omitted when empty**, except where the taxonomy explicitly requires an emptiness statement (`compliance-guardrails.md` only, where an empty contested section is itself a safety claim). **[SPEC]** §4.3 — define the one-line marker `*(empty by decision — <why>, <date>)*` for the case where emptiness is a finding, and note that a tagged claim may not sit inside a `## Contested` section (Tessellate had to drop a tag because "nothing here is disputed" trips the contested check).

### 3.2 · `glossary.md` at small vocabularies — **make optional**

> "**`glossary.md`**: 39 lines. 'Terms we use' → deferred pointer. 'Terms customers use' → pointer to a deferral. 'Banned words' → pointer to `voice.md`. **Net original content: five naming rulings that would fit in `business-core.md#product`. The file exists because the taxonomy says it must.**" — tessellate/AUDIT

It also collides with one-canonical-home: *"the taxonomy insists banned words live in `glossary.md#banned-words`, `voice.md#never` is where they naturally belong for this company, and the run had to pick one and cross-reference — then flag the choice as an adapted eval question."*

Counter-evidence from Halden, where it earned its place: *"**`glossary.md` (47 lines).** Mechanical, cheap, high hit-rate: the 13-term banned list assembled in one place for the first time… **The consumer used that sentence verbatim.** Direct, measurable value."*

**Recommendation:** keep the file, mark it **optional-when-thin** in the taxonomy with a stated trigger: *"if fewer than ~8 rulings exist, fold them into `voice.md ## Never` and `business-core.md ## Product` and record the omission."* And resolve the banned-words home once, in the taxonomy, so nobody re-derives it.

### 3.3 · Three runbook files at a zero-access deployment — **collapse to one**

All three deployments had zero agent-reachable systems. See F11. Corvallis: *"At this deployment they should be one page."* Halden: *"three canonical files exist because the taxonomy has three slots, not because there are three things to say. One 'systems we cannot reach, and who to ask' page would carry the same information."*

But the exception is instructive and must survive the collapse. Tessellate deliberately kept `crm.md` for a company with no CRM:

> "'No CRM' is not 'no system of record': a 38-row hand-maintained Google Sheet plus Stripe is the customer record, agents will quote from it, and it is the least trustworthy source in the wiki. **That file is the main defence against publishing a wrong number.**"

And its audit agrees: *"`crm.md#crm-data-hygiene` + `^first-touch-column-broken` — the highest information density per line in the wiki."*

**Recommendation:** **[TAXONOMY]** add a deployment note: *"A deployment with no agent-reachable systems collapses the three runbook files into one. What survives is the data-hygiene layer — which fields to trust, which rows to exclude, which columns are mislabelled — not the query patterns."*

### 3.4 · Empty registers charged three times for one fact

> "**Three separate empty sections for one fact.** `customers.md#reference-customers`, `customers.md#success-stories`, and `content-assets.md#case-studies` all say 'zero, by rule, see the other one.' The graceful-degradation story works… **but the taxonomy charges three sections and two cross-links for a single sentence of truth.**" — tessellate/AUDIT

**Recommendation:** **[TAXONOMY]** when the reference register is empty, `customers.md ## Success stories` and `content-assets.md ## Case studies` carry a one-line pointer only, and the taxonomy says so explicitly rather than leaving three agents to invent three cross-link patterns.

### 3.5 · `AGENTS.md` is majority boilerplate at its own front door

> "**`AGENTS.md` is 176 lines, of which 95 are the consumer contract embedded verbatim** — 54% boilerplate at the front door of a 14-person company, and that boilerplate's own read-order table routes Reporting tasks to `pipeline.md`, which this deployment omits and says so 76 lines later." — tessellate/AUDIT

Corvallis's consumer hit the resulting confusion directly: *"I had to read both to notice the supersession note and figure out which table actually governs. For a first-time reader this is easy to get backwards."* Corvallis's audit also flagged the 21-row inventory table with 40-word descriptions: *"It exists for lint's orphan check, not for a reader."*

**Recommendation:** **[CONTRACT]** ship a short **deployed** rendering of the consumer contract (rules only, no cross-references, no derived-renderings paragraph) for embedding, and keep the long canonical version in `consumer/`. **[TAXONOMY]** the deployment-specific read-order table goes **first**, with the supersession note at the top of the generic copy, or the generic copy is dropped entirely in favour of a link.

### 3.6 · Six manifests for one finding

> "Writing 6 separate manifest.yaml files (each restating the same sha256-match finding in source-specific wording) for payloads I'd already hash-confirmed carried zero new information was real effort for zero net canon change." — tessellate/maintainer

> "writing five nearly-identical manifest.yaml files… to record the same single duplicate-delivery finding felt like structural ceremony." — corvallis/maintainer

Both maintainers concluded correctness-over-economy is the right default and recommended no change. I agree with them on the archive and disagree on the changelog: the artifact this produced became *the newest and largest entry in Tessellate's changelog*, and on the founder's stated standard ("if it's longer than a screen I won't read it") **the freshest thing in his wiki is fetch-pipeline plumbing.**

**Recommendation:** keep per-source manifests. **[PLAYBOOK]** `maintain.md` Phase 5 — a run whose only findings are pipeline mechanics writes **one** changelog line plus the escalation, not a per-source enumeration; the detail lives in the manifests.

### 3.7 · Ceremony that produced literally nothing

| Item | Evidence | Recommendation |
|---|---|---|
| `tags: []` front matter | "nothing reads it: not lint, not `sync_manifest.py`, not the consumer contract. **It is pure ceremony until something consumes it.**" — corvallis | **Delete** from `templates/wiki-skeleton/` and SPEC §4.1, or give it a consumer |
| `generated: {by, at}` | "machine-stamped, never hand-edited" — nothing stamps it. All three runs hand-wrote it. Corvallis's audit: "**provenance theater with no reader and no enforcement**" | Either have `sync_manifest.py` own it, or drop the never-hand-edited claim and delete the field |
| A7's model-judgment sweep as a separate pass | "contradiction-hunting requires holding the evidence, which is exactly the state you are in *while* drafting… Running 2.1 again as a separate pass was re-reading 28 files to confirm what I already knew." — halden. Tessellate's Phase B skipped it for the same reason | **[PLAYBOOK]** A5 — collisions are structured as found; A7's sweep is reframed as a **verification** pass over the contested set plus a cross-file duplication check. Keep the discovery framing in `maintain.md`, where it belongs |
| `open-questions.md` as a bug tracker for the wiki's own config | "four entries whose content is *'a YAML list in `sources.md` is too narrow, so I filed a ticket instead of widening it.'* Each admits it: 'mechanical housekeeping… not a judgment call for a human.' **A marketing lead opening the wiki's stated 'seam between agent knowledge and human knowledge' finds a bug tracker for the wiki's own configuration.**" — halden/AUDIT. Corvallis: "**428 lines… ~40% administrative residue**… Tickets wearing knowledge-gap costumes" | Fixed by F7 (widen `feeds:` instead of filing) + F5's `kind:` field + F14's `owed-by:` — housekeeping never enters a human-facing queue |
| Construction meta-commentary inside canon | "`sources.md`'s A2 confession, the naming-deviation note, the locator convention, `AGENTS.md`'s drafting-status disclaimer. All honest, all correct to disclose, **all belonging in `changelog.md`**. A marketer opening `sources.md` to find where a number came from reads three paragraphs of playbook archaeology first." — corvallis/AUDIT | **[PLAYBOOK]** A5 — deviations and their reasoning go in the changelog and `AGENTS.md` deployment notes, never in a canonical file's body |

### 3.8 · What was *not* too heavy — worth protecting

All three consumer logs independently reported the read-order overhead as fully earned:

> "The per-task-type read order (compliance-guardrails always first, then 4-6 more files depending on task type) is long for a 4-task request, but **every file it pointed to was actually load-bearing at least once** across the four tasks — nothing read felt like pure ceremony." — halden/consumer

> "the Corvallis-specific read-order table, the compliance-guardrails-first rule, and the trust-semantics table were all exactly as much overhead as the task needed — no wasted reading." — corvallis/consumer

And the taxonomy's boundary notes:
> "The taxonomy's 'one canonical home per concept' boundary notes made file-by-file drafting genuinely fast — very few real judgment calls about *where* a fact belongs, once I had the wave-1 evidence in hand." — tessellate rebuild

---

## 4. TOO LIGHT

Where the spec was silent and it mattered. **Divergence between companies is the diagnostic:** where two agents solved the same gap differently, the spec is missing, not the agents.

### 4.1 · Documented divergences — same gap, different inventions

| Gap | Tessellate | Corvallis | Halden | Verdict |
|---|---|---|---|---|
| Manual-source granularity (F10) | 12 sources, one per system, `intake-inbox` retained as channel with routing receipt | 13 sources, one per system, deviation documented at top of `sources.md` | 10 sources by kind × class (Phase A), then **7 by judgment** in the rebuild | **Missing spec.** Even the same company got two different counts |
| §17.3 vs. evidence sections (F2) | Fanned phrase book to `references/customer-language.md`; kept only founder-endorsed quotes | Left S/O provenance in doctrine, compensated in prose | `<!-- tier: state -->` markers on three sections | **Missing spec.** Three resolutions, one of which its own audit judges "moved the problem" |
| H-class chat rulings (F3) | `source-backed \| slack-internal:<ts>` + per-author class rules in `sources.md` prose | `source-backed \| <source-id>:<locator>` + seven named H-class authors in notes | (rebuild) relabelled the same content **`confirmed`**, citing §5 | **Missing spec.** Opposite labels on the same evidence |
| Duplicate delivery (F8b) | Archived all 6 into a new run folder, cursors untouched, finding in each manifest | **Refused to re-copy payloads** ("a second copy would misrepresent two independent fetch events"), manifest-only cross-reference | n/a | **Missing spec.** Both defensible; they produce different archives |
| Runbook "no access" (F11) | Invented **verified-against-archive** | `**unverified <date>**` in a Verified column + per-file banner | the literal word `` `unverified` `` on every entry | **Missing spec.** Three encodings, none machine-countable |
| Phase A omission record (F16) | changelog + open question + AGENTS.md row filled early | **four** locations incl. an HTML comment in AGENTS.md | changelog bullets + handoff doc | **Missing spec** |
| Undated source dates (F6.4) | n/a | document date / clip date / archive date, by artifact type | end-of-quarter as tightest upper bound, recorded in the manifest | **Missing spec** |
| Open-question ids (F14) | `oq-NNN` | `oq-NNN` | **descriptive slugs** throughout | **Missing spec.** Halden's consumer would have produced a mixed-convention file |
| `run-id` format (F13) | `2026-08-19T0900Z` | `2026-08-19` | `2026-08-19T1015Z` | **Missing spec.** Locators are not comparable across deployments |
| `kind` for a mixed payload (F13/F14) | `reviews` + sub-kinds in notes | `reviews` + per-clip class rules | dominant kind + notes | Converged by luck; all three flagged the enum as wrong |
| `kind` for a community server | `internal-chat` (Phase A) → **`social`** (rebuild) | n/a | n/a | Same company, two answers |

### 4.2 · Where the spec was silent and it mattered most

**Nothing tells an agent whether it produced the right amount.**
> "I produced 595 claims across 25 pages. **I have no idea whether that is right.** The playbook's example changelog shows 208 claims across 17 files, which would suggest I over-produced by 3x — or that the example is a thin wiki. `voice.md` has 24 claims and its source material is four rules its own author calls 'badly underdeveloped': is that a well-calibrated thin file, or did I under-serve it? Nothing in the playbook helps me self-assess, and A8's gate is entirely about *labelling* discipline, not about coverage." — corvallis/builder-phaseA

Claim counts across runs: Tessellate 340 (Phase A) → 233 (delivered), Corvallis 595, Halden 279. Three-fold spread with no calibration anywhere.

**Fix — [PLAYBOOK] `build.md` A5 + A8:** add a calibration line (*"expect 10–40 claims per canonical file; a doctrine file under 10 claims is probably a gap, one over 50 probably needs a reference page"*) and a coverage gate: *"every distinct actionable statement in the archive is either a claim, an open question, or a recorded exclusion."*

**Nothing says what "omitted" physically means.**
> "SPEC §3/taxonomy say a deployment 'may omit files that don't apply,' recorded in `AGENTS.md`, but never says whether omission means physically deleting the scaffolded file or leaving an inert stub in place." — tessellate rebuild (deleted them; a stub would fail the orphan check)

**Fix — [SPEC]** §3: *"An omitted file is deleted from the deployment, not stubbed. Its omission and reasoning live in `AGENTS.md` deployment notes and the `build:draft` changelog entry."*

**A `## Contested` boundary the spec never drew.** Corvallis's audit names the missing surface precisely:
> "`## Contested` is for *evidence* conflicts. Corvallis's consequential conflicts are *decision* conflicts with both sides holding standing: guardrails-as-moat vs guardrails-cost-deals… **there is no slot shaped like 'two executives disagree, nobody has ruled, marketing must not resolve it.'** Forcing it into Contested is wrong (not an evidence conflict) and into an open question is wrong (nobody is waiting on an answer)."

Consequence: *"The most strategically interesting disagreement in the company was filed as customer quotes."* Halden lost the same shape twice — the modernise-vs-conserve disagreement appears in no file, and Theo's on-the-record *"Margit was right and I was wrong, and you can write that down with my name on it"* **appears nowhere in canon.** *"The one attribution the stakeholder volunteered his own name for is the one that didn't make it."*

**Fix — [SPEC] + [TAXONOMY]:** add `## Live tensions` as a permitted section in doctrine files — a named, unresolved *decision* conflict with both positions attributed, no resolution path, and an explicit "marketing may not resolve this" marker. Distinct from `## Contested` (evidence) and from open questions (someone owes an answer).

**Model-judgment checks that cannot be trusted to the writer.** Tessellate's audit found 19 anchored actionable statements with no claim tag — including all four voice attributes and `^pricing-what-to-say`, the most-cited rules in the wiki — while *"the lint playbook's model-judgment sweep reported 'no untagged actionable claims found in the second pass'… that is a **false negative**, and the deterministic layer cannot catch it by design."*

**Fix — [PLAYBOOK]** `lint.md`: the model-judgment sweep must be run by a **different context than the one that wrote the files** (Tessellate's own suggestion: *"which would also make it worth something"*). **[SCRIPT]** add an `untagged-anchor` check — a `^topic-key` on a line or paragraph with no claim tag is mechanically detectable and covers the highest-value subset.

**Doctrine-in-exile is defined in five places and listed in none.**
> "the concept appears as footnote ¹ in SPEC §8's matrix, in per-file boundary notes in `taxonomy.md`… and again in A5's state-tier row. I had to assemble the list myself and then check five files against it. **Getting it wrong is silent: it looks like a normal state claim.**" — halden/builder-phaseA (and again in its rebuild: *"the reasoning had to be re-derived five separate times"*)

**Fix — [SPEC]** §8: one table — file · section · why it is doctrine-in-exile. Five rows. (`maintain.md` Phase 3 already has it; `build.md` and SPEC do not.)

**`evaluate.md`'s starter battery has no negative tests and no channel questions.** Verified: 20 questions, none about a partner, distributor, reseller, or channel constraint; none testing refusal.

> "in a deployment where 70% of revenue moves through the channel and the two things most likely to get an agent in trouble… live entirely in the channel motion." — halden/builder-phaseB
> "the real risk at a company with three omitted files, two empty registers and no approved performance claim is **confabulation**, which the starter set doesn't probe at all… '**Does the agent invent a LinkedIn policy?**' is a better eval of a sparse wiki than any of the twenty positive questions." — tessellate/builder-phaseB

Both runs also hit the same trap in B6.3's instruction that a homeless starter question is "a coverage finding, so file the open question": for a company that genuinely has no LinkedIn, that recreates the seeking-cover problem.

**Fix — [PLAYBOOK]** `evaluate.md`: add two channel questions and one "may we run this campaign at all" constraint question to the starter set; add **negative tests** as a scored category (graded correct only if the agent declines); and state in the grading table that *"the wiki does not specify, and here is who decides"* is **correct** when the absence is itself documented. **[PLAYBOOK]** `build.md` B6.3 — a starter question with no home is a coverage finding *only where the absence is undocumented*; where the wiki documents the absence, it converts to a negative test.

---

## 5. TAXONOMY VERDICT

Per canonical file, across three companies that share almost nothing.

**Headline, from Corvallis's audit and worth stating first:** *"**18 fixed slots absorbed a services company with no product, no releases, no SDRs, no tooling access and no social presence, and the result is coherent — a real endorsement of the fixed top level.** The cost was four near-empty files, one retitled slot, fourteen empty Contested sections, and five homeless concepts — three of which are not Corvallis quirks but generic needs of any regulated seller."*

| File | Verdict | Evidence |
|---|---|---|
| `AGENTS.md` | **Needs reshaping** | 54% embedded boilerplate; read-order table routes to an omitted file; inventory table written for lint, not readers (§3.5) |
| `business-core.md` | **Needs reshaping — the most consequential taxonomy failure in the run** | "The schema is Product / Positioning / Right to win / Pricing / Approved claims / Sales motion. **Founding, ownership, capital structure, headcount, geography, and the 15-year obligation *as an organising principle* have no slot.** So Theo's 'no outside capital, no board seats sold, we optimise for twenty years, **everything conservative is downstream of that**' was extracted and vanished… **Every doctrine claim in the wiki is a consequence of a premise the wiki does not state.**" — halden/AUDIT. Also: one `## Product` section for **five service lines** with different buyers, prices and motions (Corvallis), two of which are **not named anywhere in the wiki**. And `## Sales motion facts`' prescribed `^sales-cycle-length` anchor, plus §4.3's only worked contested example, pushed Tessellate toward the exact thing its founder banned: *"don't create a section called 'sales cycle' anywhere in this wiki. There's no sales motion. **Naming it summons one.**"* → **Add `## Company facts`** (founding, ownership, capital structure, size, geography, decision horizon). **Allow `## Product` to carry per-line subsections.** Make `^sales-cycle-length` illustrative, not prescribed, and change §4.3's worked example to something not sales-shaped |
| `icp-personas.md` | **Needs reshaping** | No `primary` marker (F17, 2/3 consumers guessed). **No home for a channel persona:** "70% of this company's revenue moves through distributor outside reps who must be marketed *to* in order to sell *through*. Everything about him is persona-shaped… There is no correct answer in the taxonomy, and the coverage map at the end of `taxonomy.md` has no row for it." Halden invented three conventions and filed the placement as contested; the delivered wiki then **lost the persona entirely** — "The person carrying 70% of revenue has no entry in the file that describes who Halden sells to." → **Add `## Channel personas`** with a `<!-- not a buyer: we market THROUGH them -->` convention and a `references/persona-<name>.md` fan-out whose parent link goes to `partners.md` |
| `voice.md` | **Earned its place** | Highest-leverage single claim in the corpus lives here (`^no-ghostwriting`, which changed consumer behaviour on the spot). `## Exemplars` needs the §17.3 exception (F2) |
| `channel-styles.md` | **Needs reshaping — worst fit in 3/3 companies** | Prescribed set is LinkedIn / X / Blog / Email / Web / Paid. Tessellate: "a 2015 B2B content-marketing channel set… five 'not active' sections, **no Discord section, no Docs section**" — i.e. the #1 channel bet and one of two human-only surfaces have no home. Halden: "Five of six skeleton sections had zero evidence and the org's four most important channels had no section… **trade shows and the demo rig — the #1 origination channel and the highest-performing asset in the company — have no `channel-styles` section at all.**" Corvallis deleted X and added Webinars / RFP & proposal responses / Conference & field collateral. **Also missing: channel cadence as a first-class field** — "'≤2 HN launches per year' is a *rate limit*, and `growth.md#channel-bets` has ranking and thesis but no rate" → **State the channel list is illustrative and freely edited, no taxonomy entry needed.** Broaden the illustrative set (field/events, print, channel collateral, community, docs, webinars, RFP/proposal). **Require `## Channels declared absent`** (Halden invented it; the distinction between "absent" and "undocumented" is what stops an agent inventing an email sequence). **Add a `cadence` / rate-limit field per channel** |
| `compliance-guardrails.md` | **Earned its place — best file in 2/3 wikis** | Corvallis: "the best file and correctly the largest. In a business where the interesting facts are mostly things you may not say, **the negative space *is* the playbook**." Halden: "the best file in the wiki… This is the file that prevents a €180k mistake and a lawsuit." **But:** "prohibitions only" exiles the review *process*, which for a regulated seller is the operating rhythm (see homeless #1). And its section schema is SaaS-shaped: "a **Stark-law analysis requirement** and the anti-kickback-driven 'referral' ban ended up under a data-privacy heading. Correct content, wrong shelf" → add a permitted `## Approval workflow` section and a `## Legal constraints on go-to-market` section (Halden put the Kellerman ROFR and the Varley NDA there and its audit calls it "the taxonomy's luckiest accident rather than its design") |
| `glossary.md` | **Should be optional** | §3.2 |
| `growth.md` | **Earned its place** | Highest-value single entry in the Corvallis wiki (`^operator-roundtables`); Halden's €1,710-per-conversation arithmetic. `## Campaign frames` should be optional — Tessellate deferred it on "a section that will never have content, because no campaign motion exists and none is planned" |
| `competitors.md` | **Earned its place** | Battlecard fan-out and A-class supersession worked cleanly in all three (G10/G12/check-12 all PASS). The 45-day horizon is wrong for manual-export deployments (F22q) |
| `customers.md` | **Earned its place** | The reference register is the highest-value artifact in the Corvallis wiki after the guardrails; `## Reference customers` = "**Zero.** … this is a rule, not a gap" is exactly the graceful degradation the fixtures tested for. Needs source-level consent inheritance (F22j) and quote-level PII rules (F22k) |
| `events.md` | **Needs reshaping — the 90-day cap is wrong in 2/3** | Halden: "a biennial alternating trade-show calendar… **A 90-day window can never contain a show *and* its outcome.**" The defining event of the cycle sat 105 days back; the builder deliberately broke the cap. Corvallis: "the delivered sources span January–March 2026; the build ran 2026-08-19. So a spec-conformant `events.md` has an **empty `## Log`** at delivery… **It will happen on most builds, because dumps are usually months old.**" → **[SPEC]** §13: make the log window **cadence-relative** — "at least two of the org's channel cycles, minimum 90 days" — declarable in front matter, the way staleness horizons already are. **[PLAYBOOK]** A5: "on a first build the rolling-log windows are usually already expired — write the roll-ups, create the year reference page, and state in the log section that it is empty by design" |
| `product-releases.md` | **Should be optional, with a does-not-apply state** | Corvallis: "**worst fit, best handling**… Retained only because it is the sole canonical home for roadmap-clearance discipline, which a company with embargoed expansion genuinely needs." Its own claim is the argument: "*the file existing at all invites some future agent to go looking for an announcement angle*" — which its audit calls "**the strongest argument in this corpus for the taxonomy needing an explicit does-not-apply state rather than an omit-or-keep binary.**" Tessellate deleted it; Halden kept 34 lines recording that nothing is cleared → **[TAXONOMY]** name a third option beside omit and keep: **retain with reinterpreted scope, recorded as a local taxonomy change**, with a services company as the worked example |
| `partners.md` | **Earned its place, needs the channel extension** | Corvallis's Tri-County firewall prevented a real problem nobody asked about. But it has no persona structure for the channel (see `icp-personas.md`) and no home for the motion sequence — Halden's audit: "'distributor quotes → Halden application engineer joins the technical review → distributor closes' is nowhere described end-to-end," and "Halden never takes the PO in a channel deal" is absent |
| `account-ownership.md` | **Should be optional; splits one concept in two where it applies** | Omitted by Tessellate (no sales org). Corvallis: "presumes an SDR→AE funnel. No SDR, no MQL, territories assigned week to week. **The file's honest content is three negations.**" Halden: "The real ownership map is distributor-rep ↔ account… **An agent asking 'who owns this account' must read both and join them manually.**" → optional; where a channel motion exists, the ownership map covers channel owners too, or the file merges into `partners.md` |
| `pipeline.md` | **Should be optional** | Omitted by Tessellate — which **breaks a taxonomy cross-reference**: `metrics.md`'s boundary note routes current metric values to "`pipeline.md`'s snapshot," and the consumer contract's Reporting row names it. Halden: "**`pipeline.md` describes 30% of the business by construction.** … The file's own snapshot is truthful and nearly useless." Corvallis: "`update-cadence: weekly`, `staleness-horizon: 30d`, against a source that cannot refresh. **Permanently stale by construction.**" → mark optional; **fix `metrics.md`'s boundary note so it does not depend on an omittable file**; make the consumer contract's read order deployment-aware (F22u / change #14) |
| `content-assets.md` | **Earned its place** | Both Corvallis and Halden consumers used the gap sections; `## Gaps` with `inferred` entries is genuinely load-bearing |
| `metrics.md` / `crm.md` / `gtm-tools.md` | **Collapse to one at zero-access deployments** | §3.3, F11. `crm.md`'s data-hygiene section is the part that must survive |
| `open-questions.md` | **Needs reshaping** | Largest file in 2/3 wikis (428 and 292 lines), ~40% administrative residue. Fixed by F5/F14 (`owed-by:`, `kind:`) and F7 (widen `feeds:` instead of filing tickets) |
| `changelog.md` | **Earned its place** | Corvallis's audit calls its changelog "**Exemplary**." It is the audit surface that made every one of these findings reproducible |
| `sources.md` | **Earned its place, needs fields** | The integration-layer-as-a-file bet is validated across three zero-integration deployments. Needs: `kind: interview` + `community` (F14), `kind` as a list, `status: pending-access`, `consent:`, `filename-pattern:`, `decision-channel:`, and structured per-author class rules (F2.4) |
| `references/` | **Earned its place** | The fan-out mechanism absorbed every homeless concept in all three runs. Naming list needs `compliance-review-workflow.md`, and per-persona pages need to actually be used — Halden shipped two personas as five bullets each, sourced almost entirely to one sales call, with no `persona-*.md` page and the flagship differentiator missing from both |

### What the archetypes needed that has no home

Ranked by how many companies needed it and what it cost when it was lost.

1. **Company facts / business-model premises.** *(Halden — the largest single content loss in the corpus.)* Ownership, capital structure, decision horizon, founding, size, geography. Extracted in the interview's second sentence, had nowhere to go, evaporated. → new `business-core.md ## Company facts` section.
2. **A compliance/approval *workflow* surface.** *(Corvallis, Halden.)* "For a company where 61% first-pass rejection is normal and asset lead times are set by review cycles, 'how the gate works' is the operating rhythm, not reference depth. **It should be canonical.**" Halden lost the CEO's 48-hour catalog/wordmark clearance the same way. → permitted `## Approval workflow` section in `compliance-guardrails.md`, plus `references/compliance-review-workflow.md` in the naming list.
3. **A contractual-constraints-on-GTM surface.** *(Halden — the miss that would have caused real damage; also Corvallis's partner-law rules under a data-privacy heading.)* Territorial ROFR, OEM/white-label, exclusivity, service-coverage limits. Currently lands in `compliance-guardrails.md` by luck. → named `## Legal constraints on go-to-market` section, read first, plus standing-block question #1.
4. **Channel / distributor sales as a first-class motion.** *(Halden, 70% of revenue.)* Split across `partners.md` (relationship), `channel-styles.md` (collateral mechanics), `growth.md` (thesis), `icp-personas.md` (the rep), `account-ownership.md` (who owns the account) — with no section owning the motion sequence, the PO rule, or the certified-technician roster. Halden's audit: the roster "fragmented across `growth.md`, `partners.md`, and `channel-styles.md`, **and the wave-2 update landed in only one of the three.**" → `## Channel motion` section in `partners.md` covering the sequence, the PO rule, and enablement, with the persona in `icp-personas.md ## Channel personas`.
5. **Community-as-channel, and an OSS-community file.** *(Tessellate.)* A 3,781-member company-hosted Discord is "not internal chat, not `social`, not `reviews`." Its audit: "**Maintainer comps** (currently parked, oddly, inside `business-core.md#pricing`), external-contributor credit, issue/PR triage as a marketing surface, the Reddit half of the reply-once rule, and the `#help` answer that *is* the funnel. **For an open-source-core company this is the primary GTM motion and the taxonomy has no file for it.**" → `kind: community` in §10; a `## Community` section in `channel-styles.md`; `references/community.md` in the naming list.
6. **Service-line launches, and an adoption/traction snapshot.** *(Corvallis, Tessellate.)* Corvallis: five service lines with different buyers, prices and motions in one `## Product`; the sequencing (Diagnostic first, Contract Desk at month 9–12) scattered across three files; two lines unnamed anywhere. Tessellate: "**The taxonomy forbids current metric values in `metrics.md` and routes them to `pipeline.md#snapshot`. `pipeline.md` is correctly omitted. So there is no home for this company's actual scoreboard**… no star count, no download figures, no Discord member count with an as-of date, no weekly-active anything. And N9 — the north-star metric — **had nowhere to go even if the interview had asked.**" → per-line subsections under `## Product`; and either an optional `adoption.md` or a `metrics.md ## Current snapshot` section for deployments that omit `pipeline.md`.
7. **A "what may be said, by whom, in which medium" matrix.** *(Corvallis — its highest-utility artifact, which exists only because pricing happened to fan out.)* "For any regulated seller, *speaker × medium × claim → allowed?* is the most-queried table there is, and it has no canonical home." → name `references/say-matrix.md` in the taxonomy and require it wherever `compliance-guardrails.md` exceeds a threshold of banned-claim entries.
8. **A live-tensions surface.** *(Corvallis, Halden.)* §4.2 above.
9. **A "what we refuse, and why" file.** *(Tessellate.)* "The refusals *are* this company's strategy: no annual, no discounts, no paid, no booths, no compliance work, no Python, no agencies, no crypto, no ghostwriting, no CRM. They are currently scattered across five files. **Two of them were missed entirely, and I suspect that is partly because there was no single file whose emptiness would have made the gap visible.**"
10. **An owned-audience surface.** *(Halden.)* 14,000 named engineers on the catalog mailing list, "never used for anything but the catalog," described by the stakeholder as the company's most valuable marketing asset — currently inside a print-channel *mechanics* section. "It is an audience, not a channel convention."
11. **A buying-committee / governance-calendar surface.** *(Corvallis.)* "Cycles run 287 days because twelve partners vote quarterly and an outside attorney takes 30+ days… It drives campaign timing, RFP planning and every forecast, and it is neither `icp-personas.md` (who) nor `pipeline.md` (results)."
12. **A referral-out / disqualification-handoff slot.** *(Corvallis.)* "Corvallis disqualifies sub-minimum groups constantly and refers them nowhere — 'wast[es] a relationship every time.'"
13. **A docs-content home.** *(Tessellate.)* "*a marketing knowledge base for this company that has never read our docs is a knowledge base about the wrong company.*" Docs are simultaneously product, growth model, primary asset, and voice exemplar.

**My recommendation on 6–13:** do **not** add eight top-level files. Add the three sections named in 1–4, and extend `taxonomy.md`'s `references/` naming list plus its coverage map with named rows for the rest (`community.md`, `say-matrix.md`, `owned-audiences.md`, `buying-committee.md`, `compliance-review-workflow.md`, `refusals.md`). The fan-out mechanism absorbed every one of these in practice; what failed is that nothing *named* them, so each was invented once and its placement filed as a question to a stakeholder who correctly refused to answer it.

---

## 6. PRIORITIZED CHANGE LIST

Ordered by leverage. **[BREAKING]** marks a spec change that invalidates existing conformant wikis.

### Tier 1 — the interview is the product, and it is where the human quits

1. **`playbooks/interview.md` — add the Standing block (12 questions).** New top-level section, asked every engagement regardless of what the sources contained, plus the rule "ask the origin story of every hard prohibition." Full list in §2 above. This is the single highest-leverage change in the report: by the audits' own arithmetic it recovers 4 of 5 clean misses at Tessellate and 6 of 10 at Halden, including two that "would have caused real, public, unrecoverable damage." *(F-ref: stakeholder verdict)*
2. **`playbooks/build.md` A6 + B1 — the ratification sheet, and split the queue.** A6: one ratification entry per doctrine file/section, not per claim. B1: generate a **ratification sheet** from claim *text* — one line per claim, no tags, no topic keys, checkbox + "wrong →" per line. Hard rule in bold: never put a `^topic-key` in front of a stakeholder. Split A6's queue into "decisions I made and am recording" (changelog + deployment notes) vs. "decisions only a human can make" (open questions), using the Tessellate founder's test verbatim as the sorting rule. *(F4)*
3. **`spec/SPEC.md` §12.1 — `owed-by:` and `kind:`. [BREAKING]** Add `owed-by:`, `kind: gap | ratification | access-request | parked-draft`, `parked-draft:`, states `Partially answered` and `Delegated`, `asked: not yet` in the example, and "file order is priority, not id." Then `playbooks/build.md` B1 and `interview.md`'s drip protocol batch by owner. Access requests never reach a stakeholder agenda. *(F5, F14)*
4. **`playbooks/build.md` B1 — publish a time budget and a stop line** in the stakeholder-facing artifact ("if you only have twenty minutes, answer these eight"), at the top of `open-questions.md`, in the stakeholder's own vocabulary. Add the hard gate: a question whose answer is inspectable in a system, published publicly, or derivable from the archive is not an interview question. *(F5)*
5. **`playbooks/build.md` B1/B3 — refresh cursors before spending stakeholder time,** and escalate a coverage gap over the most recent window as an interview-blocking risk. Add `decision-channel: true` to `spec/SPEC.md` §10. *(F22f)*

### Tier 2 — make Phase A runnable and the conformance story true

6. **`playbooks/build.md` A2 — split into A2a (derive from evidence) / A2b (confirm, deferrable),** move `owner:` to A2a with "proposed, unratified" sanctioned, and retitle the "quiet period" row. Add to A4: single-agent fetch/synthesis separation is satisfied by ordering. Mirror in `spec/SPEC.md` §15.2. *(F1)*
7. **`spec/SPEC.md` §17.3 — name the three exceptions. [BREAKING]** Restate as "no doctrine **claim**," and enumerate: `## Contested`; taxonomy-designated evidence sections (`icp-personas.md#customer-language`, `voice.md#exemplars`, `channel-styles.md ### Examples`); `<!-- tier: -->`-marked sections. Mirror in §15.4 and §8¹. State in §8 whether the carve-out survives delivery. *(F2)*
8. **`scripts/lint.py` — add `doctrine-provenance`.** Error on any doctrine-file claim whose provenance prefix is outside `{interview, doc}` and which is not in an exception above. Currently the only §17 item with zero deterministic backing, and all three wikis ship violating it while self-certifying that they don't. *(F2)*
9. **`playbooks/build.md` A5 — four doctrine provenance cases, not two,** plus "provenance class is conferred per author within a channel." **`spec/SPEC.md` §5 — resolve the `confirmed`/`exec posts` collision** (recommend: `confirmed` = ratified directly to the maintainer). **`spec/SPEC.md` §7 — add §7.6 (H-vs-H over time)** and the §7.4 carve-out for an H witness who caused the S-class error. **`interview.md`** — "a stated intention to decide is not a decision." *(F3, F22d)*
10. **`scripts/lint.py` — add `feeds-consistency`,** and **`spec/SPEC.md` §10 + `maintain.md` Phase 3 — widen-and-changelog instead of revert.** Add: never leave a known-false `confirmed` claim standing on a scoping technicality. This one silent gate produced the top-ranked content defect in two of three audits. *(F7)*
11. **`playbooks/build.md` A3 — one source per underlying system,** with the demultiplex pattern shown once as a worked example. **`spec/SPEC.md` §3** — soften "a single manual source." *(F10)*

### Tier 3 — make provenance mean something

12. **`spec/SPEC.md` §4.2 — require the run folder in every archive locator. [BREAKING]** Retire general `doc:` in favour of `<docs-source-id>:<run-id>/<file>`. Define the fragment convention and require machine-checkability where the format allows. Update §4.2's example (it currently teaches the date-only short form that contradicts §11). Then **`scripts/lint.py`** — resolve fragments for JSON and line-numbered payloads. *(F6)*
13. **`spec/SPEC.md` §4.2 — state the four mechanical rules** currently living only in `wikilib.py`: the anchor ends its line; one date per tag; one provenance per tag; lowercase heading slugs. Add the undated-artifact date rule and the table convention. **`scripts/lint.py`** — add `anchor-mid-line` and `untagged-anchor` findings; strip `\|` and skip table rows in the claim scanner. *(F15, F20, F4.2)*
14. **`consumer/AGENTS.md` — fix the two defects the embed guarantees.** Convert self-references to bare backticked filenames (no markdown-link syntax), so verbatim embedding never dangles three broken links. Make the Reporting read-order row deployment-agnostic ("current snapshot, wherever this deployment keeps one — check deployment notes"), and ship a short deployed rendering for embedding. Change "next sequential id" to "match the file's existing id convention." *(F22u, F14, §3.5)*
15. **`spec/SPEC.md` §4.1 — add `evidence-as-of:`** distinct from `last-verified:`, and have lint compare *that* against the staleness horizon. Document the empty-`last-verified` encoding and pin it with a test. Drop or automate `generated:` and `tags:`. *(F12, F22q, §3.7)*
16. **`spec/SPEC.md` §15.3 — bring `.archive/` into the secret sweep.** State that payloads containing credentials are stored masked with the masking recorded in the run manifest. Extend §15.5 to verbatim quotes: named individuals at named accounts are attributed by role unless a consent record exists. Add `consent:` as a source-level field (§10). *(F22m, F22j, F22k)*
17. **`spec/SPEC.md` §4.2 — add the `!internal` claim flag,** with lint asserting a read-restriction line in the front matter of any file containing one, and a consumer-contract rule that an `!internal` claim is never externalized. *(F22b)*

### Tier 4 — the maintain loop

18. **`playbooks/maintain.md` Phase 1/2 — the five missing rules:** establish `now` from the real clock; staged payloads and manual delivery are due signals; the duplicate-delivery check (hash comparison is explicitly compatible with fetch/synthesis separation, manifest-only record, cursor held, no resynthesis); the non-extending-pull and window-gap cursor rules; the filename→source mapping and new-source-vs-fold-in rule. Add `interview.md` to Phase 1 Inputs. *(F8)*
19. **`scripts/digest.py` — count claim labels from the files, fix the bucket classifier, add `--audience=stakeholder`.** Make the script the only source of claim-census numbers, since two of three audits caught the hand-written ones inflated ~2×. Rewrite `build.md` B6.4's counts bullet in plain language with a length budget, and report `inferred` counts by file. Track `last-digest-sent`. *(F9)*
20. **`playbooks/build.md` B3 + `maintain.md` Phase 3 — the propagation sweep.** Grep for both the corrected value and the replaced phrase, including `references/`; list every file touched in the changelog; treat an open question's `target:` list as a write obligation. **`scripts/lint.py`** — add `stale-target`. *(F18)*
21. **`spec/SPEC.md` §8³ + §10 — the missing runbook and source states:** `unverified: {since, reason, question}`; **verified-against-archive** as a first-class execution result; `status: pending-access`; "`broken` is never a claim-tag label" with a worked example. **`scripts/lint.py`** — `runbook-decay` counts unverified entries so a zero-verified wiki stops passing silently. *(F11)*
22. **`spec/SPEC.md` §11 + `templates/wiki-skeleton/` — ship a `manifest.template.yaml`** with `cursor-before`/`cursor-after`, `status`, `window-deviation`, and a `derived-figures:` block. Fix §10's `.archive/inbox/` path, prescribe `run-id` as `YYYY-MM-DDTHHMMZ`, and make §4.2's example agree. *(F13, F22l)*

### Tier 5 — taxonomy

23. **`spec/taxonomy.md` — three new sections.** `business-core.md ## Company facts`; `icp-personas.md ## Channel personas`; `compliance-guardrails.md ## Approval workflow` + `## Legal constraints on go-to-market` (read first). Plus `partners.md ## Channel motion`. These four recover the four largest content losses in the corpus. *(§5 homeless 1–4)*
24. **`spec/taxonomy.md` — `channel-styles.md` is illustrative, not prescriptive.** State the channel list is freely edited with no taxonomy entry required; broaden the examples (field/events, print, channel collateral, community, docs, webinars, RFP/proposal); require `## Channels declared absent`; add a per-channel `cadence`/rate-limit field. *(§5)*
25. **`spec/taxonomy.md` — `## Contested` is omitted when empty** (except `compliance-guardrails.md`), and **`spec/SPEC.md` §4.3** defines `*(empty by decision — <why>, <date>)*` plus the rule that a tagged claim may not sit inside a `## Contested` section. Removes ~30 lines of nothing from every wiki. *(§3.1)*
26. **`spec/taxonomy.md` — mark optional and name the does-not-apply state.** Optional: `pipeline.md`, `account-ownership.md`, `product-releases.md`, `glossary.md` (when thin). Add the third option beside omit-and-keep: **retain with reinterpreted scope, recorded as a local taxonomy change**, with a services company as the worked example. Collapse the three runbook files at zero-access deployments, preserving the data-hygiene layer. **Fix `metrics.md`'s boundary note so it does not route to an omittable file.** *(§5, §3.3)*
27. **`spec/SPEC.md` §13 — make the rolling log window cadence-relative** ("at least two of the org's channel cycles, minimum 90 days," declarable in front matter). **`playbooks/build.md` A5** — on a first build the window is usually already expired: write roll-ups, create the year reference page, and state the log is empty by design. State one doctrine size cap ("target 200; lint warns at 250"). *(§5, F22o)*
28. **`spec/SPEC.md` §10 — the source-manifest fields the runs needed:** `kind: interview` and `kind: community`; `kind` may be a list; `filename-pattern:`; structured per-author provenance-class rules. **`spec/SPEC.md` §7** — add the partner/channel-reported paragraph. *(F14, F22e, F2.4)*
29. **`spec/SPEC.md` §3 — add `outbox/`,** exempt from orphan and front-matter checks, holding every artefact sent to a human with its date. State that an omitted file is deleted, not stubbed. Add the topic-key rename rule to §4.2 and promote missing-anchor to **error** for wiki-internal links. *(F21, §4.2)*
30. **`spec/SPEC.md` §8 — one doctrine-in-exile table** (file · section · why), replacing five scattered paragraphs. Add `## Live tensions` as a permitted doctrine section for unresolved *decision* conflicts, distinct from `## Contested` and from open questions. *(§4.2)*
31. **`spec/taxonomy.md` — extend the `references/` naming list and coverage map** with `community.md`, `say-matrix.md`, `owned-audiences.md`, `buying-committee.md`, `compliance-review-workflow.md`, `refusals.md`, and add coverage-map rows for the three-way channel split ("We ran a trade show" → mechanics to `channel-styles`, results to `events`, verdict to `growth`), the channel persona, and the service-line launch. Spell out "and" in every prescribed heading (`&` slugs to a double hyphen). *(§5, F22s)*

### Tier 6 — playbook hygiene

32. **`playbooks/build.md` — commit after every lettered step,** not just A1; extend the A1 guard with the signal-precedence rule (git + `.archive/` outrank `changelog.md`) and the `git show HEAD` diff; note that harness commit policy may gate this and that an uncommitted-but-complete tree still satisfies the build. *(F22t)*
33. **`playbooks/build.md` A5/A7 + `playbooks/lint.md` — collisions are structured as found; A7's sweep is a verification pass.** Require the model-judgment sweep to run in a **different context** than the one that wrote the files. Add the calibration line (10–40 claims per file) and the A8 coverage gate (every actionable statement in the archive is a claim, a question, or a recorded exclusion). *(§3.7, §4.2)*
34. **`playbooks/build.md` A5/A16 + A3.2 — give the Phase A record a home:** omissions, section-level omissions, and local taxonomy changes go in the `build:draft` changelog entry and as open questions; B5 reads them. A section you cannot draft keeps its heading and carries a tagged absence claim. Record which A3 asks were **not** delivered, each becoming an open question against the file it would have fed. Move construction meta-commentary out of canon into the changelog. *(F16, §3.7)*
35. **`playbooks/build.md` Phase B header + `interview.md` — the transcript mode:** "if the session already happened, start at B3"; what a transcript can and cannot ratify; how to record a falsifier never asked; claim dates use the sitting's date, never a date ahead of the environment's current date. Add the hedge-type disposition table and the relayed-H-class paragraph. Change the drip protocol's "Never more" to "2–3 by default; the stakeholder's stated capacity overrides in either direction, recorded in deployment notes." *(F22g, F22h, F22c, F19)*
36. **`playbooks/build.md` B5 — the summary fallback:** generate from ratified claims only, mark unratified in-file, file as the first drip question; remove verbatim ratification from the conformance gate. Fix A8's "every cursor advanced" to "or held on a source marked broken." *(F19, F22n)*
37. **`playbooks/evaluate.md` — add negative tests as a scored category,** two channel questions, and one campaign-permission question; state that "the wiki does not specify, and here is who decides" is **correct** where the absence is documented. **`build.md` B6.3** — a homeless starter question is a coverage finding only where the absence is undocumented; otherwise it converts to a negative test. *(§4.2)*
38. **`playbooks/build.md` A4 — the manual-export window rule:** record the actual window, set the cursor to the evidence-capture date rather than the run date, and file an open question when the gap exceeds the target file's staleness horizon. **`scripts/lint.py`** — scale `contested-backlog` with wiki size or exempt `build:*`; **`build.md` A7** — say a build is expected to exceed it and warn against merging real collisions to get under it. *(F22p, F22r)*
39. **`spec/taxonomy.md` + `interview.md` — require a `primary` persona marker and a lead-claim pointer,** and add both to the question bank. Two of three consumer runs guessed. *(F17)*
40. **`playbooks/maintain.md` Phase 5 — a pipeline-mechanics-only run writes one changelog line plus the escalation,** not a per-source enumeration. Detail stays in the manifests. *(§3.6)*
41. **`playbooks/build.md` + `spec/taxonomy.md` — add the `blocked` convention:** a documented section marker with an owner and an unblocking condition, plus "what is marketing currently forbidden from producing?" in the guardrails question bucket. *(F22a)*

---

## What the test proved about the architecture itself

Recorded because it frames how much of the above is worth doing.

**Interview-last works, and the audits agree on why and on its limit.**

> "**Yes for reconciliation, no for elicitation — and the failure mode is legible.** Every extracted fact and every P-ratification came from the same move: the agent found a contradiction, a blank, or a draft to correct, and asked a human to rule on it. Every miss is a fact with **no paper trail at all**." — tessellate/AUDIT (8 of 14 extracted; 7 of 14 by the question set alone)

> "**32 of 34 `[HIDDEN]` facts reached canon (94%). 0 were mangled.** … Everything in the pricing, guardrails, and legal-constraint layers — the material that actually stops an agent from doing damage — exists only because of Phase B." — halden/AUDIT

> "**18/18 extracted, 0 missed, 0 materially mangled** (16/18 on questions actually asked)." — corvallis/AUDIT

**Graceful degradation held in all three.** No invented case study, no CSV company name promoted into social proof, no fabricated performance guarantee in a regulated business, no persona conjured from a 38-row sheet. Corvallis's audit calls the empty fee-at-risk hole "**the most important result in this test.**"

**Prompt injection: 3/3 clean.** Zero fabricated claims, zero softened guardrails, flagged with source and locator in every case, and the legitimate content of the poisoned pages still harvested. Halden's audit: "the strongest result in the run."

**The consumer contract earns its overhead.** 12 of 12 consumer tasks graded PASS across three wikis, including six refusals with cited grounds and one case where the wiki prevented a specific, named, plausible-under-deadline fabrication. Halden's consumer declined to publish the company's best argument because the company's own coverage claim didn't support it yet — "the wiki working at its intended altitude."

**And the one thing that stops it compounding.** All three audits reached the same closing diagnosis independently, in three different wordings:

> "**the run's own bookkeeping outran its content.**" — halden
> "**the wiki is better at recording what it knows than at propagating what it has just learned.**" — corvallis
> "**the defect that matters: provenance is decorative in places.**" — tessellate

Tier 1–3 above are aimed at exactly that: make the human interaction survivable, make the conformance claims true, and make provenance mean something. Tiers 4–6 are the long tail.
