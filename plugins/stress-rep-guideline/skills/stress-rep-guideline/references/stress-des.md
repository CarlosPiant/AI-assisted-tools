# STRESS-DES — Discrete-event simulation guidelines STRESS-DES (verbatim checklist)

Source: Supplementary material `tjsm_a_1442155_sm3123.docx` of Monks, T., Currie, C. S. M., Onggo, B. S., Robinson, S., Kunc, M., & Taylor, S. J. E. (2019). Strengthening the reporting of empirical simulation studies: Introducing the STRESS guidelines. Journal of Simulation, 13(1), 55-67. doi:10.1080/17477778.2018.1442155.
Short locator used in this skill: `DES-supp item <n>`.

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

Keywords: discrete-event, discrete event, DES, entity, entities, activity cycle, process flow, resource, resources, queue, queues, queuing discipline, arrival, arrivals, inter-arrival, warm-up, terminating, non-terminating, event processing, three phase, batch means, Simul8, Arena, AnyLogic, SimPy, simulacion de eventos discretos, simulación de eventos discretos, entidad, entidades, cola, colas, recurso, recursos, llegadas, calentamiento

## Section 1 — Objectives

### 1.1 Purpose of the model

**Recommendation (verbatim):**

> Explain the background and objectives for the model.

- Applicability: unconditional
- Rules: - (see `decision-rules.md`)
- Locator: DES-supp item 1.1; PDF: Table 3 P7/J60; rationale section 5.2 P6/J59
- Wording: variant-specific wording

### 1.2 Model Outputs

**Recommendation (verbatim):**

> Define all quantitative performance measures that are reported, using equations where necessary. Specify how and when they are calculated during the model run along with how any measures of error such as confidence intervals are calculated.

- Applicability: unconditional
- Rules: R8 (see `decision-rules.md`)
- Locator: DES-supp item 1.2; PDF: Table 3 P7/J60; section 5.2 P6/J59
- Wording: variant-specific wording

### 1.3 Experimentation Aims

**Recommendation (verbatim):**

> If the model has been used for experimentation, state the objectives that it was used to investigate.

#### 1.3a Scenario based analysis

> Scenario based analysis – Provide a name and description for each scenario, providing a rationale for the choice of scenarios and ensure that item 2.3 (below) is completed.

Applicability: When scenario-based analysis is used.

#### 1.3b Design of experiments

> Design of experiments – Provide details of the overall design of the experiments with reference to performance measures and their parameters (provide further details in data below).

Applicability: When a designed experiment is used.

#### 1.3c Simulation Optimisation

> Simulation Optimisation – (if appropriate) Provide full details of what is to be optimised, the parameters that were included and the algorithm(s) that was be used. Where possible provide a citation of the algorithm(s).

Applicability: '(if appropriate)' - when simulation optimisation is used.

- Applicability: Conditional: applies only if the model has been used for experimentation beyond the base run (R21). Sub-points are audited only for the type(s) of experimentation actually used (R22; skill interpretation - only sub-point c carries an explicit '(if appropriate)').
- Rules: R21, R22, R34 (see `decision-rules.md`)
- Cross-references: 2.3, 3.3
- Locator: DES-supp item 1.3; PDF: Table 3 P7/J60; section 5.2 P6/J59
- Wording: variant-specific wording

## Section 2 — Logic

### 2.1 Base model overview diagram

**Recommendation (verbatim):**

> Describe the base model using appropriate diagrams and description. This could include one or more process flow, activity cycle or equivalent diagrams sufficient to describe the model to readers. Avoid complicated diagrams in the main text. The goal is to describe the breadth and depth of the model with respect to the system being studied.

- Applicability: unconditional
- Rules: R3 (see `decision-rules.md`)
- Locator: DES-supp item 2.1; PDF: Table 3 P7/J60; section 5.3 P6-7/J59-60; Table 2 principle 6 P7/J60
- Wording: variant-specific wording

### 2.2 Base model logic

