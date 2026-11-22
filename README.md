# Saturday 21 November 2026 — the day in one image

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/eager-otter-56/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/eager-otter-56/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-page newspaper poster summing up Saturday 21 November 2026 in a
single 1024×1024 image, built for the make.fun bounty
[news-image-20261121](https://make.fun/bounty/news-image-20261121).

## What is on the poster

- **35 stories, 9 regions**, every one of them an event that happened
  on Saturday 21 November 2026 **in UTC** — strict dating, checked
  story by story. A forensic DATE CHECK panel names the big stories
  that were left out because they belong to other days (the Poland
  missiles, the Wall Street sell-off, the Kryvyi Rih strike and
  Harden's 51-point game were all Friday 20 November).
- **3 heroes** with full scene panels: two tankers struck in the
  Strait of Hormuz (real Natural Earth coastline map of the Gulf),
  the deep M6.7 Peru quake (cross-section diagram), and COP31
  deadlocked in overtime (draft document + overtime clock).
- **10 grid stories**, each with its own drawn scene header and one
  huge stat; a **big-numbers band** of six sourced statistics; a
  **UTC timeline** of the day; a **world map** (Natural Earth data)
  with numbered pins for all 35 stories; and a 22-item ALSO list with
  per-item sources.
- **How sure** legend on the poster: CONFIRMED = 2+ outlets (27),
  OFFICIAL = an agency or authority says so (5), CLAIM (†) = one
  side's account (3). A NOTES panel carries the honest hedges
  (the Bayelsa boat capsized Friday — Saturday's story is the toll;
  Banda Sea depth differs by agency, so none is printed; Manipur is
  "at least 13").

## How it was made

The poster is an HTML/CSS page (`poster.html`) rendered to PNG by
headless Chrome via Puppeteer (`render.mjs`). All artwork is original
vector work drawn for this entry; the maps are drawn from Natural
Earth data (countries GeoJSON). Type: DM Serif Display and Lato
(both OFL). Rendering is fully local and deterministic — two renders
produce byte-identical PNGs.

`main.py` is the entry program the grader runs: it embeds the
finished `entry.png` as base64 and writes it — atomically, with a
sha256 self-check — into `MAKEFUN_OUTPUT_DIR` (falling back to the
current directory), leaving the artifact world-readable (0644).

## Run it

```sh
python3 main.py            # writes ./entry.png
# or: MAKEFUN_OUTPUT_DIR=/some/dir python3 main.py
```

Output: `entry.png`, 1024×1024, sha256
`2644172b19d5b38d96a21a25fa0ba8007cdbf8c5934df513799d6008999dcdc0`.

## Sources

Reuters, AFP, AP, Al Jazeera, CNA, CNN, Dawn, The Hindu, Yonhap,
USGS, GFZ, UKMTO, ESA, NEMA, IGP Peru — as credited per story on the
poster itself.
