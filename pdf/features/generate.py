#!/usr/bin/env python3
"""Regenerates the PDFs in this folder.

    pip install reportlab pikepdf
    python3 generate.py

Each file exercises one PDF feature the extractor reads beyond page text: annotations,
attachments, portfolios, form fields, outlines and metadata. The text on the pages is fixed so
the tests can assert on it; see README.md for what each file contains.
"""
import io
import os
import sys

import pikepdf
from pikepdf import Array, Dictionary, Name, Pdf, String
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
FONT, SIZE = "Helvetica", 14
PAGE_H = A4[1]

TEXT = [
    ["Quarterly report", "Revenue grew strongly in the third quarter.", "Costs were held flat across all regions."],
    ["Outlook", "We expect continued growth next year.", "Hiring will resume in the spring."],
]


def line_box(page_lines, page, line, first_word, last_word):
    """Rectangle (x0, y0, x1, y1) covering words first_word..last_word of one drawn line."""
    y = PAGE_H - 72 - line * 24
    words = TEXT[page][line].split(" ")
    x0 = 72 + stringWidth(" ".join(words[:first_word]) + (" " if first_word else ""), FONT, SIZE)
    x1 = 72 + stringWidth(" ".join(words[: last_word + 1]), FONT, SIZE)
    return (x0, y - 3, x1, y + SIZE - 2)


def base_pdf(extra_pages=0) -> bytes:
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4, invariant=1, pageCompression=1)
    c.setTitle("Feature fixture")
    for lines in TEXT:
        for i, line in enumerate(lines):
            c.setFont(FONT, SIZE)
            c.drawString(72, PAGE_H - 72 - i * 24, line)
        c.showPage()
    c.save()
    return buf.getvalue()


def quad(box):
    x0, y0, x1, y1 = box
    return Array([x0, y1, x1, y1, x0, y0, x1, y0])


def annot(pdf, **entries):
    return pdf.make_indirect(Dictionary(Type=Name.Annot, **entries))


def write_annotations():
    pdf = Pdf.open(io.BytesIO(base_pdf()))
    p1, p2 = pdf.pages[0], pdf.pages[1]
    page2_ref = p2.obj

    hl = line_box(TEXT, 0, 1, 0, 2)          # "Revenue grew strongly"
    ul = line_box(TEXT, 0, 2, 0, 1)          # "Costs were"
    so = line_box(TEXT, 0, 2, 4, 6)          # "across all regions."
    sq = line_box(TEXT, 0, 1, 4, 6)          # "the third quarter."

    annots1 = [
        annot(pdf, Subtype=Name.Text, Rect=Array([400, 700, 420, 720]), Contents=String("Check these numbers with finance."),
              T=String("Alice"), M=String("D:20240115120000Z"), C=Array([1, 1, 0]), Subj=String("Review"), F=4),
        annot(pdf, Subtype=Name.FreeText, Rect=Array([300, 600, 520, 660]), Contents=String("Free text callout"),
              DA=String("/Helv 12 Tf 0 g"), T=String("Bob"), F=4),
        annot(pdf, Subtype=Name.Highlight, Rect=Array(list(hl)), QuadPoints=quad(hl), C=Array([1, 0.9, 0]),
              Contents=String("Important sentence"), T=String("Carol"), M=String("D:20240201090000+01'00'"), F=4),
        annot(pdf, Subtype=Name.Underline, Rect=Array(list(ul)), QuadPoints=quad(ul), C=Array([0, 0, 1]), T=String("Carol"), F=4),
        annot(pdf, Subtype=Name.StrikeOut, Rect=Array(list(so)), QuadPoints=quad(so), C=Array([1, 0, 0]), T=String("Dave"), F=4),
        annot(pdf, Subtype=Name.Squiggly, Rect=Array(list(sq)), QuadPoints=quad(sq), C=Array([0.5]), T=String("Dave"), F=4),
        annot(pdf, Subtype=Name.Stamp, Rect=Array([400, 300, 500, 340]), Name=Name.Approved,
              Contents=String("Approved by management"), F=4),
        annot(pdf, Subtype=Name.Caret, Rect=Array([200, 500, 210, 510]), Contents=String("insert a word here"), T=String("Eve"), F=4),
        annot(pdf, Subtype=Name.Link, Rect=Array([72, 100, 250, 120]), Border=Array([0, 0, 0]),
              A=Dictionary(S=Name.URI, URI=String("https://example.com/report?q=1")), F=4),
        annot(pdf, Subtype=Name.Link, Rect=Array([72, 130, 250, 150]), Border=Array([0, 0, 0]),
              Dest=Array([page2_ref, Name.Fit]), F=4),
        annot(pdf, Subtype=Name.Link, Rect=Array([72, 160, 250, 180]), Border=Array([0, 0, 0]),
              A=Dictionary(S=Name.URI, URI=String("mailto:team@example.com")), F=4),
        annot(pdf, Subtype=Name.Square, Rect=Array([300, 400, 360, 440]), Contents=String("Boxed region"), T=String("Frank"), F=4),
        # Hidden annotation: carries text, but a viewer never draws it.
        annot(pdf, Subtype=Name.Text, Rect=Array([10, 10, 30, 30]), Contents=String("Hidden note"), F=2),
    ]
    popup = annot(pdf, Subtype=Name.Popup, Rect=Array([430, 700, 600, 780]), Open=True)
    annots1[0]["/Popup"] = popup
    annots1.append(popup)
    p1["/Annots"] = Array(annots1)

    p2["/Annots"] = Array([
        annot(pdf, Subtype=Name.Text, Rect=Array([100, 600, 120, 620]), Contents=String("Second page note"), T=String("Grace"),
              M=String("D:20240301000000Z"), F=4),
    ])
    pdf.save(os.path.join(HERE, "annotations.pdf"), static_id=True)
    print("wrote annotations.pdf")


