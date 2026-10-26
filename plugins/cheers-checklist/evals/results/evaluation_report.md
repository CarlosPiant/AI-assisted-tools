# Evaluation report — `cheers-checklist`

> **Published copy.** This is the evaluation of the skill as benchmarked on 2026-10-24. The skill shipped in this plugin differs from the benchmarked version only by wording edits made for publication, with no change to its rules, checklist text or scripts' behaviour: the description no longer names another tool (`/cheers-audit`) the reader may not have; "SOFT SmartPause" is now "pause once and ask the user to confirm"; output-location sentences say "the current project"; the provenance pointer names `references/provenance.md` instead of the unpublished design brief; and two script comments no longer mention a local setup. Run folders (`workspace/`) are not shipped; regenerate them with the protocol.

**Date:** 2026-10-24 · **Protocol:** the skill-eval protocol shipped with this repository's `skill-generator` plugin (`plugins/skill-generator/skills/generate-skill/references/skill-eval-protocol.md`) · **Config:** `evals/evals.json` — 5 evals, 56 expectations, `runs_per_case` 1, `iteration_cap` 3, threshold 0.80 (standard tier; the with-skill rate must also exceed the without-skill rate). Method mirrors the accepted sibling `skill_generator/stress-rep-guideline/evaluation_report.md`.

## Verdict

**ACCEPT** (standard tier). The with-skill mean pass rate across evals is **0.87** (expectation-weighted 48/56 = 0.857), against the 0.80 threshold. Without the skill it is **0.37** (21/56 = 0.375), so the margin is +0.50. No rubric dimension failed. The threshold was met and the baseline beaten on iteration 1, so the skill was not modified and no further iteration was run. Two caveats go into the usage document. First, each case was run once, so the rates carry no repetition variance. Second, the skill reads two items strictly (calibration note below).

## Quality rubric

| Dimension | Question | Evidence | Result |
|---|---|---|---|
| Triggering | Does the description name the phrases users say, and nothing misleading? | `SKILL.md` description (1,021 characters, under the 1,024 limit) lists 11 quoted trigger phrases: 7 English ("apply CHEERS", "CHEERS checklist", "CHEERS 2022", "check my economic evaluation against CHEERS", "is my cost-effectiveness analysis reported completely", "reporting checklist for my CEA", "fill in the CHEERS checklist for submission") and 4 Spanish ("aplicar CHEERS", "aplica CHEERS", "lista de verificación CHEERS", "¿cumple mi evaluación económica con CHEERS?"). It also names anti-triggers: cost-of-illness, burden and budget impact studies (it stops on these), and methods appraisal with Drummond or CHEC. **Overlap with the hub's `/cheers-audit`:** that skill's description contains "CHEERS checklist" and "reporting checklist for my CEA" verbatim, and "is my economic evaluation complete", which is close to this skill's "is my cost-effectiveness analysis reported completely". With both installed, the model has to pick one from the descriptions alone. This skill's description separates itself: "unlike /cheers-audit it adds no score, severity tier or pass/fail". The overlap stays open question 2 in `design.md` (retire, rename or narrow one skill at promotion). From the benchmark: the eval-3 prompt never names CHEERS ("the reporting standard for health economic evaluations") and the with-skill run audited against CHEERS 2022. The eval-2 Spanish prompt ran the full workflow. The with-skill runs were *told* to use the skill, so autonomous selection was not measured (same as the STRESS evaluation). | PASS (overlap with `/cheers-audit` to resolve at promotion) |
| Structure | Frontmatter valid, `SKILL.md` ≤ ~500 lines, references with a TOC, scripts commented | `structure_check.md`: frontmatter parses and `name` equals the folder. `SKILL.md` is 126 lines. All four reference files open with a Contents section (`cheers-checklist.md` 363 lines). `make_skeleton.py` (411 lines) and `extract_text.py` (186 lines) carry NN-1 headers, section comments and inline comments, and pass `--help`/`--list` and smoke runs. `--render-reference` reproduces the shipped reference byte for byte. `--verify` rejects a blank skeleton and a deliberately broken report. `quick_validate.py` complains only about the hub keys `argument-hint` and `effort`, as expected. In the benchmark, all four with-skill audit reports passed `--verify` inside their runs (run notes). | PASS |
| Fidelity | Every procedure, threshold, formula traces to a locator in `design.md` | Spot-check table below (12 rules traced). `tools/verify_verbatim.py`: **28/28 guidance strings** and 28/28 topic strings in `scripts/checklist.json` match the `pdftotext` layer of the Statement verbatim, and 58/58 clause fragments are literal substrings of their item's guidance. A negative control was rejected (`structure_check.md`). | PASS |
| Correctness | With-skill pass rate meets the threshold and exceeds the baseline | `benchmark.md` iteration-1: 0.87 ± 0.07 vs 0.37 ± 0.17. Every eval is ≥ 0.83 with the skill and ≤ 0.67 without. | PASS |
| Reproducibility | Same prompt → same structure of output across repetitions; scripts deterministic | `runs_per_case` = 1, so no repetition variance is available (caveat). `extract_text.py` and `make_skeleton.py` are deterministic: pure text transforms with no randomness and no network. All four with-skill audits (evals 1–4) have the same structure: a header with source, study type/form/basis, files audited, interpretation note, scope sentence and tally; seven category tables; a cross-check table; an N/A section; a Missing/Partial section with verbatim guidance; a 28-row submission table; the CC BY attribution line. The one stop case (eval 5) produced only the stop message. Item-level judgement on borderline clauses may vary between runs. | PASS with caveat |
| Safety | Writes only under the project; no hub paths; no credentials or network calls the source did not call for | Checks run after the 10 runs and 10 gradings (run start 2026-10-24T08:02:08Z = 01:02:08 PDT): (a) `find . -newer design.md -type f` outside `workspace/` returned only this phase's own `structure_check.md` (written 01:00:12, before the runs) and `benchmark.md` (written by the aggregator). No run wrote anywhere else in the project. (b) The newest mtimes of the skill, fixtures, `evals.json` and `design.md` are all ≤ 01:00:11 PDT, so no run modified them. (c) `quality_reports/` predates this session: it holds two `stress_audit_*` files dated Oct 21 and Oct 23, its directory mtime is Oct 23 20:03, and it has no `cheers_*` file. No run wrote into it. (d) `find <hub> -type f -mmin -120` returned nothing, and the hub's `.claude/skills/` has no `cheers-checklist` folder. (e) Each run's files are confined to its own `outputs/` and `scratch/` folders. The scripts make no network calls and read no credentials. | PASS |

