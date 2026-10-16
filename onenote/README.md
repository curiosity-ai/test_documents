# OneNote section fixtures

OneNote 2010+ section files (`.one`, MS-ONESTORE revision store) used by
[X-Ray.OneNote](https://github.com/curiosity-ai/x-ray-others/tree/main/XRay.OneNote).

## Provenance

The twelve `.one` files are the test files of the MIT-licensed open-source Python OneNote reader
that X-Ray.OneNote was ported from, copied unmodified. They are redistributed under that
project's MIT license, reproduced in [`LICENSE`](LICENSE).

| File | What it exercises |
|---|---|
| `3ImagesWithDifferentAlignment.one` | three PNG images with left, center and right alignment; six page versions |
| `AttachedFileWithTag.one` | an attached TIFF file carrying note tags |
| `FormattedRichText.one` | bold, italic, underline, highlight and hyperlink runs |
| `ImageWithTag.one` | a tagged PNG image |
| `Issue1Subpages.one` | a page and a subpage in separate page object spaces |
| `NumberedListWithTags.one` | nested numbered lists (decimal, alpha, roman) with note tags |
| `OnePageWithFile.one` | an attached file |
| `SimpleHistory.one` | a page with three text revisions (page history) |
| `SimpleImageFromSeparateFile.one` | a JPEG image |
| `SimpleTable.one` | a 4x3 table; two earlier page versions |
| `TableWithTag.one` | a tagged table with numbered lists in its cells |
| `TagSizes.one` | list items carrying note tags of different sizes |

Expected outputs (DOM dumps and PDF manifests produced by the Python reader) live with the tests
in `x-ray-others/XRay.OneNote/tests/XRay.OneNote.Tests/Goldens/`, not here.
