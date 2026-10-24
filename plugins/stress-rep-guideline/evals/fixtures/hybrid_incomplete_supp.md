SYNTHETIC TEST DOCUMENT — fictional study written for evaluating the stress-rep-guideline skill; not real research

# Supplementary material for "Patient flow and staff fatigue in the emergency department of St. Nowhere Hospital"

E. Placeholder — Fictional Hospital Trust (fictional)

## S1. Input parameters (base case)

| Parameter | Distribution / value | Use |
|---|---|---|
| Arrival rate by hour of day (patients/hour) | 08:00 6; 10:00 9; 12:00 11; 14:00 12; 16:00 13; 18:00 15; 20:00 13; 22:00 9; 00:00 5; 02:00 3; 04:00 3; 06:00 4 | arrival profile |
| Triage duration (minutes) | Triangular(min 3, mode 5, max 10) | triage activity |
| Assessment duration (minutes) | Lognormal(mu 3.0, sigma 0.5) | assessment activity |
| Base treatment duration (minutes) | Gamma(shape 3, scale 15) | treatment activity, before the fatigue multiplier |
| Priority category mix (1/2/3/4/5) | 0.03 / 0.12 / 0.40 / 0.35 / 0.10 | triage |
| Admission probability | 0.22 | disposition |
| Fatigue accumulation coefficient | 0.8 fatigue points per patient-hour in treatment | fatigue inflow |
| Recovery rate | 0.15 per hour | fatigue outflow |
| Maximum fatigue | 100 fatigue points | multiplier scaling |
| Initial fatigue | 0 fatigue points | — |

All parameters above are the base-case values; no other experiments have been run. Distributions were fitted to one year of ED time stamps (n = 61,400 attendances); the lognormal and gamma families were selected by lowest AIC among the exponential, gamma, lognormal and normal families.

## S2. Estimation approach

The model is stochastic. Thirty independent replications of the 7-day run were performed; the number was chosen so that the half-width of the 95 % confidence interval on the share of patients exceeding 4 hours was below 1.5 percentage points (reached at 24 replications). Common random numbers are used across future scenarios, with one random-number stream allocated to each activity (arrivals, triage, assessment, treatment).
