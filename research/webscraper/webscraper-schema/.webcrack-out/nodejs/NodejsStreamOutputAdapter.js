var n = require("readable-stream").Readable;
function o(e, t, r) {
  n.call(this, t);
  this._helper = e;
  var o = this;
  e.on("data", function (e, t) {
    if (!o.push(e)) {
      o._helper.pause();
    }
    if (r) {
      r(t);
    }
  }).on("error", function (e) {
    o.emit("error", e);
  }).on("end", function () {
    o.push(null);
  });
}
require("../utils").inherits(o, n);
o.prototype._read = function () {
  this._helper.resume();
};
module.exports = o;