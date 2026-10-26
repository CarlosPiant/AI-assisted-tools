#!/usr/bin/env python3
"""
make_skeleton.py -- render CHEERS 2022 audit skeletons and the reference file; verify finished reports

PURPOSE
    Single rendering / checking tool for the cheers-checklist skill. It reads the
    one source of truth, scripts/checklist.json (the 28 items of CHEERS 2022
    Table 1, verbatim, from Husereau et al. 2022, Value Health 25(1):3-9,
    doi:10.1016/j.jval.2021.11.1351, CC BY 4.0), and does one of four things:

      (a) --list               print the seven categories and their items;
      (b) skeleton (default)   write an audit REPORT SKELETON: header, one table
                               per CHEERS category with every item's verbatim
                               guidance, applicability and rule ids pre-filled
                               and empty State / Evidence / Locator cells,
                               cross-checks, N/A section, Missing/Partial
                               section and the paste-ready Submission checklist
                               table;
      (c) --render-reference   write references/cheers-checklist.md (the full
                               verbatim checklist with clauses and rules);
      (d) --verify REPORT      check a COMPLETED report mechanically: 28 item
                               rows, valid states, tally arithmetic, submission
                               table agreement, no leftover placeholders, no
                               "Not conducted" label, evidence present.

    Rendering skeleton and reference from the same JSON keeps them from drifting.

INPUTS
    --checklist PATH        checklist.json (default: next to this script)
    --title TEXT            document title for the skeleton header
    --modelling yes|no|unknown
                            whether the audited study uses a model. 'no' marks
                            items 16 and 22 as expected Not applicable, because
                            CHEERS gives them as examples of items that do not
                            apply to non-modelling studies (P4/J6, rule R14).
    --form full|cost-analysis
                            'cost-analysis' (costs and cost offsets only) marks
                            items 11-13 as expected Not applicable (P4/J6, R14).
    --render-reference      render the reference file instead of a skeleton
    --verify PATH           verify a completed report; exit 1 on any error
    --list                  print categories and items, then exit
    --output PATH           where to write (skeleton/reference); stdout if
                            omitted. The script writes ONLY to the path given.

OUTPUTS
    Markdown (skeleton or reference) to --output or stdout; for --verify, a
    plain-text check list to stdout and exit code 0 (clean) / 1 (errors).

CONSTANTS
    All checklist text, item numbers, locators, rule ids and the four state
    names come from checklist.json. Hard-coded here: the report layout (it
    mirrors references/report-template.md) and the placeholder strings below.

USAGE
    python3 make_skeleton.py --list
    python3 make_skeleton.py --title "My CEA" --modelling yes --output /tmp/skel.md
    python3 make_skeleton.py --modelling no --form cost-analysis --output /tmp/skel.md
    python3 make_skeleton.py --render-reference --output references/cheers-checklist.md
    python3 make_skeleton.py --verify quality_reports/cheers_checklist_mypaper.md
"""

import argparse
import json
import os
import re
import sys

# --------------------------------------------------------------------------
# Section 1: constants and loading
# --------------------------------------------------------------------------

# Placeholders start with "_(" so that --verify can find any the auditor forgot.
STATE_PH = "_(state)_"
QUOTE_PH = "_(quote)_"
LOC_PH = "_(file, p./section, table/figure)_"


def load_checklist(path):
    """Read checklist.json and return the parsed dict."""
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def items_by_id(data):
    """Map item number -> item dict (ids are integers 1..28)."""
    return {it["id"]: it for it in data["items"]}


# --------------------------------------------------------------------------
# Section 2: formatting helpers
# --------------------------------------------------------------------------

def md_cell(text):
    """Make text safe inside a Markdown table cell (pipes and newlines would break the row)."""
    return str(text).replace("|", "\\|").replace("\n", "<br>")


def rules_str(rules):
    """'R14, R30' or '-' when an item has no attached rules."""
    return ", ".join(rules) if rules else "-"


def expected_na(item, modelling, form):
    """Return the R14 reason if the study type makes this item an expected Not applicable.

    Only the two examples CHEERS itself gives are pre-marked (P4/J6): items
    11-13 for cost analyses and items 16 and 22 for non-modelling studies. All
    other Not applicable decisions are left to the auditor (rule S2)."""
    if modelling == "no" and "modelling = no" in item["na_when"]:
        return "expected Not applicable: non-modelling study (R14)"
    if form == "cost-analysis" and "form = cost analysis" in item["na_when"]:
        return "expected Not applicable: cost analysis (R14)"
    return None


# --------------------------------------------------------------------------
# Section 3: report skeleton
# --------------------------------------------------------------------------

