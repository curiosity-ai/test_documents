# HTML goldens for the OneNote fixtures

One file per `.one` fixture in the parent folder, named after it (`SimpleTable.one` ->
`SimpleTable.html`). Each holds the whole section as one HTML document, written by the X-Ray.OneNote
HTML writer (`HtmlSaveOptions { PerPage = false }`).

These are **this package's own output**, reviewed by eye, not output of any third-party library, so they
pin the writer's behaviour (regressions) and say nothing about parity with another implementation.

To keep them small, pictures are not embedded: the image callback writes placeholder sources
`img-<n>.<ext>`, where `<n>` counts pictures across the whole save from 0. The output is deterministic
(UTF-8, `\n` line endings, no timestamps).

The golden test is in `XRay.OneNote/tests/XRay.OneNote.Tests/HtmlWriterTests.cs` in
curiosity-ai/x-ray-others. It compares ignoring line-ending differences and skips when this folder
is missing. To regenerate after an intended change, run the tests with `XRAY_ONENOTE_UPDATE_GOLDENS=1` and
review the diff. To compare against reference output from elsewhere, place files under the same names in a
copy of this folder and point `XRAY_TEST_DOCUMENTS` at it; expect differences in markup, so compare text
content rather than bytes.
