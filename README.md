# GTM Agent Wiki

A markdown knowledge base your GTM agents can read, trust, and keep current.

Codebases got their wiki pattern: an agent reads the repo, writes linked markdown docs, and updates them on every commit. Marketing has no repo. Positioning lives in the CMO's head. Competitor intel lives on someone else's website. The sales cycle lives in the CRM — and it disagrees with what the VP of Sales says. There are no diffs to watch.

This repo is a spec and a set of playbooks for building that wiki anyway.

## What you get

A deployed GTM wiki is a folder of markdown files — 18 canonical pages covering positioning, ICP, voice, competitors, pipeline, tooling, and the rest — that works as a git repo, an Obsidian vault, or a Notion workspace. Any agent harness can operate on it: the wiki carries an `AGENTS.md` contract, a chat skill, and a system-prompt block. No runtime, no framework, no connector code.

Three things make it work where a doc dump fails:

**1. Claims, not prose.** Every statement an agent would act on carries a confidence label and a provenance pointer:

```markdown
We win against MetricFlow on time-to-first-dashboard: median 4 days vs. their 6 weeks.
[confirmed | interview:dana-cmo | 2026-06-02] ^win-ttfd
```

Five labels: `confirmed`, `source-backed`, `inferred`, `contested`, `watchlist`. When evidence conflicts, the claim goes to a `## Contested` section with both sides shown — and never resolves by recency alone.

**2. Provenance-gated writes, not approval gates.** No human reviews edits before they land. Instead, the class of evidence determines what an agent may change. Positioning and voice are *decisions* — only human-originated evidence (an interview answer, the CMO's Slack post) can rewrite them. Facts about the world — a competitor's pricing page, a CRM query — write freely with labels attached. Agent inference can propose, annotate, and question. It can never overwrite. The safety net is an append-only changelog, a weekly digest, and cheap reverts.

**3. Sources as config, not code.** Each deployment declares its inputs in `sources.md` — Slack, CRM, call recordings, competitor sites, review sites, or a folder the stakeholder drops files into. Each source has an access method, a cadence, and a cursor. The maintenance playbook iterates the manifest with whatever tools the harness has. An org with zero integrations still works.

## How a wiki gets built

Interview-last, not interview-first.

1. **Ingest.** Connect sources, request a data dump, pull everything into an archive, draft all 18 files from evidence — every claim labeled.
2. **Interview.** The drafts generate `open-questions.md`: gaps, conflicts, inferences needing ratification. The stakeholder confirms drafts instead of answering blank-page questions. Short session, concrete answers, each one stamped `[confirmed | interview:<person> | <date>]`.
3. **Maintain.** Scheduled runs pull each source since its cursor, apply the write rules, log to the changelog. Open questions keep accumulating; the digest delivers 2–3 back to the stakeholder each cycle. The interview never really ends — it just gets short.

## Repo tour

| Path | What it is |
|---|---|
| [spec/SPEC.md](spec/SPEC.md) | The format: tiers, claim tags, provenance classes, the write matrix |
| [spec/taxonomy.md](spec/taxonomy.md) | All 18 canonical files — what goes in each, and what doesn't |
| [playbooks/](playbooks/) | Build, interview, maintain, lint, evaluate — procedures any agent can follow |
| [consumer/](consumer/) | The reading contract: `AGENTS.md`, a chat skill, a system-prompt block |
| [templates/wiki-skeleton/](templates/wiki-skeleton/) | Copy this to start a deployment |
| [example/acme-wiki/](example/acme-wiki/) | A complete wiki for a fictional company — browse this first |
| [scripts/](scripts/) | Lint, manifest sync, digest. Python, stdlib only |
| [adapters/](adapters/) | Obsidian, Notion, GitHub deployment notes |

## Quickstart

```bash
cp -r templates/wiki-skeleton my-company-wiki
```

Then point an agent — Claude Code, Codex, Cursor, anything that reads `AGENTS.md` — at the folder and tell it to run `playbooks/build.md`. It will walk your stakeholder through sources, pull what it can, draft everything, and come back with questions.

Already have a wiki? Schedule `playbooks/maintain.md` on whatever runs agents on a clock: cron, CI, a hosted scheduled agent.

## The example

[example/acme-wiki/](example/acme-wiki/) is a full wiki for Acme Analytics, a fictional B2B attribution company. It's the spec demonstrated end to end: a contested sales-cycle claim linked to its open question, watchlist intel on a competitor moving upmarket, a broken runbook entry left flagged instead of deleted, an archive backing the source-backed claims. Start there.

## Lineage

- Andrej Karpathy's [LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki) — the pattern: agents do the bookkeeping humans abandon.
- [openwiki](https://github.com/langchain-ai/openwiki) — proved the loop for codebases and personal knowledge. This spec borrows its best ideas (raw-dump-then-synthesize ingestion, confidence labels, deterministic post-passes) and drops the parts a marketing deployment doesn't need.
- [agents.md](https://agents.md) — the manifest convention that makes the wiki harness-agnostic.

## Status

v0.2. The spec is a draft and the playbooks are young. Issues and PRs welcome — especially from people who've tried deploying one.

Built by [Lobo Growth](https://lobogrowth.com).