def render_skeleton(data, title, modelling, form):
    """Build the audit skeleton (layout documented in references/report-template.md)."""
    meta = data["meta"]
    ids = items_by_id(data)
    out = []
    out.append(f"# CHEERS 2022 reporting audit \u2014 {title}")
    out.append("")
    out.append(f"Source guideline: {meta['citation']} doi:{meta['doi']} \u2014 Table 1 (28 items).")
    study = {"yes": "model-based", "no": "empirical (non-modelling)", "unknown": "_(model-based / empirical (non-modelling))_"}[modelling]
    form_txt = "cost analysis" if form == "cost-analysis" else "_(CEA / CUA / cost-minimisation / CBA / extended or distributional CEA)_"
    out.append(f"Study type: {study}; form: {form_txt} \u2014 basis for selection: _(declared / inferred and confirmed / inferred, user said proceed / argument)_")
    out.append("Files audited: _(main document <name>, pages/sections ...; supplement(s) <names>)_")
    out.append(f"Interpretation note: {meta['ee_note']}")
    out.append(f"Scope: {meta['scope_sentence']}")
    out.append(f"{meta['tally_note']}: Addressed _n_ | Partially addressed _n_ | Missing _n_ | Not applicable _n_ (of 28)")
    out.append("")

    # One table per CHEERS category, in the Statement's order (R18).
    for sec in data["sections"]:
        out.append(f"## {sec['number']}. {sec['title']}")
        out.append("")
        out.append("| Item | State | Evidence (verbatim quote) | Locator | CHEERS 2022 guidance (verbatim) | Applicability / rules |")
        out.append("|---|---|---|---|---|---|")
        for iid in sec["items"]:
            it = ids[iid]
            app = it["applicability"]
            hint = expected_na(it, modelling, form)
            if hint:
                # The hint is a pre-filled suggestion; the auditor still confirms
                # it and states whether the document itself says so.
                app = f"{hint}; {app}"
            app += f" \u2014 rules: {rules_str(it['rules'])}"
            out.append(f"| **{it['id']} {it['topic']}** | {STATE_PH} | {QUOTE_PH} | {LOC_PH} | {md_cell(it['guidance'])} | {md_cell(app)} |")
        out.append("")

    out.append("## Cross-checks (skill-derived pairings, rule S7)")
    out.append("")
    out.append("| Pair | Consistent? | Check | Basis |")
    out.append("|---|---|---|---|")
    for cc in data["cross_checks"]:
        out.append(f"| {cc['pair']} | _(yes / no / n.a.)_ | {md_cell(cc['check'])} | {md_cell(cc['basis'])} |")
    out.append("")

    out.append("## Items marked Not applicable \u2014 rule cited and whether the document justifies it")
    out.append("")
    out.append("| Item | Rule | Document's justification (quote) or 'no justification given' |")
    out.append("|---|---|---|")
    out.append("| _(item)_ | _(R14 / S2 ...)_ | _(quote)_ |")
    out.append("")

    out.append("## Missing and partially addressed items \u2014 what CHEERS 2022 asks for")
    out.append("")
    out.append("| Item | State | CHEERS 2022 guidance (verbatim) | Locator in CHEERS | What is absent |")
    out.append("|---|---|---|---|---|")
    out.append("| _(item)_ | _(Missing / Partially addressed)_ | _(copy from the tables above)_ | _(Table 1, P3/J5 or P4/J6)_ | _(the absent clause)_ |")
    out.append("")

    out.append("## Submission checklist table (CHEERS 2022 Table 1 format)")
    out.append("")
    out.append("Paste-ready. 'Reported in section' gives where each item is found in the audited files (R13). "
               "Items that do not apply read 'Not applicable' and items not found read 'Not reported', "
               "as CHEERS asks (P4/J6); the label CHEERS asks users to avoid is not used.")
    out.append("")
    out.append("| Section/topic | Item No | Reported in section | State |")
    out.append("|---|---|---|---|")
    for sec in data["sections"]:
        for iid in sec["items"]:
            it = ids[iid]
            hint = expected_na(it, modelling, form)
            loc = "_(Not applicable \u2014 confirm R14)_" if hint else "_(section / page / table, or Not reported)_"
            out.append(f"| {it['topic']} | {it['id']} | {loc} | {STATE_PH} |")
    out.append("")
    out.append("---")
    out.append(f"Attribution: {meta['licence']}")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Section 4: reference file
# --------------------------------------------------------------------------

