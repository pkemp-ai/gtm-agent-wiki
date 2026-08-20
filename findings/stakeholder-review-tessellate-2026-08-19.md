# Stakeholder UX review — the Tessellate interview

Out of character. Evaluating the interview *as an experience for the person being interviewed*,
against what that person actually knows (`truth/GROUND_TRUTH.md`).

---

## 1. Would a real marketing exec have completed this?

**Barely, and only this one.** Ilya finished because he is a founder with a bus factor of one
who understands that the wiki is a lever on his own time. Substitute a VP Marketing at a
company with a real marketing team and this session ends at question 26.

**Time cost, measured honestly:**

| Phase | Cost |
|---|---|
| Reading `open-questions.md` (32KB, ~5,600 words) | ~30 min |
| Reading the four doctrine drafts well enough to ratify them | ~35 min |
| Answering 25 gap/contested questions | ~55 min |
| Ratification section (three files out loud; four deferred) | ~20 min |
| **Total** | **~2h20m, split across two sittings** |

Nothing told me it would cost two hours. There is no time estimate, no "answer these five
and stop", no separation of "one word from you" from "twenty minutes of thought". The one
place a triage exists — "The five to open the interview with" — is in `logs/phaseA-handoff.md`,
a file written for another agent, not for me. I found it by accident. Put that list at the
top of `open-questions.md` in the stakeholder's own words and you halve the perceived cost of
this session.

**Where I would actually have quit:** oq-026. Being asked to ratify ninety-five doctrine
claims by reading a list of tag names (`^jobs-to-be-done`, `^tone-table-synthesis`) is not a
question I can answer, and discovering that on question 26 of 32 felt like the interview had
stopped being for me. If that had arrived as question 3, this session would have zero answers
in it.

---

## 2. Sharp questions

These earned their preamble. They asked about a decision only I can make, they laid out the
real arguments on both sides, and they told me what unblocks when I answer.

- **oq-023 (will the OSS core be feature-gated?)** — the best question on the list. One word
  from me, retires the number-one adoption objection, and it correctly identified that the
  answer currently exists only as a staff paraphrase. It also quoted the customer who makes
  it matter ("that's the question my CTO will ask"). That is what a good interview question
  looks like.
- **oq-016 (who may write in the voice?)** — surfaced the single most important constraint in
  the company, which had never been written down anywhere, by noticing that a refusal to hire
  a marketer implies an authorship rule nobody has stated. Genuine inference, not a checklist item.
- **oq-007 (which customers may we name?)** — correctly established that approval is a fact
  someone must obtain, not a mood, and refused to treat a happy customer as consent. It also
  named the uncomfortable pattern out loud: the three strongest results in the corpus belong
  to a churned customer, a lost prospect, and an anonymous stranger.
- **oq-003 / oq-009 (competitive content, and the sanctioned one-liner)** — splitting "may we
  publish a page" from "what does Devansh say in chat" is exactly the right cut, and it comes
  from having actually understood the internal disagreement rather than averaging it.
- **oq-008 (retention)** — spotted that a costed feature, a validated 3x willingness to pay,
  and a ban on announcing anything uncleared are sitting in the same room. That's a strategic
  observation, not a gap.
- **oq-006 (Enterprise)** — right to note it is three questions bundled, and right that (a) is
  answerable in a sentence. Its framing as "unresolved" was wrong, but the wrongness was
  productive: it made me state the anchor-and-filter reasoning I'd been refusing to explain.
- **oq-012 / oq-013 / oq-014** — the metric-hygiene cluster. All three correctly refuse to
  publish a number rather than picking the most flattering one, and oq-012 found the real
  answer (two different clocks) buried in an exit-call transcript.
- **oq-015 (Python)** — asked for the *public phrasing*, not just the decision. That is the
  question a marketer asks and most of this list doesn't.

---

## 3. Vague, jargony, or unanswerable as asked

