---
name: cheers-checklist
description: "Audits a health economic evaluation (PDF, Word, Markdown or text, plus supplements) against the 28-item CHEERS 2022 checklist (Husereau et al., Value Health 2022) using the verbatim Table 1 guidance: each item Addressed / Partially addressed / Missing / Not applicable with a quoted evidence locator, plus a paste-ready table of where each item is reported. Handles model-based, trial-based and cost analyses with CHEERS's own Not applicable rules; stops for cost-of-illness, burden or budget impact studies. Reporting completeness only; it adds no score, severity tier or pass/fail. Use when the user says 'apply CHEERS', 'CHEERS checklist', 'CHEERS 2022', 'check my economic evaluation against CHEERS', 'is my cost-effectiveness analysis reported completely', 'reporting checklist for my CEA', 'fill in the CHEERS checklist for submission', 'aplicar CHEERS', 'aplica CHEERS', 'lista de verificación CHEERS', '¿cumple mi evaluación económica con CHEERS?'. Not for methods appraisal (Drummond, CHEC)."
argument-hint: "[document-path ...] [--modelling yes|no] [--form full|cost-analysis] [--output quality_reports/cheers_checklist_<docname>.md]"
allowed-tools: ["Read", "Grep", "Glob", "Bash", "Write"]
effort: high
---

# /cheers-checklist — CHEERS 2022 reporting-completeness audit

Audit the report of a health economic evaluation against the Consolidated Health Economic Evaluation Reporting Standards 2022: Husereau D, Drummond M, Augustovski F, et al., on behalf of the CHEERS 2022 ISPOR Good Research Practices Task Force, *Value in Health* 2022;25(1):3–9, doi:10.1016/j.jval.2021.11.1351 (CC BY 4.0; Table 1 reproduced verbatim in `references/`), with its Appendix A (GRIPP2 short form) and Appendix B (Delphi protocol). The result is one report that says, for each of the 28 items, whether the document reports it, with the evidence quoted and located, and a submission table the author can paste.

**This skill audits reporting completeness only, not the quality of the study's conduct or the appropriateness of its methods.** CHEERS's use "should be limited to assessing the quality of reporting of a study rather than the quality of its conduct" (P4/J6), and the Statement "is not intended as a scoring tool or a tool to assess the appropriateness of methods" (P2/J4).

## Usage

```
/cheers-checklist writing/manuscript.pdf
/cheers-checklist manuscript.docx technical_appendix.docx
/cheers-checklist paper.md --modelling no --form cost-analysis
```

- `document-path ...` — main document first, then any supplements (`.pdf`, `.docx`, `.md`, `.txt`). CHEERS assumes information may sit in "online and supplementary appendices" (P5/J7), so pass every file that belongs to the report.
- `--modelling yes|no`, `--form full|cost-analysis` — skip detection when you already know the study type.
- `--output` — default `quality_reports/cheers_checklist_<docname>.md` in the current project. Never write outside the project.

## Files in this skill — open them when the step says so

| File | Open when |
|---|---|
| `references/study-type-detection.md` | Step 3 — scope gate (when to stop), model-based vs empirical, form, the confirmation question and header line |
| `references/cheers-checklist.md` | Step 5 — the 28 items verbatim, with each item's clauses, applicability and rule ids |
| `references/decision-rules.md` | Steps 3, 5, 6 — state definitions, rules R1–R36 (sources) and S1–S9 (skill), evidence standards, cross-checks |
| `references/report-template.md` | Step 7 — report layout, filling rules, verification |
| `scripts/extract_text.py` | Step 2 — inputs to one corpus with `[[file]]` and `[[page n]]` markers |
| `scripts/make_skeleton.py` | Step 4 (skeleton), step 7 (`--verify`); `--list` shows the items |
| `scripts/checklist.json` | Source of truth for all CHEERS text; read only if a reference file seems inconsistent |

## Workflow

### 1. Gather inputs

