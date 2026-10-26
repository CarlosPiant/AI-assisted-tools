SYNTHETIC TEST DOCUMENT — fictional study written for evaluating the cheers-checklist skill; not real research

# Cost-utility analysis of renoprotan versus standard care for adults with stage 3 chronic kidney disease in Freedonia: a Markov model-based economic evaluation

A. Placeholder, B. Imaginary and C. Notreal — Institute of Fictional Health Economics, University of Freedonia (fictional)

## Abstract

**Objectives.** To estimate the cost-effectiveness of adding renoprotan (a fictional oral renoprotective drug) to standard care, compared with standard care alone, for adults with stage 3 chronic kidney disease (CKD) in Freedonia.

**Methods.** A cohort Markov model with four health states (CKD stage 3, CKD stage 4, CKD stage 5/dialysis, death) and annual cycles was populated with efficacy and utility data from the RENO-1 trial (fictional) and national cost data. The analysis takes the Freedonian health-care payer perspective over a lifetime horizon, discounting costs and outcomes at 3 % per year. Outcomes are quality-adjusted life years (QALYs) and incremental cost-effectiveness ratios (ICERs).

**Results.** Renoprotan added 0.39 QALYs at an additional cost of F$ 8,300 per patient, giving an ICER of F$ 21,300 per QALY gained.

**Alternative analyses.** In probabilistic sensitivity analysis renoprotan had a 71 % probability of being cost-effective at a threshold of F$ 30,000 per QALY. Results were most sensitive to the hazard ratio for progression and the drug price; the ICER rose to F$ 48,500 per QALY with a 10-year horizon.

**Conclusions.** Renoprotan is likely to be cost-effective for stage 3 CKD in Freedonia at the threshold used by the national reimbursement agency.

## 1. Introduction

Chronic kidney disease affects an estimated 9 % of Freedonian adults (fictional figure), and progression to dialysis accounts for a growing share of the national health-insurance budget. Renoprotan slowed the decline of kidney function in the RENO-1 trial, but its list price is high. The Freedonian Health Technology Agency (FHTA, fictional) must decide in 2025 whether to reimburse renoprotan for stage 3 CKD. The study question is: what is the incremental cost per QALY gained of adding renoprotan to standard care, compared with standard care alone, for adults with stage 3 CKD in Freedonia? The answer is intended to inform that reimbursement decision.

## 2. Methods

### 2.1 Study population

The modelled cohort mirrors the RENO-1 trial population: adults aged 40 to 80 years (mean 63 years), 52 % men, with an estimated glomerular filtration rate of 30–59 mL/min/1.73 m²; 38 % had type 2 diabetes and 71 % hypertension. Household income was not recorded in the trial.

### 2.2 Setting and location

Freedonia has a single national health-insurance scheme that covers outpatient nephrology, medicines and dialysis without co-payment. Haemodialysis is delivered in 42 hospital units; home dialysis is uncommon (6 % of dialysis patients). Because dialysis is fully reimbursed and expensive, delaying progression has a large effect on payer costs in this setting.

### 2.3 Comparators

We compared (i) renoprotan 10 mg once daily added to standard care with (ii) standard care alone. Standard care is an angiotensin-converting-enzyme inhibitor or angiotensin-receptor blocker titrated to the maximum tolerated dose, as recommended by the Freedonian Nephrology Guideline 2022 (fictional). Standard care was chosen as the comparator because it is current practice for all patients who would be eligible for renoprotan; no other renoprotective drug is reimbursed in Freedonia.

### 2.4 Perspective

The analysis adopts the Freedonian health-care payer perspective, including all costs borne by the national health-insurance scheme. This perspective was chosen because it is the reference case required by the FHTA methods guide (fictional).

### 2.5 Time horizon

A lifetime horizon (until age 100) was used because CKD is a chronic, progressive condition and the effect of renoprotan on progression and dialysis costs accrues over decades.

### 2.6 Discount rate

