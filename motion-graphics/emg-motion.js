/* EMG motion graphics: pause when off-screen, respect reduced motion.
   Optional. The graphics animate without it; this just saves CPU/battery. */
(function () {
  var graphics = document.querySelectorAll('.emg-mg');
  if (!graphics.length) return;

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)');

  function setPaused(el, paused) {
    el.classList.toggle('is-paused', paused);
    var svg = el.querySelector('svg');
    if (!svg || !svg.pauseAnimations) return;
    if (paused) svg.pauseAnimations(); else svg.unpauseAnimations();
  }

  if (reduce && reduce.matches) {
    graphics.forEach(function (el) { setPaused(el, true); });
    return;
  }

  if (!('IntersectionObserver' in window)) return;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) { setPaused(entry.target, !entry.isIntersecting); });
  }, { rootMargin: '100px 0px' });
  graphics.forEach(function (el) { io.observe(el); });
})();
