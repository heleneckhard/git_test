# EMG motion graphics

Three looping animations for the service pages on elysiummarkstg.wpenginepowered.com. Each one is built with SVG and CSS only. The only JavaScript is an optional script that pauses them when they're off-screen. There are no libraries or video files.

| Page | Replaces | Partial | Loop |
|---|---|---|---|
| `/web-design/` | the `elloop` process animation in `.media-content__loop` | `partials/web-design.html` | 9s |
| `/digital-marketing-solutions` | `marketing-circle@2x-1.webp` in `.media-content__media` | `partials/digital-marketing.html` | 9s |
| `/public-relations/` | `public-relations-graphic.webp` in `.media-content__media` | `partials/public-relations.html` | 10s |

Open `preview.html` in a browser to see all three. Run `node motion-graphics/build-preview.js` after you edit anything to rebuild it.

## What each one shows

Each graphic makes one point from its section's copy, in three steps or fewer.

- **Web Design: one page, built in parallel.** Strategy lays out a wireframe. Then SEO Copy, Design, and Development fill the page in *at the same time*: three progress bars run together and finish together, while words, visuals, and working parts appear side by side on the page. A client feedback bubble asks for a bolder headline, the headline updates, and the client approves ("feedback in real time").
- **Digital Marketing: follow one customer.** One person moves around the loop. They see your ad (Paid), later search and find you (Organic), then get an email and order again (Lifecycle), and the insights flow back into the next ad. Each card lights up as the customer arrives, which shows the channels handing off to each other.
- **Public Relations: from story to results.** Your story is written, becomes a featured piece of earned coverage, and that coverage lights up the three results the copy promises: search visibility, foot traffic, and quality leads.

## Changing the timing

`emg-motion.css` is generated. Timelines live at the top of `tools/build-css.py` as `(element, reveal type, start %, end %)`. Edit the numbers, then run:

```
python3 motion-graphics/tools/build-css.py && node motion-graphics/build-preview.js
```

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

Small labels written for these graphics that the team may want to reword: "Then, all at once:", the feedback bubble ("Can the headline pop more?" / "Love it. Approved!"), "One team · every channel feeds the next", the three customer captions, and "Earned coverage". Edit them in the partials.
