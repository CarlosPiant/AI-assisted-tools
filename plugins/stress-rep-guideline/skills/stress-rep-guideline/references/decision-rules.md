# STRESS audit — decision rules, state definitions, hybrid procedure, paradigm detection

Source: Monks et al. (2019), *Journal of Simulation* 13(1):55–67, doi:10.1080/17477778.2018.1442155 (article, CC BY) and its Supplementary checklists (DES-supp = `tjsm_a_1442155_sm3123.docx`, SD-supp = `tjsm_a_1442155_sm3083.docx`, ABS-supp = `tjsm_a_1442155_sm3069.docx`). `P<n>`/`J<n>` = article PDF page / journal page.

## Contents

1. State definitions (Addressed / Partially addressed / Missing / Not applicable)
2. Rules R1–R20 from the article (usage, N/A, hybrids, supplements, reuse, confidentiality)
3. Rules R21–R35 from the checklists' own applicability conditions
4. Hybrid procedure
5. Paradigm detection (skill-derived) and what to do when the paradigm is not DES/SD/ABS
6. Evidence standards (what counts, what does not)

## 1. State definitions

Exactly one state per item (and per 2.5.x sub-item / 1.3 sub-point).

| State | Definition | Must carry |
|---|---|---|
| **Addressed** | The document (main text or any supplied supplement) contains the content of every unconditional clause of the verbatim recommendation, plus every conditional clause whose trigger holds in this model. | A quoted excerpt and its locator (file, page or section). Sub-state **Addressed by reference** when a reused published model is cited and only adaptations are reported (R15). |
| **Partially addressed** | Some but not all required clauses are present. Typical: replications stated without justification (DES 4.3); a diagram without the component detail; assumptions listed but not justified (ABS 3.4); an external-URL-only pointer (R4); confidentiality declared with a QA summary (R12). | Quote, locator, and the missing clause named. |
| **Missing** | Nothing found in any supplied file for an item that applies. | The verbatim recommendation, so the author knows what to add. |
| **Not applicable** | Only where a rule below permits it (R1, R16, R21, R23, R24, R25, R29, or hybrid-only rows for non-hybrids). | The rule id and whether the document itself justifies the omission ("no justification given" is allowed but must be stated). |

Tally = plain counts of the four states over the 20 items. STRESS defines no score, weight, severity tier or pass mark; do not invent one.

## 2. Rules from the article (R1–R20)

| # | Rule (verbatim core) | Consequence | Locator |
|---|---|---|---|
| R1 | "The STRESS guidelines are not rules they are *guidelines* … There is no issue if authors find that certain sections of STRESS are not applicable. Reviewers may query omissions, and authors should be able to justify them." | N/A is legitimate; report whether the document justifies it. An unjustified omission of an applicable item is Missing. | §6 P10/J63 |
| R2 | Hybrid models: "it is recommended to apply both the STRESS-DES and STRESS-SD guidelines … some adaptation of the guidelines is needed to handle the interface … It is recommended that authors report how the two (or more) methods communicate." | Apply every relevant variant; add the interface check H.1 (section 4 below). | §6 P9/J62 |
| R3 | "The guidelines are not prescriptive in how to structure an article … We encourage authors to make use of Supplementary material and additional files." Complex diagrams → Supplementary (§5.3); initial conditions may be tabulated in Supplementary (§5.5). | Search every supplied file before marking Missing; the locator may be a supplement. | §6 P9/J62; §5.3 P7/J60; §5.5 P7/J60 |
| R4 | "Third party websites may change, break or be taken down without an author's knowledge … Journal articles are a permanent public record of the model." | Evidence that exists only behind an external URL → Partially addressed, with this note. | §6 P11/J64 |
| R5 | Mega-models/frameworks: applicability "depends on whether the contribution is the model and scientific result or the programming framework"; frameworks → software-engineering documentation; "for very complex and large models some adaption may be required". | If the document is a framework/software paper, say so at the top and flag that STRESS may not be the right instrument. | §6 P9–10/J62–63 |
| R6 | "If an author believes that their model requires additional detail in order to aid reproducibility, then they should include it for completeness of reporting." | Optional "Additional reproducibility detail" note; never an item. | §6 P10/J63 |
| R7 | "consider publishing code as an enhancement to reporting not the other way around." | A code repository link satisfies 6.1 only; it does not make 2.x–5.x Addressed. | §6 P10/J63 |
| R8 | Reproducible result for stochastic models: "ordinality, precision and output uncertainty … the point estimate should be reproducible exactly or within the given confidence interval of reported results … any sensitivity analysis … should be reproduced". | Informs what evidence satisfies 1.2 (measures of error) and 4.3. | §6 P10/J63 |
| R9 | DEVS: "these guidelines complement its use by incorporating those other details needed for full reproducibility". | A DEVS formalisation may satisfy Logic items; the rest is still audited. | §6 P10/J63 |
| R10 | "The published write-up is the permanent public record of the work." | "Details available from the authors" is not evidence for any item except as a 6.1 statement. | §6 P10/J63 |
| R11 | "The reporting guidelines apply to the model itself and the model's results. The wider aspects of the modelling process/practice … is a separate scientific area". | Do not audit stakeholder engagement, facilitation or project narrative. | §6 P10/J63 |
| R12 | Confidential models: independent third-party QA; "a summary of the quality assurance is submitted along with the model"; otherwise "it is better not to publish." | Confidentiality declared → affected items Partially addressed with "QA summary present/absent". | §6 P11/J64 |
| R13 | Licensing: Creative Commons (CC BY) recommended. | Note only, under 6.1. | §6 P11/J64 |
| R14 | "V&V is not a requirement … Nonetheless, STRESS helps with reporting of V&V. It requires verification data to be reported, either the data used to produce the scientific results or hypothetical test verification data." | No V&V grading; presence of verification data may be noted under section 3. | §6 P11/J64 |
| R15 | Reused/adapted published model: "It is only necessary to report the adaptations to the model, data or analysis that you have conducted … Provide a reference to the original paper." | Unchanged items → "Addressed by reference" with the citation as evidence; adapted parts audited normally. | §6 P11/J64 |
| R16 | "Relevant only for stochastic models the reporting of the algorithm for random sampling". | Deterministic model → 5.2 Not applicable (and 4.3 per R29). | §5.6 P9/J62 |
| R17 | Hardware/runtime "most relevant to large-scale models"; supplements: "particularly important for large scale models". | 5.4 is never automatically N/A; a Missing on a small model is noted as low impact. | §5.6 P9/J62; DES/SD/ABS-supp 5.4 |
| R18 | Unpublished commercial execution mechanism → "it is critical that author report the software version and build numbers". | 5.3 counts as Addressed when the mechanism is proprietary and 5.1 gives name, version and build. | §5.6 P9/J62; DES-supp 5.3 |
| R19 | Intended users: "authors, practitioners, editors and peer reviewers". | Confirms the reviewer use-case. | §7 P11/J64 |
| R20 | "Later work will consider how the guidelines are applicable to hybrid and distributed simulation." | Hybrid handling (R2) is provisional; say so in hybrid reports. | §8 P12/J65 |