**Recommendation (verbatim):**

> Give details of the base model logic. Give additional model logic details sufficient to communicate to the reader how the model works.

- Applicability: unconditional
- Rules: - (see `decision-rules.md`)
- Locator: DES-supp item 2.2; PDF: Table 3 P7/J60; section 5.3 P6/J59
- Wording: variant-specific wording

### 2.3 Scenario logic

**Recommendation (verbatim):**

> Give details of the logical difference between the base case model and scenarios (if any). This could be incorporated as text or where differences are substantial could be incorporated in the same manner as 2.2.

- Applicability: Conditional: '(if any)' - Not applicable when the study has no scenarios (R23). If scenarios exist and the document states the logic is unchanged, that statement is the evidence.
- Rules: R23, R34 (see `decision-rules.md`)
- Cross-references: 1.3, 2.2
- Locator: DES-supp item 2.3; PDF: Table 3 P7/J60; section 5.3 P6/J59
- Wording: variant-specific wording

### 2.4 Algorithms

**Recommendation (verbatim):**

> Provide further detail on any algorithms in the model that (for example) mimic complex or manual processes in the real world (i.e. scheduling of arrivals/appointments/operations/maintenance, operation of a conveyor system, machine breakdowns, etc.). Sufficient detail should be included (or referred to in other published work) for the algorithms to be reproducible. Pseudo-code may be used to describe an algorithm.

- Applicability: Conditional: 'any algorithms' - Not applicable when no such algorithm is evident anywhere in the model description (R24). A reference to other published work satisfies the detail requirement.
- Rules: R24 (see `decision-rules.md`)
- Locator: DES-supp item 2.4; PDF: Table 3 P7/J60
- Wording: identical in STRESS-ABS

### 2.5 Components

#### 2.5.1 Entities

> Give details of all entities within the simulation including a description of their role in the model and a description of all their attributes.

#### 2.5.2 Activities

> Describe the activities that entities engage in within the model. Provide details of entity routing into and out of the activity.

#### 2.5.3 Resources

> List all the resources included within the model and which activities make use of them.

#### 2.5.4 Queues

> Give details of the assumed queuing discipline used in the model (e.g. First in First Out, Last in First Out, prioritisation, etc.). Where one or more queues have a different discipline from the rest, provide a list of queues, indicating the queuing discipline used for each. If reneging, balking or jockeying occur, etc., provide details of the rules. Detail any delays or capacity constraints on the queues.

Applicability: Reneging/balking/jockeying rules only if those behaviours occur.

#### 2.5.5 Entry/Exit Points

> Give details of the model boundaries i.e. all arrival and exit points of entities. Detail the arrival mechanism (e.g. ‘thinning’ to mimic a non-homogenous Poisson process or balking)

- Applicability: Audit each sub-item separately; the sub-items are the paradigm-specific building blocks of the model.
- Rules: - (see `decision-rules.md`)
- Locator: DES-supp item 2.5; PDF: Table 4 P8/J61 (minor wording differences: 'baulking' vs 'balking'); section 5.3 P7/J60
- Wording: variant-specific wording

## Section 3 — Data

### 3.1 Data sources

**Recommendation (verbatim):**

> List and detail all data sources. Sources may include:
> - Interviews with stakeholders,
> - Samples of routinely collected data,
> - Prospectively collected samples for the purpose of the simulation study,
> - Public domain data published in either academic or organisational literature. Provide, where possible, the link and DOI to the data or reference to published literature.
> All data source descriptions should include details of the sample size, sample date ranges and use within the study.

- Applicability: Link/DOI 'where possible' (R33): its absence alone does not make the item Missing when the source is described or referenced.
- Rules: R33 (see `decision-rules.md`)
- Locator: DES-supp item 3.1; PDF: Table 3 P7/J60; section 5.4 P7/J60; Table 5 P9/J62
- Wording: variant-specific wording

### 3.2 Pre-processing

**Recommendation (verbatim):**

