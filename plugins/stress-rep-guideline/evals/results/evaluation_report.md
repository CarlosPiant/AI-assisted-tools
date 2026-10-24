# Evaluation report — `stress-rep-guideline`

**Date:** 2026-10-20 · **Protocol:** `the skill-eval protocol shipped with the skill-generator plugin` · **Config:** `evals/evals.json` — 5 evals, 57 expectations, `runs_per_case` 1, `iteration_cap` 3, threshold 0.80 (standard tier; the with-skill rate must also exceed the without-skill rate).

## Verdict

**ACCEPT** (standard tier). With-skill mean pass rate across evals **0.92** (expectation-weighted 52/57 = 0.912) against the 0.80 threshold; without-skill **0.33** (18/57 = 0.316); margin +0.59. No rubric dimension failed. The threshold was met and the baseline beaten on iteration 1, so the skill was not modified and no further iteration was run. Caveat carried into the usage document: one repetition per case, so the rates carry no repetition variance.

## Quality rubric

| Dimension | Question | Evidence | Result |
|---|---|---|---|
| Triggering | Does the description name the phrases users say, and nothing misleading? | `SKILL.md` description (1,044 characters) lists 10 English and 5 Spanish trigger phrases ("apply STRESS", "run the STRESS test", "is my DES / SD / ABS model reported completely", "simulation reporting checklist", "aplicar STRESS", "¿cumple mi documentación con STRESS?", …) and anti-triggers (server/finance/psychology stress tests; CHEERS/ISPOR audits). Trigger-query evidence from the benchmark: eval 3's prompt contains no "STRESS" ("Is my ABS model reported completely? … simulation reporting checklist") and the with-skill run selected STRESS-ABS with basis declared (expectation 1 passed); eval 2's Spanish prompt triggered STRESS-SD. | PASS |
| Structure | Frontmatter valid, `SKILL.md` ≤ ~500 lines, references with a TOC, scripts commented | `structure_check.md`: frontmatter parses, `name` equals the folder; `SKILL.md` 127 lines; the five reference files over ~85 lines each open with a Contents section; both scripts carry NN-1 headers, section and inline comments and pass `--help` / smoke runs; `quick_validate.py` complains only about the hub-specific keys `argument-hint` and `effort`, as expected. | PASS |
| Fidelity | Every procedure, threshold, formula traces to a locator in `design.md` | Spot-check table below (12 items traced); 140/140 recommendation chunks in `scripts/checklist.json` matched verbatim against the supplement extractions (`structure_check.md`). | PASS |
| Correctness | With-skill pass rate meets the threshold and exceeds the baseline | `benchmark.md` iteration-1: 0.92 ± 0.08 vs 0.33 ± 0.13; every eval individually ≥ 0.85 with the skill and ≤ 0.50 without. | PASS |
| Reproducibility | Same prompt → same structure of output across repetitions; scripts deterministic | `runs_per_case` = 1, so no repetition variance is available (caveat). `extract_text.py` and `make_skeleton.py` are deterministic (pure text transforms, no randomness, no network); `make_skeleton.py --render-reference` re-renders the shipped reference files byte-identically (`structure_check.md`). The four audited with-skill runs (evals 1–4) all produced the same report structure: header with variant/basis/files/numbering note/scope/tally, six section tables, cross-reference table, Not-applicable section, closing Missing/Partial table with verbatim recommendations. | PASS with caveat |
| Safety | Writes only under the project; no hub paths; no credentials or network calls the source did not call for | Checks run after the 10 runs and 10 grading runs: (a) `ls -d quality_reports` in the project root → none; (b) `find . -type f -mmin -60 -not -path './workspace/*'` → only files whose mtimes (22:43–23:04 UTC) predate the first run start (23:06:28 UTC per `eval_metadata.json`); (c) `stat` of every skill, fixture, evals.json and design.md file → all mtimes before 23:06:28 UTC, so no run modified them; (d) `find <hub>/.claude/skills -type f -mmin -60` → empty; (e) every run's deliverables are confined to its `outputs/` and `scratch/` folders (listing in `benchmark` phase log). The scripts make no network calls and read no credentials. | PASS |

### Fidelity spot-check

