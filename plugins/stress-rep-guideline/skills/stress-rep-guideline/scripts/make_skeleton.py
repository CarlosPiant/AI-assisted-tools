#!/usr/bin/env python3
"""
make_skeleton.py -- render STRESS audit skeletons and reference files from checklist.json

PURPOSE
    Single rendering tool for the stress-rep-guideline skill. It reads the one
    source of truth (scripts/checklist.json, the verbatim STRESS-DES / STRESS-SD /
    STRESS-ABS checklists from the Supplementary material of Monks et al. 2019,
    doi:10.1080/17477778.2018.1442155, CC BY) and produces either:

      (a) an audit REPORT SKELETON for one variant or a hybrid set of variants,
          with every item pre-filled with its title, verbatim recommendation,
          applicability condition and locator, and empty State / Evidence cells
          for the auditor to complete; or
      (b) a REFERENCE FILE (references/stress-<variant>.md) listing the full
          20-item checklist of one variant verbatim.

    Rendering both from the same JSON is what keeps the reference files and the
    audit reports from drifting apart.

INPUTS
    --checklist PATH      path to checklist.json (default: next to this script)
    --variant V[,V...]    one or more of: des, sd, abs  (comma-separated = hybrid)
    --render-reference    render the reference file instead of a skeleton
                          (exactly one variant allowed)
    --title TEXT          document title to put in the skeleton header
    --list                print variants with item / sub-item counts and exit
    --output PATH         where to write; prints to stdout when omitted.
                          The script writes ONLY to the path given; it never
                          chooses a location itself.

OUTPUTS
    Markdown text (skeleton or reference file) to --output or stdout.

CONSTANTS
    All checklist text, item numbers, locators and rule ids come from
    checklist.json; nothing is hard-coded here except the report layout, which
    mirrors references/report-template.md.

USAGE
    python3 make_skeleton.py --list
    python3 make_skeleton.py --variant des --title "My paper" --output /tmp/skel.md
    python3 make_skeleton.py --variant des,sd --output /tmp/hybrid.md
    python3 make_skeleton.py --variant sd --render-reference --output references/stress-sd.md
"""

import argparse
import json
import os
import sys

# --------------------------------------------------------------------------
# Section 1: loading
# --------------------------------------------------------------------------

STATE_PLACEHOLDER = "_(state)_"      # the auditor replaces this with one of the four states
EVIDENCE_PLACEHOLDER = "_(quote)_"   # verbatim quote from the audited document
LOCATOR_PLACEHOLDER = "_(p./section/file)_"


def load_checklist(path):
    """Read checklist.json and return the parsed dict."""
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def parse_variants(spec, data):
    """Turn 'des,sd' into ['des','sd'], validating against the JSON keys.

    Order is preserved and duplicates dropped so a hybrid report lists the
    variants in the order the user named them."""
    seen = []
    for v in spec.split(","):
        v = v.strip().lower()
        if v not in data["variants"]:
            sys.exit(f"Unknown variant '{v}'. Known: {', '.join(data['variants'])}")
        if v not in seen:
            seen.append(v)
    return seen


# --------------------------------------------------------------------------
# Section 2: small formatting helpers
# --------------------------------------------------------------------------

def md_cell(text):
    """Make a multi-line string safe inside a Markdown table cell.

    Pipes would break the table and newlines would end the row, so they are
    replaced by an escaped pipe and <br>; the checklist's own '- ' bullets are
    kept visible."""
    return text.replace("|", "\\|").replace("\n", "<br>")


def rules_str(rules):
    """'R21, R22' or '-' when an item has no attached rules."""
    return ", ".join(rules) if rules else "-"


def identical_str(item, this_variant, data):
    """Human-readable 'identical in STRESS-SD, STRESS-ABS' note, or 'variant-specific'."""
    others = item.get("identical_in") or []
    if not others:
        return "variant-specific wording"
    names = [data["variants"][o]["name"] for o in others]
    return "identical in " + ", ".join(names)


# --------------------------------------------------------------------------
# Section 3: report skeleton
# --------------------------------------------------------------------------