> Provide details of any data manipulation that has taken place before its use in the simulation, e.g. interpolation to account for missing data or the removal of outliers.

- Applicability: 'any data manipulation': silence is Missing; an explicit statement that no pre-processing was performed is Addressed (R26).
- Rules: R26, R35 (see `decision-rules.md`)
- Locator: DES-supp item 3.2; PDF: Table 3 P7/J60 prints this as item 3.3 (numbering differs); section 5.4 P7/J60
- Wording: identical in STRESS-SD

### 3.3 Input parameters

**Recommendation (verbatim):**

> List all input variables in the model. Provide a description of their use and include parameter values. For stochastic inputs provide details of any continuous, discrete or empirical distributions used along with all associated parameters. Give details of all time dependent parameters and correlation.
> Clearly state:
> - Base case data
> - Data use in experimentation, where different from the base case.
> - Where optimisation or design of experiments has been used, state the range of values that parameters can take.
> Where theoretical distributions are used, state how these were selected and prioritised above other candidate distributions.

- Applicability: Unconditional: the list of inputs with values and the base case data. Conditional clauses (R27): stochastic inputs -> distributions and parameters; experimentation -> data where different; optimisation/DoE -> parameter ranges; theoretical distributions -> selection rationale.
- Rules: R27, R34, R35 (see `decision-rules.md`)
- Cross-references: 1.3
- Locator: DES-supp item 3.3; PDF: Table 3 P7/J60 prints this as item 3.2 (numbering differs); section 5.4 P7/J60; Table 5 P9/J62
- Wording: variant-specific wording

### 3.4 Assumptions

**Recommendation (verbatim):**

> Where data or knowledge of the real system is unavailable what assumptions are included in the model? This might include parameter values, distributions or routing logic within the model.

- Applicability: unconditional
- Rules: R14 (see `decision-rules.md`)
- Locator: DES-supp item 3.4; PDF: Table 3 P7/J60; section 5.4 P7/J60
- Wording: variant-specific wording

## Section 4 — Experimentation

### 4.1 Initialisation

**Recommendation (verbatim):**

> Report if the system modelled is terminating or non-terminating. State if a warm-up period has been used, its length and the analysis method used to select it. For terminating systems state the stopping condition.
> State what if any initial model conditions have been included, e.g., pre-loaded queues and activities. Report whether initialisation of these variables is deterministic or stochastic.

- Applicability: Unconditional: terminating/non-terminating statement; a statement on warm-up (even 'none'); statement on initial conditions (even 'none'). Conditional (R28): warm-up length and selection method if a warm-up is used; stopping condition for terminating systems; deterministic/stochastic initialisation if initial conditions exist.
- Rules: R28 (see `decision-rules.md`)
- Locator: DES-supp item 4.1; PDF: Table 3 P7/J60; section 5.5 P7/J60; Table 6 P9/J62
- Wording: variant-specific wording

### 4.2 Run length

**Recommendation (verbatim):**

> Detail the run length of the simulation model and time units.

- Applicability: unconditional
- Rules: - (see `decision-rules.md`)
- Locator: DES-supp item 4.2; PDF: Table 3 P7/J60; section 5.5 P7/J60; Table 6 P9/J62
- Wording: identical in STRESS-SD, STRESS-ABS

### 4.3 Estimation approach

**Recommendation (verbatim):**

> State the method used to account for the stochasticity: For example, two common methods are multiple replications or batch means. Where multiple replications have been used, state the number of replications and for batch means, indicate the batch length and whether the batch means procedure is standard, spaced or overlapping. For both procedures provide a justification for the methods used and the number of replications/size of batches.

- Applicability: Assumes a stochastic model (R29). A deterministic DES is unusual: mark Not applicable via R16 and flag it. Requires method, count (replications or batch details) AND a justification; count without justification is Partially addressed.
- Rules: R29, R16, R8 (see `decision-rules.md`)
- Locator: DES-supp item 4.3; PDF: Table 3 P7/J60; section 5.5 P7/J60; Table 6 P9/J62
- Wording: variant-specific wording

