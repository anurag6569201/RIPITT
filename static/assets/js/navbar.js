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
    var mobilenav_logo=document.querySelector(".mobile-nav-logo");
    var app_wrapper=document.querySelector(".mobile-nav .app");
    var app_full_wrapper=document.querySelector(".mobile-nav .wrapper");
  document.querySelectorAll('.nav-btn').forEach(function (el) {
      el.addEventListener('click', function () {
          var nav = document.getElementById('main-nav-back');
          var _class = 'open';
          if (nav.classList.contains(_class)) {
              nav.classList.remove(_class);
              mobilenav_logo.style.opacity ="0";
              app_wrapper.style.height ="";
              app_wrapper.style.width ="";
              app_full_wrapper.style.height ="";
              app_full_wrapper.style.width ="";
          } else {
              nav.classList.add(_class);
              mobilenav_logo.style.opacity ="1";
              app_wrapper.style.height ="100vh";
              app_wrapper.style.width ="100vw";
              app_full_wrapper.style.height ="100vh";
              app_full_wrapper.style.width ="100vw";
          }
      });
  });
});