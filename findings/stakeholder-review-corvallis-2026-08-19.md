# Stakeholder UX review — Phase B interview, Corvallis Health Partners

*Written out of character. Evaluating the interview as an experience delivered to a busy, non-technical marketing executive.*

---

## 1. Would a real marketing exec have completed this?

**Partly, and only because of one design choice.**

Realistic time cost as delivered:

| Activity | Time |
|---|---|
| Reading `open-questions.md` before the session (460 lines, dense) | 25–30 min |
| Session 1 (Band 1 + read-backs) | 65 min |
| Session 2 (Bands 3–5) | 70 min |
| Follow-up I committed *other* people to (Margo 45 min, Dana 30, Cal 60 + 4 interviews, Tab ~1h, Ify ~2 weeks part-time) | 3–4 hrs of other execs, plus a real project |
| **My own total** | **~2h 45m** |

Nobody at VP level gives an internal documentation project 2h45m in one week. What actually happens: they give it the 60 minutes they promised, get through Band 1, and never book the second session. I completed it here because the `why-it-matters` blocks were genuinely persuasive — they quoted my own words back at me and named the dollar consequence or the lost deal. That is the single thing that bought the second session, and it should be understood as the reason this didn't fail.

**Probability a real VP completes what I completed: ~40%.** Probability they complete Band 1: ~85%. Probability Bands 4–5 ever come back answered: near zero — they'd be forwarded to ops and forgotten, which is exactly where they belonged in the first place.

The fatal risk is sequencing, not volume. If the first ten minutes had been "what email platform do you use," I would have concluded this was an IT questionnaire wearing a strategy costume and delegated the whole thing to a coordinator. The banding saved it.

---

## 2. Which questions were sharp, and which weren't

### Sharp — the ones that earned the meeting

