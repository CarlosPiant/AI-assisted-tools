# STRESS-SD — System Dynamics guidelines STRESS-SD (verbatim checklist)

Source: Supplementary material `tjsm_a_1442155_sm3083.docx` of Monks, T., Currie, C. S. M., Onggo, B. S., Robinson, S., Kunc, M., & Taylor, S. J. E. (2019). Strengthening the reporting of empirical simulation studies: Introducing the STRESS guidelines. Journal of Simulation, 13(1), 55-67. doi:10.1080/17477778.2018.1442155.
Short locator used in this skill: `SD-supp item <n>`.

Attribution: Checklist text (c) 2018 Monks, Currie, Onggo, Robinson, Kunc & Taylor, from the Supplementary material of doi:10.1080/17477778.2018.1442155, published Open Access under CC BY 4.0. Reproduced verbatim; the supplements' typographical slips are preserved deliberately so that the authoritative wording is not altered.

Numbering note: Numbering follows the published Supplementary checklists (3.2 Pre-processing, 3.3 Input parameters). The article's Table 3 (PDF p. 7 / journal p. 60) prints these two items in the opposite order (3.2 Input parameters, 3.3 Pre-processing).

Shared wording: Items 4.2 and 6.1 are word-for-word identical in all three variants; 1.1 is identical in SD and ABS; 2.4 in DES and ABS; 3.2 in DES and SD; 5.4 in DES and ABS. All other items differ in every variant.

Generated from `scripts/checklist.json` by `scripts/make_skeleton.py --render-reference`; edit the JSON, not this file.

## Contents

- Section 1 Objectives: 1.1 Purpose of the model, 1.2 Model Outputs, 1.3 Experimentation Aims
- Section 2 Logic: 2.1 Base model overview diagram, 2.2 Base model logic, 2.3 Scenario logic, 2.4 Algorithms, 2.5 Components
- Section 3 Data: 3.1 Data sources, 3.2 Pre-processing, 3.3 Input parameters, 3.4 Assumptions
- Section 4 Experimentation: 4.1 Initialisation, 4.2 Run length, 4.3 Estimation approach
- Section 5 Implementation: 5.1 Software or programming language, 5.2 Random sampling, 5.3 Model execution, 5.4 System Specification
- Section 6 Code Access: 6.1 Computer Model Sharing Statement

## Paradigm detection vocabulary (skill-derived, not part of STRESS)

detection_keywords are the skill's own aid for inferring the paradigm, drawn from the vocabulary of each checklist. STRESS itself gives no detection rule; an inferred paradigm must be confirmed with the user (SOFT pause) or stated as inferred in the report header.

Keywords: system dynamics, SD model, stock, stocks, level, levels, flow, flows, rate, rates, auxiliary, converter, lookup table, graphical function, feedback loop, causal loop, stock and flow, integration method, Euler, Runge-Kutta, time step, DT, Vensim, iThink, Stella, InsightMaker, Powersim, dinamica de sistemas, dinámica de sistemas, acervo, acervos, nivel, niveles, flujo, flujos, bucle de retroalimentacion, bucle de retroalimentación, diagrama causal, variable auxiliar

## Section 1 — Objectives

### 1.1 Purpose of the model

**Recommendation (verbatim):**

> Explain the background and rationale for the model.

- Applicability: unconditional
- Rules: - (see `decision-rules.md`)
- Locator: SD-supp item 1.1; PDF: Table 3 P7/J60; section 5.2 P6/J59
- Wording: identical in STRESS-ABS

### 1.2 Model Outputs

**Recommendation (verbatim):**

> Describe all outcome variables that are reported. Include details on how they are calculated during the model run. These might be as simple as detailing which specific stocks/levels are of key interest or may involve detailing equations.

- Applicability: unconditional
- Rules: R8 (see `decision-rules.md`)
- Locator: SD-supp item 1.2; PDF: Table 3 P7/J60; section 5.2 P6/J59
- Wording: variant-specific wording

### 1.3 Experimentation Aims

**Recommendation (verbatim):**

