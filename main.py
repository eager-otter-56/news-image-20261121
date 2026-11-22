#!/usr/bin/env python3
"""Place the finished poster at /output/entry.png, atomically.

The image itself is composed by compose.py and shipped beside this
file as entry.png. This script reads those bytes, writes them to a
temporary file inside /output, verifies the copy (same length and a
valid PNG signature) and only then swaps it into place with
os.replace, so a reader can never observe a half-written file and
the output bytes are exactly the shipped bytes.
"""
import os
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main():
    with open(SOURCE, "rb") as fh:
        data = fh.read()
    if not data.startswith(PNG_SIGNATURE):
        raise ValueError("source entry.png does not start with a PNG "
                         "signature")

    os.makedirs(DEST_DIR, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=DEST_DIR, prefix=".entry-",
                                    suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        with open(tmp_path, "rb") as check:
            written = check.read()
        if len(written) != len(data):
            raise IOError("length mismatch while copying entry.png")
        if not written.startswith(PNG_SIGNATURE):
            raise IOError("copied file lost its PNG signature")
        if written != data:
            raise IOError("copied bytes differ from the source poster")
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, DEST)
    except BaseException:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise
    print("wrote", DEST, len(data), "bytes")


if __name__ == "__main__":
    main()
