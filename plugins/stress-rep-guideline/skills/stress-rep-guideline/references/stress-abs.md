# STRESS-ABS — Agent based simulation guidelines STRESS-ABS (verbatim checklist)

Source: Supplementary material `tjsm_a_1442155_sm3069.docx` of Monks, T., Currie, C. S. M., Onggo, B. S., Robinson, S., Kunc, M., & Taylor, S. J. E. (2019). Strengthening the reporting of empirical simulation studies: Introducing the STRESS guidelines. Journal of Simulation, 13(1), 55-67. doi:10.1080/17477778.2018.1442155.
Short locator used in this skill: `ABS-supp item <n>`.

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

Keywords: agent-based, agent based, ABS, ABM, agent, agents, environment, grid, patch, interaction topology, network structure, agent states, state chart, emergent, emerge, NetLogo, Repast, MASON, AnyLogic, Mesa, time-stepped, time step, basado en agentes, basada en agentes, agente, agentes, entorno, topologia de interaccion, topología de interacción, emergente, comportamiento emergente

## Section 1 — Objectives

### 1.1 Purpose of the model

**Recommendation (verbatim):**

> Explain the background and rationale for the model.

- Applicability: unconditional
- Rules: - (see `decision-rules.md`)
- Locator: ABS-supp item 1.1; PDF: Table 3 P7/J60; section 5.2 P6/J59
- Wording: identical in STRESS-SD

### 1.2 Model Outputs

**Recommendation (verbatim):**

> State the qualitative or quantitative system level outputs that emerge from agent interactions within the ABS.
> Define all quantitative performance measures that are reported, using equations where necessary. Specify how and when they are calculated during the model run along with how any measures of error such as confidence intervals are calculated

- Applicability: unconditional
- Rules: R8 (see `decision-rules.md`)
- Locator: ABS-supp item 1.2; PDF: Table 3 P7/J60; section 5.2 P6/J59
- Wording: variant-specific wording

### 1.3 Experimentation Aims

**Recommendation (verbatim):**

> If the model has been used for experimentation, state the research questions that it was used to answer.

#### 1.3a Theory driven analysis

> Theory driven analysis. – Provide details and reference the theories that are tested within the model.

Applicability: When the model tests theories.

#### 1.3b Scenario based analysis

> Scenario based analysis – Provide a name and description for each scenario, including a rationale for the choice of scenarios and ensure that item 2.3 (below) is completed.

Applicability: When scenario-based analysis is used.

#### 1.3c Design of experiments

> Design of experiments – Provide details of the overall design of the experiments with reference to performance measures and their parameters (provide further details in data below).

Applicability: When a designed experiment is used.

#### 1.3d Simulation Optimisation

> Simulation Optimisation – (if appropriate) Provide full details of what is to be optimised, the parameters that were included and the algorithm(s) that was be used. Where possible provide a citation of the algorithm(s).

Applicability: '(if appropriate)' - when simulation optimisation is used.

- Applicability: Conditional: applies only if the model has been used for experimentation beyond the base run (R21). Sub-points are audited only for the type(s) of experimentation actually used (R22; skill interpretation - only sub-point d carries an explicit '(if appropriate)').
- Rules: R21, R22, R34 (see `decision-rules.md`)
- Cross-references: 2.3, 3.3
- Locator: ABS-supp item 1.3; PDF: Table 3 P7/J60; section 5.2 P6/J59
- Wording: variant-specific wording

## Section 2 — Logic

### 2.1 Base model overview diagram

**Recommendation (verbatim):**

> Provide one or more of: state chart, process flow or equivalent diagrams to describe the basic logic of the base model to readers. Avoid complicated diagrams in the main text.

- Applicability: unconditional
- Rules: R3 (see `decision-rules.md`)
- Locator: ABS-supp item 2.1; PDF: Table 3 P7/J60; section 5.3 P6-7/J59-60; Table 2 principle 6 P7/J60
- Wording: variant-specific wording

### 2.2 Base model logic

**Recommendation (verbatim):**