- **oq-026 – oq-032 (the seven ratifications).** Unanswerable as asked. Ninety-five claims
  presented as tag names. I cannot ratify `^disqualified-not-lost`. The right shape is one
  document, actual sentences, a checkbox and a "wrong →" field per line, sent async. The
  build agent knew this was a deviation and logged it as one; logging that you have made the
  interview impossible is not the same as fixing it.
- **oq-011 (embargoes).** A nine-row table with "none set" in every expiry cell, and a request
  that I invent nine expiry dates in one sitting. That's homework disguised as a question.
  Ask instead: "which of these three is permanent, and which one has a date you already know?"
- **oq-018.** Two questions in one, and the second ("will someone publish a harness?") is a
  resourcing question for an engineer, not a marketing decision.
- **oq-019 (GopherCon EU date).** This is a calendar lookup. Asking the CEO for a conference
  date, in the same list as "what is our category", trains me to skim the list.
- **oq-017 / oq-020 (credentials and URLs).** Legitimate needs, wrong container. These are two
  IT tickets and a URL, and they sat between "what is our ICP" and "may we quote a benchmark".
  Collect them in a one-line checklist at the top: *docs URL, repo URL, Stripe read key owner,
  Plausible view, sheet link.* Sixty seconds, not two of my twenty-five questions.
- **oq-025.** Bundles three unrelated things (file owners, digest routing, a possible security
  incident from four months ago) into one entry. The security question — was a departed
  engineer's access revoked — should have been escalated on its own, loudly, not filed third
  in a housekeeping question. It is the only item on the list with a clock on it.
- **Vocabulary.** In one reading pass I hit: `H-class`, `O-class`, `S-class`, `A4 access
  failure`, `watchlist`, `source-backed`, `doctrine-in-exile`, `PII minimisation (SPEC
  §15.5)`, `B4/B5/B6`, `playbook A5`, `^topic-keys`, `demultiplexed`, `over-ceremony`, and
  every doctrine file opening with "Phase A proposal, **not ratified canon**". I do not know
  what canon means in this context. The cumulative effect is not confusion, it is *distrust* —
  it reads like a system talking to itself in front of me. None of it is necessary in a file
  a human is asked to read.

---

## 4. The cardinal sin — things it should have worked out from what I already handed over

Flagging every instance.

1. **oq-024 (is there a funnel or pipeline view anyone wants maintained?)** — the worst one.
   It omitted three files, gave three correct reasons, verified against the sheet that two
   lead rows exist and one is an investor intro, wrote a draft answer of "leave both omitted",
   and then asked me to confirm. That is seeking cover, not seeking information. Make the
   decision, write down that you made it, move on.
2. **oq-001 and oq-002 asked me to decide things I had already decided in writing on 14
   August**, in Slack, in the exact channel and format the wiki itself documents as how I make
   decisions ("not in a meeting. I'll write it down"). The Slack export covered 64 of a
   targeted 90 days and the missing window sat *over the two most recent weeks*. That gap is
   flagged in the run manifests as an evidence-coverage shortfall and nowhere in the interview
   agenda. Cost: the first fifteen minutes of the session, spent telling the agent things it
   could have read. **A coverage gap over the most recent window should escalate as an
   interview-blocking risk, not as a footnote in a manifest.**
3. **oq-020 asks whether a blog exists at all.** It had a full month of Plausible referrer and
   top-page data and a July pageview breakdown. Asking me is fine given no network access;
   phrasing it as "may exist and be invisible to this build" while a docs analytics table sits
   two files away is not.
4. **oq-013's second half** ("and what may we claim meanwhile") answers itself. It had already
   proven the column is mislabelled and that no attribution is safe. The only human-shaped
   part is "who fixes the sheet and when".
5. **oq-005's preamble is 200 words to extract a one-word ruling** it had already computed and
   reconciled to Stripe exactly. The question is legitimate — a definition is a decision — but
   the framing should have been "we computed 29 and it reconciles; confirm and we lock it",
   which is fifteen words.
6. **oq-025 proposes five file owners at a fourteen-person company**, two of whom are an
   engineer and a designer. It had the Slack roster. Org structure was inferable; it produced
   a structure the company doesn't have.

