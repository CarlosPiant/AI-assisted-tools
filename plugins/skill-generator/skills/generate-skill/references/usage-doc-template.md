# [Skill name] — usage guide

**Invoke:** `/[skill-name] [arguments]` · **Lives at:** `.claude/skills/[skill-name]/` · **Version:** [1.0.0] · **Generated:** [YYYY-MM-DD]

## What it does

[Two or three sentences: the task it performs, the method it applies, and what it produces. Name the
source the method comes from.]

## When it triggers

[The phrases a user says that should load this skill, as in the description. Add the situations in which
it should *not* be used and which skill to use instead.]

## How to use it

**Inputs**

| Input | Form | Required | Notes |
|---|---|---|---|
| [input] | [file path / text / number] | [yes/no] | [constraints, formats, defaults] |

**Invocation**

```
/[skill-name] [example arguments]
```

**Outputs**

| Output | Path | Format |
|---|---|---|
| [output] | [where it is written] | [format] |

**Options and variants** — [flags, the references/ files it may open, the scripts it runs.]

## Example

[One real run from the evaluation, not a sketch.]

**Request**

> [The exact prompt a user typed.]

**What the skill did**

[Three to six sentences: the steps it took, the files it read, the decisions it made and why.]

**Result**

```
[The real output, trimmed to what a reader needs to see it worked — a table, the key numbers, the file list.]
```

## Evaluation summary

| Iteration | Cases | With skill | Without skill | Verdict |
|---|---|---|---|---|
| [N] | [k] | [pass rate ± sd] | [pass rate ± sd] | [ACCEPT / EXPERIMENTAL / REJECT] |

[One paragraph: what failed and was fixed, remaining limitations, caveats for use. Full detail in
`skill_generator/[skill-name]/evaluation_report.md`.]

## Provenance

- **Source:** [Author (Year), title, venue or URL; the file path used]
- **Evidence grade:** [A official guideline / B peer-reviewed / C working paper / D preprint or blog]
- **Scope kept from the source:** [what the skill applies verbatim]
- **Extensions beyond the source:** [none, or what and why]
- **Design brief:** `skill_generator/[skill-name]/design.md`
