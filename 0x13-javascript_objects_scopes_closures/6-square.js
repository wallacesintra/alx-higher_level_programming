#!/usr/bin/node
/**
 * Square class that inherits from Rectangle
 * @class Square
 * @extends Rectangle
 * @param {int} size - size of the square
 * @return {Square} - new Square object
 * @method charPrint(c) - prints the rectangle using the character c
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