### Fidelity spot-check

| # | Procedure / rule in the skill | Where in the skill | Locator in `design.md` (→ source) |
|---|---|---|---|
| 1 | 28 items in seven categories, audited in Table 1 order, with verbatim guidance | `SKILL.md` step 5; `scripts/checklist.json`; report section tables | §2.1, R18, R19 (Table 1, P3–P4/J5–J6; P4/J6) |
| 2 | Scope gate: stop when no alternative courses of action are compared, quoting the definition | `SKILL.md` step 3.1; `study-type-detection.md` | R1, S5 (abstract P1/J3; App. B § Objective) |
| 3 | Stop for budget impact analyses and constrained optimisation | `SKILL.md` step 3.1 | R4 (P4/J6; Summary points P2/J4) |
| 4 | No score, weight, severity tier or pass/fail; tally is plain arithmetic | `SKILL.md` description, verification list; report tally line | R7, R25, S9 (P2/J4; P4/J6; App. B) |
| 5 | Scope sentence: reporting completeness, not the quality of conduct | `SKILL.md` header; report header | R8 (P4/J6) |
| 6 | Source-designated Not applicable: 11–13 for cost analyses, 16 and 22 for non-modelling studies | `SKILL.md` step 5.1; `decision-rules.md` R14, R35, R36; `make_skeleton.py` pre-marks | R14, R35, R36 (P4/J6) |
| 7 | Submission table uses "Not applicable" / "Not reported", never "Not conducted" | `SKILL.md` step 7; `report-template.md` rule 7; `--verify` | R13, R15, R16 (P4/J6) |
| 8 | Main text and supplements form one corpus; supplement locators count | `SKILL.md` Usage and step 5.2; `extract_text.py` markers | R17 (P5/J7) |
| 9 | "No analysis plan was developed" answers item 4 (Addressed); "no discounting because 12 months" answers item 10 | `SKILL.md` step 5.3; `decision-rules.md` R29, S3 | R29, S3, J3 (Table 1 item 4, item 10) |
| 10 | 21 and 25 Not applicable on an explicit no-involvement statement; silence on both → Missing | `SKILL.md` step 5 (engagement paragraph); `decision-rules.md` R33 | R23, R33, J2 (App. A Results/Reflections; Table 1 items 21, 25) |
| 11 | Guidance quoted in English, never translated; quotes kept in the manuscript's language | `SKILL.md` step 8 | R27, J7 (P5/J7) |
| 12 | Study-type detection, the four states, clause decomposition, S2's rejection of an author's "not applicable" on unconditional items, and the cross-check pairs are the skill's own additions, labelled as such | `SKILL.md` step 3, step 5.1; `decision-rules.md` §4 (S1–S9) | §2.6 (source silent), §2.7 S1–S9, J5, J8 |

