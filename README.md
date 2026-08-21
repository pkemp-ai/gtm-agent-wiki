# GTM Agent Wiki

A proactive memory system for agents supporting a company's GTM. Built by agents. Maintained by agents and humans.

Agents doing sales and marketing work require context that comes from non-deterministic sources (not a codebase). [OpenWiki](https://github.com/langchain-ai/openwiki) introduces a CLI that builds and maintains documentation for a codebase.

Sales and marketing have no repo. This system accounts for that by building on OpenWiki's loop — ingest, synthesize, keep current — to add:

1. A flexibile taxonomy for GTM context
2. A standing backlog of questions from agents to humans
3. A framework for human approval of specific types of context
4. A standing backlog of questions from GTM agents to humans
5. A maintainer agent that merges proposed updates from GTM agents
6. Label to source where context updates came from
7. Flexibility. This is a modifiable codebase, not a connector.

## What you get

A deployed GTM wiki is a folder of markdown files — positioning, ICP, voice, competitors, pipeline, tooling, metrics, org — that works as a git repo or an Obsidian vault, and can be rendered to Notion for browsing. This repo ships the playbooks and a chat skill; the wiki is the knowledge. No runtime, no framework, no connector code.

## Quickstart

Open any writable folder in a coding agent that can manage files and run shell commands. Paste one prompt:

```text
Build a GTM wiki for <company name>.

The canonical wiki folder should be <wiki-folder>. If I have not supplied a
folder, ask me where to create it.

If this workspace does not contain the GTM Agent Wiki kit, clone
https://github.com/pkemp-ai/gtm-agent-wiki.git into
./gtm-agent-wiki-kit.

Read the kit's AGENTS.md, spec/SPEC.md, spec/taxonomy.md, and
playbooks/build.md. Then follow the build playbook from start to finish.
Build from ingestion, not a blank-page interview. Begin with whatever
evidence is already available. Ask me when you need source access, files,
or stakeholder input. Do not invent missing evidence.
```

`<wiki-folder>` means a writable folder for the canonical markdown files — for example `./acme-wiki`, `/path/to/acme-wiki`, a git repo, or an Obsidian vault. A Notion page is not a canonical destination; [the Notion adapter](adapters/notion.md) renders the markdown wiki to Notion after the build.

The agent handles cloning, scaffolding, ingestion, checks, and delivery. The build pauses only when it needs source access, files, or a stakeholder answer. At delivery it gives you a ready-to-paste maintenance prompt and the connection instructions for your GTM agents.

## How it works

### 1. Build through ingestion

The [build playbook](playbooks/build.md) maps the company's sources, archives the raw evidence, and drafts the wiki from what it finds. Gaps, conflicts, and uncertain claims become questions in `open-questions.md`.

The stakeholder comes in last to confirm drafts and answer what the sources could not. The builder then lints the wiki, checks conformance, and delivers a walkthrough.

### 2. Schedule the maintainer

The builder's handoff includes a maintenance prompt filled with the actual wiki location, playbook location, source cadence, and digest destination. Test it once, then add it to a recurring agent job.

The [maintenance playbook](playbooks/maintain.md) pulls and archives new evidence, updates the wiki, processes GTM-agent intake, runs checks, and sends a digest. Run it at the finest cadence in `sources.md` — usually daily — with one maintainer at a time. Quiet runs stop early; broken sources stay visible.

### 3. Connect your GTM agents

Give each GTM agent read access to the deployed wiki. The builder's handoff tells you which contract to use:

- Agents working in the wiki folder load its root `AGENTS.md`.
- Chat agents that support skills use [consumer/SKILL.md](consumer/SKILL.md).
- API-built agents use [consumer/system-prompt.md](consumer/system-prompt.md) with the wiki in their retrieval layer.

Consumer agents read the wiki before doing GTM work and append new facts, corrections, and questions to its intake surfaces. They never edit canon. The maintainer processes their intake on its next run.

That closes the loop: sources and people build the wiki, GTM agents make it richer through use, and one maintainer keeps it coherent.

## Explore the repo

- Start with [example/acme-wiki/](example/acme-wiki/), a complete fictional deployment with evidence-backed claims, open questions, contested evidence, consumer intake, and an archive.
- Read [spec/SPEC.md](spec/SPEC.md) for the format and write rules.
- Read [spec/taxonomy.md](spec/taxonomy.md) for the canonical files and their boundaries.
- Use [playbooks/](playbooks/) to build, interview, maintain, lint, and evaluate.
- Use [consumer/](consumer/) to connect agents that read the wiki.
- Use [templates/wiki-skeleton/](templates/wiki-skeleton/) as the starting structure.
- Use [adapters/](adapters/) for GitHub, Obsidian, and Notion deployments.
- Use [scripts/](scripts/) for dependency-free lint, manifest, and digest checks.

## Lineage

- Andrej Karpathy's [LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki) — the pattern: agents do the bookkeeping humans abandon.
- [OpenWiki](https://github.com/langchain-ai/openwiki) — the ingest, synthesize, and maintain loop.
- [agents.md](https://agents.md) — the manifest convention that keeps the wiki harness-agnostic.

## Status

v0.2. The spec is a draft and the playbooks are young. Issues and PRs welcome — especially from people who have tried deploying one.

Built by [Lobo Growth](https://lobogrowth.com).