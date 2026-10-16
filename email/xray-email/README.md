# X-Ray.Email fixtures

EML and MSG files made for X-Ray.Email (https://github.com/curiosity-ai/x-ray-others, folder
`XRay.Email`). Each one exercises a specific part of RFC 5322 / MIME or MS-OXMSG.

- `*.eml` are written by `XRay.Email/tools/corpus/make_eml_fixtures.py`: multipart/alternative,
  mixed and related structures, nested `message/rfc822`, quoted-printable and base64 bodies,
  RFC 2047 headers in UTF-8, ISO-8859-1, KOI8-R, Windows-1251, GB2312 and ISO-2022-JP, raw UTF-8
  headers (RFC 6532), RFC 2231 file names, address groups and comments, obsolete date syntax,
  a calendar invitation, undeclared 8-bit text, a multipart without closing boundary, folded
  headers, a header-only message, an mbox separator line, binary transfer encoding and odd
  header case.
- `msg/*.msg` are written by `XRay.Email/tools/XRay.Email.CorpusGen`: some of the EML files
  above converted to MSG, plus messages built through the API (an ANSI message in code page
  1251, a CFB version 4 container, many recipients and multi-valued properties, two levels of
  embedded messages). They were checked with the independent `extract_msg` reader.

All names and addresses are made up (`example.com` and similar). Licence: MIT, see `LICENSE`.
