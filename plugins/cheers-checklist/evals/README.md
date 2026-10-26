# Evaluation set for `cheers-checklist`

Everything in this folder is synthetic. The six files under `fixtures/` (five fixtures, one with a technical appendix) are fictional health economic write-ups invented for testing the skill; each opens with the banner "SYNTHETIC TEST DOCUMENT — fictional study written for evaluating the cheers-checklist skill; not real research" and names fictional authors, institutions, countries (Freedonia, Northshire, Valdeluna) and currencies. Nothing in them describes real research, real data or real institutions.

## Fixtures and what each one tests

| Fixture | Study type / form | Tests | Deliberate gaps (item → expected state) | Tally A / P / M / N/A |
|---|---|---|---|---|
| `cua_markov.md` | model-based (Markov) CUA, declared | A well-reported paper; engagement items credited; HEAP and distributional items not invented | 4 → Missing; 16 → Partially addressed (no public-availability statement); 19 → Missing | 25 / 1 / 2 / 0 |
| `cea_ensayo_es.md` (Spanish) | empirical trial-based CEA, declared | Spanish manuscript, English report, Spanish quotes, English guidance; R14 N/A for non-modelling studies; "no discounting because 12 months" is Addressed | 8 → Partially addressed (no reason for perspective); 15 → Partially addressed (no price year/dates); 28 → Missing; 16, 22 → Not applicable (R14) | 23 / 2 / 1 / 2 |
| `flu_outreach_cea.md` | model-based (decision tree) CEA, declared | Prompt never says "CHEERS"; justified N/A (21, 25) from an explicit no-involvement statement; unjustified author "Not applicable" on 19; "no plan was prepared" answers item 4 | 19 → Missing (claim flagged); 26 → Partially addressed (no ethical/equity considerations); 21, 25 → Not applicable | 24 / 1 / 1 / 2 |
| `thin_model.md` + `thin_model_appendix.md` | model-based CUA, **not declared** | Study-type inference with "just do it"; corpus rule (15 and 22 credited from the appendix only); silence on conditional items is Missing, not N/A; cross-check flags | 2, 4, 8, 12, 13, 17, 18, 19, 20, 21, 25, 27, 28 → Missing; 1, 7, 9, 10, 16, 24, 26 → Partially addressed | 8 / 7 / 13 / 0 |
| `decoy_coi.md` | cost-of-illness study, no comparator | Scope gate: the skill must stop and quote the CHEERS definition | none (no audit expected) | — |

## Running the benchmark phase

Follow the skill-eval protocol shipped with the `skill-generator` plugin in this repository (`plugins/skill-generator/skills/generate-skill/references/skill-eval-protocol.md`):

1. For each eval, launch in the same turn two fresh subagents — one given the skill path `skills/cheers-checklist/` and the prompt, one given only the prompt — each writing to `workspace/iteration-<n>/eval-<id>/{with_skill,without_skill}/outputs/`, with `eval_metadata.json` and `timing.json`. Tell both runs to write the report into their `outputs/` folder instead of `quality_reports/`.
2. Grade each run with a fresh subagent that sees only the eval's `expectations` and the `outputs/` folder (never the truth files or the skill text), writing `grading.json` with `text` / `passed` / `evidence` per expectation. Check script-checkable assertions (28 rows, tally arithmetic, submission-table labels) with a small checker of your own rather than the skill's `--verify`, so the grader stays independent of the skill.
3. Aggregate into `benchmark.md`; read the failing and near-miss transcripts; fix the skill (never the tests) and repeat up to the iteration cap of 3; finish with `evaluation_report.md` and the verdict (ACCEPT / EXPERIMENTAL / REJECT).

Paths in `evals.json` are relative to this plugin's folder (`plugins/cheers-checklist/`), so run the benchmark from there or copy `evals/` into your project root. Write run outputs under a `workspace/` folder next to `evals/`; it is not shipped. The results of the original run are in [`results/`](results/).

## Known judgment calls the benchmark exercises

- Item 22 Not applicable for the trial-based Spanish fixture even though it lists unit costs (the Statement's literal example for non-modelling studies; judgment call J4 in `../skills/cheers-checklist/references/provenance.md`).
- Item 19: an author's "Not applicable" without a reason is not accepted (rule S2; J5).
- Item 4: "No health economic analysis plan was prepared" is Addressed (rules R29 and S3; J3).
