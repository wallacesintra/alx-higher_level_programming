#!/usr/bin/node

/**
 * script that gets the contents of a webpage and stores it in a file.
 */

const fs = require('fs');
const req = require('request');

const url = process.argv[2];
const file = process.argv[3];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
