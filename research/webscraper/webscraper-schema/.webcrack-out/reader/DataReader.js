var n = require("../utils");
function o(e) {
  this.data = e;
  this.length = e.length;
  this.index = 0;
  this.zero = 0;
}
o.prototype = {
  checkOffset: function (e) {
    this.checkIndex(this.index + e);
  },
  checkIndex: function (e) {
    if (this.length < this.zero + e || e < 0) {
      throw new Error("End of data reached (data length = " + this.length + ", asked index = " + e + "). Corrupted zip ?");
    }
  },
  setIndex: function (e) {
    this.checkIndex(e);
    this.index = e;
  },
  skip: function (e) {
    this.setIndex(this.index + e);
  },
  byteAt: function () {},
  readInt: function (e) {
    var t;
    var r = 0;
    this.checkOffset(e);
    t = this.index + e - 1;
    for (; t >= this.index; t--) {
      r = (r << 8) + this.byteAt(t);
    }
    this.index += e;
    return r;
  },
  readString: function (e) {
    return n.transformTo("string", this.readData(e));
  },
  readData: function () {},
  lastIndexOfSignature: function () {},
  readAndCheckSignature: function () {},
  readDate: function () {
    var e = this.readInt(4);
    return new Date(Date.UTC(1980 + (e >> 25 & 127), (e >> 21 & 15) - 1, e >> 16 & 31, e >> 11 & 31, e >> 5 & 63, (e & 31) << 1));
  }
};
module.exports = o;