> Give details of the base model logic. This could be text to explain the overview diagram along with extra details including ABS product and process patterns. Include details of all intermediate calculations.

- Applicability: unconditional
- Rules: - (see `decision-rules.md`)
- Locator: ABS-supp item 2.2; PDF: Table 3 P7/J60; section 5.3 P6/J59
- Wording: variant-specific wording

### 2.3 Scenario logic

**Recommendation (verbatim):**

> Give details of any difference in the model logic between the base case model and scenarios. This could be incorporated as text or, where differences are substantial, could be incorporated in the same manner as 2.1.

- Applicability: 'any difference' - Not applicable when the study has no scenarios (R23).
- Rules: R23, R34 (see `decision-rules.md`)
- Cross-references: 1.3, 2.1
- Locator: ABS-supp item 2.3; PDF: Table 3 P7/J60; section 5.3 P6/J59
- Wording: variant-specific wording

### 2.4 Algorithms

**Recommendation (verbatim):**

> Provide further detail on any algorithms in the model that (for example) mimic complex or manual processes in the real world (i.e. scheduling of arrivals/appointments/operations/maintenance, operation of a conveyor system, machine breakdowns, etc.). Sufficient detail should be included (or referred to in other published work) for the algorithms to be reproducible. Pseudo-code may be used to describe an algorithm.

- Applicability: Conditional: 'any algorithms' - Not applicable when no such algorithm is evident (R24). Agent decision rules themselves are audited under 2.5.2.
- Rules: R24 (see `decision-rules.md`)
- Cross-references: 2.5.2
- Locator: ABS-supp item 2.4; PDF: Table 3 P7/J60
- Wording: identical in STRESS-DES

### 2.5 Components

#### 2.5.1 Environment

> Describe the environment agents interact within, indicating its structure, and how it is generated. For example, are agents bound within a homogeneous grid, or do they have continuous movement through a detailed landscape incorporating geographic or environmental information?

#### 2.5.2 Agents

> List all agents and agent groups within the simulation. Include a description of their role in the model, their possible states, state transitions, and all their attributes.
> Describe all decision-making rules that agents follow in either algorithmic or equation form. Where relevant authors should report:
> - The data that agents access (I.e. internal attributes or external information from the environment) and how it is used.
> - The objectives agents seek to achieve.
> - The algorithms, optimisations, heuristics and rules that agents use to achieve objectives.
> - How agents work together within a group along with any rules for changes in group membership.
> - Predictions of future events and adaptive action.

Applicability: Bulleted points 'Where relevant' - audit those that apply to the model's agents.

#### 2.5.3 Interaction Topology

> Describe how agents and agent groupings are connected with each other in the model define:
> - with whom agents can interact,
> - how recipients of interactions are selected
> - what frequency interaction occurs.
> - How agents handle and assign priorities to concurrent events
> It is recommended that interactions are described using a combination of equations pseudo-code and logic diagrams.
> Report how interactions are affected by agent states and the environment state

#### 2.5.4 Entry / Exit

> Where relevant, define how agents are created and destroyed in the model.

Applicability: 'Where relevant' - Not applicable when the agent population is fixed and the document says so (R25).

- Applicability: Audit each sub-item separately; the sub-items are the paradigm-specific building blocks of the model. (The supplement prints the first three sub-item numbers with a trailing period: '2.5.1.', '2.5.2.', '2.5.3.'.)
- Rules: - (see `decision-rules.md`)
- Locator: ABS-supp item 2.5; PDF: Table 4 P8/J61 (title there: 'Entry/Exit Points'; Table 4 lacks the final sentence of 2.5.3); section 5.3 P7/J60
- Wording: variant-specific wording

## Section 3 — Data

### 3.1 Data sources

**Recommendation (verbatim):**

> List and detail all data sources. Sources may include:
> - Interviews with stakeholders
> - samples of routinely collected data,
> - prospectively collected samples for the purpose of the simulation study,
> - public domain data published in either academic or organisational literature. Provide, where possible, the link and DOI to the data or reference to published literature.
> All data source descriptions should include details of the sample size, date ranges and use within the study.

