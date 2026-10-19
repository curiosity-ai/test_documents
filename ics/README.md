# iCalendar fixtures (`ics/`)

Calendar files (`.ics`, iCalendar RFC 5545 and vCalendar 1.0) used by the tests of X-Ray.Ics
(`x-ray-others/XRay.Ics`). Each folder is one source, with its own licence and `README.md`:

| Folder | Source | Licence |
|---|---|---|
| `xray-ics/` | hand-written for X-Ray.Ics, one tricky case per file (encodings, line folding, time zones, recurrence, attendees, attachments, vCalendar 1.0, malformed input) | MIT, Curiosity GmbH |
| `icalendar-py/` | test files and fuzzing corpus of the python `icalendar` library | BSD-2-Clause |
| `ical-net/` | test files of the Ical.Net library | MIT |

`.gitattributes` marks the files binary: line endings, byte order marks and code pages are part of them.
The expected fields of every file are in `XRay.Ics/tests/XRay.Ics.Tests/Corpus/ics-manifest.json`,
built by `XRay.Ics/tools/corpus/build_manifest.py` from independent readers.
