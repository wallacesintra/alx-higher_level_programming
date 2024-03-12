#!/usr/bin/node
/**
 * Square class that inherits from Rectangle
 * @class Square
 * @extends Rectangle
 * @param {int} size - size of the square
 * @return {Square} - new Square object
 * @method charPrint(c) - prints the rectangle using the character c
*/

const sq = require('./5-square');

class Square extends sq {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
