var n = require("./stream/GenericWorker");
exports.STORE = {
  magic: "\0\0",
  compressWorker: function () {
    return new n("STORE compression");
  },
  uncompressWorker: function () {
    return new n("STORE decompression");
  }
};
exports.DEFLATE = require("./flate");