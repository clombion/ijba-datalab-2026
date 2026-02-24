var n = require("../utils");
var o = require("./GenericWorker");
function i(e) {
  o.call(this, "DataLengthProbe for " + e);
  this.propName = e;
  this.withStreamInfo(e, 0);
}
n.inherits(i, o);
i.prototype.processChunk = function (e) {
  if (e) {
    var t = this.streamInfo[this.propName] || 0;
    this.streamInfo[this.propName] = t + e.data.length;
  }
  o.prototype.processChunk.call(this, e);
};
module.exports = i;