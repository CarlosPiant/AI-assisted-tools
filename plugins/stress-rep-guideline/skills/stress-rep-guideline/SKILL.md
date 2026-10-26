---
name: stress-rep-guideline
description: "Audits a simulation-study write-up (PDF, Word, Markdown or text, plus supplements) against the 20-item STRESS checklist (Monks et al. 2019), choosing STRESS-DES, STRESS-SD or STRESS-ABS by model type (discrete-event, system dynamics, agent-based; hybrids get a merged audit), and reports each item as Addressed / Partially addressed / Missing / Not applicable with a quoted evidence locator. Reporting completeness only, not model validity. Use when the user says 'apply STRESS', 'STRESS checklist', 'STRESS guidelines', 'run the STRESS test', 'check my simulation paper against STRESS', 'is my DES / SD / ABS model reported completely', 'simulation reporting checklist', 'reproducibility checklist for a simulation study', 'audit the model documentation', 'aplicar STRESS', 'aplica la guía STRESS', 'lista de verificación STRESS', 'revisar mi modelo de simulación con STRESS', '¿cumple mi documentación con STRESS?'. Not for stress tests of servers, finance or psychology, nor for CHEERS/ISPOR audits."
argument-hint: "[document-path ...] [--model des|sd|abs|des,sd|...] [--output quality_reports/stress_audit_<docname>.md]"
allowed-tools: ["Read", "Grep", "Glob", "Bash", "Write"]
effort: high
---

# /stress-rep-guideline — STRESS reporting-completeness audit

Audit the documentation of a simulation model against the STRESS guidelines (Strengthening The Reporting of Empirical Simulation Studies): Monks, Currie, Onggo, Robinson, Kunc & Taylor (2019), *Journal of Simulation* 13(1):55–67, doi:10.1080/17477778.2018.1442155, and its three Supplementary checklists (STRESS-DES, STRESS-SD, STRESS-ABS; CC BY, reproduced verbatim in `references/`). The result is a report that says, for each of the 20 items of the checklist that matches the model type, whether the write-up addresses it, with the evidence quoted and located.

**This skill audits reporting completeness only. It does not judge model validity, calibration, verification or the results themselves** (Monks et al. 2019 §6: V&V "is not a requirement"; the guidelines "apply to the model itself and the model's results", not the modelling process).

## Usage

```
/stress-rep-guideline writing/paper.pdf
/stress-rep-guideline writing/paper.docx writing/supplement.docx --model sd
/stress-rep-guideline manuscript.md appendix_A.md --model des,sd
```

- `document-path ...` — main document first, then any supplements (`.pdf`, `.docx`, `.md`, `.txt`). STRESS explicitly allows evidence in supplementary material, so pass every file that belongs to the write-up.
- `--model` — `des`, `sd`, `abs`, or a comma-separated set for a hybrid. Omit to let the skill detect it (step 3).
- `--output` — default `quality_reports/stress_audit_<docname>.md` in the current project. Never write outside the project.

## Files in this skill — open them when the step says so

| File | Open when |
|---|---|
| `references/stress-common.md` | Step 4 — structure, the items shared between variants, the paper's rationale and worked examples per section, numbering note, article-vs-supplement reconciliation |
| `references/stress-des.md`, `references/stress-sd.md`, `references/stress-abs.md` | Step 5 — the complete verbatim 20-item checklist of the chosen variant(s), with applicability conditions, rule ids and locators; also the paradigm-detection vocabulary used in step 3 |
| `references/decision-rules.md` | Steps 3, 5, 6 — state definitions, rules R1–R35 (N/A, hybrids, supplements, reuse, confidentiality, conditional clauses), hybrid procedure, evidence standards |
| `references/report-template.md` | Step 7 — report layout and filling rules |
| `scripts/extract_text.py` | Step 2 — converts inputs to one corpus with `[[file]]` and `[[page n]]` markers |
| `scripts/make_skeleton.py` | Step 5 — renders the pre-filled report skeleton for the variant(s) from `scripts/checklist.json` (`--list` shows variants) |
| `scripts/checklist.json` | Source of truth for all checklist text; read it only if a reference file seems inconsistent |

## Workflow

### 1. Gather inputs

Confirm which files form the write-up (main text + supplements), the output path, and whether `--model` was given. If a file is missing or unreadable, stop and ask. Check the output path: if `quality_reports/stress_audit_<docname>.md` already exists, apply overwrite protection (ask, or write `_v2`).

