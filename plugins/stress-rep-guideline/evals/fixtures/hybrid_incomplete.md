SYNTHETIC TEST DOCUMENT — fictional study written for evaluating the stress-rep-guideline skill; not real research

# Patient flow and staff fatigue in the emergency department of St. Nowhere Hospital: a simulation model

E. Placeholder — Fictional Hospital Trust, Service Improvement Team (fictional)

## 1. Background and purpose

The emergency department (ED) of St. Nowhere Hospital (fictional) misses its 4-hour target on busy evenings. Staff believe that fatigue late in a shift slows treatment and that this, rather than demand alone, causes the breaches. We built a simulation model in which individual patients flow through triage, assessment and treatment while a continuously accumulating level of staff fatigue feeds back on treatment times. The purpose is to test that belief and to give the Trust a tool for shift-planning.

## 2. Outputs

The model reports the share of patients whose time in the ED exceeds 4 hours (%), the mean time in the ED (minutes), and the level of staff fatigue at the end of each simulated hour (fatigue points). The first two are computed from each patient's arrival and departure time stamps over the whole run; the third is read directly from the fatigue level.

## 3. Experiments

The model has so far been run only for the base case; no scenario experiments have been conducted.

## 4. Model description

Figure 1 gives an overview: patients arrive, queue for triage, are assigned a priority category, wait for assessment by a doctor, are treated, and then leave or are admitted. Alongside the patient flow, a single fatigue level for the nursing and medical staff accumulates while patients are being treated and recovers during idle time; the fatigue level multiplies the treatment time of every patient currently in treatment. Fatigue therefore creates a reinforcing loop on busy evenings: more patients → more fatigue → longer treatments → more patients waiting.

Patients are individual entities with attributes: arrival time, priority category (1–5) and disposition (discharge / admission). They pass through three activities — triage (nurse), assessment (doctor) and treatment (nurse and doctor) — in that order. The resources are 6 nurses and 3 doctors per shift. A bespoke triage priority algorithm assigns each patient to one of the five categories at triage. Patients enter the model from a time-varying hourly arrival profile derived from last year's attendances and leave the model after treatment (discharge) or after a bed request is placed (admission).

The fatigue part of the model has one level, *staff fatigue*, measured in fatigue points, with an inflow *fatigue accumulation* and an outflow *recovery*. Fatigue accumulation rises with the number of patients in treatment; recovery is proportional to the current fatigue level. No graphical (lookup) functions are used.

The two parts are coupled in both directions: every simulated hour the current value of the fatigue level is read and converted into a treatment-time multiplier (1.0 at zero fatigue, up to 1.4 at the maximum fatigue of 100 points) that is applied to all treatment activities starting in the next hour; in the other direction, the number of patients in treatment at the end of each hour is passed to the fatigue accumulation inflow.

## 5. Run length

Each run covers 7 simulated days starting at 08:00 on a Monday; the time unit is minutes.

## 6. Software

The model was built in AnyLogic 8.8 (Personal Learning Edition).

## 7. Preliminary results

In the base case 14 % of patients exceeded 4 hours; the share rose to 23 % between 18:00 and 23:00, when the fatigue level averaged 71 points. Further details of the inputs and the estimation procedure are given in the supplementary material.
