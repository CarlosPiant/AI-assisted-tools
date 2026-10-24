# Skill writing guide

How the `skill-builder` agent writes and checks a skill. It follows Anthropic's published guidance for
Agent Skills and the conventions used across this repository.

## Contents

1. Anatomy of a skill
2. Frontmatter
3. Writing the description
4. Writing the body
5. Bundled files
6. Structure check

## 1. Anatomy of a skill

```text
<skill-name>/
├── SKILL.md          # required: frontmatter + instructions
├── references/       # optional: long material read only when a step says so
├── scripts/          # optional: deterministic work every run would otherwise redo
└── assets/           # optional: templates, images, or files copied into outputs
```

Skills load in three levels. The name and description are always in context, so they must be short and
precise. The body loads when the skill triggers, so it should stay under about 500 lines. Bundled files
load only when the body tells Claude to open them, so they can be as long as the material requires.

## 2. Frontmatter

```yaml
---
name: kebab-case-name                # must equal the folder name
description: "…"                     # trigger text; see section 3
argument-hint: "<input> [--option]"  # shown when the user types the slash command
allowed-tools: ["Read", "Grep", "Glob", "Bash", "Write"]   # only what the body uses
effort: medium                       # low | medium | high — depth of reasoning the skill needs
---
```

Optional keys: `disable-model-invocation: true` when the skill must only run on an explicit slash
command, for example because it writes files other work depends on; `context: fork` when the skill should
run in a fresh context so earlier conversation does not bias it.

For a skill that will also be uploaded to claude.ai, keep a copy whose frontmatter holds only `name`,
`description`, `license`, `allowed-tools`, `metadata`, and `compatibility`.

## 3. Writing the description

The model decides whether to load a skill from its description alone, and skills tend to under-trigger,
so the description carries all the "when to use" information. Use this formula:

> [What it does] + [what it produces] + [its key boundary]. Use when the user says "[phrase 1]",
> "[phrase 2]", … "[phrase 5–10]".

- Name the concrete task and output, not a category ("audits a simulation write-up against the 20 STRESS
  items", not "helps with reporting").
- List the phrases users actually say, in every language the skill supports, including requests that do
  not name the method.
- State the main boundary when a near-miss request is likely ("Not for stress tests of servers").
- Keep it under about 1,000 characters.

## 4. Writing the body

- **Open with purpose and scope.** One paragraph on what the skill does and the source it implements,
  then one sentence on what it deliberately does not do.
- **Show the invocation.** A code block with two or three real examples, then each argument in one line.
- **Map the bundled files.** A table of each file and the step at which to open it.
- **Describe outcomes, not choreography.** Use numbered steps only where order matters, such as extract
  before audit. Elsewhere say what a correct result contains and how to check it; the model plans well
  and over-scripted steps reduce output quality.
- **Give reasons, not volume.** "Quote the evidence verbatim, because the author must find it again" works
  better than capitals and "MUST". Keep emphasis for the one or two constraints whose violation is costly.
- **End with verification, examples, and troubleshooting.** A short checklist the skill runs before
  handing over; two or three examples of request, actions, and result; and the failure cases with what to
  do about each.
- **Cite the source** near the top, with its DOI or URL, and keep every procedure traceable to a locator
  in the design brief.

## 5. Bundled files

- **`references/`** hold long tables, verbatim checklists, derivations, and variant-specific procedures.
  Give any file over about 300 lines a table of contents. Split by variant so the skill opens only the one
  it needs.
- **`scripts/`** hold computations that must be exact and repeatable. Each script gets a header comment
  with its purpose, inputs, outputs, and the source of every constant, plus inline comments explaining
  why. Prefer the standard library; when a dependency is needed, fall back gracefully and say what to
  install.
- **Paths.** Refer to bundled files as `${CLAUDE_SKILL_DIR}/references/<file>` and
  `${CLAUDE_SKILL_DIR}/scripts/<file>`, so they resolve wherever the skill is installed. Never hard-code a
  machine path.
- **Licences.** When source text is reproduced, put the attribution required by the source's licence
  at the top of each file that contains it.

## 6. Structure check

Run before every hand-over and record the result in `structure_check.md`:

| Check | Pass when |
|---|---|
| Frontmatter | Parses as YAML; `name` equals the folder name; keys limited to those in section 2 |
| Description | States task, output, boundary, and at least five trigger phrases |
| Length | `SKILL.md` under about 500 lines; references over 300 lines have a table of contents |
| Paths | Every file the body mentions exists; no absolute machine paths |
| Scripts | Each runs on `--help` or a smoke input and has header and inline comments |
| Fidelity | Each procedure, threshold, and formula maps to a locator in the design brief |
| Attribution | Reproduced source text carries the licence's required notice |
