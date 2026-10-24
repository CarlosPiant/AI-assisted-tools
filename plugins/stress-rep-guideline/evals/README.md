# Evaluation set for `stress-rep-guideline`

Everything in this folder is synthetic. The five fixtures under `fixtures/` are fictional simulation write-ups invented for testing the skill; each opens with the banner "SYNTHETIC TEST DOCUMENT — fictional study written for evaluating the stress-rep-guideline skill; not real research" and names fictional authors and institutions. Nothing in them describes real research, real data or real institutions.

## Fixtures and what each one tests

| Fixture | Paradigm | Tests | Deliberate gaps (item → expected state) |
|---|---|---|---|
| `des_clinic.md` | DES, declared | A well-reported paper with a few gaps; sub-point N/A for 1.3b/c | 4.1 → Partially addressed (no warm-up selection method); 5.2 → Missing; 6.1 → Missing |
| `sd_epidemic.md` (Spanish) | SD, declared | Spanish manuscript, English report; justified N/A on 2.4 and 5.2; feedback loops under 2.1/2.2 | 3.1 → Partially addressed (no sample sizes/date ranges); 4.3 → Missing (calibration without method or runs); 5.4 → Missing |
| `abs_market.md` | ABS, declared | Prompt without the word "STRESS"; justified N/A on 2.5.4; an unjustified N/A claim on 5.4 | 3.4 → Partially addressed (assumptions not justified); 4.1 → Partially addressed (no warm-up statement); 5.4 → Missing (author's "not applicable" must be flagged) |
| `hybrid_incomplete.md` + `hybrid_incomplete_supp.md` | DES + SD, not declared | Paradigm inference with "just do it"; merged hybrid audit; interface check; multi-file corpus (3.3 and 4.3 credited from the supplement; 5.2 partial from the supplement) | 2.4, 3.1, 3.2, 3.4, 4.1, 5.3, 5.4, 6.1 → Missing; 2.5, 5.1, 5.2 → Partially addressed; 1.3, 2.3 → Not applicable |
| `decoy_markov.md` | Markov cohort CEA (not covered) | The skill must stop and name the three covered paradigms | none (no audit expected) |

Each fixture has a companion `<name>.truth.json` giving the expected paradigm, the expected state of every item and sub-item, the tally, the derivation of every deliberate gap from the fixture text, which items must be credited from a supplement, and grader tolerances where two states are defensible.

`evals.json` holds one eval per fixture (five in total), with a realistic prompt (English and Spanish, with and without the word "STRESS"), the input files, and checkable expectations drawn from the truth files. Top-level config: `iteration_cap` 3, `runs_per_case` 1, `threshold` 0.80 (the protocol's standard tier; the with-skill pass rate must also exceed the without-skill rate).

## Running the benchmark phase

Follow the skill-eval protocol shipped with the `skill-generator` plugin in this repository (`plugins/skill-generator/skills/generate-skill/references/skill-eval-protocol.md`):

1. For each eval, launch in the same turn two fresh subagents — one given the skill path `.claude/skills/stress-rep-guideline/` and the prompt, one given only the prompt — each writing to `workspace/iteration-<n>/eval-<id>/{with_skill,without_skill}/outputs/`, with `eval_metadata.json` and `timing.json`.
2. Grade each run with a fresh subagent that sees only the eval's `expectations` and the `outputs/` folder (never the truth files, the design brief or the skill text), writing `grading.json` with `text` / `passed` / `evidence` per expectation.
3. Aggregate into `benchmark.md`; read the failing and near-miss transcripts; fix the skill (never the tests) and repeat up to the iteration cap of 3; finish with `evaluation_report.md` and the verdict (ACCEPT / EXPERIMENTAL / REJECT).

Paths in `evals.json` are relative to this plugin's folder (`plugins/stress-rep-guideline/`), so run the benchmark from there or copy `evals/` into your project root. Write run outputs under a `workspace/` folder next to `evals/`; it is not shipped.
