function n(e, t, r) {
  this.name = e;
  this.dir = r.dir;
  this.date = r.date;
  this.comment = r.comment;
  this.unixPermissions = r.unixPermissions;
  this.dosPermissions = r.dosPermissions;
  this._data = t;
  this._dataBinary = r.binary;
  this.options = {
    compression: r.compression,
    compressionOptions: r.compressionOptions
  };
}
var o = require("./stream/StreamHelper");
var i = require("./stream/DataWorker");
var a = require("./utf8");
var s = require("./compressedObject");
var l = require("./stream/GenericWorker");
n.prototype = {
  internalStream: function (e) {
    var t = null;
    var r = "string";
    try {
      if (!e) {
        throw new Error("No output type specified.");
      }
      var n = (r = e.toLowerCase()) === "string" || r === "text";
      if (r === "binarystring" || r === "text") {
        r = "string";
      }
      t = this._decompressWorker();
      var i = !this._dataBinary;
      if (i && !n) {
        t = t.pipe(new a.Utf8EncodeWorker());
      }
      if (!i && n) {
        t = t.pipe(new a.Utf8DecodeWorker());
      }
    } catch (e) {
      (t = new l("error")).error(e);
    }
    return new o(t, r, "");
  },
  async: function (e, t) {
    return this.internalStream(e).accumulate(t);
  },
  nodeStream: function (e, t) {
    return this.internalStream(e || "nodebuffer").toNodejsStream(t);
  },
  _compressWorker: function (e, t) {
    if (this._data instanceof s && this._data.compression.magic === e.magic) {
      return this._data.getCompressedWorker();
    }
    var r = this._decompressWorker();
    if (!this._dataBinary) {
      r = r.pipe(new a.Utf8EncodeWorker());
    }
    return s.createWorkerFrom(r, e, t);
  },
  _decompressWorker: function () {
    if (this._data instanceof s) {
      return this._data.getContentWorker();
    } else if (this._data instanceof l) {
      return this._data;
    } else {
      return new i(this._data);
    }
  }
};
for (var c = ["asText", "asBinary", "asNodeBuffer", "asUint8Array", "asArrayBuffer"], u = function () {
    throw new Error("This method has been removed in JSZip 3.0, please check the upgrade guide.");
  }, d = 0; d < c.length; d++) {
  n.prototype[c[d]] = u;
}
module.exports = n;