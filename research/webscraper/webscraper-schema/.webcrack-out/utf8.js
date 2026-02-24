var n = require("./utils");
var o = require("./support");
var i = require("./nodejsUtils");
var a = require("./stream/GenericWorker");
var s = new Array(256);
for (var l = 0; l < 256; l++) {
  s[l] = l >= 252 ? 6 : l >= 248 ? 5 : l >= 240 ? 4 : l >= 224 ? 3 : l >= 192 ? 2 : 1;
}
function c() {
  a.call(this, "utf-8 decode");
  this.leftOver = null;
}
function u() {
  a.call(this, "utf-8 encode");
}
s[254] = s[254] = 1;
exports.utf8encode = function (e) {
  if (o.nodebuffer) {
    return i.newBufferFrom(e, "utf-8");
  } else {
    return function (e) {
      var t;
      var r;
      var n;
      var i;
      var a;
      var s = e.length;
      var l = 0;
      for (i = 0; i < s; i++) {
        if (((r = e.charCodeAt(i)) & 64512) == 55296 && i + 1 < s && ((n = e.charCodeAt(i + 1)) & 64512) == 56320) {
          r = 65536 + (r - 55296 << 10) + (n - 56320);
          i++;
        }
        l += r < 128 ? 1 : r < 2048 ? 2 : r < 65536 ? 3 : 4;
      }
      t = o.uint8array ? new Uint8Array(l) : new Array(l);
      i = a = 0;
      for (; a < l; i++) {
        if (((r = e.charCodeAt(i)) & 64512) == 55296 && i + 1 < s && ((n = e.charCodeAt(i + 1)) & 64512) == 56320) {
          r = 65536 + (r - 55296 << 10) + (n - 56320);
          i++;
        }
        if (r < 128) {
          t[a++] = r;
        } else {
          if (r < 2048) {
            t[a++] = r >>> 6 | 192;
          } else {
            if (r < 65536) {
              t[a++] = r >>> 12 | 224;
            } else {
              t[a++] = r >>> 18 | 240;
              t[a++] = r >>> 12 & 63 | 128;
            }
            t[a++] = r >>> 6 & 63 | 128;
          }
          t[a++] = r & 63 | 128;
        }
      }
      return t;
    }(e);
  }
};
exports.utf8decode = function (e) {
  if (o.nodebuffer) {
    return n.transformTo("nodebuffer", e).toString("utf-8");
  } else {
    return function (e) {
      var t;
      var r;
      var o;
      var i;
      var a = e.length;
      var l = new Array(a * 2);
      for (t = r = 0; t < a;) {
        if ((o = e[t++]) < 128) {
          l[r++] = o;
        } else if ((i = s[o]) > 4) {
          l[r++] = 65533;
          t += i - 1;
        } else {
          for (o &= i === 2 ? 31 : i === 3 ? 15 : 7; i > 1 && t < a;) {
            o = o << 6 | e[t++] & 63;
            i--;
          }
          if (i > 1) {
            l[r++] = 65533;
          } else if (o < 65536) {
            l[r++] = o;
          } else {
            o -= 65536;
            l[r++] = o >> 10 & 1023 | 55296;
            l[r++] = o & 1023 | 56320;
          }
        }
      }
      if (l.length !== r) {
        if (l.subarray) {
          l = l.subarray(0, r);
        } else {
          l.length = r;
        }
      }
      return n.applyFromCharCode(l);
    }(e = n.transformTo(o.uint8array ? "uint8array" : "array", e));
  }
};
n.inherits(c, a);
c.prototype.processChunk = function (e) {
  var t = n.transformTo(o.uint8array ? "uint8array" : "array", e.data);
  if (this.leftOver && this.leftOver.length) {
    if (o.uint8array) {
      var i = t;
      (t = new Uint8Array(i.length + this.leftOver.length)).set(this.leftOver, 0);
      t.set(i, this.leftOver.length);
    } else {
      t = this.leftOver.concat(t);
    }
    this.leftOver = null;
  }
  var a = function (e, t) {
    var r;
    if ((t = t || e.length) > e.length) {
      t = e.length;
    }
    r = t - 1;
    while (r >= 0 && (e[r] & 192) == 128) {
      r--;
    }
    if (r < 0 || r === 0) {
      return t;
    } else if (r + s[e[r]] > t) {
      return r;
    } else {
      return t;
    }
  }(t);
  var l = t;
  if (a !== t.length) {
    if (o.uint8array) {
      l = t.subarray(0, a);
      this.leftOver = t.subarray(a, t.length);
    } else {
      l = t.slice(0, a);
      this.leftOver = t.slice(a, t.length);
    }
  }
  this.push({
    data: exports.utf8decode(l),
    meta: e.meta
  });
};
c.prototype.flush = function () {
  if (this.leftOver && this.leftOver.length) {
    this.push({
      data: exports.utf8decode(this.leftOver),
      meta: {}
    });
    this.leftOver = null;
  }
};
exports.Utf8DecodeWorker = c;
n.inherits(u, a);
u.prototype.processChunk = function (e) {
  this.push({
    data: exports.utf8encode(e.data),
    meta: e.meta
  });
};
exports.Utf8EncodeWorker = u;