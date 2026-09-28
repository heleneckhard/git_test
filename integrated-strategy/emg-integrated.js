/* EMG "Two Sides, One Strategy": slides the two rings together when the
   section scrolls into view, and lifts a ring while its list is hovered. */
(function () {
  document.querySelectorAll('.emgi').forEach(function (root) {
    root.querySelectorAll('[data-side]').forEach(function (col) {
      var cls = 'is-hot-' + col.getAttribute('data-side');
      col.addEventListener('pointerenter', function () { root.classList.add(cls); });
      col.addEventListener('pointerleave', function () { root.classList.remove(cls); });
    });

    if (!('IntersectionObserver' in window)) return;
    root.classList.add('is-ready');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          root.classList.add('is-in');
          io.disconnect();
        }
      });
    }, { threshold: 0.4 });
    io.observe(root);
  });
})();
