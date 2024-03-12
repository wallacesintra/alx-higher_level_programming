#!/usr/bin/node
/**
 * @function nbOccurences - returns the number of occurrences in a list
 * @param {list} list - list of elements
 * @param {element} searchElement - element to search for
 * @return {int} - number of occurrences
*/

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