Confirm which files form the report (main text + supplements), the output path, and any `--modelling`/`--form` argument. If a file is missing or unreadable, stop and ask. If `quality_reports/cheers_checklist_<docname>.md` already exists, apply overwrite protection (ask, or write `_v2`).

### 2. Extract text

```
python3 "${CLAUDE_SKILL_DIR}/scripts/extract_text.py" <main> [<supplement> ...] --output <scratch>/cheers_corpus.txt
```

Read the whole corpus. If a PDF yields almost no text it is scanned — tell the user to OCR it and stop. Keep the `[[file: … | main document/supplement]]` and `[[page n]]` markers; every locator cites them.

### 3. Check scope, detect the study type, pause once

Open `references/study-type-detection.md`.

1. **Scope gate first.** CHEERS covers "comparative analyses of alternative courses of action in terms of their costs and consequences" (abstract, P1/J3), including comparative cost analyses (P2/J4–P4/J6). **Stop without auditing** when there is no comparison of alternatives (cost-of-illness, burden-of-disease, single-programme cost description), no costs (pure clinical study), or the study is a budget impact analysis or constrained optimisation (P4/J6). The stop message names the failing condition and quotes the sentence with its locator; write no report with item states.
2. **Study type:** argument → declaration ("Markov model", "decision tree", "trial-based", "junto a un ensayo clínico") → vocabulary inference. Model-based if any model is used, including a trial-based analysis extended by a model.
3. **Form:** cost analysis, CEA, CUA, cost-minimisation, CBA, extended/distributional CEA.

If the type or form was inferred, pause once and ask the user to confirm (template in the reference) with the evidence and its consequences for items 11–13, 16 and 22; continue after confirmation. If the user said "just do it", do not pause: proceed and write `basis for selection: inferred, user said proceed` plus one sentence of vocabulary evidence.

### 4. Render the skeleton

```
python3 "${CLAUDE_SKILL_DIR}/scripts/make_skeleton.py" --title "<document title>" --modelling <yes|no> --form <full|cost-analysis> --output <scratch>/cheers_skeleton.md
```

The skeleton carries every item's verbatim guidance, applicability and rule ids, pre-marks the R14 examples (16 and 22 for non-modelling, 11–13 for cost analyses), and contains the submission table. Do not retype guidance; audit against the skeleton text.

### 5. Audit item by item

For each of the 28 items, in Table 1 order:

1. **Applicability first** (`decision-rules.md` §2–4). Not applicable is allowed only (a) under R14's examples, or (b) for an item with conditional wording — 16, 17 per clause, 18, 21, 25, the second sentence of 24 — when the document explicitly says the activity was not undertaken (S2). Silence is **Missing** ("Not reported", R15). An author's "not applicable" on an item without conditional wording (e.g. 19) is not accepted: Missing, with the claim quoted.
2. **Search the whole corpus** — main text and every supplement — with Grep for the item's terms in English and Spanish, then read the passage. Tables and figures count.
3. **Decide clause by clause** using the clause list in `references/cheers-checklist.md`: Addressed = every applicable clause present; Partially addressed = some present (name the absent one); Missing = none. "Why chosen" / "why appropriate" / "reason chosen" are clauses. A literal "none" answer is Addressed: "no analysis plan was developed" (4), "not discounted because the horizon is 12 months" (10) (S3).
4. **Quote verbatim** in the document's language with a locator (`main paper.pdf, p. 6, Table 2` / `supplement appendix.docx, § A3`). Evidence standards (S6): a link to material not supplied → Partial, except the location clauses of 4 and 16; never judge whether a choice is appropriate (R8).

Engagement items: 21 and 25 are the patient/public involvement items (Appendix A). An explicit "no patients or public were involved" makes both Not applicable; engagement described in 21 makes 25 apply; silence makes both Missing.

### 6. Cross-checks

Fill the cross-check table (S7): 20 ↔ 24 (uncertainty methods vs their effect), 9/10 ↔ 24 (effect of discount rate and horizon "if applicable"), 21 ↔ 25, 16 ↔ 17 ↔ 22 (study type used consistently). Flag inconsistencies in the table; do not change states because of them.

