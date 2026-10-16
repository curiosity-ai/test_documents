#!/usr/bin/env python3
"""Regenerates the encrypted PDFs in this folder from one unencrypted source.

    pip install reportlab pikepdf
    python3 generate.py

Every file carries the same two pages of text (see README.md), so an extractor's output for
any of them has to equal its output for original.pdf. Passwords are deliberately fake and
documented in the README.
"""
import io
import os
import sys

import pikepdf
from pikepdf import Encryption, Permissions
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
USER, OWNER = "user-pass", "owner-pass"

PAGES = [
    ["Encrypted fixture, page one", "The quick brown fox jumps over the lazy dog.", "Pack my box with five dozen liquor jugs."],
    ["Encrypted fixture, page two", "Sphinx of black quartz, judge my vow.", "How vexingly quick daft zebras jump."],
]


def build_original() -> bytes:
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4, invariant=1, pageCompression=1)
    c.setTitle("Encrypted fixture")
    c.setAuthor("X-Ray test corpus")
    for lines in PAGES:
        y = 780
        for line in lines:
            c.setFont("Helvetica", 14)
            c.drawString(72, y, line)
            y -= 24
        c.showPage()
    c.save()
    return buf.getvalue()


def write(name: str, encryption, data: bytes) -> None:
    with pikepdf.open(io.BytesIO(data)) as pdf:
        pdf.save(os.path.join(HERE, name), encryption=encryption, static_id=True)
    print("wrote", name)


def main() -> None:
    original = build_original()
    with open(os.path.join(HERE, "original.pdf"), "wb") as f:
        f.write(original)

    restricted = Permissions(extract=False, print_lowres=True, print_highres=False, modify_other=False, modify_annotation=False)

    variants = {
        # name stem: (R, extra kwargs)
        "rc4-40": dict(R=2, metadata=False, aes=False),
        "rc4-128": dict(R=3, metadata=False, aes=False),
        "aes-128": dict(R=4),
        "aes-256": dict(R=6),
    }
    for stem, kw in variants.items():
        # A password is needed to open it.
        write(f"{stem}-user.pdf", Encryption(user=USER, owner=OWNER, allow=restricted, **kw), original)
        # The empty user password opens it; the owner password only restricts copy and print.
        write(f"{stem}-open.pdf", Encryption(user="", owner=OWNER, allow=restricted, **kw), original)

    # AES-128 with the XMP/metadata stream left in the clear.
    write("aes-128-cleartext-metadata.pdf",
          Encryption(user=USER, owner=OWNER, R=4, aes=True, metadata=False), original)
    # RC4-128 through the V4 crypt-filter machinery (CFM /V2).
    write("rc4-128-v4-user.pdf",
          Encryption(user=USER, owner=OWNER, R=4, aes=False, metadata=False), original)
    # Owner password equal to the user password.
    write("aes-256-same-passwords.pdf", Encryption(user=USER, owner=USER, R=6), original)


if __name__ == "__main__":
    sys.exit(main())
