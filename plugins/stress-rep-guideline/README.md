# stress-rep-guideline

A Claude Code skill that audits the write-up of a simulation study against the **STRESS** reporting
guidelines (Strengthening The Reporting of Empirical Simulation Studies; Monks et al., 2019,
*Journal of Simulation* 13(1):55–67, [doi:10.1080/17477778.2018.1442155](https://doi.org/10.1080/17477778.2018.1442155)).

It picks the checklist that matches the model — STRESS-DES (discrete-event), STRESS-SD (system
dynamics), STRESS-ABS (agent-based), or a merged audit for hybrids — reads the main text and every
supplement as one document, and reports each of the 20 items as **Addressed**, **Partially addressed**,
**Missing**, or **Not applicable**, with the evidence quoted and located. Every item that needs work is
listed with the verbatim STRESS recommendation, so an author knows exactly what to add.

It checks **reporting completeness only**. It does not judge whether the model is valid, verified, or
calibrated, and it gives no score or pass/fail verdict, because STRESS defines none.

## Install

In Claude Code:

```text
/plugin marketplace add CarlosPiant/AI-assisted-tools
/plugin install stress-rep-guideline@ai-assisted-tools
```

**Requirements:** Python 3 for the bundled scripts. To read PDFs, either `pdftotext` (from poppler,
e.g. `brew install poppler`) or the `pypdf` Python package. Word files need `pandoc` or
`python-docx`; Markdown and text need nothing extra. Scanned PDFs without a text layer must be OCR'd
first.

## Use

Ask in plain language, in English or Spanish — "apply STRESS to `paper.pdf`", "is my agent-based model
reported completely?", "aplica la guía STRESS a `manuscrito.docx`" — or call it directly:

```text
/stress-rep-guideline writing/paper.pdf
/stress-rep-guideline writing/paper.docx writing/supplement.docx --model sd
/stress-rep-guideline manuscript.md appendix_A.md --model des,sd
```

| Input | Required | Notes |
|---|---|---|
| Main document | yes | `.pdf`, `.docx`, `.md`, or `.txt` |
| Supplements | no | Pass every file that belongs to the write-up; STRESS accepts evidence in supplements |
| `--model` | no | `des`, `sd`, `abs`, or a set such as `des,sd`. Omitted: the skill detects the paradigm and asks you to confirm when it had to infer it |
| `--output` | no | Default `quality_reports/stress_audit_<docname>.md` in your project |

**Output:** a Markdown report with a header (variant and how it was chosen, files audited, the
numbering note, scope, tally of the four states), one table per STRESS section, cross-reference
checks, the Not-applicable items with the rule that permits them, and a closing table of every Missing
or Partially addressed item with the verbatim recommendation. The chat reply summarises the same
items in checklist order.

If the document is not a DES, SD, or ABS model — a Monte Carlo risk analysis, a Markov cohort model, a
microsimulation, an optimisation-only study — the skill says so and stops instead of auditing against
the closest checklist.

## Example

From the evaluation run on a synthetic discrete-event study (`evals/fixtures/des_clinic.md`):

> Apply STRESS to evals/fixtures/des_clinic.md and tell me what is missing before I submit it.

```text
Variant applied: STRESS-DES — basis: declared (§ 1: "We built a discrete-event simulation (DES) model").
Tally (of 20 items): Addressed 17 | Partially addressed 1 | Missing 2 | Not applicable 0.

1. 4.1 Initialisation — Partially addressed. A 4-week warm-up is stated, but not "the analysis method
   used to select it". Add how 4 weeks was chosen (e.g. Welch's method or MSER-5).
2. 5.2 Random sampling — Missing. "State the algorithm used to generate random samples in the
   software/programming language used e.g. Mersenne Twister. If common random numbers are used,
   state how seeds (or random number streams) are distributed among sampling processes."
3. 6.1 Computer Model Sharing Statement — Missing. "Describe how someone could obtain the model
   described in the paper, the simulation software and any other associated software (or hardware)
   needed to reproduce the results. Provide, where possible, the link and DOIs to these."
```

## Evaluation

The skill was built with this repository's `skill-generator` and benchmarked on five synthetic
write-ups, each run once with the skill and once without it.

| Case | With skill | Without skill |
|---|---|---|
| DES, paradigm declared | 1.00 | 0.23 |
| SD, Spanish manuscript | 0.85 | 0.23 |
| ABS, request without the word "STRESS" | 0.92 | 0.25 |
| Hybrid DES + SD, inferred, with a supplement | 0.85 | 0.46 |
| Markov model (must refuse) | 1.00 | 0.50 |
| **Mean** | **0.92** | **0.33** |

Verdict: **ACCEPT** at the standard threshold of 0.80. All five failed expectations were the skill
rating a borderline item one notch *stricter* than the answer key, never more lenient. Each case ran
once, so the rates carry no repetition variance. The fixtures, answer keys, eval prompts, benchmark,
and full evaluation report are in [`evals/`](evals/).

## Provenance and licence

The method and all checklist text come from Monks et al. (2019) and its three supplementary checklists,
reproduced verbatim under **CC BY 4.0** — see [`NOTICE`](NOTICE). The paradigm-detection procedure, the
four item states and the tally are this skill's own additions and are labelled as such; details in
[`references/provenance.md`](skills/stress-rep-guideline/references/provenance.md).

Original work in this plugin: © 2026 Carlos Pineda, [PolyForm Noncommercial 1.0.0](LICENSE). Free for
research, teaching, and personal use.
