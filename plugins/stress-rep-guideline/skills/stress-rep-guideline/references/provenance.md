# Provenance — where every part of this skill comes from

Condensed from the design brief written when the skill was generated (2026-10-20). Locators: `P<n>` = PDF page, `J<n>` = printed journal page, `<variant>-supp item <n>` = supplementary checklist item.

## Sources

| Short name | File | Content | Licence note |
|---|---|---|---|
| **PDF** | `Monks 2019 Strengthening the reporting of empirical simulation studies  Introducing the STRESS guidelines.pdf` | Monks, T., Currie, C. S. M., Onggo, B. S., Robinson, S., Kunc, M., & Taylor, S. J. E. (2019). Strengthening the reporting of empirical simulation studies: Introducing the STRESS guidelines. *Journal of Simulation*, 13(1), 55–67. doi:10.1080/17477778.2018.1442155. All 14 pages read; text layer of pp. 6–9 extracted with `pdftotext -layout` to confirm table wording. | Open Access, CC BY 4.0 (stated on P2/J55 footer) |
| **DES-supp** | `tjsm_a_1442155_sm3123.docx` | Supplementary material: "Discrete-event simulation guidelines STRESS-DES" — the complete 20-item checklist with recommendation text | Distributed with the article under the same DOI; coordinator confirms the verbatim text may be bundled with attribution |
| **SD-supp** | `tjsm_a_1442155_sm3083.docx` | Supplementary material: "System Dynamics guidelines STRESS-SD" | same |
| **ABS-supp** | `tjsm_a_1442155_sm3069.docx` | Supplementary material: "Agent based simulation guidelines STRESS-ABS" | same |

The three `.docx` files were read through faithful `pandoc -t plain --wrap=none` extractions supplied by the coordinator . The originals were not modified or moved.

**Locator convention.** `P<n>` = PDF page (1 = cover), `J<n>` = printed journal page (P2 = J55 … P12 = J65). `§` and `Table` are the paper's own. For the supplements the locator is `<DES-supp|SD-supp|ABS-supp> item <n>` (the files carry no page numbers; each is a single table).

### 2.1 Checklist structure (Table 3, P7/J60, reconciled with the three supplements)

| Section | Item | Title (as printed in the supplements) | PDF Table 3 title | Notes |
|---|---|---|---|---|
| 1. Objectives | 1.1 | Purpose of the model | Purpose of the model | |
| | 1.2 | Model Outputs | Model outputs | capitalisation differs |
| | 1.3 | Experimentation Aims | Experimentation aims | capitalisation; has sub-points a–c (DES, SD) or a–d (ABS) |
| 2. Logic | 2.1 | Base model overview diagram | Base model overview diagram | |
| | 2.2 | Base model logic | Base model logic | |
| | 2.3 | Scenario logic | Scenario logic | |
| | 2.4 | Algorithms | Algorithms | |
| | 2.5 | Components | Components | sub-items 2.5.1–2.5.5 (DES, SD), 2.5.1–2.5.4 (ABS) |
| 3. Data | 3.1 | Data sources | Data sources | |
| | **3.2** | **Pre-processing** | Input parameters | **numbering differs from PDF Table 3 (see §3)** |
| | **3.3** | **Input parameters** | Pre-processing | **numbering differs from PDF Table 3** |
| | 3.4 | Assumptions | Assumptions | |
| 4. Experimentation | 4.1 | Initialisation | Initialisation | |
| | 4.2 | Run length | Run length | |
| | 4.3 | Estimation approach | Estimation approach | |
| 5. Implementation | 5.1 | Software or programming language | Software or programming language | |
| | 5.2 | Random sampling | Random sampling | |
| | 5.3 | Model execution | Model execution | |
| | 5.4 | System Specification | System specification | capitalisation |
| 6. Code Access | 6.1 | Computer Model Sharing Statement | Computer model sharing statement | capitalisation ("Code access" in PDF) |

