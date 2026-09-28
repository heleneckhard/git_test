/* EMG "Two Sides, One Strategy": draws each item's line into the hub,
   lights a line on hover/tap, and gently cycles through the items until
   the visitor interacts. */
(function () {
  var NS = 'http://www.w3.org/2000/svg';
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  document.querySelectorAll('.emgi').forEach(function (root) {
    var svg = root.querySelector('.emgi-lines');
    var hub = root.querySelector('.emgi-hub');
    var items = [].slice.call(root.querySelectorAll('.emgi-item'));
    var narrow = window.matchMedia('(max-width: 819px)');
    var links = [];

    items.forEach(function (item) {
      item.side = item.closest('[data-side]').getAttribute('data-side');
    });
    var left = items.filter(function (i) { return i.side === 'left'; });
    var right = items.filter(function (i) { return i.side === 'right'; });
    // Alternate sides so the auto-cycle reads as "both sides, one hub".
    var order = [];
    for (var k = 0; k < Math.max(left.length, right.length); k++) {
      if (left[k]) order.push(left[k]);
      if (right[k]) order.push(right[k]);
    }
    order.forEach(function (item, i) { item.style.setProperty('--i', i); });

    function el(name, attrs) {
      var n = document.createElementNS(NS, name);
      for (var a in attrs) n.setAttribute(a, attrs[a]);
      return n;
    }

    function layout() {
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      links = [];
      if (narrow.matches) return;
      var box = root.getBoundingClientRect();
      var h = hub.getBoundingClientRect();
      var cx = h.left + h.width / 2 - box.left;
      var cy = h.top + h.height / 2 - box.top;
      var r = h.width / 2 + 16;
      svg.setAttribute('viewBox', '0 0 ' + box.width + ' ' + box.height);

      order.forEach(function (item, i) {
        var n = item.querySelector('.emgi-node').getBoundingClientRect();
        var nx = n.left + n.width / 2 - box.left;
        var ny = n.top + n.height / 2 - box.top;
        var ang = Math.atan2(ny - cy, nx - cx);
        var ex = cx + Math.cos(ang) * r;
        var ey = cy + Math.sin(ang) * r;
        var mx = nx + (ex - nx) * 0.55;
        var d = 'M' + nx + ' ' + ny + ' C' + mx + ' ' + ny + ' ' + mx + ' ' + ey + ' ' + ex + ' ' + ey;
        var g = el('g', { 'class': 'emgi-link emgi-link--' + item.side, style: '--i:' + i });
        g.appendChild(el('path', { 'class': 'emgi-line', d: d, pathLength: 100 }));
        g.appendChild(el('path', { 'class': 'emgi-flow', d: d }));
        g.appendChild(el('path', { 'class': 'emgi-glow', d: d, pathLength: 100 }));
        svg.appendChild(g);
        links.push(g);
        item.link = g;
        if (item.classList.contains('is-hot')) g.classList.add('is-hot');
      });
    }

    function heat(item) {
      items.forEach(function (i) {
        var on = i === item;
        i.classList.toggle('is-hot', on);
        if (i.link) i.link.classList.toggle('is-hot', on);
      });
      root.classList.remove('emgi--hot-left', 'emgi--hot-right');
      if (item) {
        void root.offsetWidth; // restart the hub pulse
        root.classList.add('emgi--hot-' + item.side);
      }
    }

    // Gentle auto-cycle until the visitor hovers or taps anything.
    var timer = null, step = 0, touched = false;
    function startCycle() {
      if (reduce || touched || timer) return;
      timer = setInterval(function () { heat(order[step % order.length]); step++; }, 1600);
    }
    function stopCycle() { clearInterval(timer); timer = null; }

    items.forEach(function (item) {
      item.addEventListener('pointerenter', function () { touched = true; stopCycle(); heat(item); });
      item.addEventListener('pointerleave', function (e) { if (e.pointerType === 'mouse') heat(null); });
      item.addEventListener('click', function () { touched = true; stopCycle(); heat(item); });
    });

    root.classList.add('is-ready');
    layout();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(layout);
    if ('ResizeObserver' in window) new ResizeObserver(layout).observe(root);
    else window.addEventListener('resize', layout);

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            root.classList.add('is-in');
            setTimeout(startCycle, 1800);
          } else {
            stopCycle();
          }
        });
      }, { threshold: 0.35 }).observe(root);
    } else {
      root.classList.add('is-in');
    }
  });
})();
