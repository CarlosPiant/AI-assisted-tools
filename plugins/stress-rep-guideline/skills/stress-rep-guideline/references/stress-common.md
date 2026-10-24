# STRESS — structure, shared items, and the paper's rationale

Source: Monks, T., Currie, C. S. M., Onggo, B. S., Robinson, S., Kunc, M., & Taylor, S. J. E. (2019). Strengthening the reporting of empirical simulation studies: Introducing the STRESS guidelines. *Journal of Simulation*, 13(1), 55–67. doi:10.1080/17477778.2018.1442155 (Open Access, CC BY 4.0), and its three Supplementary checklists: `tjsm_a_1442155_sm3123.docx` (STRESS-DES), `tjsm_a_1442155_sm3083.docx` (STRESS-SD), `tjsm_a_1442155_sm3069.docx` (STRESS-ABS).

Locators: `P<n>` = PDF page of the article (1 = cover), `J<n>` = printed journal page; `DES-supp / SD-supp / ABS-supp item <n>` = supplementary checklist item.

## Contents

1. What STRESS is and who it is for
2. Checklist structure (6 sections, 20 items) and numbering note
3. Items whose wording is shared between variants (stated once)
4. The paper's rationale per section, with worked reporting examples (Tables 5–7)
5. The six principles of reporting (Table 2)
6. Reconciliation: where the article and the supplements differ

## 1. What STRESS is and who it is for

STRESS ("Strengthening The Reporting of Empirical Simulation Studies") is a 20-item reporting checklist for simulation models in Operational Research and Management Science, in three instances: STRESS-DES (discrete-event simulation), STRESS-SD (system dynamics), STRESS-ABS (agent-based simulation) (abstract P2/J55; §5.1 P6/J59). Its purpose is reproducibility: "to support high quality reporting of simulation models in order to ensure that a model and its results are reproducible" (§5.1 P6/J59). It is addressed to "authors, practitioners, editors and peer reviewers" and offers reviewers "a standardised approach for assessing the quality of the research under review" (§7 P11/J64). It covers the model and its results only — not the modelling process or project story (§6 P10/J63) and not verification and validation, which are recommended but "not a requirement" (§6 P11/J64).

## 2. Checklist structure and numbering note

| Section | Items |
|---|---|
| 1. Objectives | 1.1 Purpose of the model · 1.2 Model Outputs · 1.3 Experimentation Aims (sub-points a–c; a–d in ABS) |
| 2. Logic | 2.1 Base model overview diagram · 2.2 Base model logic · 2.3 Scenario logic · 2.4 Algorithms · 2.5 Components (sub-items 2.5.1–2.5.5; 2.5.1–2.5.4 in ABS) |
| 3. Data | 3.1 Data sources · 3.2 Pre-processing · 3.3 Input parameters · 3.4 Assumptions |
| 4. Experimentation | 4.1 Initialisation · 4.2 Run length · 4.3 Estimation approach |
| 5. Implementation | 5.1 Software or programming language · 5.2 Random sampling · 5.3 Model execution · 5.4 System Specification |
| 6. Code Access | 6.1 Computer Model Sharing Statement |

Total 20 items in every variant (3 + 5 + 4 + 3 + 4 + 1).

**Numbering note.** The published checklists number the Data section 3.1 Data sources, **3.2 Pre-processing, 3.3 Input parameters**, 3.4 Assumptions. The article's Table 3 (P7/J60) prints 3.2 Input parameters and 3.3 Pre-processing. This skill follows the checklists; every audit report states this in its header.

## 3. Items whose wording is shared between variants

