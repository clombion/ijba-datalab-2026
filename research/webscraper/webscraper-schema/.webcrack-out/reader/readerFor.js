var n = require("../utils");
var o = require("../support");
var i = require("./ArrayReader");
var a = require("./StringReader");
var s = require("./NodeBufferReader");
var l = require("./Uint8ArrayReader");
module.exports = function (e) {
  var t = n.getTypeOf(e);
  n.checkSupport(t);
  if (t !== "string" || o.uint8array) {
    if (t === "nodebuffer") {
      return new s(e);
    } else if (o.uint8array) {
      return new l(n.transformTo("uint8array", e));
    } else {
      return new i(n.transformTo("array", e));
    }
  } else {
    return new a(e);
  }
};