# EMG motion graphics

Three looping animations for the service pages on elysiummarkstg.wpenginepowered.com. Each one is built with SVG and CSS only. The only JavaScript is an optional script that pauses them when they're off-screen. There are no libraries or video files.

| Page | Replaces | Partial | Loop |
|---|---|---|---|
| `/web-design/` | the `elloop` process animation in `.media-content__loop` | `partials/web-design.html` | 10s |
| `/digital-marketing-solutions` | `marketing-circle@2x-1.webp` in `.media-content__media` | `partials/digital-marketing.html` | 9s |
| `/public-relations/` | `public-relations-graphic.webp` in `.media-content__media` | `partials/public-relations.html` | 10s |

Open `preview.html` in a browser to see all three. Run `node motion-graphics/build-preview.js` after you edit anything to rebuild it.

## What each one shows

- **Web Design:** Strategy sends SEO Copy, Design, and Development into an empty browser. Each stage lights up as it builds its part of the page: headline copy types in, design shapes pop in, and a code panel gives way to real components. Then the site goes live. Speed, SEO, and GEO scores fill to 100, a cursor clicks Get Started, and a "New lead" notification lands.
- **Digital Marketing:** A comet travels around the Paid → Organic → Lifecycle loop. Each node fires as the comet passes: the megaphone's coin flips, the organic bars grow, and leads drop through the funnel and come out converted. A growth line in the center climbs with each stage.
- **Public Relations:** Paid and Organic are already flowing into "Your Story." Earned starts out as a dashed, empty slot, which answers the "Is earned media missing?" headline. Then it fills in teal, the hub lights up, and coverage spreads out: Press Feature, Podcast Guest, Influencer Post, and Search Visibility with a rising trend line.

## Installing in the theme

1. Copy `emg-motion.css` and `emg-motion.js` into `wp-content/themes/elysiumtheme/dist/`.
2. Enqueue them on the three pages. This follows the same pattern `functions.php` already uses for `elysium-loop.css`:

   ```php
   add_action('wp_enqueue_scripts', function () {
       if (!is_page(['web-design', 'digital-marketing-solutions', 'public-relations'])) return;
       $dir = get_template_directory_uri() . '/dist/';
       $ver = filemtime(get_template_directory() . '/dist/emg-motion.css');
       wp_enqueue_style('emg-motion', $dir . 'emg-motion.css', [], $ver);
       wp_enqueue_script('emg-motion', $dir . 'emg-motion.js', [], $ver, true);
   });
   ```

3. Paste each partial's markup where the old graphic goes:
   - **Web Design:** replace the whole `<div class="elloop">…</div>` inside `.media-content__loop`. You can stop enqueueing `elysium-loop.css` once it's gone.
   - **Digital Marketing / PR:** replace the `<img>` inside `.media-content__media`. If that image comes from an ACF image field, add a small "use motion graphic" option to the media-content block template and `include` the partial when it's set.

The graphics size to their container (`width: min(100%, 720px)`). They pick up the theme's Futura through `--heading-font-pt`, and colors are CSS variables on `.emg-mg` (`--emg-navy`, `--emg-teal`, `--emg-pink`, …) if you need to fine-tune them.

## Accessibility and performance

- Each graphic has `role="img"` and an `aria-label` that describes the story, so screen readers get one clear sentence instead of shapes.
- With `prefers-reduced-motion: reduce`, animation turns off and the completed graphic shows as a static image.
- `emg-motion.js` pauses a graphic while it's off-screen (CSS and SMIL both), so nothing runs where nobody can see it.
- Only `transform`, `opacity`, and `stroke-dashoffset` are animated. There are no images to load and no layout changes.

## Copy to confirm

"Capture Demand" comes from the current Digital Marketing graphic. "Build Your Presence" and "Convert & Retain" are my best read of the partly hidden captions under the other two nodes, and the four PR coverage-card labels are new. Edit the text in the partials if the team wants different wording.
