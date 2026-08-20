# Stakeholder UX review — Phase B interview, Halden Instruments

*Written out of character, evaluating the interview experience the agent designed. Reviewer = the person who just sat through it.*

---

## 1 · Would a real marketing exec have completed this?

**Not as delivered. Roughly 40% of it, then a hard stop.**

Realistic path for a real Theo Brandt:

| Stage | What actually happens |
|---|---|
| Opens `open-questions.md` | Sees "68 open questions" in the description line and a "Scale warning" telling *him* that 68 is too many for one session. Immediate reaction: *why is the number of questions my problem?* |
| First 15 min | Answers oq-064, oq-011, oq-037. These are excellent and he engages. |
| 30–50 min | Answers oq-023, oq-061, oq-013, oq-012, oq-043, oq-020, oq-015. Still good. This is the session. |
| ~55 min | Hits oq-047 ("who can grant read access to Salesforce"), then oq-004, then oq-016 ("where should the distributor-rep persona live in this wiki"). Realises he is now doing the agent's filing and IT ticketing. |
| ~60 min | "Send me the rest in an email." Ends call. |

**Time actually spent producing the transcript above:** ~2h40m across two sittings. That is not a realistic executive spend; it happened only because someone senior said the project mattered. **A normal exec gives 50 minutes and answers 12–14 questions**, which — to be fair to the agent — is exactly what its own ordering was designed for. The problem is that the design intent lives in a warning note the stakeholder shouldn't have had to read, rather than in a shorter artifact.

**The single biggest UX failure is packaging, not content.** There is no "here are your 14 questions" document. There is one 68-item file, ordered well, with a note explaining that most of it isn't for me. That inverts the work: the stakeholder has to triage before he can contribute.

**Second packaging failure:** nine items are access/admin requests routed into an interview. Every one of those is a 30-second email to a different person. Putting them in the same queue as "does the positioning statement hold" makes the queue feel like busywork and lowers trust in the whole list.

---

## 2 · Question quality — sharp, vague, and unanswerable-as-asked

### Genuinely sharp (would answer these again, gladly)

- **oq-064** — "before anything ships" is the right framing. Naming legal exposure as the cost of delay is why it got answered first, honestly, with four additions.
- **oq-015** — the best question in the set. It didn't ask "is this a disqualifier," it named *three different asks hiding behind one CEO statement* (product gate / collateral qualification / message to 900 reps). That decomposition is what unlocked the real answer, which is none of the three — it's a **quoting rule**. A generic question would never have surfaced that.
- **oq-023** — correctly identified that "publish a price" and "put a price on a rep's leave-behind" had never been separated. It found a decision that was jammed only because nobody had split it in two. Highest-value question in the file per second spent.
- **oq-043** — asked both halves ("how may we contact them" *and* "what is the distributor told"). The second half is where the real constraint lives. Most interviewers ask only the first.
- **oq-051** — "what is the attach rate a rate *of*" is exactly right, and asking it is what pulled out the 40%-by-FY27 board target. The definitional framing did work that a "what's your attach rate goal" question would not have.
- **oq-026** — asking what actually happened in 2019 rather than asking to restate the rule. That's how you get a rule that survives the next person in the job.
- **oq-019** — nobody has ever asked this company about crisis tone. It produced net-new doctrine on the spot.
- **oq-013** — put the CEO's n=1 against the CMO's n=3-unexamined and made the asymmetry explicit. Uncomfortable and correct.

### Vague, or answerable only by inventing something

- **oq-053** ("what does leadership actually want to see, and how often") — a survey question. The answerable version is "should the monthly report be one number or five, and is attach rate the headline?"
- **oq-050** ("ratify the catalog's role and **set the print run deliberately**") — a marketing lead does not set a print run in an interview, and the framing invited exactly the error the question's own why-it-matters warned about.
- **oq-044** ("is the absence of an SDR function deliberate") — nobody can answer whether an absence is deliberate. The answerable version: "is anyone accountable for a website lead within 48 hours? If yes, who?"
- **oq-017** — asked to validate five attributes that are the agent's own synthesis, with the names presented as if they were the company's. One name ("Boring on purpose") would have sunk the file with the CEO. Better: "here are five behaviours we observed; do you recognise them, and what would *you* call each?"
- **oq-002** ("confirm each source's cadence and trust notes") — unanswerable as asked. "Trust class" is the wiki's vocabulary, not the business's.

