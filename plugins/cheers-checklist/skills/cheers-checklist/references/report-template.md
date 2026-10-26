# CHEERS 2022 audit report — template

`scripts/make_skeleton.py --title "<doc title>" --modelling yes|no --form full|cost-analysis --output <path>` renders this layout with every item's verbatim guidance pre-filled. This file documents the layout and the filling rules. Output path: `quality_reports/cheers_checklist_<docname>.md` in the current project — never outside it.

## Contents

1. Layout
2. Filling rules
3. Verification

## 1. Layout

```markdown
# CHEERS 2022 reporting audit — <document title>

Source guideline: Husereau D, Drummond M, Augustovski F, et al. … Value Health. 2022;25(1):3-9. doi:10.1016/j.jval.2021.11.1351 — Table 1 (28 items).
Study type: <model-based | empirical (non-modelling)>; form: <…> — basis for selection: <declared | inferred and confirmed | inferred, user said proceed | argument>
Files audited: main document <name> (pages/sections); supplement(s) <names>
Interpretation note: CHEERS asks users to first consult the Explanation and Elaboration report (P4/J6); not available — items judged against Table 1 guidance only.
Scope: reporting completeness only, not conduct or appropriateness of methods (P4/J6; P2/J4).
Tally (arithmetic only; CHEERS 2022 has 'no validated scoring system' and scoring 'is strongly discouraged', P4/J6): Addressed n | Partially addressed n | Missing n | Not applicable n (of 28)

## 1. Title
| Item | State | Evidence (verbatim quote) | Locator | CHEERS 2022 guidance (verbatim) | Applicability / rules |
|---|---|---|---|---|---|
| **1 Title** | Addressed | "Cost-utility of …" | main, title | Identify the study as an economic evaluation and specify the interventions being compared. | unconditional — rules: - |

## 2. Abstract
## 3. Introduction
## 4. Methods              (items 4–21)
## 5. Results              (items 22–25)
## 6. Discussion           (item 26)
## 7. Other relevant information   (items 27–28)

## Cross-checks (skill-derived pairings, rule S7)
| Pair | Consistent? | Check | Basis |

## Items marked Not applicable — rule cited and whether the document justifies it
| Item | Rule | Document's justification (quote) or 'no justification given' |

## Missing and partially addressed items — what CHEERS 2022 asks for
| Item | State | CHEERS 2022 guidance (verbatim) | Locator in CHEERS | What is absent |

## Submission checklist table (CHEERS 2022 Table 1 format)
| Section/topic | Item No | Reported in section | State |
|---|---|---|---|
| Title | 1 | Title page | Addressed |
| Health economic analysis plan | 4 | Not reported | Missing |
| Rationale and description of model | 16 | Not applicable | Not applicable |

---
Attribution: CHEERS 2022 checklist (Table 1) © 2022 ISPOR / the authors … CC BY 4.0; reproduced verbatim.
```

## 2. Filling rules

1. **28 item rows, one state each**, from the four states only (`decision-rules.md` §1).
2. **Evidence column**: verbatim quote from the audited files in their own language (English or Spanish), long enough to show the clause is met; or "Table 3, rows 1–12". Never paraphrase here. Empty ("—") for Missing and for Not applicable unless the justification is quoted.
3. **Locator column**: `<main|supplement> <file>, p. <n>` for PDFs; `<main|supplement> <file>, § <heading>` for DOCX/MD; add table/figure numbers.
4. **Guidance column**: the verbatim CHEERS text from the skeleton; do not edit it. For Partial rows name the absent clause in the closing section.
5. **Not applicable rows** cite R14 or S2 (with the R29–R36 condition) and are listed in the N/A section with the document's own justification quote or "no justification given" (R14 examples may be justified by study type alone; say so).
6. **Missing/Partial section** repeats every Missing and Partially addressed item with the verbatim guidance, `Table 1, P3/J5` (items 1–23) or `Table 1 (continued), P4/J6` (items 24–28), and the absent clause. If the author claimed "not applicable" for an item without conditional wording, quote the claim here (S2).
7. **Submission checklist table**: one row per item, in Table 1 order. "Reported in section" = the document location(s) for Addressed/Partial (for Partial add "(partial)"); "Not applicable" for N/A (R14); "Not reported" for Missing (R15). Never "Not conducted" (R16).
8. **Header**: study type, form and one of the four fixed bases; files audited; interpretation note; scope; tally. If the document claims CHEERS 2013 compliance, add one line saying CHEERS 2022 replaces it (R11).
9. Report prose and state labels in English; quotes in the source language; CHEERS guidance in English (R27).
10. No score, percentage, weight, severity tier, ranking or pass/fail (R7, R25).

## 3. Verification

Run `python3 "${CLAUDE_SKILL_DIR}/scripts/make_skeleton.py" --verify <report>` before handing over. It checks 28 rows, valid states, the tally against the rows, the submission table (28 rows, matching states, "Not applicable" / "Not reported" labels), leftover `_(…)_` placeholders, a "Not conducted" label, locators on Addressed/Partial rows; it warns on quotes without quotation marks, N/A rows without a rule id, and score-like or tier wording. Fix every ERROR; read every WARNING.
