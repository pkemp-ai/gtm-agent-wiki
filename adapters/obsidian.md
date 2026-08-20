# Storage Adapter: Obsidian

The Obsidian adapter is barely an adapter: a spec-conformant wiki **is** a valid vault. Point Obsidian at the wiki folder and everything renders — no export step, no sync job, no mapping layer. This is by design ([SPEC §16](../spec/SPEC.md)): the canonical format was chosen to be Obsidian-native.

## What maps to what

| Wiki construct | Obsidian feature |
|---|---|
| YAML front matter | Properties (visible and filterable in the Properties panel) |
| `^topic-key` anchors | Block IDs — `file#^topic-key` links resolve, claims are hoverable |
| Standard markdown links | Graph edges |
| `references/` fan-out | Folder; graph clusters around canonical parents |
| `## Contested` sections | Plain headings, searchable |
| `intake/inbox/` | The drag-and-drop target for stakeholder documents |
| `.archive/` | Invisible — Obsidian ignores dot-prefixed folders automatically |

The graph view deserves emphasis. SPEC §4.4 defines links as semantic edges and treats orphan pages as lint failures; Obsidian draws that exact graph for free. A healthy wiki shows reference pages clustered around their canonical parents — battlecards orbiting `competitors.md`, persona deep dives orbiting `icp-personas.md` — and an orphan is visibly adrift before lint ever runs. It is the cheapest wiki-health visualization a stakeholder will ever get, and a genuinely good way to show a non-technical owner what their agents actually know.

## Setup

1. **Open the wiki folder as a vault** ("Open folder as vault"). The wiki directory is the vault root — `AGENTS.md` and `sources.md` sit beside the content, which is fine; they render like any page.
2. **Settings → Files and links:**
   - **Use [[Wikilinks]]: OFF.** The spec mandates standard markdown links (§16). Turning wikilinks off makes Obsidian *write* conformant links too, so anything a human adds stays valid on every other storage target.
   - **New link format: relative path to file** — matches how playbook-written links resolve.
   - **Default location for new attachments: `intake/inbox/`.** Anything a stakeholder pastes or drags into a page lands in the human drop folder, where the next maintain run finds it (§9).
3. **Settings → Editor:**
   - **Default view for new tabs: Reading view.** Stakeholders browse by default and edit only deliberately, which keeps accidental keystrokes out of canon. Edits remain one toggle away — and legitimate (see the stakeholder loop below).
4. **Core plugins:**
   - Enable **File Recovery** (see versioning below).
   - Enable **Bookmarks** and pin `AGENTS.md` — it is the wiki's front door, and its inventory table doubles as the vault's homepage.
   - Disable anything that auto-rewrites files on open — front matter (`evidence-as-of`, `last-verified`) is part of the lint contract (§4.1) and a plugin that restamps dates on open will make every file look freshly verified.

## Versioning

| Mode | Revert story | Audit granularity |
|---|---|---|
| **Vault + git underneath** (recommended) | `git revert` of a whole run | Per-run, full history |
| **Vault only** | File Recovery snapshots | Per-file, bounded window |

Git underneath is still the recommendation (§16): the maintainer commits with changelog-mirroring messages, and humans never see any of it — `.git/` is invisible inside Obsidian, and vault and repo coexist with zero friction. See the [GitHub adapter](github.md) for the commit conventions.

For deployments that truly cannot run git, **File Recovery is the revert mechanism** the spec's escape hatch names (§16): it snapshots files on change and restores from inside Obsidian. Accept the trade-offs the spec states: coarser audit granularity, per-file rather than per-run revert, and a bounded history window (raise the retention interval in File Recovery's settings). The changelog remains the normative run record either way.

If Obsidian Sync is in use, note that it skips dot-folders: `.archive/` will not replicate to other devices. On stakeholder machines that is what you want; on the machine running maintain runs it is not — keep the archive where the maintainer runs, since it is the audit trail for every `source-backed` claim (§11).

## The stakeholder loop

Stakeholders browse and read in Obsidian; that alone justifies the adapter. But Obsidian users will also edit, and that is legitimate: **a human editing a wiki file in Obsidian is an H-class event** (§7) — the same evidence class as a strategy doc dropped in `inbox/`. The flow that keeps it spec-clean:

1. **Detection.** At the start of every maintain run, before touching anything, the maintainer checks for out-of-band changes: `git status` when git is underneath, file mtimes newer than the previous run's timestamp when it is not.
2. **Attribution.** Changes not produced by the maintainer's own last run are treated as human-authored: H-class evidence with provenance `doc:<file>`.
3. **Intake processing.** Each human change goes through the same logic as an intake observation (§9): promoted into canon per the write matrix (H-class may write any tier, doctrine included), converted to an open question if ambiguous, or reverted with a changelog note if it breaks structure. Promotion usually means keeping the human's words and normalizing the mechanics around them — adding the claim tag `[confirmed | doc:business-core.md | 2026-08-19]`, a `^topic-key`, and the front-matter updates the human won't have made.
4. **Changelog.** The run's entry records each human edit and its disposition, like any other evidence.

The stakeholder never needs to know any of this happened. They typed a correction into the page where the error lived — the most natural review interface there is — and the machinery made it conformant behind them.

## Limitations

- **The Properties panel can fight freshness fields.** Obsidian happily lets a human edit `evidence-as-of` or `last-verified`. Lint catches malformed front matter; the maintainer treats human edits to those fields as noise to revert, not as evidence. (SPEC 0.2 dropped `generated:` and `tags:` — they are not part of the contract.)
- **Commenting is improvised.** Obsidian has no native comment layer. Its `%%comment%%` syntax (hidden in reading view) works as a lightweight annotation channel — sweep for `%%` blocks during detection and route them through intake like observations. Anything heavier belongs in `open-questions.md` or `inbox/`.
- **New-note creation bypasses the taxonomy.** A stakeholder can create a top-level note in two keystrokes, violating the fixed top level ([taxonomy](../spec/taxonomy.md)). Lint flags it; the maintainer relocates the content through intake.
- **Claim tags render as visible prose.** `[confirmed | interview:dana-cmo | 2026-06-02]` appears as literal text. Stakeholders learn to read past it quickly; a CSS snippet can de-emphasize the pattern if the org cares.