| Item | Verbatim recommendation | Shared by | Locator |
|---|---|---|---|
| 4.2 Run length | Detail the run length of the simulation model and time units. | DES = SD = ABS (SD-supp omits the final full stop) | DES/SD/ABS-supp 4.2 |
| 6.1 Computer Model Sharing Statement | Describe how someone could obtain the model described in the paper, the simulation software and any other associated software (or hardware) needed to reproduce the results. Provide, where possible, the link and DOIs to these. | DES = SD = ABS | DES/SD/ABS-supp 6.1 |
| 1.1 Purpose of the model | Explain the background and rationale for the model. | SD = ABS (DES: "background and objectives") | SD/ABS-supp 1.1 |
| 2.4 Algorithms | Provide further detail on any algorithms in the model that (for example) mimic complex or manual processes in the real world (i.e. scheduling of arrivals/appointments/operations/maintenance, operation of a conveyor system, machine breakdowns, etc.). Sufficient detail should be included (or referred to in other published work) for the algorithms to be reproducible. Pseudo-code may be used to describe an algorithm. | DES = ABS (SD differs) | DES/ABS-supp 2.4 |
| 3.2 Pre-processing | Provide details of any data manipulation that has taken place before its use in the simulation, e.g. interpolation to account for missing data or the removal of outliers. | DES = SD (ABS adds filtering) | DES/SD-supp 3.2 |
| 5.4 System Specification | State the model run time and specification of hardware used. This is particularly important for large scale models that require substantial computing power. For parallel, distributed and/or use grid or cloud computing, etc. state the details of all systems used in the implementation (processors, network, etc.) | DES = ABS (SD has only the first two sentences) | DES/ABS-supp 5.4 |

All other items (1.2, 1.3, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 4.1, 4.3, 5.1, 5.2, 5.3) differ in every variant: read the variant file (`stress-des.md`, `stress-sd.md`, `stress-abs.md`) for the wording to audit against. Never audit against a paraphrase.

## 4. The paper's rationale per section (show beside each section of the report)

| Section | Rationale and worked examples (quotes from the article) | Locator |
|---|---|---|
| 1 Objectives | Purpose includes "the model's intended use or experimental frame (Pidd, 2006, p. 36)"; model outputs are "the model outputs that the model will predict"; experimentation aims give "details of the input parameters that can be changed … and the objectives". Example: a shop where the purpose is the optimal number of servers, outputs are waiting time, utilisation and cost, and the experimentation varies servers and queue structure. | §5.2 P6/J59 |
| 2 Logic | "STRESS recommends the use of a recognised simulation diagramming approach … Within the main text authors should limit diagrams to conceptual or simplified overviews but complex diagrams used to communicate complete model design should be included as Supplementary material." "Components refer to the basic conceptual building blocks of the model." | §5.3 P6–7/J59–60; Table 4 P8/J61 |
| 3 Data | "A model and its results cannot be reproduced without detailing the input parameters." Stochastic-parameter example (Table 5): columns Activity / Distribution / Distribution parameters / Data source (sample size), e.g. "Service time a — Gamma — α = 4.5; β = 16.5; min = 15 — Observation (n = 125)"; "Service time c — Triangular — Min = 3, Mode = 8, Max = 15 — Expert Opinion (n = 3)". Deterministic parameters "should be reported in a similar manner". Confidential data: "reports should include hypothetical non-proprietary data so that researchers can still verify that a model has been reproduced accurately." | §5.4 P7/J60; Table 5 P9/J62 |
| 4 Experimentation | Initialisation "varies across the three checklists": DES (and stochastic ABS where appropriate) — warm-up periods and "warm-up analysis procedures (e.g., Welch's method or MSER-5; White and Robinson (2010))" and initial conditions for queues and activities; SD — "the initial values of stocks"; ABS — "an initial agent population size along with attribute values and environment set-up". Estimation approach "depends predominantly on whether the model is deterministic or stochastic"; for stochastic models "the approach that has been used to create independent samples of the output and how many samples have been taken, e.g., the number of replications" and variance reduction "such as common random numbers or antithetic variates". Table 6 examples: "The model had a run length of 180 weeks. Based on a MSER-5 analysis, a warm-up period of 60 weeks was used. No initial conditions were included. All point estimates are based on the average of 50 replications of a model run"; "The model had a run length of 30 days. The environment was initialised with a fixed size agent population (n = 10,000). All agents were in the potential adopter state initially and are connected in a random network generated using Watts–Strogatz's algorithm with mean degree 5 and rewiring probability 0.25. All results are based on an average of 1000 replications". | §5.5 P7/J60; Table 6 P9/J62 |
| 5 Implementation | "the reporting of the design should be software independent; however, the reporting of software used may help clarify specific design choices or ambiguities." Random sampling: "Relevant only for stochastic models … authors should not assume that other researchers have access to such software or its documentation … in the case of common random numbers authors should describe how streams or seeds are distributed across components." Model execution "refers to how simulated time progresses within the model" (SD: "time-step interval and integration method"; DES: "event processing mechanism (e.g., Three Phase)"; ABS: "time-step and/or event processing"); if unpublished, "it is critical that author report the software version and build numbers." Hardware/runtime "most relevant to large-scale models". Table 7 examples: "implemented in the commercial software Anylogic 7.5.3 Researcher edition and made use of its Process Modelling Library version x.2. The pseudo-random number generator was provided by the Java class Random version x.y. The model was run on a Microsoft Surface Pro 4, with a 2.2Ghz Intel Core i7 processor and 16 GB of memory under Windows 10 (build 14,393). Model run time was 5 min per replication"; "implemented in iThink 10.0.3. The integration method was set to Euler's Method. The model had a run length of 15 years with a DT of 1 month. The model was run on an Apple Macbook Air, with a 1.7Ghz Intel Core i7 processor and 8 GB of memory under OS X El Capitan version 10.11.16. Model run time was under 1 min". | §5.6 P7–9/J60–62; Table 7 P10/J63 |
| 6 Code Access | "detail whether and how the computer model can be accessed by other researchers or other modellers within an industry team … STRESS does not specify how authors make the computer model available nor that they must. Industry modellers may wish to list a secure or local directory. Researchers who wish to share models may wish to include a statement such as 'models are available on request' or provide a link to an open science repository." | §5.7 P9/J62 |

