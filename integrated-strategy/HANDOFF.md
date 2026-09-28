# Handoff: "Two Sides, One Strategy" box on /franchise-marketing/

Update the two-column box in the **"Two Sides of Franchise Growth, One Integrated Strategy"** section. **Keep the existing heading and the "Let's talk about your system" button.** Only the box between them changes.

The new box keeps the same layout (two lists in a rounded box with a divider) and adds:

- a pink ring (Franchise Development) and a teal ring (Consumer Marketing) that overlap in the middle of the divider, with the shared middle filled navy;
- the rings sliding together from each side when the section scrolls into view;
- on hover, that side comes forward: its ring grows and tints, its bullets grow, and the other side fades back.

## Files

| File | What it is |
|---|---|
| `integrated.html` | The markup for the box: both lists, with text copied word-for-word from the page, plus the rings. No heading, no button. |
| `emg-integrated.css` | All styles, scoped under `.emgi`. |
| `emg-integrated.js` | About 20 lines: triggers the slide-in on scroll and toggles the hover state. No dependencies. |

## What to change

The section on `/franchise-marketing/` currently renders like this:

```html
<section class="compare-text">
  <div class="container">
    <div class="compare-text__intro"><h2>Two Sides of Franchise Growth, …</h2></div>   <!-- KEEP -->
    <div class="compare-text__wrapper">   <!-- REPLACE with integrated.html -->
      <div class="compare-text__left compare-text__col"> …Franchise Development list… </div>
      <div class="compare-text__right compare-text__col"> …Consumer Marketing list… </div>
    </div>
    <div class="compare-text__cta text-center"> …Let's talk about your system… </div>   <!-- KEEP -->
  </div>
</section>
```

1. **Template:** in the theme template or partial that renders `compare-text`, replace the `compare-text__wrapper` div with the contents of `integrated.html`.
   - If the column titles and lists come from ACF or WYSIWYG fields, output them into the same markup instead of hard-coding:
     - each title goes in `<h4 class="emgi-title">`;
     - each list's items go as plain `<li>`s inside `<ul class="emgi-list">`.
   - Keep `data-side="left"` / `data-side="right"` on the two columns. The JS uses them.
   - Keep the `.emgi-mid` block (the rings) between the two columns.
2. **Assets:** copy `emg-integrated.css` and `emg-integrated.js` into `wp-content/themes/elysiumtheme/dist/` and enqueue them on the Franchise Marketing page only:

   ```php
   add_action('wp_enqueue_scripts', function () {
       if (!is_page('franchise-marketing')) return;
       $dir = get_template_directory_uri() . '/dist/';
       $path = get_template_directory() . '/dist/';
       wp_enqueue_style('emg-integrated', $dir . 'emg-integrated.css', [], filemtime($path . 'emg-integrated.css'));
       wp_enqueue_script('emg-integrated', $dir . 'emg-integrated.js', [], filemtime($path . 'emg-integrated.js'), true);
   });
   ```

   If the Core Values tiles (Why Us page) are going in too, keep them as a separate `is_page('why-us')` enqueue.
3. **Old styles:** if the theme's existing `.compare-text__wrapper` / `.compare-text__col` styles aren't used anywhere else, they can be left alone. The new markup doesn't use those classes.
4. **Cache:** clear the WP Engine cache.

## Check before calling it done

- The heading above the box and the pink button below it are unchanged.
- **Desktop (≥ 768px):**
  - Two lists side by side, with a vertical divider broken in the middle by the two overlapping rings.
  - On scrolling to the section, the rings slide in from each side and lock together, and the navy overlap fades in.
  - Hovering the left list: the pink ring grows and tints, the pink bullets grow, and the right side fades.
  - Hovering the right list does the mirror image in teal.
  - Moving off returns everything to normal.
- **Below 768px:** the lists stack, with the rings between them and the divider running sideways. There's no horizontal scroll.
- **Text:** all eight items match the current page exactly.
- **No-JS fallback:** with JS disabled, the rings show already overlapped, with no errors.
- **Browser console:** no errors.
- **Fonts:** text uses the theme's Futura via `var(--heading-font-pt)`. If it shows a fallback font, check that that variable exists on this page.

## Notes

- Styles are namespaced (`.emgi-*`), so they won't affect anything else on the site.
- Colors match the site (navy `#073c72`, pink `#ec1674`, teal `#36c5c1`). They're CSS variables at the top of `emg-integrated.css`.
- `prefers-reduced-motion` is respected: the rings show joined, with no sliding.
- Source of truth: `integrated-strategy/` in the `claude/motion-graphics-replacement-cumvf4` branch of `heleneckhard/git_test`.
