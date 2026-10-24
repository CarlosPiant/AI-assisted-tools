---
name: generate-skill
description: Create a new Claude Code skill from a document you provide (manuscript, methods paper, framework, guideline, tutorial, working paper) and a stated objective. The skill-builder agent studies the source in full, writes the skill with progressive disclosure, benchmarks it against a no-skill baseline on your test cases, and writes a usage guide with a worked example. Use when the user says "make a skill from this paper", "turn this framework into a skill", "create a skill that applies this guideline", "build a skill from this tutorial", "skill generator", "generar un skill a partir de este documento", "convertir este tutorial en un skill".
argument-hint: "<skill-name> --source <file-or-folder> --objective \"<what the skill must do>\" [--phase design|build|validate|evals|benchmark|iterate|describe|document|share]"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "Agent", "WebFetch"]
effort: high
---

# /generate-skill

Build a reusable skill out of source material, then prove it works. The new skill is written to the
current project's `.claude/skills/<name>/`, so it is usable in that project immediately. Working files,
evaluation runs, and the usage guide go to `skill_generator/<name>/` in the same project. Nothing is
written outside the current project.

The work is delegated to the `skill-builder` agent bundled with this plugin (it may be listed as
`skill-generator:skill-builder`), one phase at a time. That lets the user review the design before
anything is built and the evaluation before the skill is shared. Invoked without `--phase`, run
`design` and stop.

## Inputs

Required arguments:

- the skill name — kebab-case, first positional argument; becomes `.claude/skills/<name>/`
- `--source` — the file or folder with the source material
- `--objective` — what the skill must enable Claude to do, in one or two sentences
- `--phase` — optional; which phase to run (table below); omitted means `design`

Useful context to collect from the user and pass to the agent when available: trigger phrases they
expect people to say, the audience and domain, the expected inputs and outputs with formats,
constraints and conventions, whether to bundle `references/` and `scripts/`, the language, the effort
tier for the new skill, two or three test cases with expected outcomes, success criteria, the quality
threshold, runs per case, the iteration cap, and the format of the usage guide. Ask for the test cases
and success criteria before the `evals` phase if they are missing; they cannot be invented.

## Phases

| `--phase` | What skill-builder does | Writes |
|---|---|---|
| `design` | Reads the full source, extracts procedures, rules, and formulas with locators, runs the anti-hallucination checks, proposes scope and layout | `skill_generator/<name>/design.md` |
| `build` | Writes the skill from the reviewed design brief and the user's corrections | `.claude/skills/<name>/SKILL.md` (+ `references/`, `scripts/`) |
| `validate` | Structure and convention check: frontmatter, description quality, file lengths, paths, scripts smoke test | `skill_generator/<name>/structure_check.md` |
| `evals` | Turns the user's test cases and success criteria into the eval file | `skill_generator/<name>/evals/evals.json` |
| `benchmark` | Paired with-skill and without-skill runs per case, grading, aggregation | `skill_generator/<name>/workspace/iteration-N/…`, `benchmark.md` |
| `iterate` | Fixes the skill from failures and near-misses, re-runs, up to the cap; writes the verdict | updated skill, `evaluation_report.md` |
| `describe` | Optional description tuning with trigger queries; each query is a real run | updated `description`, `description_tuning.md` |
| `document` | Usage guide with a real worked example from the evaluation | `skill_generator/<name>/<name>_USAGE.md` (+ `.docx` on request) |
| `share` | Prints the commands to make the skill available in every project or to package it as a plugin; copies nothing itself | nothing |

## How to run a phase

1. Resolve the name, source, and objective from `$ARGUMENTS`. If `skill_generator/<name>/design.md`
   exists, read it first so later phases build on the reviewed brief rather than re-deriving it.
2. Launch the `skill-builder` agent with the phase, the inputs, the output paths above, and the
   absolute path of this skill's reference folder, `${CLAUDE_SKILL_DIR}/references`. The agent reads:
   - `skill-writing-guide.md` for the `build` and `validate` phases;
   - `anti-hallucination-checklist.md` and `evidence-grades.md` for `design` and `document`;
   - `skill-eval-protocol.md` for `evals`, `benchmark`, `iterate`, and `describe`;
   - `usage-doc-template.md` for `document`.
3. Report the files written. For `benchmark` and `iterate`, report the pass rates with and without the
   skill and the tokens spent. For `document`, quote the example section so the user sees it without
   opening the file.

## Guardrails

- **Write only inside the current project.** The source documents may live elsewhere; read them where
  they are and never modify them.
- **Ask before replacing an existing skill.** If `.claude/skills/<name>/` already exists, ask whether to
  overwrite it, or write `<name>-v2` instead. The existing folder may hold hand edits.
- **Every claim needs a locator.** Nothing attributed to the source may lack a page, section, table, or
  equation reference in `design.md`. The objective may extend the source only where the brief says so
  explicitly and labels the extension.
- **Benchmark runs spend tokens.** Run exactly the cases and repetitions the user set, and report the
  token count.
- **Comment every script.** Any script the new skill bundles gets a header (purpose, inputs, outputs,
  and the source of every constant) and inline comments that explain why.

## Sharing the result (`share` phase)

Print the commands and stop; the user decides. Typical options:

```bash
# Use the skill in every project on this machine
cp -R .claude/skills/<name> ~/.claude/skills/

# Or package it as its own plugin (see the stress-rep-guideline plugin in this repository for a full example)
mkdir -p <plugin>/.claude-plugin <plugin>/skills && cp -R .claude/skills/<name> <plugin>/skills/
```

Remind the user to bundle a licence and, when the source text is reproduced in `references/`, an
attribution notice that matches the source's licence.

## Related

- The `skill-creator` plugin from Anthropic, if installed, provides a viewer and aggregation scripts that
  read the same evaluation files; the agent uses it when available.
