var n = require("../compressions");
var o = require("./ZipFileWorker");
exports.generateWorker = function (e, t, r) {
  var i = new o(t.streamFiles, r, t.platform, t.encodeFileName);
  var a = 0;
  try {
    e.forEach(function (e, r) {
      a++;
      var o = function (e, t) {
        var r = e || t;
        var o = n[r];
        if (!o) {
          throw new Error(r + " is not a valid compression method !");
        }
        return o;
      }(r.options.compression, t.compression);
      var s = r.options.compressionOptions || t.compressionOptions || {};
      var l = r.dir;
      var c = r.date;
      r._compressWorker(o, s).withStreamInfo("file", {
        name: e,
        dir: l,
        date: c,
        comment: r.comment || "",
        unixPermissions: r.unixPermissions,
        dosPermissions: r.dosPermissions
      }).pipe(i);
    });
    i.entriesCount = a;
  } catch (e) {
    i.error(e);
  }
  return i;
};