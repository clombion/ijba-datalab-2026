var n = require("./utils");
var o = require("./support");
var i = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
exports.encode = function (e) {
  var t;
  var r;
  var o;
  var a;
  var s;
  var l;
  var c;
  var u = [];
  for (var d = 0, p = e.length, f = p, h = n.getTypeOf(e) !== "string"; d < e.length;) {
    f = p - d;
    o = h ? (t = e[d++], r = d < p ? e[d++] : 0, d < p ? e[d++] : 0) : (t = e.charCodeAt(d++), r = d < p ? e.charCodeAt(d++) : 0, d < p ? e.charCodeAt(d++) : 0);
    a = t >> 2;
    s = (t & 3) << 4 | r >> 4;
    l = f > 1 ? (r & 15) << 2 | o >> 6 : 64;
    c = f > 2 ? o & 63 : 64;
    u.push(i.charAt(a) + i.charAt(s) + i.charAt(l) + i.charAt(c));
  }
  return u.join("");
};
exports.decode = function (e) {
  var t;
  var r;
  var n;
  var a;
  var s;
  var l;
  var c = 0;
  var u = 0;
  var d = "data:";
  if (e.substr(0, d.length) === d) {
    throw new Error("Invalid base64 input, it looks like a data url.");
  }
  var p;
  var f = (e = e.replace(/[^A-Za-z0-9+/=]/g, "")).length * 3 / 4;
  if (e.charAt(e.length - 1) === i.charAt(64)) {
    f--;
  }
  if (e.charAt(e.length - 2) === i.charAt(64)) {
    f--;
  }
  if (f % 1 != 0) {
    throw new Error("Invalid base64 input, bad content length.");
  }
  for (p = o.uint8array ? new Uint8Array(f | 0) : new Array(f | 0); c < e.length;) {
    t = i.indexOf(e.charAt(c++)) << 2 | (a = i.indexOf(e.charAt(c++))) >> 4;
    r = (a & 15) << 4 | (s = i.indexOf(e.charAt(c++))) >> 2;
    n = (s & 3) << 6 | (l = i.indexOf(e.charAt(c++)));
    p[u++] = t;
    if (s !== 64) {
      p[u++] = r;
    }
    if (l !== 64) {
      p[u++] = n;
    }
  }
  return p;
};