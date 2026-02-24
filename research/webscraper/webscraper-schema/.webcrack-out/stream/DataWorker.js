var n = require("../utils");
var o = require("./GenericWorker");
function i(e) {
  o.call(this, "DataWorker");
  var t = this;
  this.dataIsReady = false;
  this.index = 0;
  this.max = 0;
  this.data = null;
  this.type = "";
  this._tickScheduled = false;
  e.then(function (e) {
    t.dataIsReady = true;
    t.data = e;
    t.max = e && e.length || 0;
    t.type = n.getTypeOf(e);
    if (!t.isPaused) {
      t._tickAndRepeat();
    }
  }, function (e) {
    t.error(e);
  });
}
n.inherits(i, o);
i.prototype.cleanUp = function () {
  o.prototype.cleanUp.call(this);
  this.data = null;
};
i.prototype.resume = function () {
  return !!o.prototype.resume.call(this) && (!this._tickScheduled && this.dataIsReady && (this._tickScheduled = true, n.delay(this._tickAndRepeat, [], this)), true);
};
i.prototype._tickAndRepeat = function () {
  this._tickScheduled = false;
  if (!this.isPaused && !this.isFinished) {
    this._tick();
    if (!this.isFinished) {
      n.delay(this._tickAndRepeat, [], this);
      this._tickScheduled = true;
    }
  }
};
i.prototype._tick = function () {
  if (this.isPaused || this.isFinished) {
    return false;
  }
  var e = null;
  var t = Math.min(this.max, this.index + 16384);
  if (this.index >= this.max) {
    return this.end();
  }
  switch (this.type) {
    case "string":
      e = this.data.substring(this.index, t);
      break;
    case "uint8array":
      e = this.data.subarray(this.index, t);
      break;
    case "array":
    case "nodebuffer":
      e = this.data.slice(this.index, t);
  }
  this.index = t;
  return this.push({
    data: e,
    meta: {
      percent: this.max ? this.index / this.max * 100 : 0
    }
  });
};
module.exports = i;