## 3. Rules from the checklists' own applicability conditions (R21–R35)

| # | Condition (verbatim phrase) | Consequence | Locator |
|---|---|---|---|
| R21 | 1.3 "If the model has been used for experimentation" (DES, ABS); "If the model has been used for policy analysis (user-defined experiments) and policy formulation (multiple experiments to obtain best policy)" (SD). | No experimentation beyond the base run → 1.3 Not applicable (2.3 follows via R23). | DES/ABS/SD-supp 1.3 |
| R22 | 1.3 sub-points name experimentation types: a Scenario/Policy based; b Design of experiments; c (DES, SD) / d (ABS) Simulation Optimisation "(if appropriate)" (DES, ABS); ABS a Theory driven analysis. | Audit each sub-point only when that type is used; list which apply and why. **Skill interpretation:** only the optimisation sub-point carries an explicit "(if appropriate)"; reading the others as type-conditional alternatives is the skill's reading — say so in the report when it matters. | DES/SD/ABS-supp 1.3 |
| R23 | 2.3 "scenarios (if any)" (DES); "any difference in the model logic" (ABS); SD "policies, scenarios and experiments". | No scenarios → 2.3 Not applicable. Scenarios exist and the document says the logic is unchanged → Addressed with that quote. Scenarios exist and nothing is said → Missing. | DES/ABS/SD-supp 2.3 |
| R24 | 2.4 "any algorithms … that (for example) mimic complex or manual processes". | No such algorithm evident anywhere → Not applicable with a note. Algorithm mentioned but neither detailed nor referenced "to other published work" → Missing/Partial. | DES/SD/ABS-supp 2.4 |
| R25 | ABS 2.5.4 "Where relevant, define how agents are created and destroyed". | Fixed agent population stated → Not applicable with the quote. | ABS-supp 2.5.4 |
| R26 | 3.2 "any data manipulation [or filtering]". | Silence → Missing (silence is indistinguishable from "none"); an explicit "no pre-processing was performed" → Addressed. | DES/SD/ABS-supp 3.2 |
| R27 | 3.3 conditional clauses: "For stochastic inputs …"; "Where optimisation or design of experiments has been used, state the range of values"; "Where theoretical distributions are used, state how these were selected"; ABS "Where applicable define the time/spatial dependence". | Each clause audited only when its condition holds; the parameter list with values and the base-case data are unconditional. | DES/SD/ABS-supp 3.3 |
| R28 | 4.1 DES: "Report if the system modelled is terminating or non-terminating" (unconditional); "State if a warm-up period has been used" (a statement is required even if none); "For terminating systems state the stopping condition". SD: initial values unconditional; distributions "if initial values are varied over multiple runs". ABS: "State if a warm-up period has been used"; initial agent/environment conditions. | Addressed only when the unconditional parts are present; conditional parts audited when triggered. | DES/SD/ABS-supp 4.1 |
| R29 | 4.3 DES "State the method used to account for the stochasticity" (assumes stochastic); SD "If the SD model includes stochastic inputs …" and "For model calibration or optimisation …"; ABS "State if the model is deterministic or stochastic. If the model is stochastic …". | ABS: an explicit "deterministic" statement is Addressed. SD: deterministic → first clause N/A, calibration clause audited if calibration/optimisation used. DES: deterministic DES → N/A via R16, flagged as unusual. | DES/SD/ABS-supp 4.3 |
| R30 | 5.2 DES "If common random numbers are used, state how seeds (or random number streams) are distributed among sampling processes". | Second sentence conditional on CRN use. | DES-supp 5.2 |
| R31 | 5.3 DES: "in some commercial software the event processing mechanism may not be published. In these cases authors should adhere to item 5.1"; "State all priority rules included if entities/activities compete for resources"; "If the model is parallel, distributed and/or use grid or cloud computing"; "If the HLA is used". ABS: "If the ABS model has a time component"; "In time-stepped execution state how concurrent events are resolved"; same parallel/HLA clauses. | Each clause conditional as stated. | DES-supp 5.3; ABS-supp 5.3 |
| R32 | 5.4 DES/ABS: "For parallel, distributed and/or use grid or cloud computing, etc. state the details of all systems used". | Conditional on a parallel/distributed implementation. | DES/ABS-supp 5.4 |
| R33 | 3.1 and 6.1: "Provide, where possible, the link and DOI(s)". | Absence of a link/DOI alone does not make the item Missing when the description or reference is given; mention it as a recommendation. | DES/ABS-supp 3.1; DES/SD/ABS-supp 6.1 |
| R34 | Internal cross-references: 1.3a "ensure that item 2.3 (below) is completed"; 1.3b "(provide further details in data below)" → 3.3; 2.3 "in the same manner as 2.2" (DES) / "2.1" (SD, ABS); 5.3 → 5.1. | Run the cross-reference table in the report and flag inconsistencies (e.g. 1.3 lists scenarios but 2.3 is Missing; 5.3 says "proprietary" but 5.1 lacks a build number; 3.3 lists distributions but 4.3 claims deterministic). | as cited |
| R35 | Numbering: supplements use 3.2 Pre-processing, 3.3 Input parameters; article Table 3 prints the reverse. | Use supplement numbering; the report header carries the note. | DES/SD/ABS-supp 3.2–3.3; Table 3 P7/J60 |