Costs and QALYs were discounted at 3 % per year, the rate set in the FHTA methods guide for all submissions.

### 2.7 Selection of outcomes

The measure of benefit was the QALY. Harms were included as outcomes: genital mycotic infections and episodes of acute kidney injury, each with its own cost and QALY decrement.

### 2.8 Measurement of outcomes

Health-related quality of life was measured with the EQ-5D-5L questionnaire, completed by RENO-1 participants at baseline and at 6, 12 and 24 months; mean values were calculated per CKD stage. Progression events and adverse events were recorded by trial investigators at each visit and adjudicated by a blinded committee.

### 2.9 Valuation of outcomes

EQ-5D-5L responses were valued with the Freedonian EQ-5D-5L value set, elicited with composite time trade-off from a representative sample of 1,000 adults of the Freedonian general population (fictional). QALYs were calculated as the sum of utility-weighted life years.

### 2.10 Measurement and valuation of resources and costs

Resource use per health state (nephrology visits, laboratory tests, hospital admissions, dialysis sessions) was taken from the Freedonian Renal Registry (fictional) for 2022–2023. Unit costs were valued with the 2024 national tariff of the health-insurance scheme; the renoprotan price is the 2024 list price. Adverse-event costs were valued as one outpatient visit (mycotic infection) or one hospital admission (acute kidney injury).

### 2.11 Currency, price date and conversion

All costs are in Freedonian dollars (F$) at 2024 prices. Resource quantities date from 2022–2023 (registry) and unit costs from the 2024 tariff; registry costs recorded in 2022 and 2023 prices were inflated to 2024 with the national health-care price index. No currency conversion was required.

### 2.12 Model structure

We built a cohort Markov model with four health states — CKD stage 3, CKD stage 4, CKD stage 5/dialysis and death — and annual cycles with half-cycle correction (Figure 1). Patients start in stage 3 and may progress one stage per cycle or die from any state; death is absorbing. Renoprotan reduces the transition probabilities from stage 3 to 4 and from stage 4 to 5 by the hazard ratios estimated in RENO-1. A Markov model was used because CKD progression is a sequence of irreversible stages with recurring stage-specific costs and utilities that must be extrapolated far beyond the 3-year trial follow-up.

### 2.13 Analytics and assumptions

Annual progression rates from RENO-1 were converted to annual transition probabilities using p = 1 − exp(−r·t). Beyond the 3-year trial follow-up, transition probabilities were extrapolated assuming constant hazards; a scenario assumed that the treatment effect wanes linearly to zero between years 10 and 20. Background mortality comes from Freedonian life tables, with stage-specific mortality multipliers from the registry. The model was validated in three ways: face validity was reviewed by two nephrologists; predicted 10-year dialysis incidence was compared with registry data (cross-validation); and the model was programmed independently twice (in R and in a spreadsheet) and the outputs compared (verification).

### 2.14 Characterizing heterogeneity

Results were estimated separately for patients with and without type 2 diabetes, using the subgroup hazard ratios reported by RENO-1.

### 2.15 Characterizing uncertainty

Parameter uncertainty was explored with one-way deterministic sensitivity analyses (each parameter varied over its 95 % confidence interval or ±20 % when no interval was available) and with a probabilistic sensitivity analysis of 5,000 iterations (beta distributions for probabilities and utilities, gamma for costs, lognormal for hazard ratios). Structural and methodological uncertainty was explored with scenarios: discount rates of 0 % and 5 %; time horizons of 10 and 20 years; and the treatment-effect waning scenario.

### 2.16 Engagement with patients and others

