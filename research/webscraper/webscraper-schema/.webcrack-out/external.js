var n = null;
n = typeof Promise != "undefined" ? Promise : require("lie");
module.exports = {
  Promise: n
};