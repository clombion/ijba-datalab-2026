function n(e, t, r) {
  var n;
  var o = i.getTypeOf(t);
  var s = i.extend(r || {}, l);
  s.date = s.date || new Date();
  if (s.compression !== null) {
    s.compression = s.compression.toUpperCase();
  }
  if (typeof s.unixPermissions == "string") {
    s.unixPermissions = parseInt(s.unixPermissions, 8);
  }
  if (s.unixPermissions && s.unixPermissions & 16384) {
    s.dir = true;
  }
  if (s.dosPermissions && s.dosPermissions & 16) {
    s.dir = true;
  }
  if (s.dir) {
    e = m(e);
  }
  if (s.createFolders && (n = h(e))) {
    g.call(this, n, true);
  }
  var d = o === "string" && s.binary === false && s.base64 === false;
  if (!r || r.binary === undefined) {
    s.binary = !d;
  }
  if (t instanceof c && t.uncompressedSize === 0 || s.dir || !t || t.length === 0) {
    s.base64 = false;
    s.binary = true;
    t = "";
    s.compression = "STORE";
    o = "string";
  }
  var v = null;
  v = t instanceof c || t instanceof a ? t : p.isNode && p.isStream(t) ? new f(e, t) : i.prepareContent(e, t, s.binary, s.optimizedBinaryString, s.base64);
  var y = new u(e, v, s);
  this.files[e] = y;
}
var o = require("./utf8");
var i = require("./utils");
var a = require("./stream/GenericWorker");
var s = require("./stream/StreamHelper");
var l = require("./defaults");
var c = require("./compressedObject");
var u = require("./zipObject");
var d = require("./generate");
var p = require("./nodejsUtils");
var f = require("./nodejs/NodejsStreamInputAdapter");
function h(e) {
  if (e.slice(-1) === "/") {
    e = e.substring(0, e.length - 1);
  }
  var t = e.lastIndexOf("/");
  if (t > 0) {
    return e.substring(0, t);
  } else {
    return "";
  }
}
function m(e) {
  if (e.slice(-1) !== "/") {
    e += "/";
  }
  return e;
}
function g(e, t) {
  t = t !== undefined ? t : l.createFolders;
  e = m(e);
  if (!this.files[e]) {
    n.call(this, e, null, {
      dir: true,
      createFolders: t
    });
  }
  return this.files[e];
}
function v(e) {
  return Object.prototype.toString.call(e) === "[object RegExp]";
}
var y = {
  load: function () {
    throw new Error("This method has been removed in JSZip 3.0, please check the upgrade guide.");
  },
  forEach: function (e) {
    var t;
    var r;
    var n;
    for (t in this.files) {
      n = this.files[t];
      if ((r = t.slice(this.root.length, t.length)) && t.slice(0, this.root.length) === this.root) {
        e(r, n);
      }
    }
  },
  filter: function (e) {
    var t = [];
    this.forEach(function (r, n) {
      if (e(r, n)) {
        t.push(n);
      }
    });
    return t;
  },
  file: function (e, t, r) {
    if (arguments.length !== 1) {
      e = this.root + e;
      n.call(this, e, t, r);
      return this;
    }
    if (v(e)) {
      var o = e;
      return this.filter(function (e, t) {
        return !t.dir && o.test(e);
      });
    }
    var i = this.files[this.root + e];
    if (i && !i.dir) {
      return i;
    } else {
      return null;
    }
  },
  folder: function (e) {
    if (!e) {
      return this;
    }
    if (v(e)) {
      return this.filter(function (t, r) {
        return r.dir && e.test(t);
      });
    }
    var t = this.root + e;
    var r = g.call(this, t);
    var n = this.clone();
    n.root = r.name;
    return n;
  },
  remove: function (e) {
    e = this.root + e;
    var t = this.files[e];
    if (!t) {
      if (e.slice(-1) !== "/") {
        e += "/";
      }
      t = this.files[e];
    }
    if (t && !t.dir) {
      delete this.files[e];
    } else {
      for (var r = this.filter(function (t, r) {
          return r.name.slice(0, e.length) === e;
        }), n = 0; n < r.length; n++) {
        delete this.files[r[n].name];
      }
    }
    return this;
  },
  generate: function () {
    throw new Error("This method has been removed in JSZip 3.0, please check the upgrade guide.");
  },
  generateInternalStream: function (e) {
    var t;
    var r = {};
    try {
      (r = i.extend(e || {}, {
        streamFiles: false,
        compression: "STORE",
        compressionOptions: null,
        type: "",
        platform: "DOS",
        comment: null,
        mimeType: "application/zip",
        encodeFileName: o.utf8encode
      })).type = r.type.toLowerCase();
      r.compression = r.compression.toUpperCase();
      if (r.type === "binarystring") {
        r.type = "string";
      }
      if (!r.type) {
        throw new Error("No output type specified.");
      }
      i.checkSupport(r.type);
      if (r.platform === "darwin" || r.platform === "freebsd" || r.platform === "linux" || r.platform === "sunos") {
        r.platform = "UNIX";
      }
      if (r.platform === "win32") {
        r.platform = "DOS";
      }
      var n = r.comment || this.comment || "";
      t = d.generateWorker(this, r, n);
    } catch (e) {
      (t = new a("error")).error(e);
    }
    return new s(t, r.type || "string", r.mimeType);
  },
  generateAsync: function (e, t) {
    return this.generateInternalStream(e).accumulate(t);
  },
  generateNodeStream: function (e, t) {
    if (!(e = e || {}).type) {
      e.type = "nodebuffer";
    }
    return this.generateInternalStream(e).toNodejsStream(t);
  }
};
module.exports = y;