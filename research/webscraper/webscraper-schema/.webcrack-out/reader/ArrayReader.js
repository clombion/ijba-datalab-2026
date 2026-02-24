var n = require("./DataReader");
function o(e) {
  n.call(this, e);
  for (var t = 0; t < this.data.length; t++) {
    e[t] = e[t] & 255;
  }
}
require("../utils").inherits(o, n);
o.prototype.byteAt = function (e) {
  return this.data[this.zero + e];
};
o.prototype.lastIndexOfSignature = function (e) {
  var t = e.charCodeAt(0);
  var r = e.charCodeAt(1);
  var n = e.charCodeAt(2);
  var o = e.charCodeAt(3);
  for (var i = this.length - 4; i >= 0; --i) {
    if (this.data[i] === t && this.data[i + 1] === r && this.data[i + 2] === n && this.data[i + 3] === o) {
      return i - this.zero;
    }
  }
  return -1;
};
o.prototype.readAndCheckSignature = function (e) {
  var t = e.charCodeAt(0);
  var r = e.charCodeAt(1);
  var n = e.charCodeAt(2);
  var o = e.charCodeAt(3);
  var i = this.readData(4);
  return t === i[0] && r === i[1] && n === i[2] && o === i[3];
};
o.prototype.readData = function (e) {
  this.checkOffset(e);
  if (e === 0) {
    return [];
  }
  var t = this.data.slice(this.zero + this.index, this.zero + this.index + e);
  this.index += e;
  return t;
};
module.exports = o;