### Unanswerable by *this* stakeholder — misrouted

- **oq-047, oq-054, oq-055** (Salesforce access, admin, objects) — IT/finance.
- **oq-005** (analytics platform), **oq-009** (catalog production file), **oq-029** (trademark register), **oq-006** (badge-scanner config) — vendor/agency/counsel.
- **oq-027, oq-034** (certifications, CMMS integrations) — engineering and product. The file even says "needs engineering," then queues it for the marketing interview anyway.
- **oq-048** (was the export date-filtered) — whoever ran the export.
- **oq-038** (Grand River sensors) — the product tenant. The file says so and still asks.

That's ~11 of 68 aimed at the wrong human, and the file *knows* it for most of them. Knowing and still queuing is worse than not knowing: it reads as "we didn't have anywhere else to put this."

---

## 3 · The cardinal sin — asking things it should have derived from data already handed over

Fewer instances than expected, and the agent deserves credit: it recomputed the CRM rather than asking, flagged the bogus $9.9M test row itself, and did its own arithmetic on win rates and the 186.8-day cycle. That is the right instinct and it's visible.

Still, flagging every instance:

1. **oq-011 (sales cycle) — half a sin, and the most consequential.** The agent *already worked out the answer* — its own why-it-matters says "they may not even be in conflict: they measure different intervals." Then it asked me which one is real. The correct move was to state its conclusion and ask me to sign it: "we believe 9 months is first-touch→PO and 187 days is opp-create→close; confirm, and tell us the channel figure." I'd have answered in 20 seconds instead of 3 minutes. **Asking a stakeholder to solve a problem you've already solved is a tax on the person whose time is scarcest.**
2. **oq-052 (show contribution) — same shape.** It found the 38% CRM proxy *and* diagnosed the undercount mechanism (booth-originated deals reclassified as Distributor Referral). Then asked me to define the metric from scratch. It should have proposed a definition and asked me to accept or amend.
3. **oq-035 (Rotafix price)** — the answer is on the competitor's own published page, which the agent pulled and dated. The remaining question is a sales-ops task ("capture a written competitor quote"), which its own `asked:` line says. It doesn't belong in an interview list at all.
4. **oq-045 (J. Fenn)** — borderline, and I'll allow it: the CRM gives the name, not the role. But it should have been in a batched "confirm these five names and roles" item, not a standalone numbered question about one person.
5. **oq-033 (Cantrell)** — legitimate gap, wrong target. I know less than the CRM does. Should have been routed to sales with the two opportunity IDs attached.
6. **oq-039, oq-016, oq-003, oq-001, oq-002 — the real sin, five instances.** Where a persona should live in the file tree; whether a log window should be 90 days or cadence-relative; who "owns the truth" of each file; whether the source census is complete; whether Slack exec statements are H-class. **These are the software's own design decisions dressed up as business questions.** oq-016's own text admits it ("a structure decision, not a business one… a question for whoever owns the wiki spec"). Asking them burns credibility with a non-technical stakeholder faster than anything else in the session, because they make the whole exercise feel like it exists to serve the wiki rather than the business.
7. **Batched ratifications are not questions.** oq-060 asks me to ratify **20 claims** in one item; oq-062, oq-065, oq-066, oq-067 do the same at smaller scale. Batching was the right call for list length — but the artifact I need is a read-back checklist with a tick box per claim, not one question whose `origin:` line lists nine topic keys in monospace. As delivered I had to open `business-core.md` in another window and read 130 lines to answer one bullet.

---

## 4 · Did it ask about what matters, or run a generic checklist?

**Overwhelmingly the former.** This does not read like a template. Specific evidence it understood *this* business:

