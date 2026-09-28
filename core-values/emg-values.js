/* EMG Core Values tiles: one tile open at a time.
   Click or tap any tile to open it; arrow keys move between tiles. */
(function () {
  var roots = document.querySelectorAll('.emgv');
  if (!roots.length) return;

  roots.forEach(function (root) {
    var tiles = [].slice.call(root.querySelectorAll('.emgv-tile'));
    if (!tiles.length) return;
    var narrow = window.matchMedia('(max-width: 899px)');

    function open(tile, scroll) {
      tiles.forEach(function (t) {
        var on = t === tile;
        t.classList.toggle('is-active', on);
        t.querySelector('.emgv-btn').setAttribute('aria-expanded', on ? 'true' : 'false');
        t.querySelector('.emgv-body').setAttribute('aria-hidden', on ? 'false' : 'true');
      });
      // Stacked layout: closing a tile above can push the opened one off-screen.
      if (scroll && narrow.matches) {
        setTimeout(function () {
          var top = tile.getBoundingClientRect().top;
          if (top < 0 || top > window.innerHeight * 0.6) {
            tile.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        }, 560);
      }
    }

    tiles.forEach(function (tile, i) {
      tile.addEventListener('click', function () {
        if (!tile.classList.contains('is-active')) open(tile, true);
      });
      tile.querySelector('.emgv-btn').addEventListener('keydown', function (e) {
        var j = null;
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') j = (i + 1) % tiles.length;
        if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') j = (i - 1 + tiles.length) % tiles.length;
        if (e.key === 'Home') j = 0;
        if (e.key === 'End') j = tiles.length - 1;
        if (j === null) return;
        e.preventDefault();
        open(tiles[j], false);
        tiles[j].querySelector('.emgv-btn').focus();
      });
    });

    open(root.querySelector('.emgv-tile.is-active') || tiles[0], false);
    root.classList.add('emgv--ready');
  });
})();
