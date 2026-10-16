# PDF feature fixtures

Small PDFs that each exercise one thing an extractor reads beyond page text. All share the same
page text (see `generate.py`), so a test can assert on it.

| File | Contents |
| --- | --- |
| `annotations.pdf` | Text note (author, date, colour, subject), free-text box, highlight, underline, strike-out and squiggly annotations over known words, stamp, caret, three link annotations (https URI, internal destination, mailto), a square, a **hidden** note (`/F 2`), a popup, and a second-page note. |
| `attachments.pdf` | Embedded files in the `/EmbeddedFiles` name tree (`notes.txt` with a description, `table.csv` with an `AFRelationship`, `page.html`, a nested `inner.pdf`) and a file-attachment annotation on page 2 (`margin-note.txt`). |
| `portfolio.pdf` | A PDF portfolio: a `/Collection` dictionary and two member files (`cover-letter.txt`, `figures.csv`). |
| `forms.pdf` | An AcroForm with a text field, two checkboxes (on and off), a radio group, a combo box with display text distinct from export values, and a multi-select list box. |
| `outline-metadata.pdf` | A nested outline, page labels (`i`, `A-1`), the catalog `/Lang`, XMP (title, creator, rights, language, PDF/A conformance), and an Info dictionary with a non-standard entry (`Department`). |

## Provenance

Generated, not collected. `generate.py` draws the pages with ReportLab and adds the structures
with pikepdf. Regenerate with

```sh
pip install reportlab pikepdf
python3 generate.py
```

The files contain no third-party content and are released under the MIT licence, like the
generator.
