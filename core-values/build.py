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
    """<g class="i-flag"><line x1="34" y1="44" x2="34" y2="12"/><path d="M34 12 H48 L44 18 L48 24 H34" class="fill-accent"/></g>
       <path class="i-road" pathLength="100" d="M4 44 H58"/>
       <path class="i-tip" d="M52 38 L58 44 L52 50"/>
       <path d="M8 52 H14 M20 52 H26" opacity=".45"/>""",
    # 02 Creative: a pen draws a squiggle and sparkles pop
    """<path class="i-squiggle" pathLength="100" d="M8 46 C14 34 20 34 22 42 S30 50 34 38 S42 28 46 36"/>
       <path class="i-spark i-spark-1 fill-accent" d="M50 8 l2.2 5.8 5.8 2.2 -5.8 2.2 -2.2 5.8 -2.2 -5.8 -5.8 -2.2 5.8 -2.2z"/>
       <path class="i-spark i-spark-2 fill-accent" d="M18 10 l1.5 3.8 3.8 1.5 -3.8 1.5 -1.5 3.8 -1.5 -3.8 -3.8 -1.5 3.8 -1.5z"/>
       <path class="i-spark i-spark-3 fill-accent" d="M54 40 l1.3 3.2 3.2 1.3 -3.2 1.3 -1.3 3.2 -1.3 -3.2 -3.2 -1.3 3.2 -1.3z"/>""",
    # 03 Passion: a heart beats
    """<path class="i-heart" d="M32 52 C20 43 9 35 9 23 A11 11 0 0 1 32 17 A11 11 0 0 1 55 23 C55 35 44 43 32 52Z"/>
       <path class="i-ray i-ray-1" d="M32 6 V2"/><path class="i-ray i-ray-2" d="M12 9 L9 6"/><path class="i-ray i-ray-3" d="M52 9 L55 6"/>""",
    # 04 Responsive: chat bubbles, the reply is typing
    """<path class="i-bubble i-bubble-1" d="M8 12 H38 A4 4 0 0 1 42 16 V28 A4 4 0 0 1 38 32 H18 L11 38 V32 H8 A4 4 0 0 1 4 28 V16 A4 4 0 0 1 8 12Z"/>
       <path class="i-bubble i-bubble-2 fill-soft" d="M26 34 H56 A4 4 0 0 1 60 38 V50 A4 4 0 0 1 56 54 H53 V60 L46 54 H26 A4 4 0 0 1 22 50 V38 A4 4 0 0 1 26 34Z"/>
       <circle class="i-dot i-dot-1 fill-accent" cx="33" cy="44" r="2.6"/>
       <circle class="i-dot i-dot-2 fill-accent" cx="41" cy="44" r="2.6"/>
       <circle class="i-dot i-dot-3 fill-accent" cx="49" cy="44" r="2.6"/>""",
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
					<span class="emgv-num">{v['num']}</span>
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
