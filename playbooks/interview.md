# Interview Playbook

**Converts human knowledge into H-class claims.** Two modes, one output:

- **Build gap interview** — session(s) run from Phase B of [build.md](build.md), covering the agenda drawn from `open-questions.md`; live, or applied afterward from a transcript (see Session mechanics below).
- **Drip interview** — the standing maintenance loop: 2–3 questions per digest cycle, answered asynchronously.

Both produce claims labeled `confirmed | interview:<person> | <date>`, applied through the write matrix (SPEC §8), with questions moved to Answered. The agent running this playbook is the maintainer — the single writer of canon. Nobody else applies interview answers.

Read [../spec/SPEC.md](../spec/SPEC.md) §5–§8 and §12.1 first; the question bank below is organized by [../spec/taxonomy.md](../spec/taxonomy.md).

---

## Principles

1. **Confirm drafts; never ask blank-page questions.** Blank pages are expensive for the human and vague for the wiki. Evidence exists for almost everything — present it and ask for a yes/no/correction.

   | Blank-page (don't) | Confirm-the-draft (do) |
   |---|---|
   | "What's your positioning?" | "The evidence suggests you win on time-to-first-dashboard — days, not weeks. Would you put that sentence on the homepage?" |
   | "Who's your ICP?" | "Your last twenty wins skew heavily to Series-B fintech with an in-house data team. Is that the target, or an accident?" |
   | "What's your brand voice?" | "I drafted this paragraph in what I think is your voice: ⟨exemplar⟩. Would you ship it as-is?" |

2. **One topic at a time.** Finish a bucket before opening the next. Context-switching costs the stakeholder accuracy and costs you clean provenance.

3. **Capture verbatim language.** Exact phrases — quoted, attributed — are first-class evidence. They feed `icp-personas.md#customer-language` (phrases as evidence) and `glossary.md` (the rulings). When the stakeholder says "our customers call it the Monday scramble," the quote is the asset; your paraphrase destroys it.

4. **Read back before you write.** The read-back is the ratification event: what enters the wiki is the sentence they accepted, not your memory of their answer. If they hedge — "more or less," "usually" — the claim is not `confirmed`; tighten the wording with them or park it as an open question.

5. **Standing matters.** H-class means a human with standing, speaking for the org (SPEC §7). A CMO ratifies positioning; an SDR's view of the ICP is valuable evidence but not doctrine ratification. Without standing the answer is not H, so the write matrix bites: it enters as an open question routed to whoever can ratify it, and as an `inferred` claim only where the matrix already permits an I-class write — a state file, never a new doctrine claim. Know before each session who can ratify what.

6. **The system might be right.** When an answer contradicts S-class evidence about internal systems, say so in the moment ("the CRM report shows 45 days — you're saying 90 above 20 seats?"), record **both** as a contested entry with a resolution path (SPEC §4.3, §7.4), and never silently prefer the human on system facts. For doctrine, the reverse: H supersedes, because doctrine records decisions and only humans make decisions.

7. **No mechanics on stage — including in writing.** Never say claim tag, provenance, front matter, lint, or git to the stakeholder. Say: "I'll note that." "Here's what I have so far." "Should I treat that as a rule going forward?"

   This binds every artifact a human reads, not just what you say out loud. `open-questions.md` and the digest are stakeholder-facing documents: no `H-class`/`O-class`/`S-class`, no `watchlist`/`source-backed`, no `^topic-keys`, no `doctrine-in-exile`, no SPEC section numbers, no playbook step codes (`A5`, `B4`). Tested stakeholders hit a dozen such terms in a single reading pass, and the reported effect was not confusion but **distrust** — "it reads like a system talking to itself in front of me." One reviewer measured 15% of the file they were asked to read as addressed to the software. Write the internal vocabulary in the changelog, where it belongs.

8. **The falsifier follow-up.** After any confident answer on something consequential, ask: **"What would make this claim false?"** — or its natural forms: "What would have to happen for you to change this?" "Which deal, if you lost it, would prove this wrong?" It turns assertions into bounded claims, surfaces hidden conditions worth their own entries, and gives future lint runs a doctrine-drift tripwire.

9. **Route by respondent before importance.** Sort the agenda by *who can answer*, not by what matters most. Every question carries an `owed-by:` — the person or role who can actually answer it — and each human sees only their own list. Across three test companies, 15–25% of questions were pointed at the wrong human, and it was the single largest complaint: executives asked for tool logins, for a conference date, and in one case for permission to read the company's own public website.

   **The gate:** a question whose answer is inspectable in a system you can reach, published publicly, or derivable from the archive **is not an interview question.** Access requests (credentials, URLs, view permissions) never enter a stakeholder agenda — collect them as a one-line checklist. Filing decisions about the wiki's own structure are never interview questions — including whether a new top-level file should exist, whether an omitted file should come back, and whether a file should be reinterpreted. The maintainer runs SPEC §3, records the reason, and moves on. When you have already made the correct call and merely want cover, that is not information-seeking — write down that you decided it.

10. **Never put a topic key in front of a stakeholder.** Ratification happens on **claim text**, one sentence per line, with a checkbox and a "wrong →" field. A list of anchors like `^jobs-to-be-done` is unanswerable, and asking for bulk ratification in that form was the most-cited reason a tested stakeholder would have abandoned the session: "that's not a question, that's homework with a question mark on it." Ratify per file or per section, never per claim, and send long sheets async rather than spending live time on them.

11. **Publish the cost and the stop line.** Say at the top, in their words, how long this will take and which questions matter most: *"About forty minutes. If you only have ten, answer the first five — the rest can wait for next week."* Tested sessions ran to 2h20m with no estimate given, and the triage list that did exist was filed in a document addressed to another agent. Order the file so priority is position: most important first, and say so.

## Session mechanics (live mode)

**Before:** agenda from `open-questions.md` Active, sorted by why-it-matters, grouped by taxonomy file; drafts in hand for every ratification item; standing check on who's attending.

**During:** one bucket at a time; gaps first (they need discussion), ratifications second (they're fast); read back every answer; quote verbatim phrases; stamp each question `asked: <date> (session)`. In build mode, close by ratifying the `AGENTS.md` three-sentence summary verbatim and confirming digest recipient and cadence.

**After, same day:**

1. Apply every accepted answer per the write matrix: label `confirmed`, provenance `interview:<person>`, date = session date.
2. Promotions (`inferred → confirmed`) cite the interview and land in the changelog (SPEC §5).
3. Conflicts with S-class evidence → `## Contested` entries with resolution paths, each linked to an open question.
4. Move answered questions to Answered with `applied-to` links; file new questions raised in-session as Active.
5. One changelog entry per session (SPEC §12.2).

## Session mechanics (transcript mode)

Not every session is run live — Phase B sometimes hands the maintainer a transcript of a conversation it wasn't in. Everything above still governs *what* gets written; this covers what changes about *how*.

**What a transcript can ratify.** Only an answer the transcript shows was actually given, on the record, to a question about the wiki's content: an explicit yes, a correction, a clear ruling. Silence, a change of subject, or the conversation moving on is not agreement — do not backfill a read-back that never happened.

**What a transcript cannot ratify.** Principle 4's read-back requires asking "does that sound right?", which a transcript cannot answer after the fact. A sentence merely proposed, floated, or drafted aloud with no clear yes stays unratified — `inferred` at most, with an open question, never `confirmed`.

**A stated intention to decide is not a decision.** "I'll write it down and then we'll change it," "we should probably move off that," "remind me to revisit this" — none of these are the org's decision, however confidently said. This mirrors SPEC §7.6 exactly: the prior doctrine stays binding, the doubt goes to `## Contested` with an open question, and the wiki keeps serving the last actual decision until a new one arrives. Reading for this is most of the judgment call in transcript mode, because a recorded conversation captures far more thinking-aloud than a live session's read-back ever surfaces.

**Recording a falsifier that was never asked.** The falsifier follow-up (principle 8) needs a live back-and-forth a transcript can't supply retroactively. Don't invent an answer, and don't silently drop the discipline — file it as its own open question (`kind: gap`, `owed-by:` the person who gave the original answer, `why-it-matters: no falsifier was ever asked for this claim`) so the next live or drip session asks it. The claim still enters the wiki on the strength of what was actually said; the missing falsifier is a flagged gap, not a blocker.

The **After, same day** steps above still apply once you've settled what the transcript actually ratified.

---

## The standing block — ask these every engagement

**Ask all twelve, every time, no matter what the sources contained.** The rest of this playbook builds its agenda by finding contradictions and blank sections — which means it can only ask about things somebody already wrote down. The facts that do the most damage when missing were never written anywhere, so they produce no contradiction and no blank, and a gap-driven agenda is structurally blind to them. In testing across three companies, every single miss was of this shape, and this block recovers most of them.

1. Are there agreements that constrain who we may sell to or market to — territorial rights, rights of first refusal, exclusivity, channel terms?
2. Do we sell under anyone else's brand, or does anyone sell under ours?
3. What does it cost? The actual numbers — and separately, what may be said about them publicly?
4. Which languages and geographies do we sell in, and who is allowed to author in each?
5. Who approves what, on what turnaround, before anything ships?
6. Which number do you actually run the company on? (Not the ones on the dashboard — the one you check first.)
7. Which surfaces are you personally the only allowed voice on — and may an agent post anywhere at all, or only draft?
8. How often may we use your most expensive channel? Is there a rate limit or a cadence cap?
9. Does anyone get declined for a reason that isn't written down?
10. What works that isn't written down? What's in the budget you'd rather not itemize, and why?
11. What is marketing currently forbidden from producing, and what would unblock it?
12. Which agent task should this wiki serve first?

**And one rule that applies throughout: ask the origin story of every hard prohibition,** not just the ones a source happened to explain. Rules without their stories get relaxed by the next person in the job — so record why the rule exists alongside the rule itself.

Answers here are H-class. Questions 1–5 and 11 frequently produce `compliance-guardrails.md` content, which is the file with the least tolerance for gaps.

## Question bank

A quarry, not a script. Pull only the buckets with Active questions or blank sections; skip everything the archive already answered. Within each bucket, questions are ordered gap-filling first, ratification second; each closes with its falsifier.

### `business-core.md`

1. Explain what you sell to someone at a barbecue — no product names allowed. *(Also a verbatim-language capture.)*
2. When you win a competitive deal, what's the real reason — the one sales says internally, not the website version?
3. Where does that advantage run out? Which deals *should* you lose?
4. What may we say about pricing in public — numbers, ranges, or nothing?
5. Which claims are you comfortable making on the record, and what backs each one?
6. Of those, which one leads — the **lead claim** that should head a capability announcement if you can only lead with one?
7. First call to signature — how long? Does that change above ⟨threshold seen in the CRM⟩?
8. Read-back: "Here's the positioning sentence the evidence supports: ⟨draft⟩. Would you put it on the homepage?"

*Falsifier: "Which deal, if you lost it, would tell you this positioning is wrong?"*

### `icp-personas.md`

1. Name the last three customers you were genuinely glad to win. What do they have in common?
2. Who should sales hang up on, even with budget in hand? What happened the last time you took one anyway?
3. The day before a buyer finds you — what are they doing about the problem?
4. What words do customers use for the problem? Not your words — theirs. *(Verbatim capture; quote and attribute.)*
5. Which objection actually kills deals, and which is just noise reps complain about?
6. Is one persona `primary: true` across the board, or does the right one depend on channel? If it depends on channel, which persona does each channel default to?
7. Read-back per persona: "⟨Role⟩ feels ⟨pains⟩, buys after ⟨trigger⟩, objects with ⟨objection⟩ — right? What did I miss?"

*Falsifier: "Which current customer breaks this definition — and are they a mistake or a signal?"*

### `voice.md`

1. Show me one past piece that sounds exactly like you, and one that misses. What's the difference?
2. Give me three to five words for how the brand talks — each with a "but not" ("confident, but not cocky").
3. What would you never let the brand say — words, jokes, postures?
4. Where does the voice flex — a support reply vs. a launch post vs. delivering bad news?
5. Read-back: "I wrote this in the drafted voice: ⟨exemplar⟩. Would you ship it unedited?"

*Falsifier: "What copy would pass every rule we just set and still be wrong for you?"*

### `channel-styles.md`

1. Which channels are actually alive right now — and which exist but are dormant?
2. For each live channel: the best-performing piece last quarter — what made it work?
3. What would a new hire get wrong — link policy, hashtags, emoji, send times, sign-offs?
4. How often is too often, per channel?
5. Read-back per channel: "⟨drafted rules⟩ — anything there you'd veto?"

*Falsifier: "What followed all these rules and still flopped — and what does that tell us?"*

### `compliance-guardrails.md`

The strictest file in the wiki; a contested entry here is an urgent open question. Get names and dates. **Ask the origin story of every hard prohibition here, not just the ones a source already explained** — a rule with no story gets relaxed by the next person in the job.

1. What must marketing never claim? For each: what happened — or what could?
2. Does any regulator, law, or contract bind your copy — financial-promotion rules, health claims, data-residency promises, platform terms?
3. May we name competitors? Compare against them? Under what rules?
4. Trademark and naming rules — for your marks and theirs?
5. What is embargoed right now, and when does each embargo lift? *(Every entry carries an expiry.)*
6. What customer data must never appear in outbound, even anonymized?
7. Who is the human to escalate to when something looks borderline?
8. What is marketing currently forbidden from producing right now, and what unblocks it? *(A live one gets a `blocked` marker — name the owner and the unblocking condition.)*

*Falsifier: "Which of these bans has an exception — and who alone can invoke it?"*

### `glossary.md`

1. Say each product name exactly as it should be printed. Which abbreviations are banned?
2. For each core concept, what's *our* word — and which near-synonyms do we deliberately avoid?
3. Which customer words do we translate into our vocabulary, and which do we adopt as-is?
4. What makes you wince in a draft, and what should replace it?

*Falsifier: "Which term do people inside the company still get wrong?"*

### `growth.md`

1. Your last ten customers — where did each actually come from? *(Their memory, not the attribution dashboard; differences feed contested entries.)*
2. Which channels get real money and time this quarter, and what's the thesis for each?
3. What's the current verdict on each bet — working, jury out, dying?
4. How is the target-account list defined, and who owns it?
5. Which campaign types recur, and what is each supposed to produce?
6. What did you try, kill, and would never retry?

*Falsifier: "Which number going flat for a quarter would change this mix?"*

---

The five buckets below cover **doctrine-in-exile** — sections that record decisions while sitting inside state and runbook files, and so inherit doctrine's write rules whatever tier their file declares (taxonomy boundaries). Nothing in them can be sourced; each one exists because only a human can answer it, which makes them the highest-yield questions in the bank.

### `competitors.md` — counter-positioning (doctrine-in-exile)

Everything else in this file is evidence-driven; these sections are the decision layer — how *we choose* to win — and only humans decide. The maintainer may never rewrite them from external evidence, only annotate.

1. Who do you actually lose to? *(Contrast with the drafted tracked list — they usually differ.)*
2. For each real rival: when you win head-to-head, why? Is that verified by wins, or belief? *(Belief still ratifies as the decision — but flag a win/loss data check as its resolution path.)*
3. What question should a rep plant that only you answer well?
4. What's off-limits when talking about them?
5. Read-back per battlecard: "How we win against ⟨X⟩: ⟨draft⟩ — sign off?"

*Falsifier: "Tell me about a deal where this play failed."*

### `product-releases.md` — roadmap clearances (doctrine-in-exile)

Absence is the guardrail: anything not cleared here does not appear in the wiki at all.

1. What's coming that marketing may reference externally — and in exactly what words?
2. What's the expiry on each clearance — a date, or an event?
3. What must never be mentioned, even if a prospect asks directly?
4. Who clears roadmap mentions from now on?

*Falsifier: "If the timeline slips a quarter, which of these clearances die?"*

### `customers.md` — reference approvals (doctrine-in-exile)

1. Which customers have approved public use — and precisely what: logo, quote, named case study?
2. Where is each approval recorded? *(That record becomes the claim's provenance — `doc:<file>` beats memory.)*
3. Are any logos or quotes in circulation that shouldn't be?
4. The numbers in your success stories — customer-approved, or internal estimates?

*Falsifier: "Which reference would you not want a prospect to actually call?"*

### `partners.md` — co-marketing allowances (doctrine-in-exile)

1. Which partners allow joint public marketing — and what exactly: logo swap, co-branded content, joint announcements?
2. How may each relationship be described — "partner," "integration," something weaker?
3. Is any partner sensitive about the relationship being public at all?
4. Which marketplace or platform listings actually matter to your distribution?

*Falsifier: "Which partner would object to how you currently describe them?"*

### `metrics.md` — KPI definitions (doctrine-in-exile)

The definitions are decisions; the queries that compute them are runbook and get verified by execution, not by interview.

1. For each number leadership watches: what exactly counts, and what doesn't? ("What is a 'qualified lead' here — and who disagrees?")
2. Who owns each definition?
3. Where do two dashboards disagree today, and which one is right?
4. Which of your own metrics do you not trust, and why?

*Falsifier: "If two systems disagree on this KPI next month, which one is wrong by definition?"*

---

## The drip-interview protocol (maintenance mode)

The standing loop that converts `inferred` into `confirmed` and drains the contested backlog — the mechanism behind SPEC §5's transitions and the fourth leg of §8's safety net. It runs on the digest cadence, forever.

| Step | Rule |
|---|---|
| **Source** | `open-questions.md` Active, grouped by `owed-by:` first — each stakeholder gets only their own batch, never someone else's queue — then ranked by why-it-matters within it. `kind: access-request` entries never reach a stakeholder agenda; route them to ops as a one-line checklist instead (principle 9). |
| **Batch** | 2–3 questions per digest cycle by default. The stakeholder's stated capacity overrides in either direction — more if they've asked for more, fewer if they haven't — and the override is recorded once in `AGENTS.md` deployment notes, not re-negotiated every cycle. |
| **Form** | Every question ships with its draft answer where one exists, so replying can be "yes / no / here's the correction." Confirm-the-draft survives going async. Prefer 2–3 questions on one topic over three scattered ones (principle 2 survives too). |
| **Channel** | The org's chat channel, or a reply to the digest itself — whichever `AGENTS.md` deployment notes name as the digest channel. |
| **Mark asked** | Stamp the entry `asked: <date> (digest)` per SPEC §12.1. |
| **Apply** | Answers are H-class regardless of medium — digest replies and chat answers from a human with standing count (SPEC §7). Write per the matrix: label `confirmed`, provenance `interview:<person>`, date = answer date. Promotions land in the changelog. |
| **Close** | Move the question to Answered with `applied-to` links naming every file the answer touched. One changelog entry per application run. |
| **Conflict** | An answer contradicting S-class evidence → contested entry with a resolution path; the question stays Active, re-scoped to the resolution path. Never silently overwrite system facts. |
| **Escalate** | Unanswered past 2 cycles → move to Stale (SPEC §12.1). In the next digest, do exactly one of: re-ask once, rephrased smaller; reroute to a different human with standing; or propose dropping it. Stale doctrine ratifications are flagged in the digest as standing risk — consumers are acting on unratified drafts. |

Discipline notes:

- A drip question spends stakeholder goodwill; a question the archive could have answered spends it for nothing. Check the archive first, every cycle.
- Verbatim capture applies async too: quote chat replies exactly when they feed `customer-language` or `glossary`.
- The falsifier follow-up still applies — attach it to the batch's most consequential question, not to all of them.

## What a good interview leaves behind

- [ ] Every accepted answer written as `confirmed | interview:<person> | <date>`, per the write matrix
- [ ] Verbatim phrases quoted into `icp-personas.md#customer-language` and `glossary.md`
- [ ] Contested entries for every human-vs-system conflict, each linked to an open question
- [ ] Answered questions moved with `applied-to` links; new questions filed as Active
- [ ] A changelog entry per session or application run
- [ ] Build mode only: the `AGENTS.md` three-sentence summary ratified verbatim
