# XPS fixtures

XML Paper Specification (`.xps`) documents used by
[X-Ray.PS](https://github.com/curiosity-ai/x-ray-others/tree/main/XRay.PS), which reads, edits and
renders XPS as well as PostScript.

## Provenance

These are the test data of the MIT-licensed open-source Python PostScript/XPS library that X-Ray.PS
was ported from (its `testdata/xps/` folder), copied with the folder structure kept. They are
redistributed under that project's MIT license, reproduced in [`LICENSE.txt`](LICENSE.txt).

| Folder | Contents |
|---|---|
| `integration/` | XPS documents: brushes, gradients, opacity masks, glyph runs with embedded (obfuscated) fonts, images (PNG, JPEG, TIFF, JPEG XR), print tickets, transforms |
| `resources/` | images used when building XPS documents in tests |
| `baseline/xps2pdf/`, `baseline/xps2image/` | reference renders (PNG) of the inputs, as shipped by the original project |

## Changes from the original

- `integration/epersonenbrief_Aspose.xps` and its four baseline PNGs were renamed to
  `epersonenbrief.xps`, `epersonenbrief_1.png` and `epersonenbrief_2.png`, dropping a vendor name
  from the file names. The contents are unchanged.
- `resources/arialbd.ttf` (Arial Bold, a commercial font) is not included; its license does not
  allow redistribution.
- `resources/uswebuncoated.icc` (an Adobe CMYK profile under Adobe's own profile license) is not
  included. No test reads it.

The files are otherwise unmodified.
