# Encrypted PDFs

Eleven small PDFs encrypted with the standard security handler, one per algorithm and password
arrangement, plus the unencrypted source they were made from. They exist to check that an
extractor opens an encrypted document with the right password, refuses it with the wrong or a
missing one, and reads the same text either way.

Every file holds the same two pages (see `generate.py`), so the extracted text of any of them,
opened correctly, equals the text of `original.pdf`.

| File | Revision | Algorithm | Key | Needs |
| --- | --- | --- | --- | --- |
| `rc4-40-user.pdf` | R2 | RC4 | 40 bit | `user-pass` or `owner-pass` |
| `rc4-40-open.pdf` | R2 | RC4 | 40 bit | nothing (empty user password) |
| `rc4-128-user.pdf` | R3 | RC4 | 128 bit | `user-pass` or `owner-pass` |
| `rc4-128-open.pdf` | R3 | RC4 | 128 bit | nothing |
| `aes-128-user.pdf` | R4 | AES (AESV2) | 128 bit | `user-pass` or `owner-pass` |
| `aes-128-open.pdf` | R4 | AES (AESV2) | 128 bit | nothing |
| `aes-256-user.pdf` | R6 | AES (AESV3) | 256 bit | `user-pass` or `owner-pass` |
| `aes-256-open.pdf` | R6 | AES (AESV3) | 256 bit | nothing |
| `aes-128-cleartext-metadata.pdf` | R4 | AES (AESV2) | 128 bit | `user-pass`; XMP/metadata stream left in the clear |
| `rc4-128-v4-user.pdf` | R4 | RC4 through a V2 crypt filter | 128 bit | `user-pass` |
| `aes-256-same-passwords.pdf` | R6 | AES (AESV3) | 256 bit | `user-pass` (user and owner password are the same) |

The `*-open.pdf` files authenticate with the empty password and only restrict printing and
copying (the owner password is `owner-pass`); they are the common real-world case.

Passwords are deliberately fake: user `user-pass`, owner `owner-pass`.

## Provenance

Generated, not collected. `generate.py` draws the text with ReportLab and encrypts it with
pikepdf (qpdf). Regenerate with

```sh
pip install reportlab pikepdf
python3 generate.py
```

The files contain no third-party content and are released under the MIT licence, like the
generator.
