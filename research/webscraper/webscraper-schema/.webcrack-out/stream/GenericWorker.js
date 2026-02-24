function n(e) {
  this.name = e || "default";
  this.streamInfo = {};
  this.generatedError = null;
  this.extraStreamInfo = {};
  this.isPaused = true;
  this.isFinished = false;
  this.isLocked = false;
  this._listeners = {
    data: [],
    end: [],
    error: []
  };
  this.previous = null;
}
n.prototype = {
  push: function (e) {
    this.emit("data", e);
  },
  end: function () {
    if (this.isFinished) {
      return false;
    }
    this.flush();
    try {
      this.emit("end");
      this.cleanUp();
      this.isFinished = true;
    } catch (e) {
      this.emit("error", e);
    }
    return true;
  },
  error: function (e) {
    return !this.isFinished && (this.isPaused ? this.generatedError = e : (this.isFinished = true, this.emit("error", e), this.previous && this.previous.error(e), this.cleanUp()), true);
  },
  on: function (e, t) {
    this._listeners[e].push(t);
    return this;
  },
  cleanUp: function () {
    this.streamInfo = this.generatedError = this.extraStreamInfo = null;
    this._listeners = [];
  },
  emit: function (e, t) {
    if (this._listeners[e]) {
      for (var r = 0; r < this._listeners[e].length; r++) {
        this._listeners[e][r].call(this, t);
      }
    }
  },
  pipe: function (e) {
    return e.registerPrevious(this);
  },
  registerPrevious: function (e) {
    if (this.isLocked) {
      throw new Error("The stream '" + this + "' has already been used.");
    }
    this.streamInfo = e.streamInfo;
    this.mergeStreamInfo();
    this.previous = e;
    var t = this;
    e.on("data", function (e) {
      t.processChunk(e);
    });
    e.on("end", function () {
      t.end();
    });
    e.on("error", function (e) {
      t.error(e);
    });
    return this;
  },
  pause: function () {
    return !this.isPaused && !this.isFinished && (this.isPaused = true, this.previous && this.previous.pause(), true);
  },
  resume: function () {
    if (!this.isPaused || this.isFinished) {
      return false;
    }
    var e = this.isPaused = false;
    if (this.generatedError) {
      this.error(this.generatedError);
      e = true;
    }
    if (this.previous) {
      this.previous.resume();
    }
    return !e;
  },
  flush: function () {},
  processChunk: function (e) {
    this.push(e);
  },
  withStreamInfo: function (e, t) {
    this.extraStreamInfo[e] = t;
    this.mergeStreamInfo();
    return this;
  },
  mergeStreamInfo: function () {
    for (var e in this.extraStreamInfo) {
      if (Object.prototype.hasOwnProperty.call(this.extraStreamInfo, e)) {
        this.streamInfo[e] = this.extraStreamInfo[e];
      }
    }
  },
  lock: function () {
    if (this.isLocked) {
      throw new Error("The stream '" + this + "' has already been used.");
    }
    this.isLocked = true;
    if (this.previous) {
      this.previous.lock();
    }
  },
  toString: function () {
    var e = "Worker " + this.name;
    if (this.previous) {
      return this.previous + " -> " + e;
    } else {
      return e;
    }
  }
};
module.exports = n;