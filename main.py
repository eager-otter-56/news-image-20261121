#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261121.

Copies the entry.png sitting beside this file to /output/entry.png.
The copy is atomic and self-checking: the bytes are staged in a
temporary file inside /output, read back and verified (length and
PNG signature), and only then moved into place with os.replace —
so a partial or corrupt file can never land at /output/entry.png.
No network, no randomness: every run writes the same bytes.
"""
import os
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    with open(SRC, "rb") as f:
        data = f.read()
    fd, tmp = tempfile.mkstemp(dir=DST_DIR, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        with open(tmp, "rb") as f:
            staged = f.read()
        if len(staged) != len(data):
            raise ValueError("staged copy has the wrong length")
        if not staged.startswith(PNG_SIGNATURE):
            raise ValueError("staged copy is not a PNG")
        os.replace(tmp, DST)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    os.chmod(DST, 0o644)


if __name__ == "__main__":
    main()
