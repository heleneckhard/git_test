# Core Values tiles (Why Us page)

Replaces the Core Values carousel (`section.image-content-slider` on `/why-us/`) with six interactive tiles. The heading and all six values' text are unchanged, and the reviews image is gone.

- **Desktop:** two rows of three tiles. Clicking a tile widens it, turns it navy, reveals its full text, and plays its icon's animation. The first value starts open.
- **Phones and tablets:** a stacked list that expands the same way.
- **Keyboard:** each tile is a button; arrow keys, Home and End move between them.
- **Without JavaScript:** every tile shows its full text.
- **Reduced motion:** tiles still open, but icons don't animate.

## Files

- `values.json`: the six values, copied word-for-word from the dev page.
- `emg-values.css`, `emg-values.js`: styles and interaction.
- `partials/values.html`: the markup (generated).
- `preview.html`: standalone preview (generated).

After editing `values.json`, `build.py`, or the CSS/JS, run `python3 core-values/build.py`.

## Installing

Replace the carousel block inside `section.image-content-slider` (the `image-content-slider__slides` div and the `swiper-pagination` div after it) with `partials/values.html`, then enqueue `emg-values.css` and `emg-values.js` on the Why Us page. Keep the `image-content-slider__intro` heading as is. The page's Swiper setup for this section can be removed.