Two patient partners living with CKD (members of the Freedonian Kidney Patients' Association, fictional) and one representative of the health-insurance scheme took part in two workshops during the design of the study. They reviewed the proposed model structure, the list of cost items and the adverse events to be included.

## 3. Results

### 3.1 Study parameters

Table 2 lists every model input with its base-case value, range or 95 % confidence interval, the distribution used in the probabilistic analysis and its source.

| Parameter | Base case | Range / 95 % CI | Distribution | Source |
|---|---|---|---|---|
| Annual probability stage 3 → 4, standard care | 0.062 | 0.051–0.074 | Beta | RENO-1 control arm |
| Annual probability stage 4 → 5, standard care | 0.118 | 0.097–0.141 | Beta | RENO-1 control arm |
| Hazard ratio of progression, renoprotan | 0.68 | 0.57–0.81 | Lognormal | RENO-1 |
| Utility, stage 3 / stage 4 / stage 5 | 0.81 / 0.74 / 0.58 | ±0.03 / ±0.04 / ±0.05 | Beta | RENO-1 EQ-5D-5L |
| Annual cost, stage 3 / stage 4 (F$) | 2,400 / 5,100 | ±20 % | Gamma | Renal Registry, 2024 tariff |
| Annual cost, stage 5 / dialysis (F$) | 61,800 | 52,000–72,000 | Gamma | Renal Registry, 2024 tariff |
| Renoprotan annual drug cost (F$) | 1,950 | fixed | — | 2024 list price |
| Probability of mycotic infection per year, renoprotan | 0.031 | 0.022–0.041 | Beta | RENO-1 |
| QALY decrement per acute kidney injury | 0.02 | 0.01–0.03 | Beta | RENO-1 |

### 3.2 Base-case results

Mean discounted costs per patient were F$ 148,200 with renoprotan and F$ 139,900 with standard care; mean discounted QALYs were 9.41 and 9.02. The incremental cost of F$ 8,300 and incremental 0.39 QALYs give an ICER of F$ 21,300 per QALY gained. Drug costs (F$ +24,600) were partly offset by lower dialysis costs (F$ −17,400). In the subgroup with diabetes the ICER was F$ 17,800 per QALY, and in the subgroup without diabetes F$ 26,900 per QALY.

### 3.3 Effect of uncertainty

The tornado diagram (Figure 2) shows that the ICER is most sensitive to the hazard ratio of progression and the renoprotan price. In the probabilistic analysis renoprotan was cost-effective in 71 % of iterations at F$ 30,000 per QALY (Figure 3). With discount rates of 0 % and 5 % the ICER was F$ 16,900 and F$ 25,800 per QALY; with time horizons of 10 and 20 years it was F$ 48,500 and F$ 29,400 per QALY; with waning of the treatment effect it was F$ 27,200 per QALY.

### 3.4 Effect of engagement with patients and others

The patient partners asked for travel to dialysis units to be costed; transport costs were therefore added to the dialysis state, which lowered the ICER by F$ 600 per QALY. At their request a scenario that includes caregiver time was also reported (ICER F$ 19,700 per QALY).

## 4. Discussion

Adding renoprotan to standard care gained 0.39 QALYs at an ICER of F$ 21,300 per QALY, below the FHTA's reference threshold, and the conclusion held in most sensitivity analyses except a 10-year horizon. The main limitations are the 3-year trial follow-up, which makes the lifetime results depend on the constant-hazard extrapolation, and the absence of head-to-head data against other renoprotective drugs not yet available in Freedonia. Ethical and equity considerations, such as whether access to the drug would differ by region or income, were not captured by the analysis; these could affect which patients benefit and should be weighed by the FHTA alongside the ICER. For practice, the results suggest prioritising patients with diabetes, in whom the ICER is lowest. Our findings are consistent with the two published evaluations of similar drugs in other countries.

## 5. Funding

This study was funded by the Freedonian Health Technology Agency (grant FHTA-2024-17, fictional). The funder had no role in the identification, design, conduct or reporting of the analysis.

## 6. Conflicts of interest

All authors completed the International Committee of Medical Journal Editors (ICMJE) disclosure form. B. Imaginary reports consulting fees from Fictional Pharma Ltd outside the submitted work; the other authors declare no conflicts of interest.
