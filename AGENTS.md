# AGENTS.md — working on this repo

This repo defines the GTM wiki format. It is not itself a deployed wiki — a live wiki looks like [example/acme-wiki/](example/acme-wiki/).

## Authority order

1. [spec/SPEC.md](spec/SPEC.md) is normative. Everything else conforms to it.
2. [spec/taxonomy.md](spec/taxonomy.md) defines the canonical files. Skeleton, example, playbooks, and question bank all derive from it.
3. Playbooks, consumer docs, adapters, and scripts implement the spec. Where they disagree with it, they are wrong.

## Rules for edits

- **Spec changes ripple.** If you change SPEC.md or taxonomy.md, check the playbooks, the skeleton, the consumer contract, the scripts, and the example for drift. Vocabulary is exact: tier names, confidence labels, provenance classes (H/A/S/O/I), and file names are used identically everywhere.
- **Harness-agnostic.** Playbooks and consumer docs never assume a specific agent product. Vendor tool names appear only inside `sources.md` example entries, where a deployment would declare them.
- **Scripts are Python 3 stdlib only.** No dependencies, ever. They must run against both `example/acme-wiki/` and `templates/wiki-skeleton/`.
- **The example must pass lint:** `python3 scripts/lint.py example/acme-wiki` with zero errors. It carries exactly one warning on purpose — `manifest-health` on the `social-linkedin` source, which the example declares `broken:` and escalates in its changelog and digest. Don't "fix" it; it is what a live wiki with a failing source looks like. The skeleton lints clean with no findings at all.
- **Generated blocks are generated.** After any front-matter edit in the example or the skeleton, re-run `python3 scripts/sync_manifest.py <dir>`; the `AGENTS.md` inventory table between the `INVENTORY` markers is never hand-edited.
- **The example is fictional.** Acme Analytics, its people, customers, and competitors are invented. Don't add real companies or people to it.
- **Voice.** Public-facing prose (README, spec intros) is plainspoken and concrete. No filler adjectives.

## Verify before finishing

```bash
# --today pins the example's dated content; without it, warnings accrue as real
# time passes (by design — staleness is a warning, never an error).
python3 scripts/lint.py example/acme-wiki --today 2026-08-19        # 0 errors, 1 expected warning
python3 scripts/lint.py templates/wiki-skeleton --today 2026-08-19  # 0 errors, 0 warnings
python3 scripts/sync_manifest.py example/acme-wiki --check
python3 scripts/sync_manifest.py templates/wiki-skeleton --check
python3 scripts/digest.py example/acme-wiki
```
