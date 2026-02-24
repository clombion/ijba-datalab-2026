var n = require("./utils");
var o = require("./external");
var i = require("./utf8");
var a = require("./zipEntries");
var s = require("./stream/Crc32Probe");
var l = require("./nodejsUtils");
function c(e) {
  return new o.Promise(function (t, r) {
    var n = e.decompressed.getContentWorker().pipe(new s());
    n.on("error", function (e) {
      r(e);
    }).on("end", function () {
      if (n.streamInfo.crc32 !== e.decompressed.crc32) {
        r(new Error("Corrupted zip : CRC32 mismatch"));
      } else {
        t();
      }
    }).resume();
  });
}
module.exports = function (e, t) {
  var r = this;
  t = n.extend(t || {}, {
    base64: false,
    checkCRC32: false,
    optimizedBinaryString: false,
    createFolders: false,
    decodeFileName: i.utf8decode
  });
  if (l.isNode && l.isStream(e)) {
    return o.Promise.reject(new Error("JSZip can't accept a stream when loading a zip file."));
  } else {
    return n.prepareContent("the loaded zip file", e, true, t.optimizedBinaryString, t.base64).then(function (e) {
      var r = new a(t);
      r.load(e);
      return r;
    }).then(function (e) {
      var r = [o.Promise.resolve(e)];
      var n = e.files;
      if (t.checkCRC32) {
        for (var i = 0; i < n.length; i++) {
          r.push(c(n[i]));
        }
      }
      return o.Promise.all(r);
    }).then(function (e) {
      var o = e.shift();
      for (var i = o.files, a = 0; a < i.length; a++) {
        var s = i[a];
        var l = s.fileNameStr;
        var c = n.resolve(s.fileNameStr);
        r.file(c, s.decompressed, {
          binary: true,
          optimizedBinaryString: true,
          date: s.date,
          dir: s.dir,
          comment: s.fileCommentStr.length ? s.fileCommentStr : null,
          unixPermissions: s.unixPermissions,
          dosPermissions: s.dosPermissions,
          createFolders: t.createFolders
        });
        if (!s.dir) {
          r.file(c).unsafeOriginalName = l;
        }
      }
      if (o.zipComment.length) {
        r.comment = o.zipComment;
      }
      return r;
    });
  }
};