# skill-generator

Turn a document into a tested Claude Code skill. Give it a manuscript, methods paper, framework,
reporting guideline, tutorial, or working paper, and say what the skill should enable Claude to do. A
bundled agent reads the source in full, designs the skill with every procedure tied to a page or
section, writes it, benchmarks it against Claude without the skill on your own test cases, and writes a
usage guide with a real worked example.

The [`stress-rep-guideline`](../stress-rep-guideline/) plugin in this repository was built this way and
shows what the output looks like.

## Install

In Claude Code:

```text
/plugin marketplace add CarlosPiant/AI-assisted-tools
/plugin install skill-generator@ai-assisted-tools
```

It runs in **Claude Code only**: the benchmark launches subagents, which claude.ai does not provide.
Anthropic's `skill-creator` plugin is optional; when installed, its viewer and aggregation scripts read
the same evaluation files. `pandoc` is needed only for a Word copy of the usage guide.

## Use

Work in the project where you want the skill. Run one phase at a time and review each output before
the next.

```text
/generate-skill stress-rep-guideline --source docs/monks2019.pdf --objective "Audit a simulation write-up against the STRESS checklist and report each item with quoted evidence" --phase design
```

| Phase | What happens | Output in your project |
|---|---|---|
| `design` | Full read of the source; extraction table with locators; scope, triggers, layout, open questions | `skill_generator/<name>/design.md` |
| `build` | Writes the skill from the brief you reviewed | `.claude/skills/<name>/` |
| `validate` | Frontmatter, description, file lengths, paths, scripts | `skill_generator/<name>/structure_check.md` |
| `evals` | Turns your test cases and success criteria into graded assertions | `skill_generator/<name>/evals/evals.json` |
| `benchmark` | Each case run with and without the skill in fresh subagents, then graded | `skill_generator/<name>/benchmark.md` |
| `iterate` | Fixes the skill from failures, re-runs, writes the verdict | `skill_generator/<name>/evaluation_report.md` |
| `describe` | Optional: tunes the description with trigger queries | `skill_generator/<name>/description_tuning.md` |
| `document` | Usage guide: description, triggers, how to use, worked example, evaluation, provenance | `skill_generator/<name>/<name>_USAGE.md` |
| `share` | Prints the commands to use the skill everywhere or package it as a plugin | — |

**What to prepare.** The source document; a kebab-case name; a one- or two-sentence objective; five to
ten phrases people will use to ask for it; two or three realistic test cases with the result you
expect; and checkable success criteria, such as "reports the ICER in $/QALY" rather than "is thorough".
The quality of the test cases sets the quality of the evaluation.

**Cost.** The `benchmark` and `iterate` phases make two full runs per test case per repetition, plus a
grading run each. The STRESS skill's five-case benchmark used about 1.35 million tokens.

## How the evaluation decides

Each assertion is graded pass or fail with quoted evidence by a grader that never sees the skill. The
verdict uses three tiers — conservative 90 %, standard 80 %, experimental 70 % — and in every tier the
skill must also beat the no-skill baseline:

- **ACCEPT** — threshold met, baseline beaten, no rubric dimension failed.
- **EXPERIMENTAL** — usable with the caveats written into the usage guide.
- **REJECT** — below threshold after the iteration cap, or a fidelity or safety failure.

The full protocol, file formats, and rubric are in
[`references/skill-eval-protocol.md`](skills/generate-skill/references/skill-eval-protocol.md).

## What it will not do

- Write outside the current project or modify the source documents.
- Attribute anything to the source without a locator, or fill gaps from general knowledge without
  labelling them as extensions.
- Replace an existing skill folder without asking.
- Reproduce source text whose licence does not allow it. The brief records the licence and the
  attribution the skill must carry.

## Licence

© 2026 Carlos Pineda, [PolyForm Noncommercial 1.0.0](LICENSE). Free for research, teaching, and personal
use. Skills you generate with it are yours; their licence depends on the sources you build them from.
