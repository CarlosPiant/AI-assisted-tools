#!/usr/bin/env python3
"""
extract_text.py -- turn the documents to be audited into one plain-text corpus with locators

PURPOSE
    The stress-rep-guideline skill audits a simulation write-up (main text plus
    any supplements) against the STRESS checklist and must quote evidence with a
    locator. This helper converts each input file to text and inserts markers
    the auditor can cite:

        [[file: <basename>]]      at the start of every input file
        [[page <n>]]              at every page break of a PDF
        Markdown headings (# ...) are preserved for .md and for .docx (via pandoc)

    Supported inputs: .pdf, .docx, .md, .markdown, .txt (others are rejected).

INPUTS
    positional PATH...    one or more files; the first is treated as the main
                          document, the rest as supplements (order is kept)
    --output PATH         file to write the corpus to (required). The script
                          writes only to this path; it never picks a location.
    --keep-layout         for PDFs, use `pdftotext -layout` (keeps table columns
                          aligned; default is reading order, which is better for
                          two-column journal PDFs)

OUTPUTS
    One UTF-8 text file at --output. A short summary (files, pages, characters)
    is printed to stdout so the caller can confirm the extraction worked
    (e.g. a scanned PDF with no text layer yields ~0 characters and must be
    OCR'd elsewhere before auditing).

TOOLS
    PDF : `pdftotext` (poppler) if on PATH, else the `pypdf` Python package.
    DOCX: `pandoc -t gfm --wrap=none` if on PATH, else `python-docx`
          (paragraphs and tables; headings are detected from the paragraph
          style name so `# ...` lines are still produced).
    Nothing here depends on the Claude hub or on project layout.

USAGE
    python3 extract_text.py paper.pdf supplement.docx --output /path/corpus.txt
"""

import argparse
import os
import shutil
import subprocess
import sys

# --------------------------------------------------------------------------
# Section 1: PDF
# --------------------------------------------------------------------------

def pdf_to_text(path, keep_layout=False):
    """Return PDF text with [[page n]] markers.

    pdftotext separates pages with a form feed (\\f); we convert each form feed
    into an explicit page marker so page numbers survive into the corpus and
    can be quoted as locators."""
    if shutil.which("pdftotext"):
        cmd = ["pdftotext"] + (["-layout"] if keep_layout else []) + [path, "-"]
        raw = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
        pages = raw.split("\f")
    else:
        try:
            import pypdf  # imported lazily so the script runs without it when pdftotext exists
        except ImportError:
            sys.exit("Neither pdftotext nor pypdf is available; install poppler or `pip install pypdf`.")
        reader = pypdf.PdfReader(path)
        pages = [(p.extract_text() or "") for p in reader.pages]
    # Drop a trailing empty page that the final form feed produces.
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    chunks = [f"[[page {i}]]\n{text.strip()}\n" for i, text in enumerate(pages, start=1)]
    return "\n".join(chunks), len(pages)


# --------------------------------------------------------------------------
# Section 2: DOCX
# --------------------------------------------------------------------------

def docx_to_text(path):
    """Return DOCX content as GitHub-flavoured Markdown (headings and tables kept).

    pandoc is preferred because it renders tables as pipe tables, which keeps
    STRESS-style checklist tables readable. python-docx is the fallback; it
    walks paragraphs and tables in document order."""
    if shutil.which("pandoc"):
        cmd = ["pandoc", "-t", "gfm", "--wrap=none", path]
        return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    try:
        import docx  # python-docx
    except ImportError:
        sys.exit("Neither pandoc nor python-docx is available; install one of them.")
    document = docx.Document(path)
    lines = []
    for para in document.paragraphs:
        style = (para.style.name or "").lower()
        # Word heading styles are named 'Heading 1', 'Heading 2', ...; map the
        # trailing digit to the number of '#' so headings remain locatable.
        if style.startswith("heading") and style[-1].isdigit():
            lines.append("#" * int(style[-1]) + " " + para.text)
        elif para.text.strip():
            lines.append(para.text)
    for table in document.tables:
        lines.append("")
        for row in table.rows:
            lines.append("| " + " | ".join(c.text.replace("\n", " ") for c in row.cells) + " |")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# Section 3: plain text / markdown (pass-through)
# --------------------------------------------------------------------------

def text_passthrough(path):
    """Read .md/.txt as-is (UTF-8, tolerant of stray bytes)."""
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


# --------------------------------------------------------------------------
# Section 4: dispatcher and CLI
# --------------------------------------------------------------------------

EXTRACTORS = {
    ".pdf": "pdf",
    ".docx": "docx",
    ".md": "text",
    ".markdown": "text",
    ".txt": "text",
}


def extract_one(path, keep_layout):
    """Dispatch on extension; return (text, page_count_or_None)."""
    ext = os.path.splitext(path)[1].lower()
    kind = EXTRACTORS.get(ext)
    if kind is None:
        sys.exit(f"Unsupported file type '{ext}' for {path}. Supported: {', '.join(EXTRACTORS)}")
    if kind == "pdf":
        return pdf_to_text(path, keep_layout)
    if kind == "docx":
        return docx_to_text(path), None
    return text_passthrough(path), None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help="main document first, then supplements")
    ap.add_argument("--output", required=True, help="corpus file to write")
    ap.add_argument("--keep-layout", action="store_true")
    args = ap.parse_args()

    parts = []
    for i, p in enumerate(args.paths):
        if not os.path.isfile(p):
            sys.exit(f"Not a file: {p}")
        role = "main document" if i == 0 else "supplement"
        text, pages = extract_one(p, args.keep_layout)
        # The file marker carries the role so the audit report can say whether
        # evidence came from the main text or a supplement (STRESS allows both).
        parts.append(f"[[file: {os.path.basename(p)} | {role}]]\n{text}")
        page_info = f", {pages} pages" if pages is not None else ""
        print(f"{role}: {os.path.basename(p)} -> {len(text)} characters{page_info}")
        if len(text.strip()) < 200:
            # A near-empty result almost always means a scanned PDF without a
            # text layer; the auditor must not proceed on it silently.
            print(f"  WARNING: very little text extracted from {os.path.basename(p)}; "
                  "if this is a scanned PDF, OCR it before auditing.")

    with open(args.output, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(parts))
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
