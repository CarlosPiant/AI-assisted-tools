# STRESS audit report — template

`scripts/make_skeleton.py --variant <des|sd|abs|des,sd,...> --title "<doc title>" --output <path>` renders this skeleton with every item, sub-item and verbatim recommendation pre-filled. This file documents the layout and the rules for filling it in. Output path: `quality_reports/stress_audit_<docname>.md` in the project (never in the hub).

## Layout

```markdown
# STRESS reporting audit — <document title>

Source guideline: Monks et al. (2019), J. Simulation 13(1):55–67, doi:10.1080/17477778.2018.1442155, and its Supplementary checklists <file(s)>.
Variant(s) applied: STRESS-DES | STRESS-SD | STRESS-ABS | <A + B> (hybrid) — basis for selection: declared / inferred and confirmed / inferred, user said proceed / argument
Files audited: main text (<name>, pages 1–n); supplement(s) <names>
Numbering: follows the published checklists (3.2 Pre-processing, 3.3 Input parameters); the article's Table 3 prints these in the opposite order.
Scope: reporting completeness only, not model validity.
Tally (arithmetic only; STRESS defines no score): Addressed n | Partially addressed n | Missing n | Not applicable n (of 20)

## Section 1 — Objectives
| Item | State | Evidence (quote) | Locator | STRESS asks for (verbatim) | Applicability / rules |
|---|---|---|---|---|---|
| **1.1 Purpose of the model** | Addressed | "…" | main, p. 2, §1 | <verbatim> | unconditional |
| **1.3 Experimentation Aims** | Partially addressed | "…" | main, p. 6, §4 | <verbatim lead sentence> | R21, R22; cross-refs 2.3, 3.3 |
| · 1.3a Scenario based analysis | Addressed | "…" | main, Table 3 | <verbatim> | when scenarios used |
| · 1.3b Design of experiments | Not applicable | — | — | <verbatim> | no designed experiment (R22) |
| · 1.3c Simulation Optimisation | Not applicable | — | — | <verbatim> | "(if appropriate)" — not used |

## Section 2 — Logic      (2.5 expanded to the variant's sub-items 2.5.1–2.5.5 / 2.5.1–2.5.4)
## Section 3 — Data
## Section 4 — Experimentation
## Section 5 — Implementation
## Section 6 — Code Access

## Cross-reference checks
| Pair | Consistent? | Note |
|---|---|---|
| 1.3 ↔ 2.3 | yes / no / n.a. | 1.3a: "ensure that item 2.3 (below) is completed" |
| 1.3b ↔ 3.3 | … | 1.3b: "provide further details in data below" |
| 5.3 ↔ 5.1 | … | unpublished mechanism must be covered by 5.1 version/build (R18, R31) |
| 4.3 / 5.2 ↔ 3.3 | … | deterministic/stochastic claims must agree (R16, R29) |

## Hybrid interface check — Interface between simulation methods   (hybrid reports only)
Basis: Monks et al. (2019) §6, PDF p. 9 / J p. 62 (provisional advice; §8 defers hybrids to later work).
| H.1 Interface reported | State | Evidence | Locator |

## Items marked Not applicable — rule cited and whether the document justifies the omission (R1)
| Item | Rule | Document justifies? (quote) |

## Missing and partially addressed items — what STRESS asks for
| Item | State | Verbatim recommendation | Locator in STRESS | What is absent |

---
Attribution: Checklist text © 2018 Monks, Currie, Onggo, Robinson, Kunc & Taylor, Supplementary material of doi:10.1080/17477778.2018.1442155, CC BY; reproduced verbatim.
```

## Filling rules

1. **One state per row.** Items with sub-items (1.3, 2.5) get a state for the parent row too: Addressed only if every applicable sub-row is Addressed; Partially addressed if mixed; Missing if all applicable sub-rows are Missing; Not applicable only if all sub-rows are Not applicable.
2. **Evidence column** holds a verbatim quote from the audited document, in the document's language (English or Spanish), long enough to show the clause is met (one to three sentences, or "Table 2, rows 1–8"). Never paraphrase in this column.
3. **Locator column** uses the corpus markers from `extract_text.py`: `<file role>, p. <n>` for PDFs, `<file role>, § <heading>` for docx/md, plus table/figure numbers where relevant.
4. **"STRESS asks for" column** is the verbatim recommendation copied from the variant file; for Missing/Partial rows it is repeated in the final section with the absent clause named.
5. **Not applicable rows** cite a rule id from `decision-rules.md` and are listed again in the N/A section with the document's own justification (quote) or "no justification given".
6. **Tally** counts the 20 items only (sub-rows do not count); a hybrid split item counts once at the lower of its states.
7. **Header "basis for selection"** must be one of the four fixed phrases; when the paradigm was inferred and the user said "just do it", write "inferred, user said proceed" and list the vocabulary counts that drove the inference in one sentence under the header.
8. Report prose and state labels are in English; quotes stay in the source language.
9. No scores, no severity tiers, no pass/fail verdict.
