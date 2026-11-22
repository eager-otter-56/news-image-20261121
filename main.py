"""Entry program for news-image-20261121.

Copies the poster image stored beside this file to /output/entry.png.
No network, deterministic: the output bytes are exactly the source bytes.
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
        raise ValueError("source is not a PNG file")
    os.makedirs(DEST_DIR, exist_ok=True)
    # Atomic, self-verifying copy: write to a temp file in the same
    # directory, check its length and signature against the source,
    # then os.replace it into place so readers never see a partial file.
    fd, tmp_path = tempfile.mkstemp(dir=DEST_DIR, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        with open(tmp_path, "rb") as check:
            written = check.read()
        if len(written) != len(data) or not written.startswith(PNG_SIGNATURE):
            raise IOError("verification failed: temp copy does not match source")
        if written != data:
            raise IOError("verification failed: temp copy bytes differ from source")
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, DEST)
    except BaseException:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise
    print("wrote", DEST)


if __name__ == "__main__":
    main()