- Applicability: Link/DOI 'where possible' (R33).
- Rules: R33 (see `decision-rules.md`)
- Locator: ABS-supp item 3.1; PDF: Table 3 P7/J60; section 5.4 P7/J60; Table 5 P9/J62
- Wording: variant-specific wording

### 3.2 Pre-processing

**Recommendation (verbatim):**

> Provide details of any data manipulation or filtering that has taken place before its use in the simulation, e.g. interpolation to account for missing data, removal of outliers or filtering of large scale data.

- Applicability: 'any data manipulation or filtering': silence is Missing; an explicit statement that no pre-processing was performed is Addressed (R26).
- Rules: R26, R35 (see `decision-rules.md`)
- Locator: ABS-supp item 3.2; PDF: Table 3 P7/J60 prints this as item 3.3 (numbering differs); section 5.4 P7/J60
- Wording: variant-specific wording

### 3.3 Input parameters

**Recommendation (verbatim):**

> List all input parameters in the model, providing a description of each parameter and the values used. For stochastic inputs provide details of any continuous, discrete or empirical distributions used along with all associated parameters. Where applicable define the time/spatial dependence of parameters and any correlation structure.
> Clearly state:
> - Base case inputs
> - Inputs used in experimentation, where different from the base case.
> - Where optimisation or design of experiments has been used, state the range of values that parameters can take.
> Where theoretical distributions are used, state how, , these were selected and prioritised above other candidate distributions.

- Applicability: Unconditional: the list of inputs with values and the base case inputs. Conditional clauses (R27): stochastic inputs; time/spatial dependence 'Where applicable'; experimentation inputs; optimisation/DoE ranges; theoretical distribution selection.
- Rules: R27, R34, R35 (see `decision-rules.md`)
- Cross-references: 1.3
- Locator: ABS-supp item 3.3; PDF: Table 3 P7/J60 prints this as item 3.2 (numbering differs); section 5.4 P7/J60
- Wording: variant-specific wording

### 3.4 Assumptions

**Recommendation (verbatim):**

> Where data or knowledge of the real system is unavailable, state and justify the assumptions used to set input parameter values and distributions; agent interactions or behaviour; or model logic.

- Applicability: Requires both a statement AND a justification of assumptions; a list without justification is Partially addressed.
- Rules: R14 (see `decision-rules.md`)
- Locator: ABS-supp item 3.4; PDF: Table 3 P7/J60; section 5.4 P7/J60
- Wording: variant-specific wording

## Section 4 — Experimentation

### 4.1 Initialisation

**Recommendation (verbatim):**

> State if a warm-up period has been used, its length and the analysis method used to select it.
> State what if any initial agent and environmental conditions have been included. For example, the initial agent population size, agent states and attributes, initial agent network structure(s), and resources within the environment. Report whether initialisation of these variables is deterministic or stochastic.

