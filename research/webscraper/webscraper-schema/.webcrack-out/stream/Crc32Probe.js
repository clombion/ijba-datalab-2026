var n = require("./GenericWorker");
var o = require("../crc32");
function i() {
  n.call(this, "Crc32Probe");
  this.withStreamInfo("crc32", 0);
}
require("../utils").inherits(i, n);
i.prototype.processChunk = function (e) {
  this.streamInfo.crc32 = o(e.data, this.streamInfo.crc32 || 0);
  this.push(e);
};
module.exports = i;