### 2. Extract text

Run, from the project root:

```
python3 "${CLAUDE_SKILL_DIR}/scripts/extract_text.py" <main> [<supplement> ...] --output <scratch>/stress_corpus.txt
```

Read the corpus. The script prints characters and pages per file; if a PDF yields almost no text it is scanned — tell the user it must be OCR'd first and stop. Keep the `[[file: … | main document/supplement]]` and `[[page n]]` markers: every evidence quote in the report cites them.

### 3. Detect the paradigm and pause once

STRESS gives no detection rule, so the skill's own procedure is (see `decision-rules.md` §5):

1. `--model` given → use it.
2. Otherwise look for a declaration ("discrete-event simulation", "system dynamics model", "agent-based model", "modelo de simulación de eventos discretos", "modelo de dinámica de sistemas", "modelo basado en agentes").
3. Otherwise count the distinctive vocabulary listed at the top of each variant reference file and infer the paradigm (or a hybrid set when two vocabularies are both strong and the text describes coupled components).

When the paradigm is inferred (cases 2 and 3), pause once and ask the user to confirm, stating the inference, the evidence counts, and the variant(s) you will apply; continue after confirmation. If the user has said "just do it", proceed with the inference and write `basis: inferred, user said proceed` in the report header.

If the document's paradigm is none of DES, SD or ABS (Monte Carlo risk analysis, Markov cohort or microsimulation, optimisation-only, distributed-simulation frameworks): **stop, do not audit**, and tell the user that STRESS covers discrete-event simulation, system dynamics and agent-based simulation only (Monks et al. 2019 abstract; §8 defers hybrid and distributed simulation). If the document is a modelling framework rather than a model with a result, say so (rule R5) and stop.

### 4. Select the checklist(s)

Open `references/stress-common.md`, then the variant file(s). For hybrids, follow the hybrid procedure in `decision-rules.md` §4: union of the chosen variants, plus the interface check H.1. Render the skeleton:

```
python3 "${CLAUDE_SKILL_DIR}/scripts/make_skeleton.py" --variant <des|sd|abs|des,sd> --title "<document title>" --output <scratch>/stress_skeleton.md
```

The skeleton already carries every item, 2.5 sub-item and 1.3 sub-point with its verbatim recommendation, applicability condition and rule ids. Do not retype recommendations; audit against the text in the skeleton.

### 5. Audit item by item

For each row, in checklist order:

1. **Decide applicability first.** Read the row's applicability note and the cited rules (`decision-rules.md` §2–3). Unconditional clauses always apply; conditional clauses ("if appropriate", "(if any)", "If the model is stochastic", "Where relevant", "If common random numbers are used", "If the HLA is used", …) apply only when their trigger holds in this model. Not applicable is allowed only where a rule permits it (R1, R16, R21, R23, R24, R25, R29) and must cite the rule.
2. **Search the whole corpus** — main text and every supplement (R3) — using Grep on the corpus for the item's terms in English and Spanish, then read the surrounding passage. Tables and figures count; cite their numbers.
3. **Assign one state**: Addressed (every applicable clause present), Partially addressed (some clauses present — name the absent one), Missing (nothing for an applicable item), Not applicable (rule-permitted; say whether the document justifies it). Definitions in `decision-rules.md` §1.
4. **Quote the evidence verbatim** in the document's language (English or Spanish) with its locator (`main document, p. 7` / `supplement S1, § 2.3` / `Table 4`). Evidence standards: an external URL alone → Partial (R4); "available from the authors" is not evidence (R10); a code repository satisfies 6.1 only (R7); a cited reused model with reported adaptations → "Addressed by reference" (R15); confidentiality declared → Partial with "QA summary present/absent" (R12).
5. **Sub-rows**: audit 2.5.x components and 1.3 a–d sub-points individually, then set the parent state (all applicable sub-rows Addressed → Addressed; mixed → Partially addressed; all Missing → Missing; all N/A → N/A).

Keep the item wording untouched: the "STRESS asks for" column is the verbatim text from the skeleton.

### 6. Cross-reference checks