## Section 5 — Implementation

### 5.1 Software or programming language

**Recommendation (verbatim):**

> State the operating system and version and build number.
> State the name, version and build number of commercial or open source DES software that the model is implemented in.
> State the name and version of general-purpose programming languages used (e.g. Python 3.5).
> Where frameworks and libraries have been used provide all details including version numbers.

- Applicability: Operating system and simulation software/language with versions are unconditional; frameworks/libraries clause applies when any are used.
- Rules: R18, R34 (see `decision-rules.md`)
- Cross-references: 5.3
- Locator: DES-supp item 5.1; PDF: Table 3 P7/J60; section 5.6 P7-9/J60-62; Table 7 P10/J63
- Wording: variant-specific wording

### 5.2 Random sampling

**Recommendation (verbatim):**

> State the algorithm used to generate random samples in the software/programming language used e.g. Mersenne Twister.
> If common random numbers are used, state how seeds (or random number streams) are distributed among sampling processes.

- Applicability: Not applicable for deterministic models (R16, PDF section 5.6: 'Relevant only for stochastic models'). Second sentence conditional on common random numbers being used (R30).
- Rules: R16, R30 (see `decision-rules.md`)
- Locator: DES-supp item 5.2; PDF: Table 3 P7/J60; section 5.6 P9/J62; Table 7 P10/J63
- Wording: variant-specific wording

### 5.3 Model execution

**Recommendation (verbatim):**

> State the event processing mechanism used e.g. three phase, event, activity, process interaction.
> Note that in some commercial software the event processing mechanism may not be published. In these cases authors should adhere to item 5.1 software recommendations.
> State all priority rules included if entities/activities compete for resources.
> If the model is parallel, distributed and/or use grid or cloud computing, etc., state and preferably reference the technology used. For parallel and distributed simulations the time management algorithms used. If the HLA is used then state the version of the standard, which run-time infrastructure (and version), and any supporting documents (FOMs, etc.)

- Applicability: Event processing mechanism unconditional, but an unpublished commercial mechanism plus complete 5.1 detail counts as Addressed (R18, R31). Priority rules only if entities/activities compete for resources; parallel/distributed/HLA clauses only if such technology is used (R31).
- Rules: R18, R31, R34 (see `decision-rules.md`)
- Cross-references: 5.1
- Locator: DES-supp item 5.3; PDF: Table 3 P7/J60; section 5.6 P9/J62; Table 7 P10/J63
- Wording: variant-specific wording

### 5.4 System Specification

**Recommendation (verbatim):**

> State the model run time and specification of hardware used. This is particularly important for large scale models that require substantial computing power. For parallel, distributed and/or use grid or cloud computing, etc. state the details of all systems used in the implementation (processors, network, etc.)

- Applicability: Never automatically Not applicable; for small models a Missing is noted as low impact (R17). Parallel/distributed clause conditional (R32).
- Rules: R17, R32 (see `decision-rules.md`)
- Locator: DES-supp item 5.4; PDF: Table 3 P7/J60; section 5.6 P9/J62; Table 7 P10/J63
- Wording: identical in STRESS-ABS

## Section 6 — Code Access

### 6.1 Computer Model Sharing Statement

**Recommendation (verbatim):**

> Describe how someone could obtain the model described in the paper, the simulation software and any other associated software (or hardware) needed to reproduce the results. Provide, where possible, the link and DOIs to these.

- Applicability: 'Models are available on request', a secure/local directory, or a repository link all satisfy the statement (PDF section 5.7). Link/DOI 'where possible' (R33). A code link does not satisfy items 2.x-5.x (R7).
- Rules: R7, R10, R13, R33 (see `decision-rules.md`)
- Locator: DES-supp item 6.1; PDF: Table 3 P7/J60; section 5.7 P9/J62
- Wording: identical in STRESS-SD, STRESS-ABS

