# Skill evaluation protocol

Used by the `skill-builder` agent (launched by `/generate-skill`) to benchmark a generated skill. The file formats match
Anthropic's `skill-creator` plugin so its viewer and aggregation scripts can read the results when the
plugin is installed, and so results stay comparable when it is not.

## Layout

```
skill_generator/<name>/
├── evals/evals.json                 # test prompts (+ assertions once drafted)
├── workspace/
│   └── iteration-1/
│       └── eval-<id>/
│           ├── with_skill/    outputs/, eval_metadata.json, timing.json, grading.json
│           └── without_skill/ outputs/, eval_metadata.json, timing.json, grading.json
├── benchmark.md                     # aggregated, per iteration
└── evaluation_report.md             # verdict + evidence
```

## `evals/evals.json`

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "What a real user would type",
      "expected_output": "What a correct result contains",
      "files": ["relative/path/to/input.csv"],
      "expectations": ["Assertion 1 …", "Assertion 2 …"]
    }
  ]
}
```

Write the prompts first and the `expectations` while the runs execute, from the user's success
criteria. Good assertions are checkable and specific ("reports the ICER in $/QALY with the stated
discount rate") rather than vague ("is thorough"); a passing grade on a weak assertion tells nothing.

## Runs

For each eval launch two fresh subagents in the same turn: one told to use the skill (give it the
skill path and the prompt), one given only the prompt. Each writes its deliverables to its `outputs/`
folder. Save `eval_metadata.json` (`eval_id`, `run_type`, `skill_path` or `null`, `prompt`, `started_at`)
and, when the run completes, `timing.json` (`duration_ms`, `total_tokens`) from the completion
notification. Repeat `runsPerCase` times when the user asked for more than one.

## `grading.json`

```json
{
  "expectations": [
    { "text": "Assertion text", "passed": true, "evidence": "Quote or file:line from outputs/" }
  ],
  "pass_rate": 0.67,
  "notes": "Anything the grader saw that the assertions missed"
}
```

Grade with a fresh subagent that reads only the assertions and the `outputs/` folder. Assertions that
can be checked by a script (file exists, number within tolerance, column present) are checked by a
script, not by eye. The field names `text`, `passed`, `evidence` are fixed; the viewer depends on them.

## `benchmark.md`

Per iteration, a table with one row per eval and one summary row: pass rate, duration, and tokens,
each as mean ± sd over repetitions, for with-skill and without-skill, plus the difference. When the
`skill-creator` plugin is installed, `python -m scripts.aggregate_benchmark` produces this; otherwise
compute it from the `grading.json` and `timing.json` files.

## Quality rubric (applied in `evaluation_report.md`)

| Dimension | Question | Evidence |
|---|---|---|
| Triggering | Does the description name the phrases users say, and nothing misleading? | description text; optional trigger-query run |
| Structure | Frontmatter valid, `SKILL.md` ≤ ~500 lines, references with a TOC, scripts commented | `structure_check.md` |
| Fidelity | Every procedure, threshold, formula traces to a locator in `design.md` | spot-check table |
| Correctness | With-skill pass rate meets the threshold and exceeds the baseline | `benchmark.md` |
| Reproducibility | Same prompt → same structure of output across repetitions; scripts deterministic | repetition variance |
| Safety | Writes only under the project; no credentials or network calls the source did not call for | transcript grep |

## Verdict

Three tiers: **conservative** 90 %, **standard** 80 %, **experimental**
70 % with-skill pass rate, and in every case the with-skill rate must exceed the without-skill rate
(otherwise the skill adds cost without value).

- **ACCEPT** — threshold met, baseline beaten, no rubric dimension failed.
- **EXPERIMENTAL** — threshold met on at least one iteration or baseline beaten by a small margin; ship
  with the caveat in the usage document.
- **REJECT** — below threshold after the iteration cap, or a fidelity/safety failure. Keep the files;
  state what would have to change.

## What not to do

- Do not edit a test to make it pass; fix the skill or record the limitation.
- Do not let the grader see the design brief or the skill text; it grades outputs only.
- Do not add runs beyond what the user set; each one spends tokens.
