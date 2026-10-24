# Anti-Hallucination Checklist

Apply these checks to the design brief's extraction table and to the finished skill. They were written for academic sources but apply to any document a skill is built from.

Seven failure modes that target the most dangerous forms of AI-generated misinformation in academic writing. These are dangerous because they *sound* authoritative and pass casual review.

## The 7 Failure Modes

### AH-1: Fabricated Citations

**What it is:** Citing papers that don't exist, or combining real author names with wrong titles/venues/years.

**Detection patterns:**
- Author name exists but didn't publish in that venue/year
- Title sounds plausible but returns no results in Google Scholar / Semantic Scholar
- Journal name is slightly wrong (e.g., "Journal of Health Economics" vs "Health Economics")
- Co-author combinations that never collaborated

**Severity:** CRITICAL — undermines the entire evidence base.

### AH-2: Statistical Hallucinations

**What it is:** Precise-sounding numbers that are wrong — wrong magnitude, sign, units, or entirely fabricated statistics attributed to real sources.

**Detection patterns:**
- Odds ratio reported as relative risk (magnitude difference)
- Wrong sign on effect (protective factor reported as risk factor)
- Unit confusion (% vs proportion, per 1,000 vs per 100,000)
- Specific p-values or CIs that don't match the source
- Round-number estimates where the source reports non-round values

**Severity:** CRITICAL — can reverse conclusions.

### AH-3: Methodology Misattribution

**What it is:** Attributing a method, estimator, or technique to the wrong paper or author.

**Detection patterns:**
- Common confusion pairs: Callaway & Sant'Anna vs Sun & Abraham vs de Chaisemartin & D'Haultfœuille
- Describing a weighting estimator as a DR estimator (or vice versa)
- Attributing an assumption to the wrong theorem/paper
- Confusing the contributions of papers in the same literature

**Severity:** HIGH — misrepresents intellectual lineage.

### AH-4: Temporal Anachronisms

**What it is:** Citing results or methods that didn't exist at the claimed date, or wrong publication years.

**Detection patterns:**
- Method cited as "established" before its publication
- Working paper cited with a publication year it hadn't reached yet
- Dataset version cited that didn't exist in the stated time window
- Priority claims that are incorrect (X preceded Y, but actually Y came first)

**Severity:** HIGH — undermines chronological accuracy.

### AH-5: False Consensus Claims

**What it is:** Overstating agreement when the literature is actually divided.

**Detection patterns:**
- Phrases: "it is well-established," "the literature agrees," "there is consensus," "it is widely accepted"
- Citing only one side of a debate
- Ignoring prominent contradictory findings
- "Seminal" or "landmark" applied to contested contributions

**Severity:** HIGH — can mislead readers about the state of knowledge.

### AH-6: Phantom Datasets

**What it is:** Referencing datasets that don't exist, or claiming real datasets have variables/years they lack.

**Detection patterns:**
- Survey name exists but variable name is fabricated
- Dataset claimed to cover years outside its actual range
- Sample sizes that don't match known dataset dimensions
- Administrative data claimed to contain variables it doesn't collect

**Severity:** HIGH — invalidates data-dependent claims.

### AH-7: Ghost Authorship

**What it is:** Attributing ideas, quotes, or frameworks to the wrong researchers.

**Detection patterns:**
- Famous quote attributed to wrong person
- Framework (e.g., "Donabedian's structure-process-outcome") attributed to someone else
- Conflating contributions of first author vs co-authors
- Attributing a finding to a review paper rather than the original study

**Severity:** MEDIUM — misrepresents intellectual history.


## Quick Reference Card

For copy-paste into prompts:

```
Before presenting any text with factual claims, self-check for these 7 failure modes:
1. FABRICATED CITATIONS — Does every cited paper actually exist with that author/year/venue/title?
2. STATISTICAL HALLUCINATIONS — Are all numbers correct in magnitude, sign, and units?
3. METHODOLOGY MISATTRIBUTION — Is each method attributed to the right author/paper?
4. TEMPORAL ANACHRONISMS — Did this method/data/result exist at the claimed date?
5. FALSE CONSENSUS — Am I overstating agreement? Are there dissenting views I'm ignoring?
6. PHANTOM DATASETS — Does this dataset actually contain these variables/years/populations?
7. GHOST AUTHORSHIP — Am I attributing this idea/quote/framework to the right person?
```