Item counts: **STRESS-DES 20 items** (2.5 has 5 sub-items; 1.3 has 3 sub-points) · **STRESS-SD 20 items** (2.5 has 5 sub-items; 1.3 has 3 sub-points) · **STRESS-ABS 20 items** (2.5 has 4 sub-items; 1.3 has 4 sub-points). Per section 3 + 5 + 4 + 3 + 4 + 1 = 20 (abstract P2/J55: "three 20-item checklists"). **The skill will use the supplements' numbering (3.2 Pre-processing, 3.3 Input parameters), because the supplements are the checklists authors and reviewers actually fill in; the report header will note that the paper's Table 3 prints these two in the opposite order.**

### 2.10 Where the sources are still silent (do not fill from general knowledge)

- No definition of "partially reported"; no scoring, weights, thresholds or pass/fail rule.
- No procedure for deciding which variant applies (the authors assume the modeller knows the paradigm).
- No treatment of paradigms beyond DES/SD/ABS (Monte Carlo, microsimulation, Markov cohort; distributed simulation deferred, R20).
- No statement on whether the 1.3 sub-points are alternatives or cumulative (hence the interpretation flag in R22).
- Later revisions of STRESS (post-2019) are outside the sources and must not be imported.

---

## 4. Scope

### The skill WILL

- Take one or more documents describing a simulation study (PDF, `.docx`, `.md`, `.txt`; main text plus optional supplementary files, per R3) and extract their text with page/section locators.
- Determine the model type — DES, SD, ABS, or a hybrid combination — by (a) an explicit user argument, (b) a declared statement in the document, or (c) keyword evidence drawn from the checklists' own vocabulary (entities/activities/resources/queues/arrivals/event processing → DES; stocks/levels/flows/rates/auxiliary variables/lookup tables/feedback loops/integration method/DT → SD; agents/environment/interaction topology/agent states/network structure/time-stepped → ABS). When detection is inferred rather than declared, confirm with the user before auditing (single confirmation question; the sources give no detection rule, so this step is the skill's, not the source's, and will be labelled as such).
- Select the matching variant checklist (STRESS-DES / -SD / -ABS) and audit all 20 items with the variant's verbatim recommendation text. For hybrids, apply every relevant variant's wording for the paradigm-specific items and add the "how the methods communicate" check (R2), clearly marked as FAQ-derived.
- Assign one state per item: **Addressed** / **Partially addressed** / **Missing** / **Not applicable**. Every Addressed or Partially addressed item carries a quoted evidence excerpt with its locator (page, section heading, table/figure number, or supplementary file name). Not applicable carries the rule (R1, R16, R21–R29) and whether the document justifies the omission. Missing carries the verbatim recommendation so the author knows what to add.
- Report 2.5 at sub-item granularity (2.5.1–2.5.5 / 2.5.1–2.5.4) and 1.3 at sub-point granularity (a–c / a–d), because those are where the variants differ most.
- Apply the applicability conditions R21–R34 and the cross-reference checks (1.3 ↔ 2.3, 1.3b ↔ 3.3, 5.3 ↔ 5.1).
- Write the report to the project (`quality_reports/stress_audit_<docname>.md`) and summarise in chat.

### The skill will NOT

- Judge model validity, verification, calibration, or the scientific merit of results (R14; R11).
- Produce a numeric quality score, severity tiers, or a pass/fail verdict — the sources define none (§2.10). At most a tally (n Addressed / n Partial / n Missing / n N/A of 20), labelled as arithmetic rather than a STRESS construct (open question 3).
- Apply STRESS to paradigms the sources do not cover (Monte Carlo, Markov cohort, microsimulation, distributed simulation). If the detected paradigm is none of DES/SD/ABS, the skill stops and says so (R5, R20), offering the closest variant only if the user asks.
- Import wording from later STRESS revisions or other reporting guidelines (ODD, MMRR, CHEERS); fidelity is to the 2019 article and its three supplements only.
- Edit the audited document.

### Why these boundaries

The objective is a *reporting-completeness* review "based on the type of model constructed". The paper's own framing (guidelines for authors and a checklist for reviewers, §7) matches that exactly; everything the sources are silent on (scores, detection, other paradigms) would have to be invented.

---