## 4. Hybrid procedure (R2, R20)

1. Name every paradigm present (e.g. DES + SD) and the basis for that judgement.
2. Build one merged skeleton with `scripts/make_skeleton.py --variant des,sd` (any set of `des`, `sd`, `abs`). Items whose wording differs between the chosen variants appear once per variant, labelled; 2.5 sub-items and 1.3 sub-points are the union.
3. Audit each labelled row against its own variant's wording; where a component belongs clearly to one paradigm (e.g. stocks in the SD part) the other paradigm's row for that component is Not applicable, citing R2.
4. Add the interface check H.1: does the document report how the methods communicate — what passes between the components, when, in which direction? Cite the FAQ (§6 P9/J62) and label the check as the paper's provisional advice (R20).
5. Keep one tally over the 20 items; count a split item (two labelled rows) once, using the lower of its two states.

## 5. Paradigm detection (skill-derived) and uncovered paradigms

STRESS gives no rule for deciding which variant applies; the author is assumed to know. The skill therefore:

1. Uses an explicit `--model` argument if given.
2. Otherwise looks for a declaration in the document ("a discrete-event simulation model was built", "system dynamics model", "agent-based model", "modelo de simulación de eventos discretos", "modelo de dinámica de sistemas", "modelo basado en agentes").
3. Otherwise infers from vocabulary using the keyword lists in each variant file (section "Paradigm detection vocabulary"), reporting the counts of distinctive terms found; then pauses (SOFT) to confirm. If the user says "just do it", proceed and write "basis: inferred, user said proceed" in the header.

If the document's paradigm is none of DES, SD or ABS (Monte Carlo risk analysis, cohort Markov or microsimulation models, pure optimisation, distributed simulation frameworks), **stop and do not audit**: STRESS covers discrete-event simulation, system dynamics and agent-based simulation only (abstract P2/J55; §8 P12/J65 defers hybrid and distributed simulation). Tell the user which three paradigms are covered and that the closest-variant audit would be outside the guideline. If the document is a modelling framework rather than a model with a result, apply R5.

## 6. Evidence standards

- Quote the document verbatim (in its own language; English or Spanish manuscripts are both audited) and give the locator: `[[file]]` + `[[page n]]` or heading from the extracted corpus, or table/figure number.
- A table or figure counts as evidence; cite its number and the file it is in.
- Evidence may come from any supplied supplement (R3). It may not come from an external URL alone (R4), from "contact the authors" (R10), or from the existence of a code repository (R7).
- Never alter the recommendation text when quoting what STRESS asks for; copy it from the variant file or `checklist.json`.
- Do not grade model validity, calibration quality or results; reporting completeness only (R11, R14).
