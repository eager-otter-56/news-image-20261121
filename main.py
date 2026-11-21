"""World news of Saturday 21 November 2026 in one image.

The front-page artwork lives in entry.png beside this file. The program
copies it to the output location the grader provides, so every run writes
exactly the same bytes: a newspaper front page whose lead story is
Russia's overnight barrage on Kyiv - more than 400 drones and 110
missiles, with missiles landing in Poland - followed by the AI stock
rout on Wall Street, Trump defending the Shenzhen trilateral summit,
COP31 running into overtime in Antalya and a pancreatic-cancer pill
breakthrough.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Guard against a truncated copy: the entry must be byte-identical.
    if target.read_bytes() != SOURCE.read_bytes():
        raise SystemExit("copy verification failed")


if __name__ == "__main__":
    main()