> If the model has been used for policy analysis (user-defined experiments) and policy formulation (multiple experiments to obtain best policy), state the research questions that it was used to answer.

#### 1.3a Policy based analysis

> Policy based analysis – Provide a name and description of each policy tested, providing a rationale for the choice of policies and parameters employed. Ensure that item 2.3 (below) is completed.

Applicability: When policies/scenarios are tested.

#### 1.3b Design of experiments

> Design of experiments – Provide details of the design and the parameters that will be used. This for example, may be to perform a sensitivity analysis.

Applicability: When a designed experiment or sensitivity analysis is used.

#### 1.3c Simulation Optimisation

> Simulation Optimisation - Provide full details of what is to be optimised and the parameters that will be included and the algorithm that will be used. Where possible provide a citation of the algorithm/calibration method.

Applicability: When optimisation or calibration is used.

- Applicability: Conditional: applies only if the model has been used for policy analysis / policy formulation (R21). Sub-points are audited only for the type(s) of experimentation actually used (R22; skill interpretation).
- Rules: R21, R22, R34 (see `decision-rules.md`)
- Cross-references: 2.3, 3.3
- Locator: SD-supp item 1.3; PDF: Table 3 P7/J60; section 5.2 P6/J59
- Wording: variant-specific wording

## Section 2 — Logic

### 2.1 Base model overview diagram

**Recommendation (verbatim):**

> Provide one or more causal loop, stock and flow (a.k.a level and rate) or equivalent diagrams to describe the basic logic of base model to readers. Avoid complicated diagrams in the main text. To aid readers understanding authors should document the key feedback loops that drive system behaviour.

