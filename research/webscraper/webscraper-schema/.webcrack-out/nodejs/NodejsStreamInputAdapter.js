var n = require("../utils");
var o = require("../stream/GenericWorker");
function i(e, t) {
  o.call(this, "Nodejs stream input adapter for " + e);
  this._upstreamEnded = false;
  this._bindStream(t);
}
n.inherits(i, o);
i.prototype._bindStream = function (e) {
  var t = this;
  (this._stream = e).pause();
  e.on("data", function (e) {
    t.push({
      data: e,
      meta: {
        percent: 0
      }
    });
  }).on("error", function (e) {
    if (t.isPaused) {
      this.generatedError = e;
    } else {
      t.error(e);
    }
  }).on("end", function () {
    if (t.isPaused) {
      t._upstreamEnded = true;
    } else {
      t.end();
    }
  });
};
i.prototype.pause = function () {
  return !!o.prototype.pause.call(this) && (this._stream.pause(), true);
};
i.prototype.resume = function () {
  return !!o.prototype.resume.call(this) && (this._upstreamEnded ? this.end() : this._stream.resume(), true);
};
module.exports = i;