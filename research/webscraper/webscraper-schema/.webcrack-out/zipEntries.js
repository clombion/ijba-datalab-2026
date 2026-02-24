var n = require("./reader/readerFor");
var o = require("./utils");
var i = require("./signature");
var a = require("./zipEntry");
var s = require("./support");
function l(e) {
  this.files = [];
  this.loadOptions = e;
}
l.prototype = {
  checkSignature: function (e) {
    if (!this.reader.readAndCheckSignature(e)) {
      this.reader.index -= 4;
      var t = this.reader.readString(4);
      throw new Error("Corrupted zip or bug: unexpected signature (" + o.pretty(t) + ", expected " + o.pretty(e) + ")");
    }
  },
  isSignature: function (e, t) {
    var r = this.reader.index;
    this.reader.setIndex(e);
    var n = this.reader.readString(4) === t;
    this.reader.setIndex(r);
    return n;
  },
  readBlockEndOfCentral: function () {
    this.diskNumber = this.reader.readInt(2);
    this.diskWithCentralDirStart = this.reader.readInt(2);
    this.centralDirRecordsOnThisDisk = this.reader.readInt(2);
    this.centralDirRecords = this.reader.readInt(2);
    this.centralDirSize = this.reader.readInt(4);
    this.centralDirOffset = this.reader.readInt(4);
    this.zipCommentLength = this.reader.readInt(2);
    var e = this.reader.readData(this.zipCommentLength);
    var t = s.uint8array ? "uint8array" : "array";
    var r = o.transformTo(t, e);
    this.zipComment = this.loadOptions.decodeFileName(r);
  },
  readBlockZip64EndOfCentral: function () {
    this.zip64EndOfCentralSize = this.reader.readInt(8);
    this.reader.skip(4);
    this.diskNumber = this.reader.readInt(4);
    this.diskWithCentralDirStart = this.reader.readInt(4);
    this.centralDirRecordsOnThisDisk = this.reader.readInt(8);
    this.centralDirRecords = this.reader.readInt(8);
    this.centralDirSize = this.reader.readInt(8);
    this.centralDirOffset = this.reader.readInt(8);
    this.zip64ExtensibleData = {};
    var e;
    var t;
    var r;
    for (var n = this.zip64EndOfCentralSize - 44; n > 0;) {
      e = this.reader.readInt(2);
      t = this.reader.readInt(4);
      r = this.reader.readData(t);
      this.zip64ExtensibleData[e] = {
        id: e,
        length: t,
        value: r
      };
    }
  },
  readBlockZip64EndOfCentralLocator: function () {
    this.diskWithZip64CentralDirStart = this.reader.readInt(4);
    this.relativeOffsetEndOfZip64CentralDir = this.reader.readInt(8);
    this.disksCount = this.reader.readInt(4);
    if (this.disksCount > 1) {
      throw new Error("Multi-volumes zip are not supported");
    }
  },
  readLocalFiles: function () {
    var e;
    var t;
    for (e = 0; e < this.files.length; e++) {
      t = this.files[e];
      this.reader.setIndex(t.localHeaderOffset);
      this.checkSignature(i.LOCAL_FILE_HEADER);
      t.readLocalPart(this.reader);
      t.handleUTF8();
      t.processAttributes();
    }
  },
  readCentralDir: function () {
    var e;
    for (this.reader.setIndex(this.centralDirOffset); this.reader.readAndCheckSignature(i.CENTRAL_FILE_HEADER);) {
      (e = new a({
        zip64: this.zip64
      }, this.loadOptions)).readCentralPart(this.reader);
      this.files.push(e);
    }
    if (this.centralDirRecords !== this.files.length && this.centralDirRecords !== 0 && this.files.length === 0) {
      throw new Error("Corrupted zip or bug: expected " + this.centralDirRecords + " records in central dir, got " + this.files.length);
    }
  },
  readEndOfCentral: function () {
    var e = this.reader.lastIndexOfSignature(i.CENTRAL_DIRECTORY_END);
    if (e < 0) {
      throw this.isSignature(0, i.LOCAL_FILE_HEADER) ? new Error("Corrupted zip: can't find end of central directory") : new Error("Can't find end of central directory : is this a zip file ? If it is, see https://stuk.github.io/jszip/documentation/howto/read_zip.html");
    }
    this.reader.setIndex(e);
    var t = e;
    this.checkSignature(i.CENTRAL_DIRECTORY_END);
    this.readBlockEndOfCentral();
    if (this.diskNumber === o.MAX_VALUE_16BITS || this.diskWithCentralDirStart === o.MAX_VALUE_16BITS || this.centralDirRecordsOnThisDisk === o.MAX_VALUE_16BITS || this.centralDirRecords === o.MAX_VALUE_16BITS || this.centralDirSize === o.MAX_VALUE_32BITS || this.centralDirOffset === o.MAX_VALUE_32BITS) {
      this.zip64 = true;
      if ((e = this.reader.lastIndexOfSignature(i.ZIP64_CENTRAL_DIRECTORY_LOCATOR)) < 0) {
        throw new Error("Corrupted zip: can't find the ZIP64 end of central directory locator");
      }
      this.reader.setIndex(e);
      this.checkSignature(i.ZIP64_CENTRAL_DIRECTORY_LOCATOR);
      this.readBlockZip64EndOfCentralLocator();
      if (!this.isSignature(this.relativeOffsetEndOfZip64CentralDir, i.ZIP64_CENTRAL_DIRECTORY_END) && (this.relativeOffsetEndOfZip64CentralDir = this.reader.lastIndexOfSignature(i.ZIP64_CENTRAL_DIRECTORY_END), this.relativeOffsetEndOfZip64CentralDir < 0)) {
        throw new Error("Corrupted zip: can't find the ZIP64 end of central directory");
      }
      this.reader.setIndex(this.relativeOffsetEndOfZip64CentralDir);
      this.checkSignature(i.ZIP64_CENTRAL_DIRECTORY_END);
      this.readBlockZip64EndOfCentral();
    }
    var r = this.centralDirOffset + this.centralDirSize;
    if (this.zip64) {
      r += 20;
      r += 12 + this.zip64EndOfCentralSize;
    }
    var n = t - r;
    if (n > 0) {
      if (!this.isSignature(t, i.CENTRAL_FILE_HEADER)) {
        this.reader.zero = n;
      }
    } else if (n < 0) {
      throw new Error("Corrupted zip: missing " + Math.abs(n) + " bytes.");
    }
  },
  prepareReader: function (e) {
    this.reader = n(e);
  },
  load: function (e) {
    this.prepareReader(e);
    this.readEndOfCentral();
    this.readCentralDir();
    this.readLocalFiles();
  }
};
module.exports = l;