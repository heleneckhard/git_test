// Builds preview.html: all three graphics inlined in a mock of the
// site's media-content section, for review before installing in WordPress.
// Usage: node motion-graphics/build-preview.js
const fs = require('fs');
const path = require('path');

const dir = __dirname;
const read = (f) => fs.readFileSync(path.join(dir, f), 'utf8');
const css = read('emg-motion.css');
const js = read('emg-motion.js');

const sections = [
  {
    file: 'partials/web-design.html',
    page: 'Web Design',
    replaces: 'Replaces the current "elloop" process animation',
    title: '<span class="pink">Our Website</span><br>Development Process',
    body: 'Every Elysium website starts with strategy. Before design begins, we interview your key stakeholders, study your audience and competitors, and create a sitemap. From there, copy, design, and development run in parallel.',
  },
  {
    file: 'partials/digital-marketing.html',
    page: 'Digital Marketing',
    replaces: 'Replaces marketing-circle@2x-1.webp',
    title: '<span class="pink">Full-Funnel Marketing</span><br>Built Around Your Business',
    body: 'With Elysium, your paid advertising strategists, organic marketing specialists, and lifecycle marketers all work as an integrated team to fuel one continuous growth loop.',
  },
  {
    file: 'partials/public-relations.html',
    page: 'Public Relations',
    replaces: 'Replaces public-relations-graphic.webp',
    title: 'Is Earned Media Missing<br>From Your Strategy?',
    body: 'Through traditional press coverage, thought leadership, brand storytelling, and influencer partnerships, we tell your brand’s stories intentionally.',
  },
];

const blocks = sections.map((s) => `
<section class="demo">
  <p class="demo__tag">${s.page} <span>· ${s.replaces}</span></p>
  <div class="demo__row">
    <div class="demo__media">${read(s.file).replace(/<!--[\s\S]*?-->\s*/, '')}</div>
    <div class="demo__copy"><h2>${s.title}</h2><p>${s.body}</p></div>
  </div>
</section>`).join('\n');

const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>EMG Motion Graphics</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root { --navy: #073c72; --pink: #ec1674; --bg: #ffffff; --muted: #44526a; --line: #e4e8ef; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg: #ffffff; } }
:root[data-theme="dark"] { --bg: #ffffff; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--navy); font-family: 'Jost', 'Futura', Arial, sans-serif; }
header.top { background: var(--navy); color: #fff; padding: 28px 16px; text-align: center; }
header.top h1 { margin: 0; font-size: clamp(22px, 4vw, 32px); letter-spacing: .04em; text-transform: uppercase; }
header.top p { margin: 8px auto 0; max-width: 640px; color: #c7d6e6; font-size: 15px; }
.demo { max-width: 1240px; margin: 0 auto; padding: 56px 16px; border-bottom: 1px solid var(--line); }
.demo__tag { margin: 0 0 24px; font-size: 12px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--pink); }
.demo__tag span { color: var(--muted); font-weight: 500; letter-spacing: .04em; text-transform: none; font-size: 13px; }
.demo__row { display: grid; grid-template-columns: 1.1fr 1fr; gap: 48px; align-items: center; }
.demo__copy { text-align: center; }
.demo__copy h2 { margin: 0 0 14px; font-size: clamp(24px, 3vw, 38px); line-height: 1.05; text-transform: uppercase; font-weight: 500; }
.demo__copy h2 .pink { color: var(--pink); font-weight: 700; }
.demo__copy p { margin: 0; font-size: 17px; line-height: 1.4; }
@media (max-width: 820px) { .demo__row { grid-template-columns: 1fr; gap: 28px; } }
${css}
</style>
</head>
<body>
<header class="top">
  <h1>Motion Graphics</h1>
  <p>Three looping, code-only animations for the Web Design, Digital Marketing, and Public Relations pages.</p>
</header>
${blocks}
<script>
${js}
</script>
</body>
</html>
`;

fs.writeFileSync(path.join(dir, 'preview.html'), html);
console.log('Wrote', path.join(dir, 'preview.html'));
