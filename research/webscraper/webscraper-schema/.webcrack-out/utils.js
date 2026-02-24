var n = require("./support");
var o = require("./base64");
var i = require("./nodejsUtils");
var a = require("./external");
function s(e) {
  return e;
}
function l(e, t) {
  for (var r = 0; r < e.length; ++r) {
    t[r] = e.charCodeAt(r) & 255;
  }
  return t;
}
require("setimmediate");
exports.newBlob = function (e, t) {
  exports.checkSupport("blob");
  try {
    return new Blob([e], {
      type: t
    });
  } catch (r) {
    try {
      var n = new (self.BlobBuilder || self.WebKitBlobBuilder || self.MozBlobBuilder || self.MSBlobBuilder)();
      n.append(e);
      return n.getBlob(t);
    } catch (e) {
      throw new Error("Bug : can't construct the Blob.");
    }
  }
};
var c = {
  stringifyByChunk: function (e, t, r) {
    var n = [];
    var o = 0;
    var i = e.length;
    if (i <= r) {
      return String.fromCharCode.apply(null, e);
    }
    while (o < i) {
      if (t === "array" || t === "nodebuffer") {
        n.push(String.fromCharCode.apply(null, e.slice(o, Math.min(o + r, i))));
      } else {
        n.push(String.fromCharCode.apply(null, e.subarray(o, Math.min(o + r, i))));
      }
      o += r;
    }
    return n.join("");
  },
  stringifyByChar: function (e) {
    var t = "";
    for (var r = 0; r < e.length; r++) {
      t += String.fromCharCode(e[r]);
    }
    return t;
  },
  applyCanBeUsed: {
    uint8array: function () {
      try {
        return n.uint8array && String.fromCharCode.apply(null, new Uint8Array(1)).length === 1;
      } catch (e) {
        return false;
      }
    }(),
    nodebuffer: function () {
      try {
        return n.nodebuffer && String.fromCharCode.apply(null, i.allocBuffer(1)).length === 1;
      } catch (e) {
        return false;
      }
    }()
  }
};
function u(e) {
  var t = 65536;
  var n = exports.getTypeOf(e);
  var o = true;
  if (n === "uint8array") {
    o = c.applyCanBeUsed.uint8array;
  } else if (n === "nodebuffer") {
    o = c.applyCanBeUsed.nodebuffer;
  }
  if (o) {
    while (t > 1) {
      try {
        return c.stringifyByChunk(e, n, t);
      } catch (e) {
        t = Math.floor(t / 2);
      }
    }
  }
  return c.stringifyByChar(e);
}
function d(e, t) {
  for (var r = 0; r < e.length; r++) {
    t[r] = e[r];
  }
  return t;
}
exports.applyFromCharCode = u;
var p = {};
p.string = {
  string: s,
  array: function (e) {
    return l(e, new Array(e.length));
  },
  arraybuffer: function (e) {
    return p.string.uint8array(e).buffer;
  },
  uint8array: function (e) {
    return l(e, new Uint8Array(e.length));
  },
  nodebuffer: function (e) {
    return l(e, i.allocBuffer(e.length));
  }
};
p.array = {
  string: u,
  array: s,
  arraybuffer: function (e) {
    return new Uint8Array(e).buffer;
  },
  uint8array: function (e) {
    return new Uint8Array(e);
  },
  nodebuffer: function (e) {
    return i.newBufferFrom(e);
  }
};
p.arraybuffer = {
  string: function (e) {
    return u(new Uint8Array(e));
  },
  array: function (e) {
    return d(new Uint8Array(e), new Array(e.byteLength));
  },
  arraybuffer: s,
  uint8array: function (e) {
    return new Uint8Array(e);
  },
  nodebuffer: function (e) {
    return i.newBufferFrom(new Uint8Array(e));
  }
};
p.uint8array = {
  string: u,
  array: function (e) {
    return d(e, new Array(e.length));
  },
  arraybuffer: function (e) {
    return e.buffer;
  },
  uint8array: s,
  nodebuffer: function (e) {
    return i.newBufferFrom(e);
  }
};
p.nodebuffer = {
  string: u,
  array: function (e) {
    return d(e, new Array(e.length));
  },
  arraybuffer: function (e) {
    return p.nodebuffer.uint8array(e).buffer;
  },
  uint8array: function (e) {
    return d(e, new Uint8Array(e.length));
  },
  nodebuffer: s
};
exports.transformTo = function (e, t) {
  t = t || "";
  if (!e) {
    return t;
  }
  exports.checkSupport(e);
  var n = exports.getTypeOf(t);
  return p[n][e](t);
};
exports.resolve = function (e) {
  for (var t = e.split("/"), r = [], n = 0; n < t.length; n++) {
    var o = t[n];
    if (o !== "." && (o !== "" || n === 0 || n === t.length - 1)) {
      if (o === "..") {
        r.pop();
      } else {
        r.push(o);
      }
    }
  }
  return r.join("/");
};
exports.getTypeOf = function (e) {
  if (typeof e == "string") {
    return "string";
  } else if (Object.prototype.toString.call(e) === "[object Array]") {
    return "array";
  } else if (n.nodebuffer && i.isBuffer(e)) {
    return "nodebuffer";
  } else if (n.uint8array && e instanceof Uint8Array) {
    return "uint8array";
  } else if (n.arraybuffer && e instanceof ArrayBuffer) {
    return "arraybuffer";
  } else {
    return undefined;
  }
};
exports.checkSupport = function (e) {
  if (!n[e.toLowerCase()]) {
    throw new Error(e + " is not supported by this platform");
  }
};
exports.MAX_VALUE_16BITS = 65535;
exports.MAX_VALUE_32BITS = -1;
exports.pretty = function (e) {
  var t;
  var r;
  var n = "";
  for (r = 0; r < (e || "").length; r++) {
    n += "\\x" + ((t = e.charCodeAt(r)) < 16 ? "0" : "") + t.toString(16).toUpperCase();
  }
  return n;
};
exports.delay = function (e, t, r) {
  setImmediate(function () {
    e.apply(r || null, t || []);
  });
};
exports.inherits = function (e, t) {
  function r() {}
  r.prototype = t.prototype;
  e.prototype = new r();
};
exports.extend = function () {
  var e;
  var t;
  var r = {};
  for (e = 0; e < arguments.length; e++) {
    for (t in arguments[e]) {
      if (Object.prototype.hasOwnProperty.call(arguments[e], t) && r[t] === undefined) {
        r[t] = arguments[e][t];
      }
    }
  }
  return r;
};
exports.prepareContent = function (e, t, i, s, c) {
  return a.Promise.resolve(t).then(function (e) {
    if (n.blob && (e instanceof Blob || ["[object File]", "[object Blob]"].indexOf(Object.prototype.toString.call(e)) !== -1) && typeof FileReader != "undefined") {
      return new a.Promise(function (t, r) {
        var n = new FileReader();
        n.onload = function (e) {
          t(e.target.result);
        };
        n.onerror = function (e) {
          r(e.target.error);
        };
        n.readAsArrayBuffer(e);
      });
    } else {
      return e;
    }
  }).then(function (t) {
    var u = exports.getTypeOf(t);
    if (u) {
      if (u === "arraybuffer") {
        t = exports.transformTo("uint8array", t);
      } else if (u === "string") {
        if (c) {
          t = o.decode(t);
        } else if (i && s !== true) {
          t = function (e) {
            return l(e, n.uint8array ? new Uint8Array(e.length) : new Array(e.length));
          }(t);
        }
      }
      return t;
    } else {
      return a.Promise.reject(new Error("Can't read the data of '" + e + "'. Is it in a supported JavaScript type (String, Blob, ArrayBuffer, etc) ?"));
    }
  });
};