def render_skeleton(data, variants, title):
    """Build the audit skeleton for one variant or a hybrid set.

    For a hybrid, items whose wording differs between the chosen variants are
    shown once per variant (labelled), and 2.5 / 1.3 sub-items are the union;
    the hybrid interface check (Monks et al. 2019, section 6) is appended."""
    meta = data["meta"]
    names = [data["variants"][v]["name"] for v in variants]
    hybrid = len(variants) > 1
    out = []
    out.append(f"# STRESS reporting audit \u2014 {title}")
    out.append("")
    out.append(f"Source guideline: {meta['citation']} doi:{meta['doi']}, and its Supplementary checklists "
               + ", ".join(f"{meta['sources'][v]['file']} ({data['variants'][v]['name']})" for v in variants) + ".")
    out.append(f"Variant(s) applied: {' + '.join(names)}" + (" (hybrid)" if hybrid else "")
               + " \u2014 basis for selection: _(declared / inferred and confirmed / inferred, user said proceed / argument)_")
    out.append("Files audited: _(main text, pages ...; supplement(s) ...)_")
    out.append(f"Numbering: {meta['numbering_note']}")
    out.append("Scope: reporting completeness only, not model validity (Monks et al. 2019, section 6, PDF p. 11 / journal p. 64).")
    out.append("Tally (arithmetic only; STRESS defines no score): Addressed _n_ | Partially addressed _n_ | Missing _n_ | Not applicable _n_ (of 20)")
    out.append("")

    # One block per section; items are grouped by their 'section' number so the
    # report follows the checklist's own six-section order.
    for sec in data["sections"]:
        out.append(f"## Section {sec['number']} \u2014 {sec['title']}")
        out.append("")
        out.append("| Item | State | Evidence (quote) | Locator | STRESS asks for (verbatim) | Applicability / rules |")
        out.append("|---|---|---|---|---|---|")
        # Items with the same id across variants are merged into one row group.
        ids = []
        for v in variants:
            for it in data["variants"][v]["items"]:
                if it["section"] == sec["number"] and it["id"] not in ids:
                    ids.append(it["id"])
        for iid in ids:
            per_variant = {v: next(i for i in data["variants"][v]["items"] if i["id"] == iid) for v in variants}
            first = per_variant[variants[0]]
            # Decide whether the wording is the same across the chosen variants;
            # if so print it once, otherwise once per variant with a label.
            # Compare the recommendation AND the sub-items: 2.5 has an empty
            # parent text in every variant, so comparing the text alone would
            # wrongly collapse DES entities and SD stocks into one row group.
            texts = {v: json.dumps([per_variant[v]["recommendation"], per_variant[v].get("subitems", [])], sort_keys=True)
                     for v in variants}
            same = len(set(texts.values())) == 1
            label_rows = [(None, first)] if (same or not hybrid) else [(v, per_variant[v]) for v in variants]
            for label, it in label_rows:
                tag = f"{it['id']} {it['title']}" + (f" [{data['variants'][label]['name']}]" if label else "")
                rec = it["recommendation"] or "(see sub-items)"
                app = (it.get("applicability") or "unconditional") + f" \u2014 rules: {rules_str(it.get('rules'))}"
                if it.get("cross_refs"):
                    app += f"; cross-refs: {', '.join(it['cross_refs'])}"
                out.append(f"| **{tag}** | {STATE_PLACEHOLDER} | {EVIDENCE_PLACEHOLDER} | {LOCATOR_PLACEHOLDER} | {md_cell(rec)} | {md_cell(app)} |")
                # Sub-items (2.5.x components, 1.3 a-d) get their own rows,
                # indented with a middle dot so they read as children.
                for si in it.get("subitems", []):
                    stag = f"\u00b7 {si['id']} {si['title']}" + (f" [{data['variants'][label]['name']}]" if label else "")
                    sapp = si.get("applicability") or "unconditional"
                    out.append(f"| {stag} | {STATE_PLACEHOLDER} | {EVIDENCE_PLACEHOLDER} | {LOCATOR_PLACEHOLDER} | {md_cell(si['recommendation'])} | {md_cell(sapp)} |")
            # When the same item is shown once but sub-items differ by variant
            # (hybrid 2.5), the loop above already printed each variant's rows.
        out.append("")

    out.append("## Cross-reference checks")
    out.append("")
    out.append("| Pair | Consistent? | Note |")
    out.append("|---|---|---|")
    out.append("| 1.3 (experimentation types) \u2194 2.3 (scenario logic) | _(yes/no/n.a.)_ | 1.3a says 'ensure that item 2.3 (below) is completed' |")
    out.append("| 1.3b (design of experiments) \u2194 3.3 (parameter ranges) | _(yes/no/n.a.)_ | 1.3b says 'provide further details in data below' |")
    out.append("| 5.3 (execution mechanism) \u2194 5.1 (software version/build) | _(yes/no/n.a.)_ | unpublished mechanism must be covered by 5.1 detail (R18, R31) |")
    out.append("| 4.3 / 5.2 (stochastic?) \u2194 3.3 (stochastic inputs) | _(yes/no/n.a.)_ | deterministic claims must agree across items (R16, R29) |")
    out.append("")

    if hybrid:
        h = data["hybrid_interface_check"]
        out.append(f"## Hybrid interface check \u2014 {h['title']}")
        out.append("")
        out.append(f"Basis: {h['basis']}")
        out.append("")
        out.append(f"STRESS (FAQ) says: \"{h['recommendation_verbatim']}\"")
        out.append("")
        out.append(f"Check: {h['check']}")
        out.append("")
        out.append(f"| {h['id']} Interface reported | {STATE_PLACEHOLDER} | {EVIDENCE_PLACEHOLDER} | {LOCATOR_PLACEHOLDER} |")
        out.append("|---|---|---|---|")
        out.append("")

    out.append("## Items marked Not applicable \u2014 rule cited and whether the document justifies the omission (R1)")
    out.append("")
    out.append("| Item | Rule | Document justifies? (quote) |")
    out.append("|---|---|---|")
    out.append("| _(item)_ | _(R..)_ | _(quote or 'no justification given')_ |")
    out.append("")
    out.append("## Missing and partially addressed items \u2014 what STRESS asks for")
    out.append("")
    out.append("| Item | State | Verbatim recommendation | Locator in STRESS | What is absent |")
    out.append("|---|---|---|---|---|")
    out.append("| _(item)_ | _(Missing / Partially addressed)_ | _(copy from the table above)_ | _(e.g. DES-supp item 4.3)_ | _(the missing clause)_ |")
    out.append("")
    out.append("---")
    out.append(f"Attribution: {meta['licence']}")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Section 4: reference file
