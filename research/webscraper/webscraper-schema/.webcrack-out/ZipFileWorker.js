function n(e, t) {
  var r;
  var n = "";
  for (r = 0; r < t; r++) {
    n += String.fromCharCode(e & 255);
    e >>>= 8;
  }
  return n;
}
function o(e, t, r, o, a, u) {
  var d;
  var p;
  var f = e.file;
  var h = e.compression;
  var m = u !== s.utf8encode;
  var g = i.transformTo("string", u(f.name));
  var v = i.transformTo("string", s.utf8encode(f.name));
  var y = f.comment;
  var b = i.transformTo("string", u(y));
  var w = i.transformTo("string", s.utf8encode(y));
  var S = v.length !== f.name.length;
  var x = w.length !== y.length;
  var A = "";
  var _ = "";
  var C = "";
  var E = f.dir;
  var k = f.date;
  var O = {
    crc32: 0,
    compressedSize: 0,
    uncompressedSize: 0
  };
  if (!t || !!r) {
    O.crc32 = e.crc32;
    O.compressedSize = e.compressedSize;
    O.uncompressedSize = e.uncompressedSize;
  }
  var T = 0;
  if (t) {
    T |= 8;
  }
  if (!m && (!!S || !!x)) {
    T |= 2048;
  }
  var P = 0;
  var R = 0;
  if (E) {
    P |= 16;
  }
  if (a === "UNIX") {
    R = 798;
    P |= function (e, t) {
      var r = e;
      if (!e) {
        r = t ? 16893 : 33204;
      }
      return (r & 65535) << 16;
    }(f.unixPermissions, E);
  } else {
    R = 20;
    P |= function (e) {
      return (e || 0) & 63;
    }(f.dosPermissions);
  }
  d = k.getUTCHours();
  d <<= 6;
  d |= k.getUTCMinutes();
  d <<= 5;
  d |= k.getUTCSeconds() / 2;
  p = k.getUTCFullYear() - 1980;
  p <<= 4;
  p |= k.getUTCMonth() + 1;
  p <<= 5;
  p |= k.getUTCDate();
  if (S) {
    _ = n(1, 1) + n(l(g), 4) + v;
    A += "up" + n(_.length, 2) + _;
  }
  if (x) {
    C = n(1, 1) + n(l(b), 4) + w;
    A += "uc" + n(C.length, 2) + C;
  }
  var I = "";
  I += "\n\0";
  I += n(T, 2);
  I += h.magic;
  I += n(d, 2);
  I += n(p, 2);
  I += n(O.crc32, 4);
  I += n(O.compressedSize, 4);
  I += n(O.uncompressedSize, 4);
  I += n(g.length, 2);
  I += n(A.length, 2);
  return {
    fileRecord: c.LOCAL_FILE_HEADER + I + g + A,
    dirRecord: c.CENTRAL_FILE_HEADER + n(R, 2) + I + n(b.length, 2) + "\0\0\0\0" + n(P, 4) + n(o, 4) + g + A + b
  };
}
var i = require("../utils");
var a = require("../stream/GenericWorker");
var s = require("../utf8");
var l = require("../crc32");
var c = require("../signature");
function u(e, t, r, n) {
  a.call(this, "ZipFileWorker");
  this.bytesWritten = 0;
  this.zipComment = t;
  this.zipPlatform = r;
  this.encodeFileName = n;
  this.streamFiles = e;
  this.accumulate = false;
  this.contentBuffer = [];
  this.dirRecords = [];
  this.currentSourceOffset = 0;
  this.entriesCount = 0;
  this.currentFile = null;
  this._sources = [];
}
i.inherits(u, a);
u.prototype.push = function (e) {
  var t = e.meta.percent || 0;
  var r = this.entriesCount;
  var n = this._sources.length;
  if (this.accumulate) {
    this.contentBuffer.push(e);
  } else {
    this.bytesWritten += e.data.length;
    a.prototype.push.call(this, {
      data: e.data,
      meta: {
        currentFile: this.currentFile,
        percent: r ? (t + (r - n - 1) * 100) / r : 100
      }
    });
  }
};
u.prototype.openedSource = function (e) {
  this.currentSourceOffset = this.bytesWritten;
  this.currentFile = e.file.name;
  var t = this.streamFiles && !e.file.dir;
  if (t) {
    var r = o(e, t, false, this.currentSourceOffset, this.zipPlatform, this.encodeFileName);
    this.push({
      data: r.fileRecord,
      meta: {
        percent: 0
      }
    });
  } else {
    this.accumulate = true;
  }
};
u.prototype.closedSource = function (e) {
  this.accumulate = false;
  var t = this.streamFiles && !e.file.dir;
  var r = o(e, t, true, this.currentSourceOffset, this.zipPlatform, this.encodeFileName);
  this.dirRecords.push(r.dirRecord);
  if (t) {
    this.push({
      data: function (e) {
        return c.DATA_DESCRIPTOR + n(e.crc32, 4) + n(e.compressedSize, 4) + n(e.uncompressedSize, 4);
      }(e),
      meta: {
        percent: 100
      }
    });
  } else {
    for (this.push({
      data: r.fileRecord,
      meta: {
        percent: 0
      }
    }); this.contentBuffer.length;) {
      this.push(this.contentBuffer.shift());
    }
  }
  this.currentFile = null;
};
u.prototype.flush = function () {
  var e = this.bytesWritten;
  for (var t = 0; t < this.dirRecords.length; t++) {
    this.push({
      data: this.dirRecords[t],
      meta: {
        percent: 100
      }
    });
  }
  var r = this.bytesWritten - e;
  var o = function (e, t, r, o, a) {
    var s = i.transformTo("string", a(o));
    return c.CENTRAL_DIRECTORY_END + "\0\0\0\0" + n(e, 2) + n(e, 2) + n(t, 4) + n(r, 4) + n(s.length, 2) + s;
  }(this.dirRecords.length, r, e, this.zipComment, this.encodeFileName);
  this.push({
    data: o,
    meta: {
      percent: 100
    }
  });
};
u.prototype.prepareNextSource = function () {
  this.previous = this._sources.shift();
  this.openedSource(this.previous.streamInfo);
  if (this.isPaused) {
    this.previous.pause();
  } else {
    this.previous.resume();
  }
};
u.prototype.registerPrevious = function (e) {
  this._sources.push(e);
  var t = this;
  e.on("data", function (e) {
    t.processChunk(e);
  });
  e.on("end", function () {
    t.closedSource(t.previous.streamInfo);
    if (t._sources.length) {
      t.prepareNextSource();
    } else {
      t.end();
    }
  });
  e.on("error", function (e) {
    t.error(e);
  });
  return this;
};
u.prototype.resume = function () {
  return !!a.prototype.resume.call(this) && (!this.previous && this._sources.length ? (this.prepareNextSource(), true) : this.previous || this._sources.length || this.generatedError ? undefined : (this.end(), true));
};
u.prototype.error = function (e) {
  var t = this._sources;
  if (!a.prototype.error.call(this, e)) {
    return false;
  }
  for (var r = 0; r < t.length; r++) {
    try {
      t[r].error(e);
    } catch (e) {}
  }
  return true;
};
u.prototype.lock = function () {
  a.prototype.lock.call(this);
  for (var e = this._sources, t = 0; t < e.length; t++) {
    e[t].lock();
  }
};
module.exports = u;