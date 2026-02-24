var n = require("./ArrayReader");
function o(e) {
  n.call(this, e);
}
require("../utils").inherits(o, n);
o.prototype.readData = function (e) {
  this.checkOffset(e);
  if (e === 0) {
    return new Uint8Array(0);
  }
  var t = this.data.subarray(this.zero + this.index, this.zero + this.index + e);
  this.index += e;
  return t;
};
module.exports = o;