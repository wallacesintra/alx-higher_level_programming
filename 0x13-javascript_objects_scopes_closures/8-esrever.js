#!/usr/bin/node
/**
 * @function esrever - returns the reversed version of a list
 * @param {list} list - list of elements
 * @return {list} - reversed list
*/

exports.esrever = function (list) {
  const reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