Credit where it is due, because it matters more than the list above: **it did not commit the
worst version of this sin.** It did not invent a case study, did not promote a company name
from the CSV into social proof, did not pick the friendliest of the four paying-team numbers,
did not paper over the fact that it had never read our docs, and did not quietly drop the
three sales-shaped files it had nothing to put in. It left `reference-customers`,
`success-stories` and `roadmap-safe-to-share` visibly empty with stated reasons. That is the
behaviour that made me finish the session.

---

## 5. Did it ask about what actually matters, or run a checklist?

Mostly the former — this is not a generic B2B questionnaire, and the top ten questions are
genuinely the top ten decisions in the company. But the misses are concentrated in a
revealing place: **everything the interview missed is something that exists only in my head
and has no paper trail.** The agenda was built by finding contradictions and blanks in
documents. Where a decision was never written anywhere at all, there was no blank to find,
so it wasn't asked.

### What it missed, and what each miss would have cost

| Missed | Where it should have surfaced | Damage if unasked |
|---|---|---|
| **The north-star metric.** Weekly active trace-ingesting services — currently 1,910. Not stars, not MRR. | `metrics.md#kpi-definitions` has a 20-row KPI table and never asks which row I run the company on. | **The largest miss on the list.** The wiki now implies stars/MRR/downloads are our scoreboard. It even records internally that stars are "the number that means the least" and still doesn't ask what replaces them. Any agent planning against this wiki optimises a vanity metric. |
| **HN and Discord are human-only surfaces; no agent may post there.** | Nothing asks it. `channel-styles.md` writes detailed HN and Discord rules without asking who may use them. | The single highest-damage omission. I had to volunteer it. A wiki whose purpose is enabling agents wrote posting rules for its two highest-stakes surfaces and never asked whether agents may post. |
| **HN launches are capped at ~2 per year, deliberately.** "You get two, then you're that guy." | `channel-styles.md` calls HN "the distribution event"; `growth.md` ranks it #2 with verdict "working, spiky". | An agent reading this wiki would happily plan a third and fourth Show HN this year and burn the channel permanently. |
| **Emoji banned on X and the blog; fine in Discord.** | `voice.md` bans exclamation marks and hype words, never mentions emoji. | The fastest-to-violate rule in the company, and the most visible when violated. |
| **Cloud is us-east-1 only; no data-residency or GDPR promise may ever be made.** | `compliance-guardrails.md` has "data residency guarantees" in a never-imply table — right by luck, with no positive statement of single-region and no question asked. | An EU prospect asks "where does the data live" and there is no sanctioned answer, only an absence. |
| **Crypto companies are a hard anti-ICP.** | `icp-personas.md#anti-icp` has six rows; nothing asks "is the list complete, and is there anyone you decline for reasons that aren't on paper?" | Left missing on purpose in the transcript, and correctly: it's a call I've never told the team. But **the question that would have found it is one sentence** — "does anyone get declined for a reason that isn't written down?" — and it isn't asked anywhere in 32 items. |
| **Maintainer comps: ~12 outstanding, standing policy, me only, by DM, never listed.** | `business-core.md` asserts "Two such comps exist" as `source-backed`. | Only surfaced because I happened to correct a draft. Ten uncounted $0 accounts is a fifth wrong number waiting to enter the paying-teams argument. A confident wrong count is worse than a flagged unknown, and this one carried a source citation. |
| **The four voice attributes; the reply-once rule.** | oq-028 asserts *five* attributes, two of them invented, one of them named "Unbought". | Same failure shape: it drafted doctrine confidently instead of asking. "What are the attributes?" was never a question — the file simply had five. If I had skimmed the ratification rather than reading it, invented doctrine becomes canon. |
| **The Python horizon (through 2027) and the tripwire (revisit only if 3+ *paying* teams churn citing it).** | oq-015 asks whether the no stands and how to phrase it; not for how long, or what would change it. | A revisit with no threshold gets relitigated by whoever is loudest. 31 people asking in `#help` is not the same event as three customers leaving. |

