function n() {
  if (!(this instanceof n)) {
    return new n();
  }
  if (arguments.length) {
    throw new Error("The constructor with parameters has been removed in JSZip 3.0, please check the upgrade guide.");
  }
  this.files = Object.create(null);
  this.comment = null;
  this.root = "";
  this.clone = function () {
    var e = new n();
    for (var t in this) {
      if (typeof this[t] != "function") {
        e[t] = this[t];
      }
    }
    return e;
  };
}
(n.prototype = require("./object")).loadAsync = require("./load");
n.support = require("./support");
n.defaults = require("./defaults");
n.version = "3.10.1";
n.loadAsync = function (e, t) {
  return new n().loadAsync(e, t);
};
n.external = require("./external");
module.exports = n;