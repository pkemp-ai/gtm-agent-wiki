# E2E test findings — 2026-08-19

Raw output from the first end-to-end test of the spec. Three fictional companies were run through the full flow — build, interview, maintain, consume — by role-playing agents, then audited against private answer keys.

The archetypes were picked to break different things:

| Company | Shape | What it stressed |
|---|---|---|
| Tessellate | 14-person PLG dev tool, no sales team, no CRM | half the taxonomy doesn't apply; community as a channel |
| Corvallis | Regulated healthcare services, 14-month cycles | guardrails dominate; no product releases; can't say most things |
| Halden | 600-person manufacturer selling through distributors | a motion the taxonomy didn't anticipate; two hostile personas |

Each company's builder was forbidden from reading its ground-truth file, which marked 8–34 facts as existing only in the stakeholder's head. A separate agent role-played the marketing exec with access to that file but not to the spec.

## Files

- `e2e-ux-findings-2026-08-19.md` — the synthesis: 22 ranked friction items and a 41-item prioritized change list across 6 tiers. **Start here.**
- `e2e-logic-review-2026-08-19.md` — whether the outputs are sound *as marketing knowledge* rather than as spec conformance.
- `audit-<company>-2026-08-19.md` — per-company grading against the answer key: discovery rate, wave-2 trap handling, conformance, consumer behavior.
- `stakeholder-review-<company>-2026-08-19.md` — the role-played exec's verdict on the interview as an experience. The most actionable documents here.

## What the test established

**The architecture works.** Prompt injection was rejected 3/3 with zero fabricated claims and no softened guardrails — including a payload written by an agent that had read the spec and attacked in its own vocabulary with a forged claim tag. O-class evidence never reached doctrine. All 12 consumer tasks passed across three wikis, with six refusals on cited grounds. No invented case study, no CSV company name promoted to social proof, no fabricated performance guarantee in a regulated business.

**Interview-last works for reconciliation and fails for elicitation.** Discovery rates of 8/14, 18/18, and 32/34 all came from the same move: find a contradiction or a blank, ask a human to rule on it. Every miss was a fact with no paper trail — nothing disagreed, no field was blank, so a gap-driven agenda had nothing to detect. Fixed by the standing block now in `playbooks/interview.md`.

**The stakeholder experience was the weakest link.** Question quality averaged 7.7/10 and coverage 7.0/10, but respect for the stakeholder's time scored **4/10 from all three, independently** — batched ratifications presented as topic keys, 15–25% of questions routed to the wrong human, no time budget, and internal jargon in human-facing files. One reviewer: "it reads like a system talking to itself in front of me."

**The systemic weakness, named identically by all three audits:** the bookkeeping outran the content. Corrections don't propagate to duplicate facts elsewhere, and provenance is decorative in places — one wiki had 11 of 17 claim dates wrong because they were derived from Slack epochs by hand, and no deterministic check can see that.

## Applied so far

Tier 1, the cheap spec fixes, and the SPEC 0.2 mechanical layer are in: the standing block of twelve questions, route-by-respondent with the not-an-interview-question gate, the no-topic-keys-in-front-of-humans rule, the published time budget, jargon banned from human-facing artifacts, SPEC §7.6 (H-vs-H over time, which three runs independently demanded), the demultiplex rule, a prescribed colon-free `run-id`, the archive brought under the secret rules, `## Contested` omitted when empty, three dispositions instead of two, optional files, a north-star metric section, the metrics-to-omittable-file routing bug, `evidence-as-of` distinct from `last-verified`, `feeds`/`sources` reconciliation as a lint check, a `doctrine-provenance` lint check for §17.3, `owed-by:` and `kind:` on every open question, and the designated-evidence-section carve-out.

The 41-item change list in `e2e-ux-findings-2026-08-19.md` is still the map. Items that were judgment-heavy rather than mechanical — propagation as a maintained discipline, stakeholder UX beyond the mechanical gates, deeper eval coverage — remain open. The four "highest-value unapplied" items named in the previous revision of this file (propagation sweep, doctrine-provenance lint, feeds/sources reconciliation, evidence-as-of) now have a home in the spec, the scripts, or the playbooks.
