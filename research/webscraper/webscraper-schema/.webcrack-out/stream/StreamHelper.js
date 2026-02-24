var n = require("../utils");
var o = require("./ConvertWorker");
var i = require("./GenericWorker");
var a = require("../base64");
var s = require("../support");
var l = require("../external");
var c = null;
if (s.nodestream) {
  try {
    c = require("../nodejs/NodejsStreamOutputAdapter");
  } catch (e) {}
}
function u(e, t) {
  return new l.Promise(function (r, o) {
    var i = [];
    var s = e._internalType;
    var l = e._outputType;
    var c = e._mimeType;
    e.on("data", function (e, r) {
      i.push(e);
      if (t) {
        t(r);
      }
    }).on("error", function (e) {
      i = [];
      o(e);
    }).on("end", function () {
      try {
        var e = function (e, t, r) {
          switch (e) {
            case "blob":
              return n.newBlob(n.transformTo("arraybuffer", t), r);
            case "base64":
              return a.encode(t);
            default:
              return n.transformTo(e, t);
          }
        }(l, function (e, t) {
          var r;
          var n = 0;
          var o = null;
          var i = 0;
          for (r = 0; r < t.length; r++) {
            i += t[r].length;
          }
          switch (e) {
            case "string":
              return t.join("");
            case "array":
              return Array.prototype.concat.apply([], t);
            case "uint8array":
              o = new Uint8Array(i);
              r = 0;
              for (; r < t.length; r++) {
                o.set(t[r], n);
                n += t[r].length;
              }
              return o;
            case "nodebuffer":
              return Buffer.concat(t);
            default:
              throw new Error("concat : unsupported type '" + e + "'");
          }
        }(s, i), c);
        r(e);
      } catch (e) {
        o(e);
      }
      i = [];
    }).resume();
  });
}
function d(e, t, r) {
  var a = t;
  switch (t) {
    case "blob":
    case "arraybuffer":
      a = "uint8array";
      break;
    case "base64":
      a = "string";
  }
  try {
    this._internalType = a;
    this._outputType = t;
    this._mimeType = r;
    n.checkSupport(a);
    this._worker = e.pipe(new o(a));
    e.lock();
  } catch (e) {
    this._worker = new i("error");
    this._worker.error(e);
  }
}
d.prototype = {
  accumulate: function (e) {
    return u(this, e);
  },
  on: function (e, t) {
    var r = this;
    if (e === "data") {
      this._worker.on(e, function (e) {
        t.call(r, e.data, e.meta);
      });
    } else {
      this._worker.on(e, function () {
        n.delay(t, arguments, r);
      });
    }
    return this;
  },
  resume: function () {
    n.delay(this._worker.resume, [], this._worker);
    return this;
  },
  pause: function () {
    this._worker.pause();
    return this;
  },
  toNodejsStream: function (e) {
    n.checkSupport("nodestream");
    if (this._outputType !== "nodebuffer") {
      throw new Error(this._outputType + " is not supported by this method");
    }
    return new c(this, {
      objectMode: this._outputType !== "nodebuffer"
    }, e);
  }
};
module.exports = d;