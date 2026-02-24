var n = require("./GenericWorker");
var o = require("../utils");
function i(e) {
  n.call(this, "ConvertWorker to " + e);
  this.destType = e;
}
o.inherits(i, n);
i.prototype.processChunk = function (e) {
  this.push({
    data: o.transformTo(this.destType, e.data),
    meta: e.meta
  });
};
module.exports = i;