# Scope gate and study-type detection

CHEERS 2022 defines what it covers (R1, R2, R4, R5) but gives no procedure for recognising a study type. The vocabulary lists below are this skill's own aid (rule S4); an inferred type is confirmed with the user (one confirmation question) or labelled "inferred, user said proceed".

## Contents

1. Scope gate — stop or continue
2. Study type: model-based or empirical
3. Form of evaluation
4. The confirmation question and the header line

## 1. Scope gate — stop or continue

Run this before anything else. Both conditions of the definition must hold: **(a)** two or more alternative courses of action are compared, and **(b)** costs are part of the comparison.

> "Health economic evaluations are comparative analyses of alternative courses of action in terms of their costs and consequences." (CHEERS 2022, abstract, P1/J3)

| Document | Decision | Quote in the stop message |
|---|---|---|
| Cost-of-illness, burden-of-disease or economic-burden study: costs of a condition with no intervention compared ("costo de la enfermedad", "carga de la enfermedad", "carga económica") | **Stop** — no comparison of alternative courses of action | R1 definition above |
| Single-intervention cost description (costs of one programme, no comparator) | **Stop** — same reason | R1 |
| Clinical trial or effectiveness study with no costs | **Stop** — no costs | R1 |
| Budget impact analysis ("impacto presupuestario"), affordability projection | **Stop** | "budget impact analyses and constrained optimization studies are beyond the scope of CHEERS guidance, as they require additional reporting that addresses population dynamics and feasibility constraints and are addressed in other guidance reports." (P4/J6) |
| Constrained optimisation / mathematical programming of resource allocation ("optimización con restricciones") | **Stop** | same R4 quote |
| Comparative cost analysis (costs and cost offsets of two or more options, no outcomes) | **Continue** — in scope (R2); items 11–13 Not applicable (R14) | — |
| CEA, CUA, cost-minimisation, CBA, extended or distributional CEA, model-based or empirical | **Continue** | — |
| Intervention is a service, programme, public-health or social-care intervention | **Continue** (R6) | — |

A study that combines an out-of-scope analysis with a comparative evaluation (for example a CEA plus a budget impact section) is audited as a CEA; say in the header that the budget impact part is outside CHEERS (R4).

**Stop message (no audit, no report file with item states):** say what the document is, which part of the definition fails (no comparator / no costs / BIA / constrained optimisation), quote the matching sentence with its locator, and state that no CHEERS audit was performed. Do not offer a "closest fit" audit unless the user asks for one.

Signals of a missing comparator: one intervention or condition throughout; results reported as total or per-patient costs of a disease, prevalence-based or incidence-based cost estimates, productivity losses, DALYs or QALYs lost to a condition — with no "versus", "compared with", "frente a", "comparado con", no incremental results and no ICER.

## 2. Study type: model-based or empirical (R5, R14, R20)

Order: argument (`--modelling yes|no`) → declaration in the document → vocabulary inference.

**Declarations** (any one is enough): "decision-analytic model", "decision model", "Markov model", "state-transition model", "decision tree", "partitioned survival model", "microsimulation", "discrete event simulation", "cohort model", "economic model"; "trial-based", "alongside a randomised controlled trial", "within-trial", "piggy-back", "patient-level data from the … trial"; ES: "modelo de Markov", "modelo de decisión", "árbol de decisión", "modelo de supervivencia particionada", "microsimulación", "modelo económico", "evaluación económica junto a un ensayo clínico", "basada en ensayo", "datos individuales de pacientes del ensayo".

**Model vocabulary (infer model-based):** health states, cycle / cycle length, half-cycle correction, transition probabilities, hypothetical cohort, extrapolation beyond follow-up, lifetime horizon with yearly cycles, model structure, absorbing state, tunnel state, parametric survival curves fitted for extrapolation; ES: estados de salud, ciclo, corrección de medio ciclo, probabilidades de transición, cohorte hipotética, extrapolación, estructura del modelo.

**Empirical vocabulary (infer empirical):** randomised / cluster-randomised trial participants, case report forms, resource-use questionnaires or diaries, follow-up visits, bootstrapping of patient-level costs and outcomes, seemingly unrelated regression, multiple imputation of missing patient data, within-trial horizon; ES: participantes del ensayo, cuestionarios de uso de recursos, remuestreo (bootstrap), imputación múltiple, horizonte del ensayo.

**Mixed:** a trial-based analysis extended by a model (for example within-trial results plus a Markov extrapolation) counts as **model-based** for items 16, 17 and 22, because "modelling is used".

## 3. Form of evaluation (R2, R3, R14)

| Form | Declared as / signals |
|---|---|
| Cost analysis (costs and cost offsets only) | "cost analysis", "cost comparison", "análisis de costos"; costs of ≥2 options, no outcome measure → items 11–13 Not applicable |
| Cost-effectiveness (CEA) | "cost-effectiveness", "costo-efectividad", "coste-efectividad"; cost per natural unit (event avoided, life-year) |
| Cost-utility (CUA) | "cost-utility", "costo-utilidad", "coste-utilidad"; cost per QALY / AVAC |
| Cost-minimisation | "cost-minimisation", "minimización de costos/costes" |
| Cost-benefit (CBA) | "cost-benefit", "benefit-cost", "costo-beneficio"; monetary valuation of health outcomes (R3: if labelled CBA without it, add a note) |
| Extended / distributional CEA | "extended cost-effectiveness", "distributional cost-effectiveness", equity weights, outcomes by income group |

## 4. The confirmation question and the header line

When the study type or the form is inferred (not given as an argument or declared), pause once before auditing:

```
Confirmation — study type inferred
Inferred: <model-based | empirical>; form: <form>.
Evidence: <n> model terms (e.g. "health states", "cycle length"), <n> empirical terms; form signal: "<quote>".
Consequence: items 16 and 22 <apply | Not applicable (R14)>; items 11–13 <apply | Not applicable (R14)>.
Continue with this, or correct it?
```

If the user has said "just do it" (or equivalent), do not pause: proceed and write the inference in the header.

Header line, one of four fixed bases:

```
Study type: model-based; form: cost-utility analysis — basis for selection: declared
Study type: empirical (non-modelling); form: cost-effectiveness analysis — basis for selection: inferred and confirmed
Study type: model-based; form: cost-utility analysis — basis for selection: inferred, user said proceed
Study type: empirical (non-modelling); form: cost analysis — basis for selection: argument
```

When inferred, add one sentence under the header with the vocabulary evidence (terms and counts).
