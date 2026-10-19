# HTML preview fixtures

Hand-written messages used by the X-Ray.Email HTML preview tests
(`XRay.Email/tests/XRay.Email.Tests/Goldens/html`). All names and addresses are made up.

- `script-and-handlers.eml`: an HTML body with `script` elements, event handler attributes,
  `javascript:` URLs (plain and obfuscated), an iframe, an object, an svg, a form, CSS
  `expression()` and `@import`, a base element and a meta refresh.
- `inline-images-cid.eml`: a related part with two images referenced by `cid:` (one with a
  percent-escaped id), one referenced by `Content-Location`, one reference that resolves to
  nothing, and a `cid:` URL inside CSS; plus an ordinary attachment.
- `plain-text-urls.eml`: a plain text body with markup characters, indentation, tabs, URLs and a Bcc.
- `rtf-encapsulated-html.msg`, `rtf-formatted.msg`: MSG files whose only body is RTF: HTML
  encapsulated per MS-OXRTFEX, and a Word-style RTF with character formatting, a colour table,
  a hyperlink field, a table and Unicode text. Written by `XRay.Email/tools/XRay.Email.CorpusGen`.

Licence: MIT, same as the sibling `xray-email` fixtures; see `../LICENSE`.