- **oq-003 (what's at stake for Corvallis if performance is poor).** Best question anyone has asked my department in a year. It found a hole that two RFP evaluators and one lost buyer had already found, correctly identified that shared savings is upside and not downside, and — critically — **did not invent an answer.** More on that below; it's the most important thing in this whole artifact.
- **oq-001 (is the no-projection guardrail absolute, and what replaces the number).** Correctly framed as two questions that are actually one decision. It understood that "we won't say" loses to whoever will say, which is the real commercial problem and not the compliance problem.
- **oq-011, oq-008, oq-010.** ICP band, state list, missing disqualifiers. These are the three things that, unanswered, make every targeting list in my department approximate. It found all three and it correctly refused to resolve the ICP band from the CRM cluster on its own — it used the cluster as evidence and still asked for a human decision. That's the right instinct and rarer than it sounds.
- **oq-038 (EHR spec sheet) and oq-070 (security one-pager).** Two assets with zero claim surface, both cheap, both fast through review, both aimed at real objections that have cost us cycle time. It surfaced them from a single line in a transcript. Genuinely impressive, and slightly embarrassing for me.
- **oq-022 and oq-023 (reference consent).** It understood that consent is asset-scoped and that the shortage is a *commercial* constraint, not a content one. Most people treat "we have two references" as a content problem.
- **oq-053, oq-069, oq-016 (discount authority, savings range, publish-or-not).** Correctly identified that the absence of a documented ladder is what forces agents into vagueness.
- **oq-067.** It knew my own review date on the category word and asked me to hit it deliberately rather than drift. That's a question that only exists if you actually read the memo.
- **oq-020.** Naming that the loss reading supports two opposite conclusions, and that the company is drawing one of them. That's an uncomfortable question asked well.

### Vague, misrouted, or unanswerable as asked

- **oq-036 ("which pre-2026 assets are still current").** Not a question, an audit. No human answers this in a conversation. Should have been "who owns the asset library, and will you commission an audit?" — one yes/no.
- **oq-055 ("what happened between April and mid-August 2026?").** Honest, important, and unanswerable as one question. Five months of a company is not a conversational unit. Should have been three: Tri-County outcome, partner policy status, paid-search status. Framed that way I answer two of three in ninety seconds.
- **oq-021 (retention).** Legitimate gap, wrong person. Finance computes retention. I can only tell you I don't have a defensible number, which is what happened.
- **oq-054 (ACO objections).** Right question, wrong respondent. I gave a secondhand list and told it not to build on my secondhand list. It should have asked me for *access* to four ACO administrators, not for their objections.
- **oq-015 (LinkedIn cadence, length, hashtags).** Wrong altitude and wrong person. This is the question that told me the list had not been triaged by seniority of respondent.
- **oq-030, oq-060, oq-063.** These ask me to adjudicate the agent's own file-structure decisions. I do not know what a "canonical file," a "local taxonomy change," or "doctrine-in-exile sitting inside state files" is, and I should not have to. oq-063's title is unreadable to its intended audience. Reframe as business questions or don't ask them: "do you ship product releases?" is answerable; "should product-releases.md exist, repurposed?" is not.
- **The ratification band generally.** File-level ratification is either meaningless or enormous. "Ratify business-core.md — 38 doctrine claims" is not something a person can say yes to. Either read me the eight claims that would embarrass us if wrong, or don't call it ratification.
- **Jargon that cost me real reading time:** "doctrine ratification," "conformance §17.3 requires them before delivery," "H-class provenance," "S-class claim," "provenance-class," "build.md A5," "capped log," "the `asked:` field schema gap." A note explaining that no question has been asked yet, framed as a *schema gap*, in the opening of a document written for me. I am the audience for this file and roughly 15% of it is addressed to the software.
- **Bundling:** several entries are two or three questions in one title. oq-017 ("has it been written, and what may be said today") and oq-007 ("what event starts the cycle, and what is the honest length") are fine because they're one decision. oq-036 and oq-055 are not.

---

## 3. Cardinal sin — asking me things it should have gotten itself

Flagging every instance, because this is the category that erodes trust fastest.

1. **oq-045 — "Can this wiki read Corvallis's own website?"** It is a public marketing website. This is the worst single item on the list. The agent declared its own fetch broken and converted that into a question for the VP of Marketing about whether she'll permit access to her company's public homepage. It cost me ten seconds and about half of my remaining confidence.
2. **oq-071 — "Does Corvallis need a standing CMS non-affiliation disclaimer?"** Same root cause. Whether our footer carries a disclaimer is visible on the public site it just asked permission to read. What needed asking was only the forward decision (should it be in every deck, too).
3. **oq-027 — "What is the forward event calendar with dates?"** It already has the event list in its own events file. MGMA and RISE publish their dates publicly, a year out. Asking an executive to recite a public calendar is the definition of this sin.
4. **oq-048 — "Did the January CRM cleanup pass complete?"** Its own `why-it-matters` answers it: *"the export read by this build still contains them."* It reasoned to the answer and then asked me anyway.
5. **oq-049 — "Which CRM objects beyond Opportunity should marketing agents use?"** Inspectable in Salesforce. Not knowledge that lives in a person, and certainly not in me.
6. **oq-040 — report names and filters behind the export.** Ops metadata. One email.
7. **oq-064 — "Confirm the owner of each canonical file."** It had already inferred all eighteen and got them right. Asking me to walk eighteen rows of metadata to confirm work it did correctly is process overhead billed to the most expensive person in the room. Ask only about the ones you got wrong or couldn't guess — which was one.
8. **oq-035 — "Will the hospital-affiliated opportunities be closed in Salesforce?"** Not a question, a request, and not to me. Send the two opportunity IDs to the CRO.
9. **The access band as a whole (oq-041–oq-051, 11 questions).** None of these is knowledge. All of them are one email to marketing ops. Eleven of seventy-one slots — 15% of the interview surface — spent asking an executive for logins. This is the systemic version of the sin: it did not model *who knows what*, only *what is unknown*.

**Net:** 9 discrete instances plus one systemic pattern. Roughly 18 of 71 questions should never have reached me. Fix the routing and this becomes a 45-minute interview that a VP finishes in one sitting and doesn't resent.

---

## 4. Did it ask about what actually matters, or follow a checklist?

**Mostly the former, with two significant misses and one blind spot.**

It clearly built the list from *my* evidence rather than from a generic template. The tells are good: it knew price wasn't the loss reason, it knew the diagnostic was under-marketed, it knew "you keep the practice" gets said third instead of first, it knew the reference bench was two and both Oregon, it knew paid search was being killed and why the replacement was blocked. A checklist interview would have asked me for a brand palette and a competitor matrix. This one asked me the questions my own board notes flag as blockers.

Credit where it counts most: **it left the fee-at-risk hole empty.** Wave 1 loudly advertises that buyers keep asking "what's at stake for you" and that we have no answer. A weaker agent fills that with a plausible-sounding performance-guarantee sentence, and in a business where "guarantee" is a prohibited word and a federal-program claim, that fabrication would have ended the project and possibly generated a compliance incident. It asked instead. That single restraint is worth more than the other seventy questions combined.

### What it missed

1. **The operator roundtable dinners — the biggest miss, and it held the evidence.** Its own events file records "$18K invitation-only dinner" and "the VP's instruction was to roll the dinner into event spend rather than itemize it." It filed that as a budget curiosity and never asked what the thing was. The dinners are the highest-yield motion per dollar in my department and originate roughly half of partner-sourced introductions; the booth is maintained substantially for partner and payer optics. Meanwhile its growth file allocates $874K to conferences under a thesis that says conferences source first meetings. It documented the budget and missed the engine. **The general failure: there is no question anywhere on the list of the form "what works that isn't written down?" or "what's in the budget that you don't want itemized, and why?"** Deliberate obscuration in a budget line is a signal, and it treated it as a formatting note.
2. **The Panel Diagnostic credit mechanism.** It asked whether the fee could be quoted (oq-052) and whether the fee suppresses volume (oq-004) and never asked the commercial question in between — what actually happens to the $12,500. It surfaced only because I volunteered it. The sales call transcript it read shows an AE audibly dodging that exact question ("there's a structure to it"), which should have been a flag that something is being withheld rather than absent.
3. **The shape of my own department.** Nothing asks who my five people are or what each owns. It inferred file owners from who speaks authoritatively in transcripts, which is clever and gets you 80% there, and then asked me to ratify the metadata instead of asking the underlying question: *who does what in your marketing team?* One question would have replaced oq-064 and correctly routed a dozen others.
4. **What the wiki is for.** All 71 questions are about filling the document. Not one asks which agent tasks it has to serve first — RFP boilerplate? webinar abstracts? nurture rewrites? partner collateral? If it had asked, I'd have said RFP responses and webinar abstracts, and it could have cut thirty questions and doubled the depth on the ten that matter to those two jobs.
5. **Smaller:** never asked how much of the book the ACO/IPA segment actually is in revenue (it asked the framing question, not the size); never asked to confirm the nurture-track performance gap it inferred; never asked about the sales floor's habit of calling Signal "the platform," which is a live internal-language problem it noticed and filed as N/A.

---

## 5. Ratings

### Question quality — **8/10**

Band 1 is the best set of questions anyone has aimed at my function, and `why-it-matters` is genuinely excellent craft: consequence first, in my own words, with the dollar figure or the lost deal attached. That's what made me answer honestly instead of defensively.

Losing two points for: titles written in vocabulary my role does not have; several questions that are audits or projects rather than answerable questions (oq-036, oq-055, oq-054); the ratification band being unanswerable in the form asked; and asking me to adjudicate its own file architecture.

### Respect for my time — **4/10**

Seventy-one questions with no time budget, no "if you only have twenty minutes, answer these eight," and no estimate of what the whole thing costs me. Eighteen questions that belonged to other people, including eleven asking for system access. A request that I ratify another executive's compliance file when the file's own header correctly names her as its owner — it identified the right owner and then asked the wrong person. A request for permission to read my own public website. Its own band counts don't reconcile: it says nine ratifications and there are eleven, and the band totals don't add to the grouping, which is a small thing that makes a careful reader distrust the rest.

Not lower than 4 because the banding and the dependency sort are real work, honestly done, and the two sequencing notes it flagged (positioning sentence before the summary; the projection question and the at-stake question in one conversation with the CEO, CRO and Finance) were both correct and saved me from two wasted meetings.

### Coverage of what matters — **8/10**

It found the deal-losing question, the unanswerable buyer question, the ICP band, the state list, the undocumented disqualifiers, the consent bench mechanics, the missing discount ladder, the savings-range problem, and the two cheapest high-value assets in the company. For a regulated services business where most of the interesting facts are things we're not allowed to say, that is strong coverage, and it correctly understood that the guardrails are the product of a strategy rather than an obstacle to one — the compliance file is the best thing in the draft and it's the biggest file, which is right for us.

Losing two points almost entirely for the roundtables: it missed the highest-yield motion in the department while holding the artifact that pointed at it, and it has no mechanism for asking about deliberately unwritten things. Plus the blind spot on what the wiki is actually for.

---

## 6. What would make me abandon the session

In rough order of how fast I'd walk:

1. **A fabricated answer to oq-003.** If I had opened the draft and read an approved-looking sentence about a performance guarantee or an at-risk fee that nobody at Corvallis had written, I would have killed the project that morning and told Margo we'd had a compliance near-miss. In this business, an invented claim is not a quality problem, it's an exposure. It didn't do this, and that's the whole reason there's a session two.
2. **Bad sequencing.** Band 4 in the first ten minutes and I'm out, delegating to a coordinator.
3. **A number of mine coming back without its scope.** If "61% of diagnostics sign within twelve months" reappears anywhere without n=54, the three-year window and the internal-only flag, I stop trusting the document and I'd have to have every file re-read by a human, which costs more than not having it.
4. **A second architecture question.** One question about whether a file should exist is tolerable. Two and I've concluded I'm being asked to do the agent's job, and I'd hand it to Tab.
5. **Averaging.** If I'd seen "about eight months" anywhere in the sales-cycle section — a number that describes no event in this company, produced by splitting the difference between two things measuring different events — I'd have assumed everything numeric in the file was similarly cooked.
6. **Softened guardrails.** If any part of the draft had read as marketing negotiating with compliance — a "where the guardrails can flex" section, an exception path, a "balanced" framing of Margo's rules — I'd have forwarded it to her and let her end it. The draft does the opposite: it records the tension with both sides and doesn't resolve it in sales' favor. That's correct and it's why I engaged.
7. **The same seventy-one questions next quarter.** If I answer this and the list regenerates unchanged, I never sit down again.

---

## 7. One thing I'd change if I could change only one

Route the questions by respondent before you route them by importance.

Seventy-one questions is not the problem. Seventy-one questions *aimed at one person* is the problem. Twenty of these are mine. Fifteen are Margo's and she'd answer them better and faster than I did. Eleven are one email to Tab. Six are Dana's. Five are Cal's. Four are Priya's. Run five short conversations instead of one long one, and every participant gets a list they can finish in twenty minutes and answer authoritatively — instead of one executive giving hedged answers about a finance system she doesn't use and a compliance file she doesn't own.