Fill the cross-reference table (R34): 1.3 ↔ 2.3 (scenarios named but scenario logic absent?), 1.3b ↔ 3.3 (designed experiment but no parameter ranges?), 5.3 ↔ 5.1 (proprietary execution mechanism but no software version/build?), 4.3 / 5.2 ↔ 3.3 (deterministic claim but stochastic input distributions?). For hybrids, audit H.1: does the document say how the simulation methods communicate (what passes between components, when, in which direction)? Label H.1 as the paper's provisional advice (R2, R20).

### 7. Write the report

Complete the skeleton following `references/report-template.md` and save it to `quality_reports/stress_audit_<docname>.md` (project root; create `quality_reports/` if needed). The header must state: variant(s) and basis for selection; files audited; the numbering note (published checklists use 3.2 Pre-processing / 3.3 Input parameters; the article's Table 3 prints the reverse); the scope sentence; and the tally — plain counts of the four states over the 20 items. No score, no severity tiers, no pass/fail. The N/A section lists each N/A item with its rule and the document's justification or "no justification given"; the final section repeats every Missing/Partial item with the verbatim recommendation and the absent clause so the author can fix it.

### 8. Summarise to the user

In chat: the variant(s) applied and why; the tally; the Missing and Partially addressed items in checklist order, each with one line on what to add (verbatim STRESS wording, not a paraphrase); any cross-reference inconsistencies; the report path. Report prose and state labels in English; quotes in the source language.

## Verification before handing over

- Exactly 20 item rows (plus sub-rows) are present and each has one state.
- Every Addressed / Partially addressed row has a verbatim quote and a locator from the corpus markers.
- Every Not applicable row cites a rule id and says whether the document justifies the omission.
- The header carries variant(s) + basis, files audited, numbering note, scope sentence, tally.
- No recommendation text was altered; no score or verdict was added; nothing was written outside the project.

## Examples

**DES paper, paradigm declared.** "Apply STRESS to writing/ed_simulation.pdf." → corpus extracted (12 pages); "discrete-event simulation" declared on p. 2 → STRESS-DES, basis: declared → skeleton rendered → audit finds 4.1 Partially addressed ("A warm-up of 2 weeks was used" but no selection method and no terminating/non-terminating statement), 5.2 Missing, 1.3c Not applicable (R22, no optimisation) → report at `quality_reports/stress_audit_ed_simulation.md`; chat lists the 5 Missing/Partial items with the verbatim clauses to add.

**SD paper, Spanish, paradigm inferred.** "Aplica la guía STRESS a manuscrito.docx y anexo.docx." → vocabulary: 41 SD terms (acervos, flujos, bucles de retroalimentación, Vensim), 3 DES terms → SOFT pause: "Inferred: system dynamics → STRESS-SD. Confirm?" → user confirms → audit; 2.1 Addressed with the quote "El diagrama causal (Figura 2) muestra los tres bucles de retroalimentación…" (main document, p. 5, Figura 2); 5.3 Missing (no integration method or DT) → report in English with Spanish quotes.

**Hybrid DES + SD.** `--model des,sd` → merged skeleton: 2.5 shows both entities/activities/resources/queues/entry-exit and stocks/flows/auxiliaries/lookups/sources-sinks; 4.1, 4.3, 5.3 appear once per variant; H.1 asks how the DES and SD parts exchange information. Items that belong to only one part are N/A on the other variant's row, citing R2.

## Troubleshooting

- **Corpus is nearly empty for a PDF** — scanned document; ask the user to OCR it (or supply the Word source) and stop.
- **Two paradigms score similarly** — treat as a candidate hybrid; in the confirmation question offer "hybrid des,sd" vs the single variant and let the user choose.
- **Paradigm is Monte Carlo / Markov / microsimulation / optimisation** — stop; STRESS covers DES, SD and ABS only.
- **Document says details are confidential** — apply R12: items that depend on the withheld content are Partially addressed, noting whether an independent QA summary is included.
- **Reference files disagree with each other** — `scripts/checklist.json` is the source of truth; regenerate the variant file with `make_skeleton.py --variant <v> --render-reference --output references/stress-<v>.md`.

## Provenance

Monks et al. (2019) doi:10.1080/17477778.2018.1442155 (Open Access, CC BY 4.0) and its Supplementary checklists `tjsm_a_1442155_sm3123.docx` (DES), `tjsm_a_1442155_sm3083.docx` (SD), `tjsm_a_1442155_sm3069.docx` (ABS). Source table, the article-vs-supplement reconciliation, where the source is silent, and the scope decisions: `references/provenance.md`.
