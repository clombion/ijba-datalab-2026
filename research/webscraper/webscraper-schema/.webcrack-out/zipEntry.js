var n = require("./reader/readerFor");
var o = require("./utils");
var i = require("./compressedObject");
var a = require("./crc32");
var s = require("./utf8");
var l = require("./compressions");
var c = require("./support");
function u(e, t) {
  this.options = e;
  this.loadOptions = t;
}
u.prototype = {
  isEncrypted: function () {
    return !(~this.bitFlag & 1);
  },
  useUTF8: function () {
    return !(~this.bitFlag & 2048);
  },
  readLocalPart: function (e) {
    var t;
    var r;
    e.skip(22);
    this.fileNameLength = e.readInt(2);
    r = e.readInt(2);
    this.fileName = e.readData(this.fileNameLength);
    e.skip(r);
    if (this.compressedSize === -1 || this.uncompressedSize === -1) {
      throw new Error("Bug or corrupted zip : didn't get enough information from the central directory (compressedSize === -1 || uncompressedSize === -1)");
    }
    if ((t = function (e) {
      for (var t in l) {
        if (Object.prototype.hasOwnProperty.call(l, t) && l[t].magic === e) {
          return l[t];
        }
      }
      return null;
    }(this.compressionMethod)) === null) {
      throw new Error("Corrupted zip : compression " + o.pretty(this.compressionMethod) + " unknown (inner file : " + o.transformTo("string", this.fileName) + ")");
    }
    this.decompressed = new i(this.compressedSize, this.uncompressedSize, this.crc32, t, e.readData(this.compressedSize));
  },
  readCentralPart: function (e) {
    this.versionMadeBy = e.readInt(2);
    e.skip(2);
    this.bitFlag = e.readInt(2);
    this.compressionMethod = e.readString(2);
    this.date = e.readDate();
    this.crc32 = e.readInt(4);
    this.compressedSize = e.readInt(4);
    this.uncompressedSize = e.readInt(4);
    var t = e.readInt(2);
    this.extraFieldsLength = e.readInt(2);
    this.fileCommentLength = e.readInt(2);
    this.diskNumberStart = e.readInt(2);
    this.internalFileAttributes = e.readInt(2);
    this.externalFileAttributes = e.readInt(4);
    this.localHeaderOffset = e.readInt(4);
    if (this.isEncrypted()) {
      throw new Error("Encrypted zip are not supported");
    }
    e.skip(t);
    this.readExtraFields(e);
    this.parseZIP64ExtraField(e);
    this.fileComment = e.readData(this.fileCommentLength);
  },
  processAttributes: function () {
    this.unixPermissions = null;
    this.dosPermissions = null;
    var e = this.versionMadeBy >> 8;
    this.dir = !!(this.externalFileAttributes & 16);
    if (e == 0) {
      this.dosPermissions = this.externalFileAttributes & 63;
    }
    if (e == 3) {
      this.unixPermissions = this.externalFileAttributes >> 16 & 65535;
    }
    if (!this.dir && this.fileNameStr.slice(-1) === "/") {
      this.dir = true;
    }
  },
  parseZIP64ExtraField: function () {
    if (this.extraFields[1]) {
      var e = n(this.extraFields[1].value);
      if (this.uncompressedSize === o.MAX_VALUE_32BITS) {
        this.uncompressedSize = e.readInt(8);
      }
      if (this.compressedSize === o.MAX_VALUE_32BITS) {
        this.compressedSize = e.readInt(8);
      }
      if (this.localHeaderOffset === o.MAX_VALUE_32BITS) {
        this.localHeaderOffset = e.readInt(8);
      }
      if (this.diskNumberStart === o.MAX_VALUE_32BITS) {
        this.diskNumberStart = e.readInt(4);
      }
    }
  },
  readExtraFields: function (e) {
    var t;
    var r;
    var n;
    var o = e.index + this.extraFieldsLength;
    for (this.extraFields ||= {}; e.index + 4 < o;) {
      t = e.readInt(2);
      r = e.readInt(2);
      n = e.readData(r);
      this.extraFields[t] = {
        id: t,
        length: r,
        value: n
      };
    }
    e.setIndex(o);
  },
  handleUTF8: function () {
    var e = c.uint8array ? "uint8array" : "array";
    if (this.useUTF8()) {
      this.fileNameStr = s.utf8decode(this.fileName);
      this.fileCommentStr = s.utf8decode(this.fileComment);
    } else {
      var t = this.findExtraFieldUnicodePath();
      if (t !== null) {
        this.fileNameStr = t;
      } else {
        var r = o.transformTo(e, this.fileName);
        this.fileNameStr = this.loadOptions.decodeFileName(r);
      }
      var n = this.findExtraFieldUnicodeComment();
      if (n !== null) {
        this.fileCommentStr = n;
      } else {
        var i = o.transformTo(e, this.fileComment);
        this.fileCommentStr = this.loadOptions.decodeFileName(i);
      }
    }
  },
  findExtraFieldUnicodePath: function () {
    var e = this.extraFields[28789];
    if (e) {
      var t = n(e.value);
      if (t.readInt(1) !== 1 || a(this.fileName) !== t.readInt(4)) {
        return null;
      } else {
        return s.utf8decode(t.readData(e.length - 5));
      }
    }
    return null;
  },
  findExtraFieldUnicodeComment: function () {
    var e = this.extraFields[25461];
    if (e) {
      var t = n(e.value);
      if (t.readInt(1) !== 1 || a(this.fileComment) !== t.readInt(4)) {
        return null;
      } else {
        return s.utf8decode(t.readData(e.length - 5));
      }
    }
    return null;
  }
};
module.exports = u;