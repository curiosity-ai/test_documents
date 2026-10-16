# PostScript and EPS fixtures

PostScript (`.ps`) and Encapsulated PostScript (`.eps`) documents used by
[X-Ray.PS](https://github.com/curiosity-ai/x-ray-others/tree/main/XRay.PS).

## Provenance

These are the test data of the MIT-licensed open-source Python PostScript/XPS library that X-Ray.PS
was ported from (its `testdata/ps/` folder), copied with the folder structure kept. They are
redistributed under that project's MIT license, reproduced in [`LICENSE.txt`](LICENSE.txt).

| Folder | Contents |
|---|---|
| `functional/` | per-chapter language and graphics test programs (arcs, clipping, color, fonts, forms, images, operators, lines, paths, patterns, text, transforms) |
| `integration/` | larger real-world PS and EPS files (gradients, embedded TrueType and Type 1 fonts, CJK text, images) |
| `images/` | PNG, JPEG, TIFF and BMP inputs for the image-to-EPS converter |
| `xmp/` | EPS files carrying XMP metadata packets |
| `baseline/ps2pdf/`, `baseline/ps2image/` | reference renders (PNG) of the inputs above, as shipped by the original project |

## What was left out

- `necessary_fonts/` of the original: commercial fonts (Helvetica, Palatino, Optima, Myriad, Arial
  Unicode, ITC Zapf Dingbats, and others) whose licenses do not allow redistribution. Tests that
  need them take a font folder from the environment; without it the bundled Liberation fonts and
  the system fonts stand in, which changes glyph shapes but not the document structure.

The files are otherwise unmodified.