## Per-eval results (iteration 1)

| Eval | Name | Pass with | Pass without | Δ | Duration with / without | Tokens with / without |
|---|---|---|---|---|---|---|
| 1 | cua_markov_declared | 0.85 (11/13) | 0.23 (3/13) | +0.62 | 121 s / 118 s | 144,699 / 112,118 |
| 2 | cea_ensayo_es_spanish | 0.85 (11/13) | 0.31 (4/13) | +0.54 | 164 s / 144 s | 149,342 / 114,709 |
| 3 | flu_outreach_no_keyword | 0.83 (10/12) | 0.33 (4/12) | +0.50 | 178 s / 160 s | 149,983 / 114,447 |
| 4 | thin_model_inferred_with_appendix | 0.83 (10/12) | 0.67 (8/12) | +0.17 | 200 s / 138 s | 152,101 / 111,604 |
| 5 | decoy_cost_of_illness_stop | 1.00 (6/6) | 0.33 (2/6) | +0.67 | 30 s / 98 s | 107,987 / 105,786 |
| **mean ± sd (across evals)** | | **0.87 ± 0.07** | **0.37 ± 0.17** | **+0.50** | 139 ± 67 s / 132 ± 24 s | 140,822 ± 18,553 / 111,733 ± 3,597 |

Expectation-weighted: with-skill 48/56 = 0.857; without-skill 21/56 = 0.375. Source: `benchmark.md`. Raw files are under `workspace/iteration-1/eval-<id>/{with_skill,without_skill}/`.

What the baseline got wrong, for contrast:
- It never stated the basis for the study type. In eval 4 it did not say the type was inferred.
- It named files without the `cheers_checklist_` prefix and, in eval 1, put all 28 items in one flat table without the seven categories.
- It paraphrased evidence and CHEERS guidance instead of quoting them.
- It omitted the submission table in evals 1, 3 and 4.
- It added severity or priority tiers ("Must fix / Should fix", "Imprescindibles / Recomendadas / Menores", "Addressed (minor)").
- On the Spanish eval it wrote the report, labels and translated guidance in Spanish and rated item 22 Partially addressed instead of following CHEERS's Not-applicable example for non-modelling studies.
- On eval 3 it marked item 21 Addressed despite the explicit no-involvement statement.
- On the cost-of-illness decoy it ran a full 28-item "closest fit" audit with a tally, which it was not asked for.

The baseline did best on eval 4 (0.67), where a thin paper makes most gaps obvious.

## The eight failed with-skill expectations

Seven of the eight are the skill rating an item **one notch stricter** than the truth file. The skill was never more lenient outside the tolerances the truth file allows (`diff_truth.py`: the only lenient deviations are items 7, 12, 17 and 20 in eval 4, all inside the stated tolerance). Each strict call names a gap that exists in the fixture text. For example, cua_markov's Table 2 says it "lists every model input" but has no background-mortality or AKI-probability rows, although § 2.7 and § 2.13 use them. No failure is structural. Every with-skill run got these right: study type and basis, the "just do it" handling, the scope gate, 28 items in seven categories, the R14 Not-applicable items, rejection of the author's unjustified N/A on item 19, Spanish quotes with English guidance, the submission-table labels, and no score.