def stream(pdf, data: bytes, subtype=None, **params):
    s = pikepdf.Stream(pdf, data)
    s["/Type"] = Name.EmbeddedFile
    if subtype:
        s["/Subtype"] = Name("/" + subtype)
    s["/Params"] = Dictionary(Size=len(data), **params)
    return pdf.make_indirect(s)


def filespec(pdf, name, data, relationship=None, desc=None, subtype=None):
    f = stream(pdf, data, subtype, CreationDate=String("D:20240101000000Z"), ModDate=String("D:20240202000000Z"))
    spec = Dictionary(Type=Name.Filespec, F=String(name), UF=String(name), EF=Dictionary(F=f, UF=f))
    if relationship:
        spec["/AFRelationship"] = Name("/" + relationship)
    if desc:
        spec["/Desc"] = String(desc)
    return pdf.make_indirect(spec)


def add_names(pdf, pairs, kids=False):
    items = []
    for name, spec in pairs:
        items += [String(name), spec]
    tree = Dictionary(Names=Array(items))
    if "/Names" not in pdf.Root:
        pdf.Root["/Names"] = Dictionary()
    pdf.Root.Names["/EmbeddedFiles"] = pdf.make_indirect(tree)


def write_attachments():
    pdf = Pdf.open(io.BytesIO(base_pdf()))
    notes = filespec(pdf, "notes.txt", b"Attachment notes: the budget was approved on Monday.\n", desc="Meeting notes", subtype="text/plain")
    table = filespec(pdf, "table.csv", b"region,revenue\nnorth,10\nsouth,20\n", relationship="Data", subtype="text/csv")
    page = filespec(pdf, "page.html", b"<html><body><h1>Embedded page</h1><p>Hello from HTML.</p></body></html>", subtype="text/html")
    inner = Pdf.open(io.BytesIO(base_pdf()))
    ib = io.BytesIO(); inner.save(ib)
    nested = filespec(pdf, "inner.pdf", ib.getvalue(), subtype="application/pdf")
    # Names must be in sorted order for a valid name tree.
    add_names(pdf, sorted([("inner.pdf", nested), ("notes.txt", notes), ("page.html", page), ("table.csv", table)]))

    # A file-attachment annotation on page 2, with its own file.
    ann_file = filespec(pdf, "margin-note.txt", b"A note attached to a paperclip icon.\n", subtype="text/plain")
    pdf.pages[1]["/Annots"] = Array([
        annot(pdf, Subtype=Name.FileAttachment, Rect=Array([50, 700, 70, 720]), Name=Name.Paperclip,
              Contents=String("Paperclip"), FS=ann_file, F=4),
    ])
    pdf.save(os.path.join(HERE, "attachments.pdf"), static_id=True)
    print("wrote attachments.pdf")