| # | Procedure / rule in the skill | Where in the skill | Locator in `design.md` (→ source) |
|---|---|---|---|
| 1 | 20 items in six sections; three variants STRESS-DES / -SD / -ABS selected by model type | `SKILL.md` header and step 4; `scripts/checklist.json` | §2.1 (Table 3, P7/J60; abstract P2/J55; §5.1 P6/J59) |
| 2 | Numbering 3.2 Pre-processing / 3.3 Input parameters, with the header note that the article's Table 3 prints the reverse | `SKILL.md` step 7; `report-template.md` | §2.1 and D1, R35 (supplements 3.2–3.3 vs PDF Table 3 P7/J60) |
| 3 | Scope sentence: reporting completeness only, not validity, verification or calibration | `SKILL.md` header; report header | R14 (§6, P11/J64), R11 (§6, P10/J63) |
| 4 | Supplements are searched before any item is marked Missing; multi-file corpus | `SKILL.md` steps 1–2, 5.2 | R3 (§6, P9/J62; §5.3 P7/J60; §5.5 P7/J60) |
| 5 | Deterministic model → 5.2 Random sampling Not applicable | `decision-rules.md` R16; `SKILL.md` step 5.1 | R16 (§5.6, P9/J62) and D11 (SD-supp / ABS-supp 4.3) |
| 6 | 5.4 System Specification is never automatically Not applicable; Missing for small models noted as low impact | `decision-rules.md` R17 | R17 (§5.6, P9/J62; DES/SD/ABS-supp 5.4 "particularly important for large scale models") |
| 7 | Hybrid: apply both STRESS-DES and STRESS-SD and add the interface check H.1, labelled provisional | `SKILL.md` steps 4 and 6; `decision-rules.md` §4 | R2 (§6, P9/J62), R20 (§8, P12/J65) |
| 8 | No experimentation beyond the base run → 1.3 Not applicable and 2.3 follows | `decision-rules.md` R21, R23 | R21 (DES-supp / ABS-supp / SD-supp 1.3), R23 (DES-supp 2.3 "(if any)") |
| 9 | "Available from the authors" is not evidence except as a 6.1 statement; a code link satisfies 6.1 only | `SKILL.md` step 5.4; `decision-rules.md` R7, R10 | R10 (§6, P10/J63), R7 (§6, P10/J63) |
| 10 | External URL alone → Partially addressed | `SKILL.md` step 5.4 | R4 (§6, P11/J64) |
| 11 | Confidential model → Partially addressed with "QA summary present/absent" | `SKILL.md` troubleshooting; `decision-rules.md` R12 | R12 (§6, P11/J64) |
| 12 | Paradigm detection (argument → declaration → vocabulary) and the four states / tally are the skill's own additions, labelled as such; no score, severity tier or pass/fail | `SKILL.md` step 3 ("STRESS gives no detection rule"), step 7 | §2.10 (source silent on detection, states, scoring; "STRESS test" informal, §8 P12/J65); §4 scope |

## Per-eval results (iteration 1)

| Eval | Name | Pass with | Pass without | Δ | Duration with / without | Tokens with / without |
|---|---|---|---|---|---|---|
| 1 | des_clinic_declared | 1.00 (13/13) | 0.23 (3/13) | +0.77 | 231 s / 232 s | 160,703 / 115,278 |
| 2 | sd_epidemic_spanish | 0.85 (11/13) | 0.23 (3/13) | +0.62 | 253 s / 215 s | 156,351 / 115,619 |
| 3 | abs_market_no_keyword | 0.92 (11/12) | 0.25 (3/12) | +0.67 | 283 s / 222 s | 161,516 / 114,530 |
| 4 | hybrid_inferred_with_supplement | 0.85 (11/13) | 0.46 (6/13) | +0.38 | 445 s / 218 s | 189,760 / 113,762 |
| 5 | decoy_markov_stop | 1.00 (6/6) | 0.50 (3/6) | +0.50 | 66 s / 136 s | 116,593 / 106,054 |
| **mean ± sd (across evals)** | | **0.92 ± 0.08** | **0.33 ± 0.13** | **+0.59** | 256 ± 135 s / 205 ± 39 s | 156,985 ± 26,175 / 113,049 ± 3,975 |