- It made the **channel/distributor motion first-class** — rebuilt `channel-styles.md` around trade shows, the print catalog and distributor leave-behinds instead of the LinkedIn/Blog/Email/Paid skeleton, and declared the digital channels absent rather than silently dropping them. That's the correct read of a 70%-channel company and it's the single best decision in the build.
- It **added a third persona** for the distributor rep with a "we market *through* him" marker. Right call.
- It **broke its own 90-day event cap** for Hannover and said why. Right call.
- It kept **both personas separate with a no-mixing rule**, and found the "competent vs safe" axis and the blame question. That is the actual central marketing fact of this company and it got it from transcripts.
- It **did not smooth over contradictions.** Sales cycle, Pemberton loss cause, publish-the-price — all left contested with both sides named. That is the hardest thing to do and it did it.
- The **`why-it-matters` ordering** is the best UX decision in the whole artifact. Every question justified its own existence in business terms, in my language, with the cost of delay named. It is why I answered as much as I did.
- It **invented nothing.** Zero fabricated interview answers, `last-verified` deliberately unset, "0 confirmed claims." Given how much of this wiki is unsourced, the restraint is the reason I trusted the parts that were sourced.

### What it MISSED from the ground truth

Ordered by damage:

1. **Contractual constraints on go-to-market — never asked, in any form.** The Kellerman right-of-first-refusal on Midwest pulp & paper makes "go direct" legally unavailable in our best vertical. Twelve source files, 68 questions, and nothing asks "are there agreements that constrain who we can sell to or market to." It asked nine questions around the edge of the channel relationship (price on a rep sheet, logos, who contacts whom, co-marketing) without ever asking the load-bearing one. **This is the miss that would have caused real damage** — the wiki as drafted would happily authorise a Midwest paper direct campaign.
2. **OEM / white-label relationships — never asked.** The Varley Pump agreement is 11% of hardware revenue, constrains all pump-segment messaging, and is under NDA. A single question ("do we sell under anyone else's brand?") would have surfaced it. Its absence from a confidentiality-sensitive wiki is a live risk.
3. **"What does it cost" — never asked outright.** Extraordinary. It asked what agents may *say* about price (oq-068), whether a rep sheet may *carry* a price (oq-023), and whether a discount schedule exists (oq-014) — three permission questions about a number it never asked for. The price points came out only because I volunteered them to make oq-023 answerable. Had I been terser, the wiki would have shipped with pricing doctrine and no prices.
4. **Language and geography — never asked.** We are a German company with US operations, selling in EMEA and the Americas, and there is not one question about localisation. The German-authored-in-German rule roughly doubles campaign cost and is non-negotiable. A campaign plan built without it is wrong by 2x.
5. **Approval workflow — asked only for one artifact.** oq-024 asks who approves the website rebuild. Nobody asks who approves *anything else*. The CEO personally clears every catalog page and every use of the wordmark on a 48-hour turn. That is the binding constraint on content velocity and it's invisible in the draft.
6. **Imagery rules — near-miss.** oq-022 asks about a "photography standard" for the catalog only. The actual rule (no stock photography of people in hard hats pointing at tablets; every image a real installation with written permission) is company-wide, explains why we have almost no imagery, and would otherwise be discovered by an agent generating exactly the forbidden brief.
7. **Asymmetric curiosity about rule origins.** It asked brilliantly about 2019 (oq-026) and then *inferred* the no-field-install rule, even noting it was "the loss mechanism in a documented six-figure deal," without ever asking why it exists. Calder Ridge — 45 mis-mounted sensors, six months of unusable data, €180k remediation, a legal threat, and the CEO ending direct installation that week — is what makes the rule survive the next person in the job. If you're going to ask "what happened in 2019," ask it about every hard prohibition.
8. **Service/recalibration footprint — never asked.** We don't sell where we can't recalibrate. That's why LATAM outside Sonora is anti-ICP, and it explains a blank-reason loss sitting in the CRM the agent read.
9. **Decline-to-bid policy — never asked.** "Are there deals you refuse on principle?" would have produced the CDO-led-IIoT rule, which cost us two of the largest FY25 losses before it existed.
10. **Success definition — arrived sideways.** The 40%-by-FY27 attach target is the only Signal number on the board scorecard, and it surfaced only as a by-product of oq-051's definitional question. No question asks "what does FY27 success look like."

