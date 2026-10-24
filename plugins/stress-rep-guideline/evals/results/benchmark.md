# Benchmark — `stress-rep-guideline`

Generated 2026-10-20 by `workspace/_tools/aggregate_benchmark.py` from the `grading.json` / `timing.json` files under `workspace/`. Protocol: `the skill-eval protocol shipped with the skill-generator plugin`. Config from `evals/evals.json`: threshold 0.80 (standard tier), runs_per_case 1, iteration_cap 3.

Pass rate = passed expectations / expectations for that eval. Per-eval sd is n/a because `runs_per_case` is 1 (one repetition per case); the summary row's ± is the sd **across evals**. Δ = with-skill − without-skill. Tokens and durations are the subagent totals reported by the harness for each run (the run itself; grading runs are listed separately).

## iteration-1

| Eval | Name | Pass with | Pass without | Δ pass | Duration with | Duration without | Δ dur | Tokens with | Tokens without | Δ tokens |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | des_clinic_declared | 1.00 (13/13) ± n/a | 0.23 (3/13) ± n/a | +0.77 | 231 s | 232 s | -1 s | 160,703 | 115,278 | +45,425 |
| 2 | sd_epidemic_spanish | 0.85 (11/13) ± n/a | 0.23 (3/13) ± n/a | +0.62 | 253 s | 215 s | +37 s | 156,351 | 115,619 | +40,732 |
| 3 | abs_market_no_keyword | 0.92 (11/12) ± n/a | 0.25 (3/12) ± n/a | +0.67 | 283 s | 222 s | +61 s | 161,516 | 114,530 | +46,986 |
| 4 | hybrid_inferred_with_supplement | 0.85 (11/13) ± n/a | 0.46 (6/13) ± n/a | +0.38 | 445 s | 218 s | +228 s | 189,760 | 113,762 | +75,998 |
| 5 | decoy_markov_stop | 1.00 (6/6) ± n/a | 0.50 (3/6) ± n/a | +0.50 | 66 s | 136 s | -70 s | 116,593 | 106,054 | +10,539 |
| **mean ± sd (across evals)** | | **0.92 ± 0.08** | **0.33 ± 0.13** | **+0.59** | 256 ± 135 s | 205 ± 39 s | +51 s | 156,985 ± 26,175 | 113,049 ± 3,975 | +43,936 |

Expectation-weighted pass rate: with-skill **52/57 = 0.912**, without-skill 18/57 = 0.316. Run tokens this iteration: with-skill 784,923, without-skill 565,243, total 1,350,166.

Threshold 0.80: MET (mean across evals); baseline beaten.

### Failed with-skill expectations

- eval 2 (sd_epidemic_spanish): Reports 3.1 Data sources as Partially addressed, naming the absent details (sample size, date ranges, use within the study).
- eval 2 (sd_epidemic_spanish): The tally reads Addressed 15, Partially addressed 1, Missing 2, Not applicable 2 and matches the per-item states.
- eval 3 (abs_market_no_keyword): Every item other than 3.4, 4.1 and 5.4 is Addressed and the tally reads Addressed 17, Partially addressed 2, Missing 1, Not applicable 0.
- eval 4 (hybrid_inferred_with_supplement): Reports 3.3 Input parameters as Addressed with a locator in hybrid_incomplete_supp.md (section S1).
- eval 4 (hybrid_inferred_with_supplement): Reports 4.2 Run length as Addressed (7 days, minutes) and 1.1, 1.2, 2.1, 2.2 as Addressed.

