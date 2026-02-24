var n = require("./utils");
var o = function () {
  var e;
  var t = [];
  for (var r = 0; r < 256; r++) {
    e = r;
    for (var n = 0; n < 8; n++) {
      e = e & 1 ? e >>> 1 ^ 3988292384 : e >>> 1;
    }
    t[r] = e;
  }
  return t;
}();
module.exports = function (e, t) {
  if (e !== undefined && e.length) {
    if (n.getTypeOf(e) !== "string") {
      return function (e, t, r, n) {
        var i = o;
        var a = n + r;
        e ^= -1;
        for (var s = n; s < a; s++) {
          e = e >>> 8 ^ i[(e ^ t[s]) & 255];
        }
        return ~e;
      }(t | 0, e, e.length, 0);
    } else {
      return function (e, t, r, n) {
        var i = o;
        var a = n + r;
        e ^= -1;
        for (var s = n; s < a; s++) {
          e = e >>> 8 ^ i[(e ^ t.charCodeAt(s)) & 255];
        }
        return ~e;
      }(t | 0, e, e.length, 0);
    }
  } else {
    return 0;
  }
};