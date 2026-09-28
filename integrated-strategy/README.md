# "Two Sides, One Strategy" (Franchise Marketing page)

Replaces the two-column box in `section.compare-text` on `/franchise-marketing/` (the `.compare-text__wrapper` div). **Keep** the `compare-text__intro` heading and the `compare-text__cta` button.

## How it behaves

- It keeps the original layout: two lists in a rounded box with a divider between them.
- In the middle of the divider, a pink ring (Franchise Development) and a teal ring (Consumer Marketing) overlap, and the shared middle is filled navy.
- When the section scrolls into view, the rings slide in from each side and lock together. That's the only animation.
- Hovering either list thickens that side's ring.
- **Under 768px:** the rings sit between the stacked lists, and the divider runs sideways.
- **Without JS, or with reduced motion:** the rings simply show overlapped.

The text is word-for-word from the dev page. The box adds no words.

## Files

- `partials/integrated.html`: the markup.
- `emg-integrated.css`: styles, all under `.emgi`.
- `emg-integrated.js`: about 20 lines. Triggers the slide-in on scroll and the hover emphasis.
- `preview.html`: standalone preview. Rebuild it with `python3 integrated-strategy/build.py`.

## Installing

1. In the template that renders `compare-text`, replace `.compare-text__wrapper` with `partials/integrated.html`. If the lists come from ACF, loop them into the two `<ul class="emgi-list">` elements.
2. Copy the CSS and JS into `wp-content/themes/elysiumtheme/dist/` and enqueue them on the franchise-marketing page only (same pattern as the Core Values handoff, with `is_page('franchise-marketing')`).
3. Clear the WP Engine cache.