## 5. The six principles of reporting (Table 2, P7/J60, verbatim)

1. State the purpose of the study and the model's intended use
2. Provide enough detail to reproduce the results of the base run of the model and any simulation experiments conducted as part of the study
3. Ensure that descriptions of the model are software and hardware independent
4. Include data for verification and parameter values. Where proprietary or ethical issues prevent the inclusion of data, "hypothetical" test data should be included for verification purposes
5. Document all software and where necessary hardware-specific implementation
6. Provide additional visualisation of model logic or algorithms using a recognised diagramming approach

These are the paper's thematic synthesis of six earlier guidelines (§5 P6/J59); they are rationale, not checklist items.

## 6. Reconciliation: where the article and the supplements differ

The supplements govern checklist content; the article governs rationale and decision rules.

| # | Difference | Resolution |
|---|---|---|
| D1 | Data section numbering swapped (article Table 3: 3.2 Input parameters, 3.3 Pre-processing). | Supplement numbering; header note. |
| D2 | Title capitalisation ("Model Outputs", "Experimentation Aims", "System Specification", "Computer Model Sharing Statement", "Code Access" in supplements; sentence case in Table 3). | Cosmetic; supplements' form used. |
| D3 | §5.3 says STRESS-SD focuses on "stocks, flows and feedback loops", but Table 4 has no feedback-loop component. SD-supp puts feedback loops under 2.1 and 2.2. | Audit feedback loops under SD 2.1/2.2. |
| D4 | SD 2.5.3 title "Constants / Converters / auxiliary variables" (Table 4: "Constants/auxiliary variables"). | Supplement title. |
| D5 | ABS 2.5.4 title "Entry / Exit" (Table 4: "Entry/Exit Points"). | Supplement title. |
| D6 | ABS 2.5.3 ends with "Report how interactions are affected by agent states and the environment state", absent from Table 4. | Included. |
| D7 | DES 2.5.4/2.5.5 "balking" (Table 4 "baulking"); "occur, etc., provide details". | Supplement wording; both spellings are detection keywords. |
| D8 | SD 2.5.2 "if they act a delay" (Table 4 "act as a delay"). | Quoted as printed. |
| D10 | ABS warm-up: §5.5 "where appropriate for stochastic ABS models"; ABS-supp 4.1 asks unconditionally. | A warm-up statement is required (may be "none"). |
| D11 | 5.2 "Relevant only for stochastic models" is in the article (§5.6), not in the supplements' 5.2; the stochastic condition sits in SD/ABS 4.3. | Deterministic model → 5.2 Not applicable (rule R16). |
| D12 | DES/ABS 5.3 in the supplements add priority rules, variable-update order, concurrency and parallel/distributed/HLA details not described in the article. | Supplement content governs. |
| D15 | Supplement typographical slips ("that was be used", "these were these selected", "how, , these", "provide all detailed", "with in", "I.e.", "a.k.a level") are preserved verbatim in the reference files. | Quote as printed; paraphrase only when explaining, never when quoting. |