Expectation-weighted: with-skill 52/57 = 0.912; without-skill 18/57 = 0.316. Source: `benchmark.md`; raw files under `workspace/iteration-1/eval-<id>/{with_skill,without_skill}/`.

What the baseline got wrong, for contrast: it did not state the basis for the variant, named report files without the `stress_audit_` prefix, collapsed or skipped the 2.5 sub-items, never used Not applicable with a rule, paraphrased rather than quoted both evidence and recommendations, added Must/Should priority tiers, omitted the numbering note, and on the Markov decoy ran a "closest variant" STRESS-DES audit using the PSA's Monte Carlo draws as evidence of a simulation paradigm. On the Spanish eval it wrote the whole report in Spanish.

## The five failed with-skill expectations

All five are the skill rating a borderline item one notch *stricter* than the ground truth, never more lenient, and none is a structural failure (variant selection and basis, file naming, 20 items in six sections, sub-item expansion, rule-cited N/A handling, verbatim recommendations, the no-score rule, the hybrid interface check, supplement locators and the Markov stop passed on every eval).

| Eval | Expectation | What the run did | Explanation |
|---|---|---|---|
| 2 | 3.1 Partially addressed naming sample size, date ranges *and* use within the study as absent | Partially addressed, but judged "use within the study" present because § 6.3 / § 4.5 describe how the series are used | Clause-level judgement explained in the row; the state is right |
| 2 | Tally 15 / 1 / 2 / 2 | 14 / 3 / 1 / 2: read "se calibró" as engaging sub-point 1.3c Simulation optimisation (so 1.3 Partially addressed) and rated 4.3 Partially addressed (the deterministic/single-run clause is present) rather than Missing | `decision-rules.md` has no rule on whether a calibration mention engages 1.3c; the run flagged the ambiguity in its header. The companion expectation (4.3 "Missing or Partially addressed") passed |
| 3 | Tally 17 / 2 / 1 / 0 | 15 / 4 / 1 / 0: also Partially addressed on 3.3 (no selection rationale for the Uniform firm-threshold distribution; fee-rule constants unlisted) and 5.1 (NumPy version absent) | The skill applies "state how these were selected and prioritised above other candidate distributions" and "provide all details including version numbers" to every distribution and library; the truth file applies them to the main ones only |
| 4 | 3.3 Addressed from the supplement | Item Partially addressed: SD row Addressed (supplement S1) but DES row Partially addressed (Triangular triage distribution has no rationale); the hybrid rule takes the lower state | Same strictness on 3.3, amplified by the hybrid lower-state rule |
| 4 | 2.1 Addressed | Partially addressed: SD row lacks a causal-loop / stock-and-flow diagram; DES row Addressed | Hybrid lower-state rule applied to the SD 2.1 wording "Provide one or more causal loop, stock and flow … diagrams" |

Disposition: no change to the skill. The stricter reading follows the verbatim clause wording, so it is not a fidelity problem; it is a calibration preference recorded in the usage document, with `references/decision-rules.md` §6 (evidence standards) as the place to adjust it if the user wants the lenient reading. The tests and fixtures were not edited.

## Tokens spent

| Stage | Runs | Tokens |
|---|---|---|
| With-skill runs | 5 | 784,923 |
| Without-skill runs | 5 | 565,243 |
| Grading runs (fresh graders, outputs + assertions only) | 10 | 1,130,064 |
| **Total** | 20 | **2,480,230** |

Exactly `runs_per_case` = 1; no repetitions or extra runs were added. Durations: with-skill runs 66–445 s (the hybrid eval is the slowest because it audits two variants plus the interface check), without-skill 136–232 s.

## Files

- `benchmark.md` — per-iteration table, generated by `workspace/_tools/aggregate_benchmark.py`
- `workspace/iteration-1/eval-<id>/{with_skill,without_skill}/` — `outputs/`, `eval_metadata.json`, `timing.json`, `grading.json`
- `workspace/_tools/` — `setup_iteration.py`, `write_timing.py`, `aggregate_benchmark.py` (commented per NN-1)
- `design.md` — iteration log appended (Phase 3) and document-phase line (Phase 4)
- `stress-rep-guideline_USAGE.md` / `.docx` — usage document with the eval-1 worked example
