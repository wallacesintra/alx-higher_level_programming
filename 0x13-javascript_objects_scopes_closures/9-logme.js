#!/usr/bin/node
/**
 * @function logMe - logs the number of times it has been called
 * @param {any} item - item to log
*/
exports.logMe = function (item) {
  if (this.count === undefined) {
    this.count = 0;
  }
  console.log(`${this.count}: ${item}`);
  this.count++;
};
