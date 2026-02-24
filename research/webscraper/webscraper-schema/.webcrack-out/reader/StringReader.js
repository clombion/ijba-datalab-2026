var n = require("./DataReader");
function o(e) {
  n.call(this, e);
}
require("../utils").inherits(o, n);
o.prototype.byteAt = function (e) {
  return this.data.charCodeAt(this.zero + e);
};
o.prototype.lastIndexOfSignature = function (e) {
  return this.data.lastIndexOf(e) - this.zero;
};
o.prototype.readAndCheckSignature = function (e) {
  return e === this.readData(4);
};
o.prototype.readData = function (e) {
  this.checkOffset(e);
  var t = this.data.slice(this.zero + this.index, this.zero + this.index + e);
  this.index += e;
  return t;
};
module.exports = o;