#!/usr/bin/env python3
"""Builds preview.html for the "Two Sides, One Strategy" component.
Usage: python3 integrated-strategy/build.py"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
partial = (HERE / "partials" / "integrated.html").read_text()
css = (HERE / "emg-integrated.css").read_text()
js = (HERE / "emg-integrated.js").read_text()

(HERE / "preview.html").write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Two Sides, One Strategy</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{ --navy: #073c72; --pink: #ec1674; --bg: #ffffff; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg: #ffffff; }} }}
:root[data-theme="dark"] {{ --bg: #ffffff; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--navy); font-family: 'Jost', 'Futura', Arial, sans-serif; }}
.section {{ max-width: 1100px; margin: 0 auto; padding: 56px 16px 72px; }}
.section h2 {{ margin: 0 0 32px; font-size: clamp(24px, 3vw, 34px); font-weight: 700; }}
.cta {{ text-align: center; margin-top: 40px; }}
.cta a {{ display: inline-block; padding: 12px 28px; border-radius: 999px; background: var(--pink); color: #fff; font-weight: 700; text-transform: uppercase; text-decoration: none; letter-spacing: .02em; }}
.spacer {{ height: 40px; }}
{css}
</style>
</head>
<body>
<section class="section">
  <h2>Two Sides of Franchise Growth, One Integrated Strategy</h2>
{partial}
  <div class="cta"><a href="#">Let’s talk about your system</a></div>
</section>
<script>
{js}
</script>
</body>
</html>
""")
print("Wrote preview.html")