def render_reference(data):
    """Render references/cheers-checklist.md: all 28 items verbatim with clauses, rules, locators."""
    meta = data["meta"]
    ids = items_by_id(data)
    out = []
    out.append("# CHEERS 2022 \u2014 the 28-item checklist (verbatim) with applicability and rules")
    out.append("")
    out.append(f"Source: {meta['citation']} doi:{meta['doi']}, Table 1.")
    out.append("")
    out.append(f"Attribution: {meta['licence']}")
    out.append("")
    out.append(f"Locators: {meta['locator_note']}")
    out.append("")
    out.append(f"Clauses: {meta['clause_note']}")
    out.append("")
    out.append("Generated from `scripts/checklist.json` by `scripts/make_skeleton.py --render-reference`; edit the JSON, not this file. Rule ids (R.., S..) are defined in `decision-rules.md`.")
    out.append("")
    out.append("## Contents")
    out.append("")
    for sec in data["sections"]:
        out.append(f"- {sec['number']}. {sec['title']}: " + ", ".join(f"{i} {ids[i]['topic']}" for i in sec["items"]))
    out.append("- Cross-checks")
    out.append("")
    for sec in data["sections"]:
        out.append(f"## {sec['number']}. {sec['title']}")
        out.append("")
        for iid in sec["items"]:
            it = ids[iid]
            out.append(f"### Item {it['id']} \u2014 {it['topic']}")
            out.append("")
            out.append(f"> {it['guidance']}")
            out.append("")
            out.append(f"- Locator: {it['locator']}")
            out.append(f"- Applicability: {it['applicability']}")
            if it["na_when"]:
                out.append(f"- Not applicable when: {'; '.join(it['na_when'])}")
            out.append(f"- Rules: {rules_str(it['rules'])}")
            # Clauses are listed so the auditor can name exactly which part is absent.
            out.append("- Clauses (skill decomposition, verbatim fragments):")
            for c in it["clauses"]:
                cond = f" \u2014 condition: {c['condition']}" if c["condition"] else ""
                out.append(f"  - \"{c['text']}\"{cond}")
            out.append("")
    out.append("## Cross-checks")
    out.append("")
    for cc in data["cross_checks"]:
        out.append(f"- **{cc['pair']}** \u2014 {cc['check']} ({cc['basis']})")
    out.append("")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Section 5: verification of a completed report
# --------------------------------------------------------------------------

def split_row(line):
    """Split a Markdown table row into stripped cells, honouring escaped pipes (\\|)."""
    cells = re.split(r"(?<!\\)\|", line.strip())
    return [c.strip() for c in cells[1:-1]]