- Applicability: Unconditional: a statement on warm-up (even 'none'; the supplement asks unconditionally, unlike PDF section 5.5's 'where appropriate for stochastic ABS' - discrepancy D10); statement on initial agent/environment conditions. Conditional (R28): warm-up length and selection method if used; deterministic/stochastic initialisation if initial conditions exist.
- Rules: R28 (see `decision-rules.md`)
- Locator: ABS-supp item 4.1; PDF: Table 3 P7/J60; section 5.5 P7/J60; Table 6 P9/J62
- Wording: variant-specific wording

### 4.2 Run length

**Recommendation (verbatim):**

> Detail the run length of the simulation model and time units.

- Applicability: unconditional
- Rules: - (see `decision-rules.md`)
- Locator: ABS-supp item 4.2; PDF: Table 3 P7/J60; section 5.5 P7/J60; Table 6 P9/J62
- Wording: identical in STRESS-DES, STRESS-SD

### 4.3 Estimation approach

**Recommendation (verbatim):**

> State if the model is deterministic or stochastic. If the model is stochastic, state the number of replications that have been used. If an alternative estimation method has been used (e.g. batch means), provide full details.

- Applicability: The deterministic/stochastic statement is unconditional - an explicit 'deterministic' statement is Addressed (R29). Replications (or alternative method details) required only if stochastic.
- Rules: R29, R16, R8 (see `decision-rules.md`)
- Cross-references: 5.2
- Locator: ABS-supp item 4.3; PDF: Table 3 P7/J60; section 5.5 P7/J60; Table 6 P9/J62
- Wording: variant-specific wording

## Section 5 — Implementation

### 5.1 Software or programming language

**Recommendation (verbatim):**

> State the operating system and version and build number.
> State the name, version and build number of commercial or open source ABS software that the model is implemented in.
> State the name and version of general-purpose programming languages used (e.g. Python 3.5.2). Where packages, frameworks and libraries have been used provide all detailed including version numbers.

- Applicability: Operating system and software/language with versions unconditional; packages clause only if any are used.
- Rules: R18 (see `decision-rules.md`)
- Locator: ABS-supp item 5.1; PDF: Table 3 P7/J60; section 5.6 P7-9/J60-62; Table 7 P10/J63
- Wording: variant-specific wording

### 5.2 Random sampling

**Recommendation (verbatim):**

> State the algorithm or package used to generate random samples within the software/programming language used e.g. Mersenne Twister or Java.Random version x.y

- Applicability: Not applicable for deterministic models (R16; PDF section 5.6; ABS-supp 4.3 asks for the deterministic/stochastic statement).
- Rules: R16 (see `decision-rules.md`)
- Cross-references: 4.3
- Locator: ABS-supp item 5.2; PDF: Table 3 P7/J60; section 5.6 P9/J62; Table 7 P10/J63
- Wording: variant-specific wording

### 5.3 Model execution

**Recommendation (verbatim):**

> If the ABS model has a time component, describe how time is modelled (e.g. fixed time steps or discrete-event). State the order of variable updating within the model. In time-stepped execution state how concurrent events are resolved.
> If the model is parallel, distributed and/or use grid or cloud computing, etc., state and preferably reference the technology used. For parallel and distributed simulations the time management algorithms used. If the HLA is used then state the version of the standard, which run-time infrastructure (and version), and any supporting documents (FOMs, etc.)

- Applicability: Time-modelling clause 'If the ABS model has a time component' (almost always); concurrency clause only for time-stepped execution; parallel/distributed/HLA clauses only if such technology is used (R31). Unpublished commercial mechanism plus full 5.1 detail counts as Addressed (R18).
- Rules: R18, R31 (see `decision-rules.md`)
- Cross-references: 5.1
- Locator: ABS-supp item 5.3; PDF: Table 3 P7/J60; section 5.6 P9/J62
- Wording: variant-specific wording

### 5.4 System Specification

**Recommendation (verbatim):**

> State the model run time and specification of hardware used. This is particularly important for large scale models that require substantial computing power. For parallel, distributed and/or use grid or cloud computing, etc. state the details of all systems used in the implementation (processors, network, etc.)

- Applicability: Never automatically Not applicable; for small models a Missing is noted as low impact (R17). Parallel/distributed clause conditional (R32).
- Rules: R17, R32 (see `decision-rules.md`)
- Locator: ABS-supp item 5.4; PDF: Table 3 P7/J60; section 5.6 P9/J62; Table 7 P10/J63
- Wording: identical in STRESS-DES

## Section 6 — Code Access

### 6.1 Computer Model Sharing Statement

**Recommendation (verbatim):**

> Describe how someone could obtain the model described in the paper, the simulation software and any other associated software (or hardware) needed to reproduce the results. Provide, where possible, the link and DOIs to these.

- Applicability: 'Models are available on request', a secure/local directory, or a repository link all satisfy the statement (PDF section 5.7). Link/DOI 'where possible' (R33). A code link does not satisfy items 2.x-5.x (R7).
- Rules: R7, R10, R13, R33 (see `decision-rules.md`)
- Locator: ABS-supp item 6.1; PDF: Table 3 P7/J60; section 5.7 P9/J62
- Wording: identical in STRESS-DES, STRESS-SD

