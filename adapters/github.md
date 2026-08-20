# Storage Adapter: GitHub

GitHub is the native fit — the spec's default versioning story ([SPEC §16](../spec/SPEC.md)) with a browsing UI on top. One repository per wiki, repo root = wiki root, so agent harnesses auto-load `AGENTS.md` on entry. There is no mapping layer: GitHub renders the markdown as-is.

## What maps to what

| Wiki construct | GitHub feature |
|---|---|
| Wiki folder | Repository (private by default — it holds pipeline, customer, and pricing facts) |
| Maintain run | One commit, message mirroring the run's changelog entry (§12.2, §16) |
| `changelog.md` | Normative record; `git log` is its mirror, `git revert` its one-operation undo |
| Canonical + reference pages | Rendered markdown; front matter displays as a table atop each file |
| Claim tags, `^topic-keys` | Literal text (harmless; anchors don't link in GitHub's renderer) |
| Digest review-after loop | Commit and compare views, for stakeholders who want the raw diff |
| `.archive/` | Committed or ignored — see below |

## Setup

1. Create a private repo from the wiki folder; commit the built wiki as the initial state.
2. **Commit convention:** one commit per maintain run, no-ops included (matching §12.2). Subject line names the run kind and sources — `maintain: [slack-gtm, web-metricflow]` — and the body is the changelog entry verbatim. The changelog stays normative (it must stand alone for git-less deployments); the mirror makes `git log` a readable run history and `git revert <sha>` an undo of an entire run — safety net (b) of §8.
3. Interview sessions and build runs commit the same way (`interview: dana-cmo`, `build: initial`).

## Pull requests are an override, not a default

The spec's default is **no approval gates** (§8): every write is provenance-gated by evidence class, changelogged, and revertable, and human review is asynchronous via the digest. Committing straight to the default branch is the conformant baseline.

Some orgs will still want a human in the loop for doctrine-touching runs. That is a legitimate per-org override, taken with eyes open:

- **Scope it narrowly.** Branch protection plus CODEOWNERS on doctrine files only (`business-core.md`, `voice.md`, `compliance-guardrails.md`, …), so state, runbook, and system writes stay gate-free and routine maintain runs stay cheap.
- **Understand the cost.** A PR gate reintroduces exactly the approval latency the write matrix was designed to replace, and an unreviewed doctrine PR is worse than the default: the change is neither live nor reviewed, and consumers read stale doctrine while it waits.
- **Record the override** in `AGENTS.md` deployment notes.

## Scheduling maintain runs with Actions

Actions is one scheduling option among many — the playbooks don't care what invokes them. A generic sketch:

```yaml
name: wiki-maintain
on:
  schedule:
    - cron: "0 9 * * 1-5"
  workflow_dispatch: {}
concurrency:
  group: wiki-maintainer        # single-writer rule (§9): never two maintain runs at once
  cancel-in-progress: false
jobs:
  maintain:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run maintain playbook
        # Invoke your agent harness's CLI here. Source credentials come from
        # repo secrets, referenced by env-var name per SPEC §15.3 — never by value.
        run: <your-agent-cli> --dir . --playbook playbooks/maintain.md
      - name: Commit and push
        run: |
          git config user.name "wiki-maintainer"
          git add -A
          git commit -F changelog-entry.txt && git push
```

`scripts/lint.py` is dependency-free by design (§14) and runs well as a separate check on every push and PR.

## `.archive/` and repo visibility

§11 requires the archive to exist *somewhere*; where depends on who can see the repo:

| Repo visibility | Recommendation |
|---|---|
| **Private** | Commit `.archive/` — the full audit trail rides with the wiki, every provenance pointer resolves for anyone who clones, and evals need nothing beyond the repo |
| **Public** (or broadly shared) | Add `.archive/` to `.gitignore` and keep it on the maintainer's storage, path recorded in `sources.md`. Raw pulls contain third-party content, internal exports, and possibly PII — none of it publishable |

This is §11's retention trade-off in miniature: an archive outside the clone means claim audits run only where the archive lives, and any pruning is recorded in `changelog.md` so audits mark affected claims `unverifiable-archived` rather than `invented`. Repo size is the other pressure — raw pulls grow monotonically, and heavy deployments relocate the archive out of git regardless of visibility.

## Human edits via the GitHub UI

Stakeholders were promised they never need git (§1), but the web editor makes drive-by edits possible, and they are legitimate: **a non-maintainer commit is an H-class event** (§7), the same as a human-edited file in an Obsidian vault. Detection is trivial here — commits since the last run not authored by the maintainer — and each such diff goes through intake logic (§9): promoted per the write matrix with provenance `doc:<file>` and a claim tag stamped `[confirmed | doc:<file> | 2026-08-19]`, converted to an open question, or reverted with a changelog note. Never rebase or force-push over a human's commit; process it, then commit the normalization on top.

## Limitations

- GitHub's renderer neither hides claim tags nor links `^topic-key` anchors; the browsing experience is honest but plain. Orgs wanting a friendlier read surface layer the [Obsidian](obsidian.md) or [Notion](notion.md) adapter over the same repo.
- GitHub's own "Wiki" tab is a separate repo with different semantics; don't use it — the wiki *is* the repository.
- Actions logs can leak payload fragments if a fetch step echoes content; keep fetching quiet and let `.archive/` be the record (§15.2).
