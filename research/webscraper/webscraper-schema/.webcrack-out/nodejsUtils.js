module.exports = {
  isNode: typeof Buffer != "undefined",
  newBufferFrom: function (e, t) {
    if (Buffer.from && Buffer.from !== Uint8Array.from) {
      return Buffer.from(e, t);
    }
    if (typeof e == "number") {
      throw new Error("The \"data\" argument must not be a number");
    }
    return new Buffer(e, t);
  },
  allocBuffer: function (e) {
    if (Buffer.alloc) {
      return Buffer.alloc(e);
    }
    var t = new Buffer(e);
    t.fill(0);
    return t;
  },
  isBuffer: function (e) {
    return Buffer.isBuffer(e);
  },
  isStream: function (e) {
    return e && typeof e.on == "function" && typeof e.pause == "function" && typeof e.resume == "function";
  }
};