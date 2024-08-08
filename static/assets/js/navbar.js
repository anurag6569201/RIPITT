(function (cb) {
  if (document.readyState === "complete") {
      return setTimeout(cb);
  }

  if (window.addEventListener) {
      return window.addEventListener("load", cb, false);
  }

  if (window.attachEvent) {
      return window.attachEvent("onload", cb);
  }
})(function () {
  document.querySelectorAll('.nav-btn').forEach(function (el) {
      el.addEventListener('click', function () {
          var nav = document.getElementById('main-nav-back');
          var _class = 'open';
          if (nav.classList.contains(_class)) {
              nav.classList.remove(_class);
          } else {
              nav.classList.add(_class);
          }
      });
  });
});