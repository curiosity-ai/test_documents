# python icalendar sample files

`.ics` files from the test suite and fuzzing corpus of the `icalendar` Python library.

- Source: https://github.com/collective/icalendar, folders `src/icalendar/tests/{calendars,events,alarms,freebusy,journals,todos,timezones,availabilities}` and `src/icalendar/fuzzing/corpus`
- Commit: `bfa0e10f27cd63d6d1ff66f1bda39526ba9e6451` (2026-10-15)
- Licence: BSD-2-Clause, Copyright (c) 2012-2013 Plone Foundation, see `LICENSE.rst` (copied from the repository root).

Only the `.ics` files are included, unchanged, in their original relative folders. Some are deliberately
malformed (the fuzzing corpus and the `issue_*` regression files). Used by X-Ray.Ics' corpus tests.