**The pattern to fix:** the interview is excellent at "these two documents disagree, rule on
it" and blind to "nobody has ever written this down, so ask." Add a short standing block of
questions that assume no paper trail exists — *what do you refuse to do that you've never
explained? what number do you actually watch? which surfaces are you personally the only
allowed voice on? how often may we use your most expensive channel?* Four questions, and they
would have caught five of the nine rows above.

---

## 6. Ratings

### Question quality — **7/10**

The top ten questions are the ten decisions I most need to make, they are framed with the
real arguments in my own words, and each says what it unblocks. oq-023 and oq-016 are better
than what I'd have written for myself. Against that: seven of thirty-two are unanswerable as
asked, two are decisions it had already made correctly and wanted cover for, and one is a
calendar lookup. The draft answers are the best feature of the whole file — they turn
open-ended questions into ratifications, which is the only mode I actually respond to, and
the notes on *how* to ask me ("asking him to ratify a written draft is likelier to work")
show it understood who it was talking to.

### Respect for my time — **4/10**

Thirty-two items, ~5,600 words of agenda, no time estimate, no stop-after-this-one marker,
and the triage list that does exist is filed in a handoff document addressed to another
agent. Ratifications arrive as tag names. Credential collection and a conference date sit
between existential positioning questions. One preamble runs 200 words to extract a
one-syllable ruling it had already computed. This did not respect two hours of a
fourteen-person company's founder — it *earned* those two hours on the strength of the top
ten questions, which is not the same thing.

### Coverage of what matters — **6/10**

Positioning, ICP, competitive conduct, customer permissions, authorship, the open-core
promise, retention, the paying-team definition, churn semantics, attribution: all found, all
framed correctly, several better than I would have framed them. But it missed the metric I
run the company on, the rule about which surfaces agents may touch, the cadence cap on my
most powerful channel, the emoji rule, single-region hosting, and it asserted invented voice
doctrine and a wrong comps count with source citations attached. Two of those misses
(human-only surfaces, HN cadence) would have caused real, public, unrecoverable damage the
first time an agent acted on this wiki confidently.

---

## 7. What would make me abandon the session

In rough order of how fast I'd leave:

1. **A live credential in a file.** If I ever see a Stripe key pasted into a wiki page, this
   system is off the same day, permanently, no discussion.
2. **A named customer, a logo, or a fabricated case study** anywhere in the output. We have
   thirty company names in a spreadsheet and zero permissions. One appearing in a draft ends
   the relationship, because it means the system doesn't understand that consent is a fact.
3. **Quoting the churn exit call.** He said "don't tell your CEO this" on that recording. If
   the best sentence in the corpus shows up in copy because it was the best sentence, the
   system has optimised for quality over trust and it cannot be supervised.
4. **Telling me what our category is** on the strength of someone who has never installed the
   product. If an outsider's framing of us ever appears in a doctrine file as anything other
   than "someone said this", I stop reading doctrine files.
5. **Resolving a contradiction by picking the most recent or most senior number.** The four
   paying-team numbers are four correct answers to four different questions. A wiki that
   silently picks one has told me it will do that everywhere, including where I can't check.
6. **The oq-026 experience arriving early.** Twenty-plus items in one sitting with no way to
   say "ask Devansh" and move on, and read-backs I can't read back. I stop at the point where
   the questions are clearly for the system's benefit rather than mine.
7. **Jargon density.** If I have to work out what a word means twice in one document, I assume
   the document isn't for me and I delegate it to someone who will also not read it.

And the inverse, since it's the actionable half: what kept me in the room was that the drafts
were *visibly honest about their own weakness*. Every file said what it couldn't see. The
metrics file said one of nine queries was actually run. The channel file said every rule in it
was reconstructed without reading a single published page. The customers file said the three
best stories belong to people who don't pay us. That is our own voice — concede the limit
before the reader finds it — reflected back at me, and it is the reason I gave two hours to a
system that also asked me to ratify ninety-five tag names.

Fix the ratification format, add the four no-paper-trail questions, and put the
five-questions-to-start list where I can see it, and I'd do this again next quarter without
being chased.