| Eval | Expectation | What the run did | Explanation |
|---|---|---|---|
| 1 | Every other item (incl. 22) Addressed | 22 Partially addressed: Table 2 omits mortality multipliers and background mortality, the AKI probability, the mycotic-infection QALY decrement and cost, adverse-event unit costs, and transport costs | Strict reading of "Report **all** analytic inputs"; the run labels it its own judgement of "all" |
| 1 | Tally 25 / 1 / 2 / 0 | 24 / 2 / 2 / 0 | Follows from item 22 (tally matches the run's own rows) |
| 2 | 16 and 22 N/A *citing CHEERS's statement* | States and justification quote correct, but the rows cite only the skill's internal rule id "R14 (non-modelling study)", not CHEERS's sentence or its locator P4/J6 | Presentation gap, not a judgement error. `report-template.md` rule 5 asks for "the rule id"; the R14 text with P4/J6 is in `decision-rules.md` but not carried into the report. Readers without the skill cannot resolve "R14" |
| 2 | Tally 23 / 2 / 1 / 2 | 22 / 3 / 1 / 2 | Item 23 Partially addressed: total cost per arm only, no means by the main cost categories. The run itself flags "a strict reading of 'main categories'; you could argue the item is met" |
| 3 | Every other item Addressed | 12, 22, 23, 24 Partially addressed: harms (adverse events incl. GBS) named but no measurement described; inputs used but missing from the parameter table; no means by cost category; time-horizon effect not reported | 22 and 23 as above. 12 and 24 are clause-strict readings of "benefit(s) **and harm(s)**" and "effect of choice of … time horizon, if applicable" |
| 3 | Tally 24 / 1 / 1 / 2 | 20 / 5 / 1 / 2 | Follows from the four items above |
| 4 | 22 Addressed from appendix § A2 | 22 Partially addressed: home-visit frequency, transitions out of the readmitted state and the hip-fracture multiplier value are not reported | Same strict "all analytic inputs" reading. The appendix is credited as the location |
| 4 | Tally within ±2 per state (8 / 7 / 13 / 0) | 7 / 11 / 10 / 0: 22 and 23 stricter (outside the tolerance set) plus 7, 12, 17, 20 inside the tolerance set | Out-of-tolerance part comes only from 22 and 23 |

Disposition: **no change to the skill**. Iteration 1 met the threshold and beat the baseline, and the protocol forbids editing tests to make them pass, so these were not "fixed". The stricter readings follow the verbatim clause wording, so they are not a fidelity problem. They are a calibration preference, recorded in the usage document with the places to adjust them:
- **Strictness:** `references/decision-rules.md` §5 (evidence standards). For example, "all analytic inputs" could be read as the inputs the parameter table claims to list, and "main categories of costs" as satisfied by totals per arm.
- **N/A wording:** `references/report-template.md` §2 rule 5. Have Not-applicable rows quote R14's sentence with P4/J6 instead of the bare rule id.

The tests, fixtures and truth files were not edited.

**Grading-tool note.** The independent checker `workspace/_tools/check_report.py` first read the Spanish label "No cumple" (= Missing) as Addressed. The eval-2 baseline grader saw this and graded item 28 by reading the report. The pattern order was corrected after grading, and a re-run reproduces the grader's recount of 20 / 6 / 1 / 1. No grade changed.

## Tokens spent

| Stage | Runs | Tokens |
|---|---|---|
| With-skill runs | 5 | 704,112 |
| Without-skill runs | 5 | 558,664 |
| Grading runs (fresh graders, expectations + outputs only) | 10 | 1,103,521 |
| **Total** | 20 | **2,366,297** |

Exactly `runs_per_case` = 1; no repetitions or extra runs were added. Durations:
- With skill: 30–200 s. The thin model with its appendix is the slowest; the stop case is the fastest, because the skill stops at the scope gate.
- Without skill: 98–160 s.

## Files

- `benchmark.md`: per-iteration table, generated by `workspace/_tools/aggregate_benchmark.py`.
- `workspace/iteration-1/eval-<id>/`:
  - `expectations.json`: the grader's only view of the eval.
  - `{with_skill,without_skill}/`: `outputs/`, `eval_metadata.json`, `timing.json`, `grading.json`; with-skill runs also have `scratch/`.
- `workspace/_tools/`, all commented per NN-1:
  - `setup_iteration.py`, `write_timing.py` and `aggregate_benchmark.py`, adapted from stress-rep-guideline.
  - `check_report.py`: the independent grading checker.
  - `diff_truth.py`: orchestrator-only comparison against the truth files.
- `design.md`: iteration log appended.
- `cheers-checklist_USAGE.md` / `.docx`: usage document with the eval-2 worked example.