Pattern across all ten: **the agent asked exceptionally well about the things its sources mentioned, and did not ask about categories its sources were silent on.** It reasoned from what was in the dump, not from what a company of this shape must have. A checklist of "every industrial manufacturer has: OEM deals, channel agreements with territorial terms, service-coverage limits, an approval hierarchy, a language policy" would have caught six of these ten with six questions.

---

## 5 · Ratings

### Question quality — **8/10**

The top 15 questions are better than what most consultants produce after a week of discovery. oq-015's three-way decomposition, oq-023's publish-vs-quote split, and oq-051's "a rate of *what*" are genuinely excellent — each one unlocked a decision that had been stuck for months, precisely because it was framed as a decomposition rather than a request for information. Every question justified itself in business terms.

Losing two points for: batched ratifications that aren't answerable as single questions; ~5 questions that are the wiki's own filing decisions; ~11 misrouted to the wrong human; and 2–3 where the agent had already done the analysis and asked me to redo it anyway.

### Respect for my time — **4/10**

The intent was there — the ordering, the "items 1–14 are the session" note, the batching decision, the explicit acknowledgment that 68 is too many. The execution put the triage burden on me.

- No short agenda exists. One 68-item file, and the stakeholder must read a meta-note to learn most of it isn't for him.
- Nine access requests interleaved with strategy questions.
- Ratification items require opening a second file and reading 130 lines to answer one bullet.
- Filing questions in an exec's queue.
- Asking me to re-solve problems it had already solved.

The floor is 4 rather than 2 because it never wasted my time on something it could have looked up in the data I gave it — the sin it mostly avoided is the one that would actually have ended the session.

### Coverage of what matters — **7/10**

Nailed the hard part: two conflicting personas with a no-mixing rule, channel as first-class rather than a footnote, trade shows as the dominant channel with the biennial cadence, the distributor data blind spot as a known gap, the renewal hole, the loss-cause and sales-cycle contradictions left contested with the CEO/CMO disagreement named. That's the spine of this business and it's all there.

Missing a whole category: **the contractual and constraint layer.** No question about channel agreements, OEM arrangements, territorial rights, service-coverage limits, language policy, or approval workflow. Those aren't nice-to-haves — the Kellerman clause alone invalidates a strategy the draft would otherwise authorise. Also missing the actual price, in a file whose pricing section is three paragraphs of permission rules.

---

## 6 · What would make me abandon the session

In order of how fast it would end the call:

1. **Asking me anything I could have answered by opening a file I already sent you.** Instant loss of trust in every other question, because now I have to wonder which of the other 67 are also busywork. (Largely avoided — the CRM recomputation earned real credit.)
2. **A number in the draft I'd never say, presented as if I'd said it.** "World-class brand equity with roughly two thousand vibration specialists." It's flagged `inferred`, which the agent deserves credit for, but it reads as a quote from me and it would be repeated as one. If I find two of those I stop believing the labels and start re-reading the whole document, which I don't have time to do — so instead I abandon it.
3. **Being asked to ratify 20 claims in a single line item.** That's not a question, that's homework with a question mark on it.
4. **Filing questions.** "Should events.md keep a 90-day rolling window" told me this exercise partly exists to serve the document. One more of those and I'd have delegated the whole thing to a junior.
5. **Any hint that a guardrail was softened because an outsider disagreed with it.** If a future version of this wiki relaxes the AI ban because an analyst says engineer-native language costs deals, I shut the project down. That rule is forty years of trust with two thousand vibration specialists and it is not a marketing preference.
6. **Length.** If the file an agent reads before drafting a one-page rep sheet is eight pages long, humans will stop using the system, and in six months I own an unused wiki. The interview should have asked me what the *shortest useful version* looks like.

---

## 7 · One-line verdict

The best-reasoned discovery artifact I've seen from a machine, wrapped in the worst possible packaging for the one human whose time it needed — and blind to an entire category of question (contracts, constraints, approvals, languages) that its own sources never happened to mention.
