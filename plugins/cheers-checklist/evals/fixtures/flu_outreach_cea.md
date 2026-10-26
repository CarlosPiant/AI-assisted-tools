SYNTHETIC TEST DOCUMENT — fictional study written for evaluating the cheers-checklist skill; not real research

# Pharmacist-led outreach versus invitation letters to increase influenza vaccination in adults aged 65 and over: a cost-effectiveness analysis

G. Madeup and H. Pretend — Centre for Imaginary Public Health Economics, Northshire (fictional)

## Abstract

**Background.** Influenza vaccination uptake among adults aged 65 and over in Northshire (fictional) is 58 %, below the regional target of 75 %.

**Methods.** A decision-analytic model (decision tree over one influenza season, with lifetime QALY losses for influenza deaths) compared community-pharmacist telephone outreach with the current invitation letters, from the perspective of the Northshire health service.

**Results.** Outreach increased uptake by 9 percentage points at an incremental cost of N$ 4.10 per person invited and gained 0.00031 QALYs per person, an incremental cost-effectiveness ratio (ICER) of N$ 13,200 per QALY.

**Sensitivity analyses.** The probability that outreach is cost-effective at N$ 20,000 per QALY was 82 %; results were most sensitive to the uptake effect and to vaccine effectiveness.

**Conclusion.** Pharmacist-led outreach is likely to be cost-effective in Northshire.

## 1. Introduction

Each winter influenza causes about 2,300 hospital admissions and 310 deaths among Northshire residents aged 65 and over (fictional surveillance data). The regional public-health board currently sends one invitation letter per season and must decide by June 2025 whether to commission an outreach service in which community pharmacists telephone unvaccinated older adults. The study question is: what is the incremental cost per QALY gained of pharmacist-led telephone outreach compared with invitation letters alone? The answer will inform the board's commissioning decision.

## 2. Methods

### 2.1 Health economic analysis plan

No health economic analysis plan was prepared for this study.

### 2.2 Population

The population is all community-dwelling adults aged 65 and over registered with a Northshire general practice in the 2023–24 season (n = 412,000; 55 % women; 41 % aged 75 or over; 23 % with a chronic respiratory or cardiac condition).

### 2.3 Setting and location

Northshire is a fictional region with a tax-funded health service. Vaccines are free at general practices and pharmacies; 92 % of older adults live within 2 km of a community pharmacy, which makes telephone outreach followed by a pharmacy appointment feasible.

### 2.4 Comparators

Strategy A (current practice): one invitation letter from the general practice in September. Strategy B: the same letter plus up to two telephone calls from a community pharmacist to every person not vaccinated by 15 October. Letters were chosen as the comparator because they are the current practice; outreach was chosen because a 2023 pilot in two towns increased uptake.

### 2.5 Perspective

The Northshire health-service perspective was adopted because the public-health board, which pays for the outreach and for influenza-related care, is the decision maker.

### 2.6 Time horizon

Costs and events were counted over one influenza season (September to April), because vaccination protects for a single season; QALYs lost from influenza deaths were counted over the remaining lifetime of those who died, because death removes all future quality-adjusted life.

### 2.7 Discount rate

Future QALYs lost from deaths were discounted at 3.5 % per year, the rate in the national public-health appraisal guidance; costs fall within one season and were not discounted.

### 2.8 Outcomes

The measure of benefit is the QALY. Health outcomes counted were influenza-like illness, hospital admission and death. Harms were vaccine adverse events (injection-site reactions and, rarely, Guillain–Barré syndrome).

### 2.9 Measurement of outcomes

Vaccination uptake was measured from the regional immunisation register in the two pilot towns and four matched control towns. Influenza illness, admissions and deaths among unvaccinated and vaccinated people come from the regional surveillance system. Quality-of-life losses for influenza illness and admission were measured with the EQ-5D-3L in a published cohort of older adults with laboratory-confirmed influenza (Fictional et al. 2021).

### 2.10 Valuation of outcomes

EQ-5D-3L health states were valued with the national time trade-off value set, elicited from a general-population sample of 3,395 adults. QALYs lost from death were the discounted quality-adjusted life expectancy at the age of death, from life tables combined with age-specific population utility norms.

### 2.11 Costs

Outreach costs (pharmacist time at the pharmacist hourly wage, telephone costs, training, administration) were measured in the pilot. Vaccine purchase and administration fees, general practice visits and hospital admissions were valued with the 2024 regional tariff.

### 2.12 Currency and price date

