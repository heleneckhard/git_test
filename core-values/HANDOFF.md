# Handoff: Core Values tiles on /why-us/

Replace the Core Values carousel on the Why Us page with an interactive tile grid. **Keep the existing section heading** ("Learn More About the Elysium Way / with our Core Values" with the pink underline). Only the carousel under it changes.

## Files

| File | What it is |
|---|---|
| `values.html` | The markup. Six tiles holding the exact text currently on the page. No heading. |
| `emg-values.css` | All styles, scoped under `.emgv`. |
| `emg-values.js` | The interaction: one tile open at a time, click, tap, and arrow keys. No dependencies. |

## What to change

The carousel lives in `section.image-content-slider` on `/why-us/`. Server-rendered, it looks like this:

```html
<section class="image-content-slider">
  <div class="container">
    <div class="image-content-slider__intro">   <!-- KEEP: the heading -->
      ...
    </div>
    <div class="image-content-slider__slides swiper">   <!-- REPLACE -->
      <div class="swiper-wrapper"> ...6 slides, each with the reviews image... </div>
    </div>
    <div class="swiper-pagination"></div>   <!-- REMOVE (if it's in the template) -->
  </div>
</section>
```

1. **Template:** in the theme template or partial that renders `image-content-slider`, replace the `image-content-slider__slides` block (and the `swiper-pagination` element after it, if the template outputs one) with the contents of `values.html`. Keep `image-content-slider__intro` as is. The six values can stay hard-coded as in `values.html`. Or, if the slides come from ACF fields, loop the same fields into the tile markup. Each tile needs:
   - the title in `.emgv-title`
   - the body paragraphs in `.emgv-body-inner`
   - unique `id`s on the button and body (`emgv-btn-N` / `emgv-body-N`)
   - `is-active` and `aria-expanded="true"` on the first tile only

   Keep the icons as they are in `values.html`.
2. **Swiper:** remove or guard the Swiper initialization for `.image-content-slider__slides` in the theme JS, since that element no longer exists. Make sure nothing throws.
3. **Assets:** copy `emg-values.css` and `emg-values.js` into `wp-content/themes/elysiumtheme/dist/` and enqueue them on the Why Us page only:

   ```php
   add_action('wp_enqueue_scripts', function () {
       if (!is_page('why-us')) return;
       $dir = get_template_directory_uri() . '/dist/';
       $path = get_template_directory() . '/dist/';
       wp_enqueue_style('emg-values', $dir . 'emg-values.css', [], filemtime($path . 'emg-values.css'));
       wp_enqueue_script('emg-values', $dir . 'emg-values.js', [], filemtime($path . 'emg-values.js'), true);
   });
   ```
4. **Reviews image:** it's no longer used on this page. Leave the upload in the media library.
5. **Cache:** clear the WP Engine cache.

## Check before calling it done

- The heading above the tiles is unchanged.
- **Desktop (≥ 900px):**
  - Two rows of three tiles. "We Go the Extra Mile" starts open (navy, full text showing).
  - Clicking another tile opens it and closes the previous one.
  - Each icon animates when its tile opens.
- **Below 900px:** the tiles stack into a single column and expand in place, with no horizontal scroll.
- **Text:**
  - "We Deliver Creative We're Proud Of" shows its last line ("If it doesn't say Wow to us…") as a separate paragraph.
  - "We are Responsive & Communicative" has two paragraphs.
- **No-JS fallback:** with JS disabled, all six tiles show their full text.
- **Browser console:** no errors (for example, from the old Swiper init).
- **Fonts:** the tiles use the theme's Futura via `var(--heading-font-pt)`. If the tiles show a fallback font, check that that variable exists on this page.

## Notes

- Styles are namespaced (`.emgv-*`, `@keyframes emgv-*`), so they won't touch the rest of the theme.
- Colors match the site (navy `#073c72`, pink `#ec1674`, teal `#36c5c1`). They're CSS variables at the top of `emg-values.css`.
- `prefers-reduced-motion` is respected: the tiles still open, but the icons don't animate.
- Source of truth, if the text or icons ever change: `core-values/` in the `claude/motion-graphics-replacement-cumvf4` branch of `heleneckhard/git_test`. Edit `values.json` or `build.py`, then run `python3 core-values/build.py`.
