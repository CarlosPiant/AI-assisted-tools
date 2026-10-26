# Provenance — where every part of this skill comes from

Condensed from the design brief written when the skill was generated (2026-10-24). Locators: `P<n>/J<n>` = PDF page / printed journal page of the Statement (P1 = J3 … P7 = J9). Table 1 items 1–23 are on P3/J5, items 24–28 on P4/J6. Appendices: `App. A, <row>`; `App. B, § <heading>`.

## Sources

| Short name | File | Content | Licence note |
|---|---|---|---|
| **Statement** | `cheers2022.pdf` | Husereau D, Drummond M, Augustovski F, de Bekker-Grob E, Briggs AH, Carswell C, Caulley L, Chaiyakunapruk N, Greenberg D, Loder E, Mauskopf J, Mullins CD, Petrou S, Pwu R-F, Staniszewska S, on behalf of the CHEERS 2022 ISPOR Good Research Practices Task Force. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) Statement: Updated Reporting Guidance for Health Economic Evaluations. *Value in Health* 2022;25(1):3–9. doi:10.1016/j.jval.2021.11.1351. All 7 pages read; Table 1 wording confirmed against the PDF text layer. | CC BY 4.0 (P1/J3 footer) |
| **App. A** | `1-s2.0-S1098301521031466-mmc1.docx` | Appendix A, "GRIPP2 – Short Form: Public Involvement in CHEERS" | No licence line of its own; supplementary data of the Statement. Only short quotes are bundled. |
| **App. B** | `1-s2.0-S1098301521031466-mmc2.docx` | Appendix B, "Protocol for Delphi Process" | same |

**Not used:** the CHEERS 2022 Explanation and Elaboration report (Husereau et al., *Value Health* 2022;25(1):10–31, doi:10.1016/j.jval.2021.11.008, cited by the Statement as its reference 39). The Statement asks users to "first consult the Explanation and Elaboration report to ensure the appropriate interpretation of each item description" (P4/J6). It was not available when the skill was built, so every report notes that items are judged against the Table 1 text only. Nothing from it was reconstructed.

**Verbatim check.** All 28 "Guidance for reporting" strings in `scripts/checklist.json` match the Statement's text layer word for word after ligature and whitespace normalisation. The Statement's own typographical slips (items 24, 25, 27, 28) are kept as printed.

## Licence

P1/J3 footer: "This article is published under the Creative Commons CC-BY license." and "This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/)." CC BY 4.0 permits redistribution with attribution, so Table 1 is bundled verbatim in `scripts/checklist.json` and `references/cheers-checklist.md` with the attribution given in the plugin's `NOTICE`.

## Where the sources are silent (not filled from general knowledge)

- How to judge a partially reported item. The Statement gives one or two sentences per item and the E&E report was not supplied, so the skill splits each item's guidance into verbatim clauses (rule S8, labelled as the skill's).
- How to recognise the study type. The vocabulary lists in `study-type-detection.md` are the skill's own aid (S4); an inferred type is confirmed with the user.
- Whether an author's "not applicable" for an item without conditional wording should be accepted (S2: it is not; the claim is quoted).
- How to treat links to material that was not supplied (S6).
- Any score, threshold, severity tier or pass/fail rule. None exists, and the Statement discourages scoring (R7).

## Scope

### The skill WILL

- Take one health economic evaluation (PDF, DOCX, MD, TXT) plus any supplements or technical appendices as one corpus with per-file locators (R17).
- Check scope first (R1, R4) and stop with a quoted reason when the document is not a health economic evaluation in the Statement's sense (cost-of-illness or burden studies, budget impact analyses, constrained optimisation, pure clinical studies).
- Record the study type (model-based or empirical) and form (cost analysis, CEA, CUA, cost-minimisation, CBA, extended or distributional CEA), declared or inferred and confirmed once.
- Audit all 28 items against the verbatim Table 1 guidance: one state each, a verbatim quote and locator for Addressed and Partially addressed, the verbatim guidance for every Missing or Partially addressed item, and rule plus justification for every Not applicable.
- Write one report, `quality_reports/cheers_checklist_<docname>.md`, including a paste-ready submission checklist table (R13–R15).
- Audit English and Spanish manuscripts. Report prose and labels are in English; quotes stay in the source language; guidance is quoted in English (R27).

### The skill will NOT

- Score, weight, rank, tier (for example Critical/Major/Minor) or give pass/fail (R7, R25). Those are not part of CHEERS.
- Judge methods, the appropriateness of choices, or results (R8).
- Audit against CHEERS 2013, GRIPP2, CONSORT or other guidance (R10, R11, R24), or reconstruct the E&E report (R12).
- Translate the checklist (R27) or edit the audited document.

## Judgment calls made when the skill was built

| # | Call | Why |
|---|---|---|
| J1 | The Statement's scope (cost analyses included) prevails over Appendix B's "both … costs and consequences". | The Statement is the published guidance; Appendix B is the protocol. |
| J2 | Items 21 and 25 become Not applicable together when the document explicitly says no one was involved. | R23 ties the engagement items to involvement "when it is carried out"; R33. |
| J3 | Item 4 "no plan was developed" is Addressed, not Not applicable. | "Indicate whether" is answered by that statement (R29). |
| J4 | Item 22 is Not applicable for non-modelling studies even when inputs are listed. | The Statement's literal example (R14). |
| J5 | Item 19 has no conditional wording, so an author's "not applicable" without a reason is reported as Missing with the claim quoted. | S2. |
| J6 | Evidence that exists only behind an external link is Partially addressed, except for the location clauses of items 4 and 16. | S6; the sources are silent. |
| J7 | Guidance is never translated; Spanish quotes from the document are kept. | R27. |
| J8 | Cross-checks are limited to item pairs named by Table 1 titles or wording (20↔24, 9/10↔24, 21↔25, 16↔17↔22). | S7. |
| J9 | `make_skeleton.py --verify` checks a finished report: 28 rows, tally arithmetic, submission-table labels, no "Not conducted". | A mechanical check every run would otherwise do by hand. |