- Applicability: Feedback loops are audited here and in 2.2 (the PDF's section 5.3 gloss 'stocks, flows and feedback loops' has no 2.5 row; discrepancy D3).
- Rules: R3 (see `decision-rules.md`)
- Locator: SD-supp item 2.1; PDF: Table 3 P7/J60; section 5.3 P6-7/J59-60; Table 2 principle 6 P7/J60
- Wording: variant-specific wording

### 2.2 Base model logic

**Recommendation (verbatim):**

> Give details of the base model logic in terms of feedback loops. This could be text to explain the overview diagram along with extra details including any use of system archetypes.

- Applicability: unconditional
- Rules: - (see `decision-rules.md`)
- Locator: SD-supp item 2.2; PDF: Table 3 P7/J60; section 5.3 P6/J59
- Wording: variant-specific wording

### 2.3 Scenario logic

**Recommendation (verbatim):**

> Give details of the logical difference between the base case model and policies, scenarios and experiments. This could be incorporated as text or where differences are substantial could be incorporated in the same manner as 2.1.

- Applicability: Not applicable when the study has no policies/scenarios/experiments beyond the base run (R23).
- Rules: R23, R34 (see `decision-rules.md`)
- Cross-references: 1.3, 2.1
- Locator: SD-supp item 2.3; PDF: Table 3 P7/J60; section 5.3 P6/J59
- Wording: variant-specific wording

### 2.4 Algorithms

**Recommendation (verbatim):**

> Provide detail on any algorithms, functions or equations that mimic complex or manual processes in the real world. E.g. scheduling of arrivals/appointments/operations/maintenance. Sufficient detail should be included (or referred to in other published work) for the algorithms to be reproducible. For clarity, it is recommended that algorithms are represented as pseudo-code.

- Applicability: Conditional: 'any algorithms, functions or equations' of this kind - Not applicable when none is evident (R24).
- Rules: R24 (see `decision-rules.md`)
- Locator: SD-supp item 2.4; PDF: Table 3 P7/J60
- Wording: variant-specific wording

### 2.5 Components

#### 2.5.1 Stocks/Levels

> Give details of all stocks within the simulation including a description of their role in the model. Provide the stocks units and make sure that all inflows and outflows can easily be identified (note that in a large model a diagram is unlikely to sufficiently clear for other researchers to use. Please consider tables in addition to any diagrams).

#### 2.5.2 Flows/Rates

> List all flows within the model along with units and equations. Describe the role of flows in the model e.g. if they act a delay.

#### 2.5.3 Constants / Converters / auxiliary variables

> List all variables within the model and detail their equations (if applicable) including units.

#### 2.5.4 Graphical functions/lookup tables

> List and detail all graphical functions within the model and describe their data sources.

Applicability: Not applicable if the model has no graphical functions/lookup tables and says so.

#### 2.5.5 Sources and Sinks

> Give details of the model boundaries i.e. all infinite sources and sinks within the model.

- Applicability: Audit each sub-item separately; the sub-items are the paradigm-specific building blocks of the model.
- Rules: - (see `decision-rules.md`)
- Locator: SD-supp item 2.5; PDF: Table 4 P8/J61 (title there: 'Constants/auxiliary variables'; 'act as a delay'); section 5.3 P7/J60
- Wording: variant-specific wording

## Section 3 — Data

### 3.1 Data sources

**Recommendation (verbatim):**

> List and detail of all data sources. Sources may include:
> - Interviews with stakeholders,
> - samples of routinely collected data,
> - prospectively collected samples for the purpose of the simulation study ,
> - Public domain data published in either academic or organisational literature. For published literature include the reference.
> All data source descriptions should include details of the sample size, date ranges and use within the study.

- Applicability: unconditional
- Rules: R33 (see `decision-rules.md`)
- Locator: SD-supp item 3.1; PDF: Table 3 P7/J60; section 5.4 P7/J60; Table 5 P9/J62
- Wording: variant-specific wording

### 3.2 Pre-processing

**Recommendation (verbatim):**

> Provide details of any data manipulation that has taken place before its use in the simulation, e.g. interpolation to account for missing data or the removal of outliers.

- Applicability: 'any data manipulation': silence is Missing; an explicit statement that no pre-processing was performed is Addressed (R26).
- Rules: R26, R35 (see `decision-rules.md`)
- Locator: SD-supp item 3.2; PDF: Table 3 P7/J60 prints this as item 3.3 (numbering differs); section 5.4 P7/J60
- Wording: identical in STRESS-DES

### 3.3 Input parameters

**Recommendation (verbatim):**

> List of all input variables in the model, provide a description of its use and include parameter values. For stochastic inputs provide details of any continuous, discrete or empirical distributions used along with all associated parameters. Give details of all time dependent parameters, correlation and any graphical functions.
> Clearly state:
> - Base case data
> - Data use in experimentation (where different from the base case).
> - Where optimisation or design of experiments has been used, state the range of values that parameters can take.
> Where theoretical distributions are used, state how these were these selected and prioritised above other candidate distributions.

- Applicability: Unconditional: the list of inputs with values and the base case data. Conditional clauses (R27): stochastic inputs; experimentation data; optimisation/DoE ranges; theoretical distribution selection.
- Rules: R27, R34, R35 (see `decision-rules.md`)
- Cross-references: 1.3, 2.5.4
- Locator: SD-supp item 3.3; PDF: Table 3 P7/J60 prints this as item 3.2 (numbering differs); section 5.4 P7/J60
- Wording: variant-specific wording

### 3.4 Assumptions

**Recommendation (verbatim):**

> Where data or knowledge of the real system is unavailable what assumptions are included in the model? This might include parameter values, distributions or flow logic within the model.

- Applicability: unconditional
- Rules: R14 (see `decision-rules.md`)
- Locator: SD-supp item 3.4; PDF: Table 3 P7/J60; section 5.4 P7/J60
- Wording: variant-specific wording

## Section 4 — Experimentation

### 4.1 Initialisation

**Recommendation (verbatim):**

> List all initial values of stocks and auxiliary variables within the model.
> Provide details of empirical or theoretical distributions used, if initial values are varied over multiple runs of the model (e.g. for calibration or optimisation).

- Applicability: Initial values unconditional (R28). Distributions clause only if initial values are varied over multiple runs.
- Rules: R28 (see `decision-rules.md`)
- Locator: SD-supp item 4.1; PDF: Table 3 P7/J60; section 5.5 P7/J60 ('SD would need to detail the initial values of stocks')
- Wording: variant-specific wording

### 4.2 Run length

**Recommendation (verbatim):**

> Detail the run length of the simulation model and time units

- Applicability: unconditional
- Rules: - (see `decision-rules.md`)
- Locator: SD-supp item 4.2; PDF: Table 3 P7/J60; section 5.5 P7/J60; Table 7 P10/J63
- Wording: identical in STRESS-DES, STRESS-ABS

### 4.3 Estimation approach

**Recommendation (verbatim):**

> If the SD model includes stochastic inputs report if multiple replications or an alternative approach has been used in estimating model outputs.
> For model calibration or optimisation report the algorithm/search method used and the number replications (runs) of the simulation model.

- Applicability: First clause only if the model has stochastic inputs; second clause only if calibration or optimisation is used (R29). A deterministic SD model with no calibration -> Not applicable, citing both clauses.
- Rules: R29, R16 (see `decision-rules.md`)
- Cross-references: 1.3c
- Locator: SD-supp item 4.3; PDF: Table 3 P7/J60; section 5.5 P7/J60
- Wording: variant-specific wording

## Section 5 — Implementation

### 5.1 Software or programming language

**Recommendation (verbatim):**

> State the operating system and version and build number.
> State the name, version and build number of commercial or open source SD software that the model is implemented in (e.g. Vensim, iThink, InsightMaker). Many modern SD packages provide specialised stocks to act as delays e.g. conveyers, queues and ovens. Provide details all specialised stocks and where they are used in the model.
> State the name and version of general-purpose programming languages used (e.g. Python 3.5.2). Where packages, frameworks and libraries have been used provide all detailed including version numbers.

- Applicability: Operating system and software/language with versions unconditional; specialised-stock details only if such stocks are used; packages clause only if any are used.
- Rules: R18 (see `decision-rules.md`)
- Locator: SD-supp item 5.1; PDF: Table 3 P7/J60; section 5.6 P7-9/J60-62; Table 7 P10/J63
- Wording: variant-specific wording

### 5.2 Random sampling

**Recommendation (verbatim):**

> State the algorithm used to generate random samples with in the software/programming language used e.g. Mersenne Twister.

- Applicability: Not applicable for deterministic models (R16; PDF section 5.6; see also SD-supp 4.3's stochastic condition).
- Rules: R16 (see `decision-rules.md`)
- Cross-references: 4.3
- Locator: SD-supp item 5.2; PDF: Table 3 P7/J60; section 5.6 P9/J62
- Wording: variant-specific wording

### 5.3 Model execution

**Recommendation (verbatim):**

> Report the integration method used along with time step settings.

- Applicability: unconditional
- Rules: R18 (see `decision-rules.md`)
- Cross-references: 5.1
- Locator: SD-supp item 5.3; PDF: Table 3 P7/J60; section 5.6 P9/J62; Table 7 P10/J63 ('Euler's Method ... DT of 1 month')
- Wording: variant-specific wording

### 5.4 System Specification

**Recommendation (verbatim):**

> State the model run time and specification of hardware used. This is particularly important for large scale models that require substantial computing power.

- Applicability: Never automatically Not applicable; for small models a Missing is noted as low impact (R17).
- Rules: R17 (see `decision-rules.md`)
- Locator: SD-supp item 5.4; PDF: Table 3 P7/J60; section 5.6 P9/J62; Table 7 P10/J63
- Wording: variant-specific wording

## Section 6 — Code Access

### 6.1 Computer Model Sharing Statement

**Recommendation (verbatim):**

> Describe how someone could obtain the model described in the paper, the simulation software and any other associated software (or hardware) needed to reproduce the results. Provide, where possible, the link and DOIs to these.

- Applicability: 'Models are available on request', a secure/local directory, or a repository link all satisfy the statement (PDF section 5.7). Link/DOI 'where possible' (R33). A code link does not satisfy items 2.x-5.x (R7).
- Rules: R7, R10, R13, R33 (see `decision-rules.md`)
- Locator: SD-supp item 6.1; PDF: Table 3 P7/J60; section 5.7 P9/J62
- Wording: identical in STRESS-DES, STRESS-ABS

