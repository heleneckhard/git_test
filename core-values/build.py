#!/usr/bin/env python3
"""Builds the Core Values tiles.

values.json holds the six values exactly as they appear on the Why Us page
(number, title, body HTML). This script wraps them in the tile markup with an
animated icon each and writes:

  partials/values.html  drop-in replacement for the carousel
  preview.html          standalone page for review

Usage: python3 core-values/build.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
VALUES = json.loads((HERE / "values.json").read_text())

# One line icon per value (64x64). Classes starting with i- are animated in emg-values.css.
ICONS = [
    # 01 Extra mile: the path runs straight past the finish flag and keeps going
    """<path class="i-road" pathLength="100" d="M4 46 H58"/>
       <path class="i-tip" d="M52 40 L58 46 L52 52"/>
       <path d="M8 54 H14 M20 54 H26" opacity=".45"/>
       <g class="i-flag"><path class="i-pennant fill-accent" d="M34 10 H48 L44 16 L48 22 H34 Z"/><line x1="34" y1="46" x2="34" y2="6"/></g>""",
    # 02 Creative: a paint palette fills with color while the brush dabs
    """<path d="M30 8 C16 8 6 18 6 31 C6 44 16 55 28 55 C33 55 34 51 32 48 C30 45 32 41 36 41 H44 C51 41 56 36 56 29 C56 17 44 8 30 8 Z"/>
       <circle class="i-well i-well-1 fill-accent" cx="17" cy="28" r="4.5"/>
       <circle class="i-well i-well-2 w-teal" cx="22" cy="17" r="4.5"/>
       <circle class="i-well i-well-3 w-blue" cx="33" cy="14" r="4.5"/>
       <g class="i-brush"><path d="M60 4 L45 25" stroke-width="4"/><path class="fill-accent" d="M45 25 C41 26 38 30 39 35 C44 35 47 32 47.5 28 Z" stroke-width="2"/></g>
       <path class="i-spark fill-accent" d="M50 47 l1.5 3.8 3.8 1.5 -3.8 1.5 -1.5 3.8 -1.5 -3.8 -3.8 -1.5 3.8 -1.5z"/>""",
    # 03 Passion: a heart beats
    """<path class="i-heart" d="M32 54 C32 54 8 40 8 23 C8 15 14 10 21 10 C26 10 30 13 32 17 C34 13 38 10 43 10 C50 10 56 15 56 23 C56 40 32 54 32 54 Z"/>
       <path class="i-ray i-ray-1" d="M32 6 V2"/><path class="i-ray i-ray-2" d="M12 8 L9 5"/><path class="i-ray i-ray-3" d="M52 8 L55 5"/>""",
    # 04 Responsive: chat bubbles, the reply is typing
    """<path class="i-bubble i-bubble-1" d="M7 4 H33 A4 4 0 0 1 37 8 V19 A4 4 0 0 1 33 23 H16 L9 29 V23 H7 A4 4 0 0 1 3 19 V8 A4 4 0 0 1 7 4 Z"/>
       <path class="i-bubble i-bubble-2 fill-soft" d="M27 34 H57 A4 4 0 0 1 61 38 V50 A4 4 0 0 1 57 54 H54 V60 L47 54 H27 A4 4 0 0 1 23 50 V38 A4 4 0 0 1 27 34 Z"/>
       <circle class="i-dot i-dot-1 fill-accent" cx="34" cy="44" r="2.6"/>
       <circle class="i-dot i-dot-2 fill-accent" cx="42" cy="44" r="2.6"/>
       <circle class="i-dot i-dot-3 fill-accent" cx="50" cy="44" r="2.6"/>""",
    # 05 Numbers driven: the chart ticks up, then gets checked again
    """<path d="M10 10 V54 H58"/>
       <path class="i-line" pathLength="100" d="M16 46 L28 36 L38 40 L52 22"/>
       <circle class="i-point fill-accent" cx="52" cy="22" r="3.5"/>
       <g class="i-check"><circle cx="24" cy="18" r="8" class="fill-accent"/><path d="M20.5 18.2 l2.5 2.5 4.5-5"/></g>""",
    # 06 Laugh: a grin that bounces
    """<g class="i-face"><circle cx="32" cy="32" r="24"/>
       <path class="i-eye" d="M21 27 q3 -4 6 0"/><path class="i-eye" d="M37 27 q3 -4 6 0"/>
       <path class="i-mouth fill-soft" d="M20 36 H44 A12 12 0 0 1 20 36Z"/></g>""",
]


def tile(i, v):
    n = i + 1
    return f"""		<div class="emgv-tile{' is-active' if i == 0 else ''}" data-value="{n}">
			<h3 class="emgv-head">
				<button type="button" class="emgv-btn" id="emgv-btn-{n}" aria-expanded="{'true' if i == 0 else 'false'}" aria-controls="emgv-body-{n}">
					<svg class="emgv-icon emgv-icon-{n}" viewBox="0 0 64 64" aria-hidden="true" focusable="false">
						{ICONS[i]}
					</svg>
					<span class="emgv-title">{v['title']}</span>
					<span class="emgv-plus" aria-hidden="true"></span>
				</button>
			</h3>
			<div class="emgv-body" id="emgv-body-{n}" role="region" aria-labelledby="emgv-btn-{n}">
				<div class="emgv-body-inner">
					{v['body']}
				</div>
			</div>
		</div>"""


rows = [VALUES[0:3], VALUES[3:6]]
parts = []
for r, row in enumerate(rows):
    parts.append('\t<div class="emgv-row">\n' + "\n".join(tile(r * 3 + i, v) for i, v in enumerate(row)) + "\n\t</div>")

partial = (
    "<!-- EMG Core Values: six tiles, one open at a time. Replaces the image-content-slider carousel.\n"
    "     Needs emg-values.css and emg-values.js. Without JS every tile shows its full text. -->\n"
    '<div class="emgv">\n' + "\n".join(parts) + "\n</div>\n"
)
(HERE / "partials" / "values.html").write_text(partial)

css = (HERE / "emg-values.css").read_text()
js = (HERE / "emg-values.js").read_text()
preview = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Core Values Tiles</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{ --navy: #073c72; --pink: #ec1674; --bg: #ffffff; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg: #ffffff; }} }}
:root[data-theme="dark"] {{ --bg: #ffffff; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--navy); font-family: 'Jost', 'Futura', Arial, sans-serif; }}
.section {{ max-width: 1240px; margin: 0 auto; padding: 64px 16px 80px; }}
.heading {{ text-align: center; margin: 0 0 48px; text-transform: uppercase; line-height: 1.05; }}
.heading small {{ display: block; font-size: clamp(22px, 3vw, 38px); font-weight: 400; }}
.heading strong {{ display: inline-block; font-size: clamp(28px, 4vw, 52px); font-weight: 700; border-bottom: 4px solid var(--pink); padding-bottom: 4px; }}
{css}
</style>
</head>
<body>
<section class="section">
  <h2 class="heading"><small>Learn More About the Elysium Way</small><strong>With Our Core Values</strong></h2>
{partial}
</section>
<script>
{js}
</script>
</body>
</html>
"""
(HERE / "preview.html").write_text(preview)
print("Wrote partials/values.html and preview.html")