Costs are in Northshire dollars (N$) at 2024 prices; pilot resource use was recorded in the 2023–24 season. No currency conversion was needed.

### 2.13 Model

The model is a decision tree (Figure 1). Each simulated person is vaccinated or not (probabilities by strategy); then has influenza-like illness or not; ill people are treated in the community or admitted; admitted people survive or die. A decision tree was chosen because all effects of a seasonal vaccination occur within one season and there are no recurring health states to track. The model was programmed in R 4.3; the code and input files are publicly available at https://example.org/flu-outreach-model (fictional repository).

### 2.14 Analytics and assumptions

The uptake effect of outreach (+9 percentage points) was estimated by a difference-in-differences comparison of pilot and control towns. Probabilities of illness, admission and death were derived from surveillance rates per 100,000. No extrapolation beyond the season was needed except the life-expectancy calculation for deaths, which uses national life tables. The model was validated by checking face validity with two public-health physicians and by comparing the predicted number of admissions under current practice with the observed 2023–24 count (predicted 2,260; observed 2,310).

### 2.15 Subgroups

Results were estimated separately for people aged 65–74 and 75 and over.

### 2.16 Distributional effects

Not applicable to this analysis.

### 2.17 Uncertainty

One-way sensitivity analyses varied each parameter over its 95 % confidence interval. A probabilistic sensitivity analysis drew 10,000 parameter sets (beta for probabilities and utilities, gamma for costs, normal for the uptake effect). Scenario analyses used discount rates of 0 % and 5 % for QALYs lost from deaths, and vaccine effectiveness from a low-match season.

### 2.18 Patient and public involvement

No patients, members of the public or other stakeholders were involved in the design of this study.

## 3. Results

### 3.1 Parameters

| Parameter | Base case | 95 % CI / range | Distribution | Source |
|---|---|---|---|---|
| Uptake, letters | 0.58 | 0.57–0.59 | Beta | Immunisation register |
| Uptake effect of outreach (percentage points) | 9.0 | 6.1–11.9 | Normal | Pilot difference-in-differences |
| Vaccine effectiveness against admission | 0.40 | 0.28–0.51 | Beta | Regional surveillance |
| Seasonal influenza-like illness, unvaccinated | 0.081 | 0.070–0.093 | Beta | Regional surveillance |
| Admission given illness, unvaccinated | 0.069 | 0.058–0.081 | Beta | Regional surveillance |
| Death given admission | 0.135 | 0.118–0.153 | Beta | Regional surveillance |
| QALY loss per community illness / admission | 0.006 / 0.021 | ±25 % | Beta | Fictional et al. 2021 |
| Outreach cost per person invited (N$) | 3.20 | 2.60–3.90 | Gamma | Pilot |
| Vaccine and administration (N$) | 21.50 | fixed | — | 2024 tariff |
| Admission cost (N$) | 6,850 | 5,900–7,900 | Gamma | 2024 tariff |

### 3.2 Main results

Per person invited, mean costs were N$ 18.60 with letters and N$ 22.70 with outreach (incremental N$ 4.10), and mean QALY losses were 0.00412 and 0.00381 (0.00031 QALYs gained). The ICER was N$ 13,200 per QALY gained; outreach averted an estimated 61 admissions and 8 deaths per season in the region. The ICER was N$ 9,800 per QALY in people aged 75 and over and N$ 24,100 in people aged 65–74.

### 3.3 Effect of uncertainty

The tornado diagram (Figure 2) shows the ICER is most sensitive to the uptake effect and to vaccine effectiveness. Outreach was cost-effective at N$ 20,000 per QALY in 82 % of probabilistic iterations (Figure 3). With discount rates of 0 % and 5 % the ICER was N$ 11,900 and N$ 14,000 per QALY; in a low-match season it was N$ 21,600.

## 4. Discussion

Pharmacist-led outreach is likely to be cost-effective for adults aged 65 and over in Northshire, particularly for those aged 75 and over. The main limitations are that the uptake effect comes from a non-randomised pilot in two towns and that indirect protection of other age groups was not modelled, which makes the results conservative. If the board commissions the service, monitoring uptake in the first season would reduce the main uncertainty. Our results agree with two published evaluations of reminder-based interventions.

## 5. Funding

Funded by the Northshire Public Health Research Fund (fictional). The funder had no role in the identification, design, conduct or reporting of the analysis.

## 6. Competing interests

All authors completed the ICMJE uniform disclosure form and declare no competing interests.
