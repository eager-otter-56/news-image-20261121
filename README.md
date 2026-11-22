# Saturday 21 November 2026 — the day in one image

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/eager-otter-56/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/eager-otter-56/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-page newspaper poster summing up Saturday 21 November 2026 in a
single 1024×1024 image: **37 stories, 9 regions** — 28 CONFIRMED,
5 OFFICIAL, 4 CLAIM.

## What the poster shows

- **Masthead and region strip** — the day, the standfirst, and the
  nine regions with their story counts (Middle East 8, Europe 7,
  North America 5, South Asia 4, Global 4, East Asia 3, South
  America 2, Africa 2, Southeast Asia 2).
- **Timeline** — the day on a real UTC axis: 00:09 the M6.7 Junín
  quake, 05:00 the first tanker hit off Khasab, c.06:50 the Sparta II
  strike, 09:42 the M6.8 Banda Sea quake, c.12:12 the EU–Indonesia
  signing, 18:24 BepiColombo's Mercury orbit insertion.
- **Big numbers** — 98.5% of tariff lines, 730m people, 130+
  countries, 128 states, 37–12, 82,500 marchers, each with its source.
- **Three heroes, drawn as scenes** — a real coastline map of the
  Strait of Hormuz with the two tanker strikes marked; a cross-section
  of the deep Peru quake (epicentre ≈129 km down); COP31's calendar
  strip running to a 13th day, with the draft's struck-through
  "fossil fuels" and a 1.5° thermometer.
- **Ten grid cards**, every one with its own drawn visual header and
  big stat: Sparta II ablaze, the EU–Indonesia pact, the Geneva
  killer-robot talks, the Banda Sea quake, the capture of "El Chapo
  Isidro", Manipur's tainted liquor, the Bayelsa boat toll, England's
  record win over the All Blacks, BTS's five-award MAMA haul, and
  France's sixth straight Saturday of marches.
- **Where It Happened** — a world map with a numbered pin for every
  one of the 37 stories, and an ALSO list of the remaining 24, each
  with its own source credit († marks a one-sided CLAIM).

## The strict-UTC method

A story counts only if the event itself happened on Saturday
21 November 2026 **in UTC** — "first reported on Saturday" is not
enough. That rule is enforced visibly in the poster's DATE CHECK:
the Russian missiles in Poland, the Wall Street tech sell-off, the
Kryvyi Rih double-tap strike and Harden's 51-point game were all
Friday 20 November, the Shenzhen summit was Thursday 19 November,
and the Las Vegas Grand Prix falls on Sunday 22 November — all are
named and left out. Hedges are printed, not hidden: the Bayelsa boat
capsized on Friday, so Saturday's story is NEMA's toll reaching 24;
the Banda Sea depth differs by agency (117–143 km), so no depth is
printed; Manipur's toll is "at least 13" because counts moved during
the day; two of BTS's five awards were won on Friday night, and the
poster says Saturday's Album of the Year *completed* the haul.

Statuses: **CONFIRMED** = two or more outlets, **OFFICIAL** = an
agency or authority says so, **CLAIM** = one side's account.

Sources: Reuters, AFP, AP, Al Jazeera, CNA, CNN, Dawn, The Hindu,
Yonhap, USGS, UKMTO, ESA, NEMA and the others named beside each story.

## How it was made

The poster is an HTML/CSS page (`poster.html`) rendered to PNG by
headless Chrome via Puppeteer (`render.mjs`) — no PIL, no raster
drawing. The maps are real geography: country polygons derived from
Natural Earth, projected and drawn as SVG in the page, with a zoomed
Gulf coastline for the Hormuz hero. Type is DM Serif Display and Lato
(both OFL). All scene drawings — the quake cross-section, the ship,
the robot, the COP31 calendar and thermometer, and every card icon —
are original vector work drawn for this poster. Rendering is fully
offline (local fonts and map data only) and deterministic: two runs
of `node render.mjs` produce byte-identical PNGs.

`main.py` is the entry program: it embeds the finished PNG as base64
and, when run, writes `./entry.png` through an atomic, self-verifying
copy (temp file, SHA-256 check against the embedded digest, then
`os.replace`).

## Licences and credits

- Map data: Natural Earth (public domain), via the world.geo.json
  country collection derived from it.
- Fonts: DM Serif Display and Lato, SIL Open Font License 1.1.
- All other artwork and text: original to this entry.
