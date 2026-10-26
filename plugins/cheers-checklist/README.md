# cheers-checklist

A Claude Code skill that audits the report of a health economic evaluation against the **CHEERS 2022**
checklist (Consolidated Health Economic Evaluation Reporting Standards; Husereau et al., 2022,
*Value in Health* 25(1):3–9, [doi:10.1016/j.jval.2021.11.1351](https://doi.org/10.1016/j.jval.2021.11.1351)).

It reads the main text and every supplement or technical appendix as one document and reports each of
the 28 items as **Addressed**, **Partially addressed**, **Missing**, or **Not applicable**, with the
evidence quoted and located. Every item that needs work is listed with the verbatim CHEERS guidance, and
the report ends with a paste-ready table of where each item is reported, the form journals ask for at
submission.

It follows CHEERS's own rules for items that do not apply: items 11–13 for cost analyses, items 16 and
22 for studies without a model. It checks **reporting completeness only**. It does not judge whether
the methods are appropriate, and it gives no score, severity tier, or pass/fail verdict, because CHEERS
says it "is not intended as a scoring tool" and that scoring "is strongly discouraged".

## Install

In Claude Code:

```text
/plugin marketplace add CarlosPiant/AI-assisted-tools
/plugin install cheers-checklist@ai-assisted-tools
```

**Requirements:** Python 3 for the bundled scripts. To read PDFs, either `pdftotext` (from poppler,
e.g. `brew install poppler`) or the `pypdf` Python package. Word files need `pandoc` or
`python-docx`; Markdown and text need nothing extra. Scanned PDFs without a text layer must be OCR'd
first.

## Use

Ask in plain language, in English or Spanish — "apply CHEERS to `paper.pdf`", "is my cost-effectiveness
analysis reported completely?", "aplica CHEERS a `manuscrito.docx`" — or call it directly:

```text
/cheers-checklist writing/paper.pdf
/cheers-checklist writing/paper.docx writing/technical_appendix.docx
/cheers-checklist manuscript.md --modelling no --form cost-analysis
```

| Input | Required | Notes |
|---|---|---|
| Main document | yes | `.pdf`, `.docx`, `.md`, or `.txt` |
| Supplements | no | Pass every appendix that belongs to the report; CHEERS counts information in online appendices |
| `--modelling` | no | `yes` or `no`. Omitted: the skill reads the study type from the document and asks you to confirm when it had to infer it |
| `--form` | no | `full` or `cost-analysis` |
| `--output` | no | Default `quality_reports/cheers_checklist_<docname>.md` in your project |

**Output:** a Markdown report with a header (study type and form and how they were chosen, files
audited, scope, tally of the four states), one table per CHEERS section, cross-checks between related
items, the Not-applicable items with the rule that permits them, a closing table of every Missing or
Partially addressed item with the verbatim guidance, and the submission checklist table. The chat
reply summarises what to add, in item order.

If the document is not a health economic evaluation in the CHEERS sense — a cost-of-illness or burden
study with no comparator, a budget impact analysis, a pure clinical study — the skill says so, quotes
the CHEERS definition, and stops.

## Example

From the evaluation run on a synthetic trial-based study written in Spanish (`evals/fixtures/cea_ensayo_es.md`):

> Aplica CHEERS a evals/fixtures/cea_ensayo_es.md y prepárame la tabla de verificación para enviarla a la revista.

```text
Study type: empirical (non-modelling), trial-based. Form: cost-effectiveness analysis. Basis: declared
(§ 2.1: "No se utilizó ningún modelo de decisión").
Tally (of 28 items): Addressed 22 | Partially addressed 3 | Missing 1 | Not applicable 2.

- 8 Perspective — Partially addressed. CHEERS: "State the perspective(s) adopted by the study and why
  chosen." § 2.5 states only the perspective; add the reason for choosing it.
- 15 Currency, price date, and conversion — Partially addressed. § 2.12 gives the currency only; add the
  price year, the period of resource use, and the conversion year or a statement that none was needed.
- 23 Summary of main results — Partially addressed. No mean costs by main category (a strict reading).
- 28 Conflicts of interest — Missing.
Not applicable: items 16 and 22, because the study used no model, as the document itself states.
```

## Evaluation

The skill was built with this repository's `skill-generator` and benchmarked on five synthetic
write-ups, each run once with the skill and once without it.

| Case | With skill | Without skill |
|---|---|---|
| Model-based cost-utility, study type declared | 0.85 | 0.23 |
| Trial-based CEA, Spanish manuscript | 0.85 | 0.31 |
| Request without the word "CHEERS" | 0.83 | 0.33 |
| Study type inferred, with a technical appendix | 0.83 | 0.67 |
| Cost-of-illness study (must refuse) | 1.00 | 0.33 |
| **Mean** | **0.87** | **0.37** |

Verdict: **ACCEPT** at the standard threshold of 0.80 (expectation-weighted 48/56 with the skill, 21/56
without). Seven of the eight failed expectations were the skill rating a borderline item one notch
*stricter* than the answer key, each naming a gap that exists in the test document; the eighth was
citing an internal rule id where the CHEERS sentence was expected. Each case ran once, so the rates
carry no repetition variance. The fixtures, answer keys, eval prompts, benchmark, and full evaluation
report are in [`evals/`](evals/). The published skill differs from the benchmarked one only by wording
edits for publication, listed at the top of the evaluation report.

**Known limitation:** the CHEERS 2022 Explanation and Elaboration report, which gives per-item examples,
was not used. Items are judged against the Table 1 guidance alone, and every report says so.

## Provenance and licence

The checklist text comes from the CHEERS 2022 Statement, reproduced verbatim under **CC BY 4.0** —
see [`NOTICE`](NOTICE). The study-type detection, the four item states, the clause-by-clause reading
and the tally are this skill's own additions and are labelled as such; details in
[`references/provenance.md`](skills/cheers-checklist/references/provenance.md).

Original work in this plugin: © 2026 Carlos Pineda, [PolyForm Noncommercial 1.0.0](LICENSE). Free for
research, teaching, and personal use.
