# MimeKit test messages

MIME messages from the unit-test data of MimeKit by Jeffrey Stedfast and the .NET Foundation.

- Source: https://github.com/jstedfast/MimeKit, folder `UnitTests/TestData/messages`
- Commit: `d7fc9633e987e0259f58cbfe3f82a6f10106fd24` (2026-10-16)
- Licence: MIT, see `LICENSE` (copied from the repository root).

The files are unchanged; those named `*.txt` upstream were renamed to `*.eml`. The
`*.anonymized.eml` duplicates were left out. The set covers delivery-status and disposition
reports, digests, embedded messages, MHTML, ISO-2022-JP, format=flowed, preamble/epilogue
handling, an empty multipart, a type without subtype, and `stack-overflow.eml` (very deep
nesting). Used by X-Ray.Email's corpus tests.
