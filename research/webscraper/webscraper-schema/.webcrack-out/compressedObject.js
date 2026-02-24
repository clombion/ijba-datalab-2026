var n = require("./external");
var o = require("./stream/DataWorker");
var i = require("./stream/Crc32Probe");
var a = require("./stream/DataLengthProbe");
function s(e, t, r, n, o) {
  this.compressedSize = e;
  this.uncompressedSize = t;
  this.crc32 = r;
  this.compression = n;
  this.compressedContent = o;
}
s.prototype = {
  getContentWorker: function () {
    var e = new o(n.Promise.resolve(this.compressedContent)).pipe(this.compression.uncompressWorker()).pipe(new a("data_length"));
    var t = this;
    e.on("end", function () {
      if (this.streamInfo.data_length !== t.uncompressedSize) {
        throw new Error("Bug : uncompressed data size mismatch");
      }
    });
    return e;
  },
  getCompressedWorker: function () {
    return new o(n.Promise.resolve(this.compressedContent)).withStreamInfo("compressedSize", this.compressedSize).withStreamInfo("uncompressedSize", this.uncompressedSize).withStreamInfo("crc32", this.crc32).withStreamInfo("compression", this.compression);
  }
};
s.createWorkerFrom = function (e, t, r) {
  return e.pipe(new i()).pipe(new a("uncompressedSize")).pipe(t.compressWorker(r)).pipe(new a("compressedSize")).withStreamInfo("compression", t);
};
module.exports = s;