def verify_report(data, path):
    """Return (errors, warnings, summary) for a completed report."""
    states = data["meta"]["states"]
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    errors, warnings = [], []

    # 5a. Item rows of the seven category tables: first cell is "**<n> <topic>**".
    item_state, item_cells = {}, {}
    for ln in lines:
        if not ln.startswith("| **"):
            continue
        cells = split_row(ln)
        m = re.match(r"\*\*(\d{1,2})\s", cells[0])
        if not m:
            continue
        iid = int(m.group(1))
        if iid in item_state:
            errors.append(f"item {iid} appears more than once in the category tables")
        item_state[iid] = cells[1] if len(cells) > 1 else ""
        item_cells[iid] = cells
    missing_ids = sorted(set(range(1, 29)) - set(item_state))
    if missing_ids:
        errors.append(f"category tables lack items {missing_ids}")
    for iid, st in sorted(item_state.items()):
        if st not in states:
            errors.append(f"item {iid}: state '{st}' is not one of {states}")
            continue
        cells = item_cells[iid]
        # Addressed / Partial need a quote and a locator (decision 2 / S6).
        if st in ("Addressed", "Partially addressed"):
            ev = cells[2] if len(cells) > 2 else ""
            loc = cells[3] if len(cells) > 3 else ""
            if not re.search(r"[\"\u201c\u201d\u00ab\u00bb]", ev):
                warnings.append(f"item {iid} ({st}): evidence cell has no quotation marks")
            if not loc or loc.startswith("_("):
                errors.append(f"item {iid} ({st}): locator missing")
        if st == "Not applicable":
            app = " ".join(cells[4:]) if len(cells) > 4 else ""
            if not re.search(r"\b[RS]\d+\b", app):
                warnings.append(f"item {iid} (Not applicable): no rule id (R../S..) in the row")

    counts = {s: sum(1 for v in item_state.values() if v == s) for s in states}

    # 5b. Tally line must match the counted states and sum to 28.
    tally = re.search(r"Addressed\s+(\d+)\s*\|\s*Partially addressed\s+(\d+)\s*\|\s*Missing\s+(\d+)\s*\|\s*Not applicable\s+(\d+)", text)
    if not tally:
        errors.append("tally line not found or not filled in")
    else:
        stated = dict(zip(states, map(int, tally.groups())))
        if stated != counts:
            errors.append(f"tally {stated} does not match the item rows {counts}")
        if sum(stated.values()) != 28:
            errors.append(f"tally sums to {sum(stated.values())}, not 28")

    # 5c. Submission checklist table: 28 rows, same states, CHEERS labels.
    sub_rows = {}
    in_sub = False
    for ln in lines:
        if ln.startswith("## "):
            in_sub = ln.lower().startswith("## submission checklist table")
            continue
        if in_sub and ln.startswith("|") and not ln.startswith("|---"):
            cells = split_row(ln)
            if len(cells) >= 4 and cells[1].isdigit():
                sub_rows[int(cells[1])] = cells
    if len(sub_rows) != 28:
        errors.append(f"submission checklist table has {len(sub_rows)} item rows, expected 28")
    for iid, cells in sorted(sub_rows.items()):
        loc, st = cells[2], cells[3]
        if iid in item_state and st != item_state[iid]:
            errors.append(f"submission table item {iid}: state '{st}' differs from category table '{item_state[iid]}'")
        if st == "Not applicable" and "Not applicable" not in loc:
            errors.append(f"submission table item {iid}: location should read 'Not applicable' (R14)")
        if st == "Missing" and "Not reported" not in loc:
            errors.append(f"submission table item {iid}: location should read 'Not reported' (R15)")
        if st in ("Addressed", "Partially addressed") and ("Not reported" in loc or not loc):
            errors.append(f"submission table item {iid}: {st} but no location given")

    # 5d. Leftover placeholders and forbidden labels.
    if "_(" in text:
        n = text.count("_(")
        errors.append(f"{n} unfilled placeholder(s) '_(...)_' remain")
    # R16 forbids "Not conducted" as a LABEL. A verbatim quote from the audited
    # document may contain the words, so only state and location cells are errors.
    label_cells = list(item_state.values()) + [c[2] for c in sub_rows.values()] + [c[3] for c in sub_rows.values()]
    if any(re.search(r"not conducted", c, re.I) for c in label_cells):
        errors.append("'Not conducted' used as a state or location label; CHEERS asks users to avoid it (R16)")
    elif re.search(r"not conducted", text, re.I):
        warnings.append("'not conducted' appears in the text; fine inside a quote from the document, not as a label (R16)")
    # Scores and severity tiers are not part of CHEERS (R7); flag likely uses.
    for pat, what in [(r"\b(critical|major|minor)\s+(gap|issue|item)s?\b", "severity tier wording"),
                      (r"\b\d+(\.\d+)?\s*/\s*(28|100)\b", "a score-like fraction"),
                      (r"\b(pass|fail)(ed|s)?\b", "pass/fail wording")]:
        if re.search(pat, text, re.I):
            warnings.append(f"possible {what} found; CHEERS defines no score or tiers (R7)")

    summary = f"items {len(item_state)}/28; states {counts}; submission rows {len(sub_rows)}"
    return errors, warnings, summary


# --------------------------------------------------------------------------
# Section 6: command line
# --------------------------------------------------------------------------

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--checklist", default=os.path.join(here, "checklist.json"))
    ap.add_argument("--title", default="(document title)")
    ap.add_argument("--modelling", choices=["yes", "no", "unknown"], default="unknown")
    ap.add_argument("--form", choices=["full", "cost-analysis"], default="full")
    ap.add_argument("--render-reference", action="store_true")
    ap.add_argument("--verify", metavar="REPORT")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--output")
    args = ap.parse_args()

    data = load_checklist(args.checklist)

    if args.list:
        ids = items_by_id(data)
        for sec in data["sections"]:
            print(f"{sec['number']}. {sec['title']} ({len(sec['items'])}): "
                  + "; ".join(f"{i} {ids[i]['topic']}" for i in sec["items"]))
        print(f"total items: {len(data['items'])}; clauses: {sum(len(i['clauses']) for i in data['items'])}")
        return

    if args.verify:
        errors, warnings, summary = verify_report(data, args.verify)
        print(summary)
        for w in warnings:
            print("WARNING:", w)
        for e in errors:
            print("ERROR:", e)
        print("verify: OK" if not errors else f"verify: {len(errors)} error(s)")
        sys.exit(1 if errors else 0)

    text = render_reference(data) if args.render_reference else render_skeleton(data, args.title, args.modelling, args.form)
    if args.output:
        # Only the caller decides where output goes (the script never chooses a location itself).
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {args.output} ({text.count(chr(10))} lines)")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
