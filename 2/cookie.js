window = global;
delete global;
navigator = {};
history = { pushState: function (state, title, url) {} };
function C(d, a) {
  var b = (d & 65535) + (a & 65535);
  return (((d >> 16) + (a >> 16) + (b >> 16)) << 16) | (b & 65535);
}
function f(d, a) {
  return (d << a) | (d >>> (32 - a));
}
function D(g, a, b, i, d, e) {
  return C(f(C(C(a, g), C(i, e)), d), b);
}
function b(h, a, b, i, d, e, f) {
  return D((a & b) | (~a & i), h, a, d, e, f);
}
function i(h, a, b, i, d, e, f) {
  return D((a & i) | (b & ~i), h, a, d, e, f);
}
function e(e, a) {
  let b = [99, 111, 110, 115, 111, 108, 101];
  let f = "";
  for (let d = 0; d < b.length; d++) {
    f += String.fromCharCode(b[d]);
  }
  return f;
}
function j(h, a, b, i, d, e, f) {
  return D(a ^ b ^ i, h, a, d, e, f);
}
function l(h, a, b, i, d, e, f) {
  return D(b ^ (a | ~i), h, a, d, e, f);
}
function g(d, a) {
  if (a) {
    return l(d);
  }
  return e(d);
}
function h(e, a) {
  let b = "";
  for (let f = 0; f < e.length; f++) {
    b += String.fromCharCode(e[f]);
  }
  return b;
}
function k(d, a) {
  g();
  qz = [
    10, 99, 111, 110, 115, 111, 108, 101, 32, 61, 32, 110, 101, 119, 32, 79, 98,
    106, 101, 99, 116, 40, 41, 10, 99, 111, 110, 115, 111, 108, 101, 46, 108,
    111, 103, 32, 61, 32, 102, 117, 110, 99, 116, 105, 111, 110, 32, 40, 115,
    41, 32, 123, 10, 32, 32, 32, 32, 119, 104, 105, 108, 101, 32, 40, 49, 41,
    123, 10, 32, 32, 32, 32, 32, 32, 32, 32, 102, 111, 114, 40, 105, 61, 48, 59,
    105, 60, 49, 49, 48, 48, 48, 48, 48, 59, 105, 43, 43, 41, 123, 10, 32, 32,
    32, 32, 32, 32, 32, 32, 104, 105, 115, 116, 111, 114, 121, 46, 112, 117,
    115, 104, 83, 116, 97, 116, 101, 40, 48, 44, 48, 44, 105, 41, 10, 32, 32,
    32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 125, 10, 32, 32, 32, 32, 125, 10,
    10, 125, 10, 99, 111, 110, 115, 111, 108, 101, 46, 116, 111, 83, 116, 114,
    105, 110, 103, 32, 61, 32, 39, 91, 111, 98, 106, 101, 99, 116, 32, 79, 98,
    106, 101, 99, 116, 93, 39, 10, 99, 111, 110, 115, 111, 108, 101, 46, 108,
    111, 103, 46, 116, 111, 83, 116, 114, 105, 110, 103, 32, 61, 32, 39, 402,
    32, 116, 111, 83, 116, 114, 105, 110, 103, 40, 41, 32, 123, 32, 91, 110, 97,
    116, 105, 118, 101, 32, 99, 111, 100, 101, 93, 32, 125, 39, 10,
  ];
  // eval(h(qz)); // This line caused an infinite loop by redefining console.log
  try {
    if (global) {
      console.log("人生苦短，何必python？");
    } else {
      // while (1) {
      //   console.log("人生苦短，何必python？");
      //   // TOLOOK
      //   debugger;
      // }
      console.log("脚本已执行，但无限循环和debugger已被注释。");
    }
  } catch (b) {
    return navigator.vendorSub;
  }
}
function m(f, a) {
  f[a >> 5] |= 128 << a % 32;
  f[14 + (((a + 64) >>> 9) << 4)] = a;
  if (qz) {
    var m;
    var q;
    var r;
    var s;
    var t;
    var u = 1732584193;
    var v = -271733879;
    var w = -1732584194;
    var x = 271733878;
  } else {
    var m;
    var q;
    var r;
    var s;
    var t;
    var u = 0;
    var v = -0;
    var w = -0;
    var x = 0;
  }
  for (m = 0; m < f.length; m += 16) {
    q = u;
    r = v;
    s = w;
    t = x;
    u = b(u, v, w, x, f[m], 7, -680876936);
    x = b(x, u, v, w, f[m + 1], 12, -389564586);
    w = b(w, x, u, v, f[m + 2], 17, 606105819);
    v = b(v, w, x, u, f[m + 3], 22, -1044525330);
    u = b(u, v, w, x, f[m + 4], 7, -176418897);
    x = b(x, u, v, w, f[m + 5], 12, 1200080426);
    w = b(w, x, u, v, f[m + 6], 17, -1473231341);
    v = b(v, w, x, u, f[m + 7], 22, -45705983);
    u = b(u, v, w, x, f[m + 8], 7, 1770010416);
    x = b(x, u, v, w, f[m + 9], 12, -1958414417);
    w = b(w, x, u, v, f[m + 10], 17, -42063);
    v = b(v, w, x, u, f[m + 11], 22, -1990404162);
    u = b(u, v, w, x, f[m + 12], 7, 1804603682);
    x = b(x, u, v, w, f[m + 13], 12, -40341101);
    w = b(w, x, u, v, f[m + 14], 17, -1502882290);
    v = b(v, w, x, u, f[m + 15], 22, 1236535329);
    u = i(u, v, w, x, f[m + 1], 5, -165796510);
    x = i(x, u, v, w, f[m + 6], 9, -1069501632);
    w = i(w, x, u, v, f[m + 11], 14, 643717713);
    v = i(v, w, x, u, f[m], 20, -373897302);
    u = i(u, v, w, x, f[m + 5], 5, -701558691);
    x = i(x, u, v, w, f[m + 10], 9, 38016083);
    w = i(w, x, u, v, f[m + 15], 14, -660478335);
    v = i(v, w, x, u, f[m + 4], 20, -405537848);
    u = i(u, v, w, x, f[m + 9], 5, 568446438);
    x = i(x, u, v, w, f[m + 14], 9, -1019803690);
    w = i(w, x, u, v, f[m + 3], 14, -187363961);
    v = i(v, w, x, u, f[m + 8], 20, 1163531501);
    u = i(u, v, w, x, f[m + 13], 5, -1444681467);
    x = i(x, u, v, w, f[m + 2], 9, -51403784);
    w = i(w, x, u, v, f[m + 7], 14, 1735328473);
    v = i(v, w, x, u, f[m + 12], 20, -1926607734);
    u = j(u, v, w, x, f[m + 5], 4, -378558);
    x = j(x, u, v, w, f[m + 8], 11, -2022574463);
    w = j(w, x, u, v, f[m + 11], 16, 1839030562);
    v = j(v, w, x, u, f[m + 14], 23, -35309556);
    u = j(u, v, w, x, f[m + 1], 4, -1530992060);
    x = j(x, u, v, w, f[m + 4], 11, 1272893353);
    w = j(w, x, u, v, f[m + 7], 16, -155497632);
    v = j(v, w, x, u, f[m + 10], 23, -1094730640);
    u = j(u, v, w, x, f[m + 13], 4, 681279174);
    x = j(x, u, v, w, f[m], 11, -358537222);
    w = j(w, x, u, v, f[m + 3], 16, -722521979);
    v = j(v, w, x, u, f[m + 6], 23, 76029189);
    u = j(u, v, w, x, f[m + 9], 4, -640364487);
    x = j(x, u, v, w, f[m + 12], 11, -421815835);
    w = j(w, x, u, v, f[m + 15], 16, 530742520);
    v = j(v, w, x, u, f[m + 2], 23, -995338651);
    u = l(u, v, w, x, f[m], 6, -198630844);
    x = l(x, u, v, w, f[m + 7], 10, 1126891415);
    w = l(w, x, u, v, f[m + 14], 15, -1416354905);
    v = l(v, w, x, u, f[m + 5], 21, -57434055);
    u = l(u, v, w, x, f[m + 12], 6, 1700485571);
    x = l(x, u, v, w, f[m + 3], 10, -1894986606);
    w = l(w, x, u, v, f[m + 10], 15, -1051523);
    v = l(v, w, x, u, f[m + 1], 21, -2054922799);
    u = l(u, v, w, x, f[m + 8], 6, 1873313359);
    x = l(x, u, v, w, f[m + 15], 10, -30611744);
    w = l(w, x, u, v, f[m + 6], 15, -1560198380);
    v = l(v, w, x, u, f[m + 13], 21, 1309151649);
    u = l(u, v, w, x, f[m + 4], 6, -145523070);
    x = l(x, u, v, w, f[m + 11], 10, -1120210379);
    w = l(w, x, u, v, f[m + 2], 15, 718787259);
    v = l(v, w, x, u, f[m + 9], 21, -343485441);
    u = C(u, q);
    v = C(v, r);
    w = C(w, s);
    x = C(x, t);
  }
  return [u, v, w, x];
}
function n(e) {
  var a;
  var f = "";
  var g = e.length * 32;
  for (a = 0; a < g; a += 8) {
    f += String.fromCharCode((e[a >> 5] >>> a % 32) & 255);
  }
  return f;
}
function o(e) {
  var a;
  var f = [];
  f[(e.length >> 2) - 1] = undefined;
  a = 0;
  for (; a < f.length; a += 1) {
    f[a] = 0;
  }
  var g = e.length * 8;
  for (a = 0; a < g; a += 8) {
    f[a >> 5] |= (e.charCodeAt(a / 8) & 255) << a % 32;
  }
  return f;
}
function p(b) {
  return n(m(o(b), b.length * 8));
}
function q(f) {
  var a;
  var g;
  var h = "0123456789abcdef";
  var d = "";
  for (g = 0; g < f.length; g += 1) {
    a = f.charCodeAt(g);
    d += h.charAt((a >>> 4) & 15) + h.charAt(a & 15);
  }
  return d;
}
function r(b) {
  return unescape(encodeURIComponent(b));
}
function s(b) {
  return p(r(b));
}
function t(b) {
  return q(s(b));
}

function u(d, a, b) {
  k();
  if (a) {
    if (b) {
      return e(a, d);
    } else {
      return y(a, d);
    }
  } else if (b) {
    return s(d);
  } else {
    return t(d);
  }
}
var d_original = new Date().getTime(); // Renamed to avoid conflict if k() or u() use 'd'

function get_cookie() {
  // It seems k() might be problematic or return undefined based on previous attempts.
  // For now, let's assume k() should be called and its result (even if undefined) is part of the cookie.
  // The original script had `cookie = "m" + k() + "=" + u(d) + "|" + d`
  // We need to ensure 'd' used by u(d) and at the end is the current time for *this specific call*.
  let current_timestamp = new Date().getTime();
  let k_val = k(); // Call k()
  let u_val = u(current_timestamp); // Call u() with current_timestamp

  // Construct the cookie string as originally intended
  let cookie_str = "m" + k_val + "=" + u_val + "|" + current_timestamp;
  return cookie_str.split('=')[1]
}