def write_portfolio():
    pdf = Pdf.open(io.BytesIO(base_pdf()))
    a = filespec(pdf, "cover-letter.txt", b"Cover letter text of the portfolio.\n", subtype="text/plain")
    b = filespec(pdf, "figures.csv", b"year,value\n2023,1\n2024,2\n", subtype="text/csv")
    add_names(pdf, sorted([("cover-letter.txt", a), ("figures.csv", b)]))
    pdf.Root["/Collection"] = Dictionary(Type=Name.Collection, View=Name.D,
                                         Schema=Dictionary(Type=Name.CollectionSchema))
    pdf.save(os.path.join(HERE, "portfolio.pdf"), static_id=True)
    print("wrote portfolio.pdf")


def write_forms():
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4, invariant=1)
    c.setFont(FONT, SIZE)
    c.drawString(72, 780, "Application form")
    form = c.acroForm
    form.textfield(name="full_name", tooltip="Name", x=72, y=700, width=200, height=20, value="Ada Lovelace", borderStyle="inset")
    form.checkbox(name="subscribe", tooltip="Subscribe", x=72, y=660, size=16, checked=True)
    form.checkbox(name="terms", tooltip="Terms", x=72, y=630, size=16, checked=False)
    form.radio(name="size", tooltip="Small", value="small", selected=False, x=72, y=590, size=14)
    form.radio(name="size", tooltip="Large", value="large", selected=True, x=120, y=590, size=14)
    form.choice(name="country", tooltip="Country", value="Germany", options=[("Germany", "DE"), ("France", "FR")],
                x=72, y=540, width=150, height=20, fieldFlags="combo")
    form.listbox(name="topics", tooltip="Topics", value=["a", "c"], options=[("Alpha", "a"), ("Beta", "b"), ("Gamma", "c")],
                 x=72, y=440, width=150, height=60, fieldFlags="multiSelect")
    c.showPage()
    c.save()
    pdf = Pdf.open(io.BytesIO(buf.getvalue()))
    pdf.save(os.path.join(HERE, "forms.pdf"), static_id=True)
    print("wrote forms.pdf")


def write_outline_and_metadata():
    pdf = Pdf.open(io.BytesIO(base_pdf()))
    with pdf.open_outline() as outline:
        part1 = pikepdf.OutlineItem("Quarterly report", 0)
        part1.children.append(pikepdf.OutlineItem("Revenue", 0))
        part1.children.append(pikepdf.OutlineItem("Costs", 0))
        part2 = pikepdf.OutlineItem("Outlook", 1)
        outline.root.extend([part1, part2])
    pdf.Root["/PageLabels"] = Dictionary(Nums=Array([
        0, Dictionary(S=Name.r), 1, Dictionary(S=Name.D, St=1, P=String("A-")),
    ]))
    pdf.Root["/Lang"] = String("en-GB")
    with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
        meta["dc:title"] = "Feature fixture, XMP title"
        meta["dc:creator"] = ["XMP Author"]
        meta["dc:rights"] = "(c) Example Corp"
        meta["dc:language"] = ["en-GB"]
        meta["pdfaid:part"] = "1"
        meta["pdfaid:conformance"] = "B"
    pdf.docinfo["/Title"] = String("Feature fixture")
    pdf.docinfo["/Author"] = String("Info Author")
    pdf.docinfo["/Subject"] = String("Feature test")
    pdf.docinfo["/Keywords"] = String("pdf, outline; metadata")
    pdf.docinfo["/Creator"] = String("generate.py")
    pdf.docinfo["/Producer"] = String("pikepdf")
    pdf.docinfo["/CreationDate"] = String("D:20240115120000Z")
    pdf.docinfo["/ModDate"] = String("D:20240116130000Z")
    pdf.docinfo["/Department"] = String("Finance")
    pdf.save(os.path.join(HERE, "outline-metadata.pdf"), static_id=True)
    print("wrote outline-metadata.pdf")


def main():
    write_annotations()
    write_attachments()
    write_portfolio()
    write_forms()
    write_outline_and_metadata()


if __name__ == "__main__":
    sys.exit(main())
