var n = require("./Uint8ArrayReader");
function o(e) {
  n.call(this, e);
}
require("../utils").inherits(o, n);
o.prototype.readData = function (e) {
  this.checkOffset(e);
  var t = this.data.slice(this.zero + this.index, this.zero + this.index + e);
  this.index += e;
  return t;
};
module.exports = o;