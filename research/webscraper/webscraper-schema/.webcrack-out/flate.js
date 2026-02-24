var n = typeof Uint8Array != "undefined" && typeof Uint16Array != "undefined" && typeof Uint32Array != "undefined";
var o = require("pako");
var i = require("./utils");
var a = require("./stream/GenericWorker");
var s = n ? "uint8array" : "array";
function l(e, t) {
  a.call(this, "FlateWorker/" + e);
  this._pako = null;
  this._pakoAction = e;
  this._pakoOptions = t;
  this.meta = {};
}
exports.magic = "\b\0";
i.inherits(l, a);
l.prototype.processChunk = function (e) {
  this.meta = e.meta;
  if (this._pako === null) {
    this._createPako();
  }
  this._pako.push(i.transformTo(s, e.data), false);
};
l.prototype.flush = function () {
  a.prototype.flush.call(this);
  if (this._pako === null) {
    this._createPako();
  }
  this._pako.push([], true);
};
l.prototype.cleanUp = function () {
  a.prototype.cleanUp.call(this);
  this._pako = null;
};
l.prototype._createPako = function () {
  this._pako = new o[this._pakoAction]({
    raw: true,
    level: this._pakoOptions.level || -1
  });
  var e = this;
  this._pako.onData = function (t) {
    e.push({
      data: t,
      meta: e.meta
    });
  };
};
exports.compressWorker = function (e) {
  return new l("Deflate", e);
};
exports.uncompressWorker = function () {
  return new l("Inflate", {});
};