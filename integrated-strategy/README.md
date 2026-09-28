# "Two Sides, One Strategy" (Franchise Marketing page)

Replaces the two-column box in `section.compare-text` on `/franchise-marketing/` (the `.compare-text__wrapper` div). **Keep** the `compare-text__intro` heading and the `compare-text__cta` button.

## How it behaves

- **Desktop:** both lists sit on either side of a navy "One Strategy" hub. Every item has a line into the hub.
  - When the section scrolls into view, the lines draw in and the items fade up. After that, soft dots keep flowing inward along the lines.
  - Hovering or tapping an item lights its line and that side of the hub's ring (pink for Franchise Development, teal for Consumer Marketing).
  - Until the visitor interacts, the lines light up one at a time, alternating sides. This stops as soon as they hover or tap.
- **Under 820px:** the lists stack above and below the hub, joined by a short line. Items still highlight on tap.
- **Reduced motion:** no flow, no auto-cycle, no animated draw-in.
- **Without JS:** the lists and hub still show, without the lines.

The text is word-for-word from the dev page. There's no new copy.

## Files

- `partials/integrated.html`: the markup.
- `emg-integrated.css`: styles, all under `.emgi`.
- `emg-integrated.js`: draws the lines, re-measures on resize, and handles hover and auto-cycle. No dependencies.
- `preview.html`: standalone preview. Rebuild it with `python3 integrated-strategy/build.py`.

## Installing

1. In the template that renders `compare-text`, replace `.compare-text__wrapper` with `partials/integrated.html`. If the lists come from ACF, loop them into the `.emgi-item` markup. Left items put `.emgi-node` after the text; right items put it before.
2. Copy the CSS and JS into `wp-content/themes/elysiumtheme/dist/` and enqueue them on the franchise-marketing page only (same pattern as the Core Values handoff, with `is_page('franchise-marketing')`).
3. Clear the WP Engine cache.
