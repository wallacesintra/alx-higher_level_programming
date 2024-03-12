#!/usr/bin/node
/**
 * Imports an array and computes a new array.
 * @param {Array} list - The array to be computed.
 * @param {Function} map - The function to be applied to the array.
 * @return {Array} - The new array.
*/
const list = require('./100-data').list;
const newList = list.map(function (num, index) {
  return num * index;
});

console.log(list);
console.log(newList);
