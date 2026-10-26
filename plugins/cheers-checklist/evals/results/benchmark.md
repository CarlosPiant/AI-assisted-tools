# Benchmark — `cheers-checklist`

> **Published copy.** This is the evaluation of the skill as benchmarked on 2026-10-24. The skill shipped in this plugin differs from the benchmarked version only by wording edits made for publication, with no change to its rules, checklist text or scripts' behaviour: the description no longer names another tool (`/cheers-audit`) the reader may not have; "SOFT SmartPause" is now "pause once and ask the user to confirm"; output-location sentences say "the current project"; the provenance pointer names `references/provenance.md` instead of the unpublished design brief; and two script comments no longer mention a local setup. Run folders (`workspace/`) are not shipped; regenerate them with the protocol.

Generated 2026-10-24 by `workspace/_tools/aggregate_benchmark.py` from the `grading.json` / `timing.json` files under `workspace/`. Protocol: the skill-eval protocol shipped with this repository's `skill-generator` plugin (`plugins/skill-generator/skills/generate-skill/references/skill-eval-protocol.md`). Config from `evals/evals.json`: threshold 0.80 (standard tier), runs_per_case 1, iteration_cap 3.

Pass rate = passed expectations / expectations for that eval. Per-eval sd is n/a because `runs_per_case` is 1 (one repetition per case); the summary row's ± is the sd **across evals**. Δ = with-skill − without-skill. Tokens and durations are the subagent totals reported by the harness for each run (the run itself; grading runs are listed separately).

## iteration-1

| Eval | Name | Pass with | Pass without | Δ pass | Duration with | Duration without | Δ dur | Tokens with | Tokens without | Δ tokens |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | cua_markov_declared | 0.85 (11/13) ± n/a | 0.23 (3/13) ± n/a | +0.62 | 121 s | 118 s | +3 s | 144,699 | 112,118 | +32,581 |
| 2 | cea_ensayo_es_spanish | 0.85 (11/13) ± n/a | 0.31 (4/13) ± n/a | +0.54 | 164 s | 144 s | +20 s | 149,342 | 114,709 | +34,633 |
| 3 | flu_outreach_no_keyword | 0.83 (10/12) ± n/a | 0.33 (4/12) ± n/a | +0.50 | 178 s | 160 s | +18 s | 149,983 | 114,447 | +35,536 |
| 4 | thin_model_inferred_with_appendix | 0.83 (10/12) ± n/a | 0.67 (8/12) ± n/a | +0.17 | 200 s | 138 s | +61 s | 152,101 | 111,604 | +40,497 |
| 5 | decoy_cost_of_illness_stop | 1.00 (6/6) ± n/a | 0.33 (2/6) ± n/a | +0.67 | 30 s | 98 s | -68 s | 107,987 | 105,786 | +2,201 |
| **mean ± sd (across evals)** | | **0.87 ± 0.07** | **0.37 ± 0.17** | **+0.50** | 139 ± 67 s | 132 ± 24 s | +7 s | 140,822 ± 18,553 | 111,733 ± 3,597 | +29,090 |

Expectation-weighted pass rate: with-skill **48/56 = 0.857**, without-skill 21/56 = 0.375. Run tokens this iteration: with-skill 704,112, without-skill 558,664, total 1,262,776.

Threshold 0.80: MET (mean across evals); baseline beaten.

### Failed with-skill expectations

- eval 1 (cua_markov_declared): Reports every other item (1-3, 5-15, 17, 18, 20, 22-28) as Addressed.
- eval 1 (cua_markov_declared): The tally reads Addressed 25, Partially addressed 1, Missing 2, Not applicable 0 and matches the per-item states.
- eval 2 (cea_ensayo_es_spanish): Reports items 16 and 22 as Not applicable, citing CHEERS's statement that items 16 and 22 do not apply to non-modelling studies, and quotes 'No se utilizó ningún modelo de decisión' as the document's justification.
- eval 2 (cea_ensayo_es_spanish): The tally reads Addressed 23, Partially addressed 2, Missing 1, Not applicable 2 and matches the per-item states.
- eval 3 (flu_outreach_no_keyword): Reports every other item (1-3, 5-15, 17, 20, 22-24, 27, 28) as Addressed.
- eval 3 (flu_outreach_no_keyword): The tally reads Addressed 24, Partially addressed 1, Missing 1, Not applicable 2 and matches the per-item states.
- eval 4 (thin_model_inferred_with_appendix): Reports item 22 (Study parameters) as Addressed with a locator in thin_model_appendix.md (section A2).
- eval 4 (thin_model_inferred_with_appendix): The tally over the 28 items is consistent with the per-item states shown (expected Addressed 8, Partially addressed 7, Missing 13, Not applicable 0; deviations of up to 2 per state acceptable if they come from items 1, 7, 12, 17 or 20).