### 7. Write and verify the report

Complete the skeleton following `references/report-template.md` and save it to `quality_reports/cheers_checklist_<docname>.md` (project root; create `quality_reports/` if needed). The header states the study type, form and basis; files audited; the interpretation note (the Explanation and Elaboration report was not available, P4/J6); the scope sentence; the tally — plain counts of the four states over 28 items. Then:

- **N/A section:** each N/A item with its rule and the document's justification quote or "no justification given".
- **Missing/Partial section:** each item with the verbatim guidance, its Table 1 locator, and the absent clause.
- **Submission checklist table:** item topic, number, "Reported in section" (document location; "Not applicable"; or "Not reported"), state. Never use the label "Not conducted" — CHEERS asks users to avoid it (P4/J6).

Run `python3 "${CLAUDE_SKILL_DIR}/scripts/make_skeleton.py" --verify <report>` and fix every ERROR before handing over.

### 8. Summarise to the user

In chat: study type, form and basis; the tally; the Missing and Partially addressed items in item order, each with the verbatim CHEERS wording of what to add; justified and unjustified N/A claims; cross-check flags; the report path. Prose and labels in English; quotes in the source language; CHEERS guidance in English (the skill does not translate the checklist, P5/J7).

## Verification before handing over

- `--verify` reports OK: 28 rows, valid states, tally matches, submission table has 28 matching rows, no placeholders, no "Not conducted" label.
- Every Addressed / Partially addressed row has a verbatim quote and a locator.
- Every Not applicable row cites R14 or S2 and says whether the document justifies it.
- No guidance text altered or translated; no score, percentage, tier, ranking or pass/fail; nothing written outside the project.

## Examples

**Model-based CUA, declared.** "Apply CHEERS to writing/cua_manuscript.pdf." → corpus (14 pages); "Markov model" declared on p. 4 → model-based CUA, basis: declared → audit: 4 Missing (no statement on an analysis plan), 16 Partially addressed ("A four-state Markov model … was chosen because …" but no statement whether the model is publicly available), 19 Missing → report with the submission table; chat lists the three items with the verbatim guidance.

**Trial-based CEA in Spanish.** "Aplica CHEERS a manuscrito.docx." → "evaluación económica junto a un ensayo clínico aleatorizado" declared → empirical CEA → 16 and 22 Not applicable (R14, non-modelling) → 15 Partially addressed: "Los costos se expresan en euros" but no price year → report in English, quotes in Spanish.

**Cost-of-illness study.** "CHEERS checklist for burden_paper.pdf." → total annual costs of a disease, no alternative compared → stop: quote "Health economic evaluations are comparative analyses of alternative courses of action in terms of their costs and consequences" (abstract, P1/J3); no audit.

## Troubleshooting

- **Scanned PDF** — ask for OCR or the Word source; stop.
- **Model and trial both present** — model-based for 16, 17 and 22 (modelling is used).
- **CEA with a budget impact section** — audit the CEA; note in the header that the budget impact part is outside CHEERS (P4/J6).
- **Document cites "CHEERS 2013"** — audit against 2022 and add the header note that 2022 replaces 2013 (P4/J6).
- **Author's own CHEERS table disagrees with the text** — audit the text; mention the disagreement in the item row.
- **Reference files disagree** — `scripts/checklist.json` is the source of truth; regenerate with `make_skeleton.py --render-reference --output references/cheers-checklist.md`.

## Provenance

Husereau et al. (2022) doi:10.1016/j.jval.2021.11.1351 (Open Access, CC BY 4.0), Table 1 (P3–P4/J5–J6), § Scope and § How to use CHEERS (P2–P4/J4–J6), Box 1 (P5/J7); Appendix A `1-s2.0-S1098301521031466-mmc1.docx`; Appendix B `1-s2.0-S1098301521031466-mmc2.docx`. Not used: the CHEERS 2022 Explanation and Elaboration report (not supplied). Source table, licence, where the source is silent, scope decisions and judgment calls: `references/provenance.md`.
