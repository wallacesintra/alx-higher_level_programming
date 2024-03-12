#!/usr/bin/node
/**
 * class Rectangle that defines a rectangle
 * If w or h is equal to 0 or not a positive integer, create an empty object
*/

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
