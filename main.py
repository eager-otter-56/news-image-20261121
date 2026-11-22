"""Copy the bundled entry.png to /output/entry.png, byte for byte.

The copy is atomic and self-verifying: the bytes land in a temp file
inside /output first, are checked against the source (length, PNG
signature and a full byte comparison), and only then replace the
destination via os.replace, so /output/entry.png is never half-written.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")
TMP = os.path.join(DST_DIR, ".entry.png.tmp")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    with open(SRC, "rb") as fh:
        data = fh.read()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("source is not a PNG: %s" % SRC)
    os.makedirs(DST_DIR, exist_ok=True)
    with open(TMP, "wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    with open(TMP, "rb") as fh:
        back = fh.read()
    if len(back) != len(data) or back != data:
        os.unlink(TMP)
        raise SystemExit("verification failed: copy differs from source")
    os.replace(TMP, DST)
    os.chmod(DST, 0o644)
    print("wrote", DST, len(data), "bytes, verified identical")


if __name__ == "__main__":
    main()