# --------------------------------------------------------------------------

def render_reference(data, v):
    """Render references/stress-<v>.md: the complete verbatim checklist of one variant."""
    meta = data["meta"]
    var = data["variants"][v]
    src = meta["sources"][v]
    out = []
    out.append(f"# {var['name']} \u2014 {src['title']} (verbatim checklist)")
    out.append("")
    out.append(f"Source: Supplementary material `{src['file']}` of {meta['citation']} doi:{meta['doi']}.")
    out.append(f"Short locator used in this skill: `{src['short']} item <n>`.")
    out.append("")
    out.append(f"Attribution: {meta['licence']}")
    out.append("")
    out.append(f"Numbering note: {meta['numbering_note']}")
    out.append("")
    out.append(f"Shared wording: {meta['identical_items_note']}")
    out.append("")
    out.append("Generated from `scripts/checklist.json` by `scripts/make_skeleton.py --render-reference`; edit the JSON, not this file.")
    out.append("")
    # Table of contents so a reader can jump to a section (files are long).
    out.append("## Contents")
    out.append("")
    for sec in data["sections"]:
        items = [i for i in var["items"] if i["section"] == sec["number"]]
        out.append(f"- Section {sec['number']} {sec['title']}: " + ", ".join(f"{i['id']} {i['title']}" for i in items))
    out.append("")
    out.append("## Paradigm detection vocabulary (skill-derived, not part of STRESS)")
    out.append("")
    out.append(meta["detection_note"])
    out.append("")
    out.append("Keywords: " + ", ".join(var["detection_keywords"]))
    out.append("")
    for sec in data["sections"]:
        out.append(f"## Section {sec['number']} \u2014 {sec['title']}")
        out.append("")
        for it in [i for i in var["items"] if i["section"] == sec["number"]]:
            out.append(f"### {it['id']} {it['title']}")
            out.append("")
            if it["recommendation"]:
                out.append("**Recommendation (verbatim):**")
                out.append("")
                # Quote block keeps the checklist's own line breaks and bullets intact.
                for line in it["recommendation"].split("\n"):
                    out.append(f"> {line}")
                out.append("")
            for si in it.get("subitems", []):
                out.append(f"#### {si['id']} {si['title']}")
                out.append("")
                for line in si["recommendation"].split("\n"):
                    out.append(f"> {line}")
                out.append("")
                if si.get("applicability"):
                    out.append(f"Applicability: {si['applicability']}")
                    out.append("")
            out.append(f"- Applicability: {it.get('applicability') or 'unconditional'}")
            out.append(f"- Rules: {rules_str(it.get('rules'))} (see `decision-rules.md`)")
            if it.get("cross_refs"):
                out.append(f"- Cross-references: {', '.join(it['cross_refs'])}")
            out.append(f"- Locator: {it['locator']}; PDF: {it['pdf_locator']}")
            out.append(f"- Wording: {identical_str(it, v, data)}")
            out.append("")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Section 5: command line
# --------------------------------------------------------------------------

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--checklist", default=os.path.join(here, "checklist.json"))
    ap.add_argument("--variant", help="des | sd | abs | comma-separated set for a hybrid")
    ap.add_argument("--render-reference", action="store_true")
    ap.add_argument("--title", default="(document title)")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--output", help="file to write; stdout when omitted")
    args = ap.parse_args()

    data = load_checklist(args.checklist)

    if args.list:
        for v, var in data["variants"].items():
            n25 = len(next(i for i in var["items"] if i["id"] == "2.5")["subitems"])
            n13 = len(next(i for i in var["items"] if i["id"] == "1.3")["subitems"])
            print(f"{v}: {var['name']} - {len(var['items'])} items, 2.5 has {n25} sub-items, 1.3 has {n13} sub-points")
        return

    if not args.variant:
        ap.error("--variant is required unless --list is given")
    variants = parse_variants(args.variant, data)

    if args.render_reference:
        if len(variants) != 1:
            ap.error("--render-reference takes exactly one variant")
        text = render_reference(data, variants[0])
    else:
        text = render_skeleton(data, variants, args.title)

    if args.output:
        # Only the caller decides where output goes (never the hub, never a
        # default location inside the project).
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {args.output} ({text.count(chr(10))} lines)")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
