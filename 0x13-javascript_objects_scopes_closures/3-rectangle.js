#!/usr/bin/node
/**
 * class Rectangle that defines a rectangle
 * If w or h is equal to 0 or not a positive integer, create an empty object
*/

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let x;
    let str = '';
    for (i = 0; i < this.height; i++) {
      for (x = 0; x < this.width; x++) {
        str += 'X';
      }
      console.log(str);
      str = '';
    }
  }
}

module.exports = Rectangle;
