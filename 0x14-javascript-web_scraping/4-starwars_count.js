#!/usr/bin/node

/**
 * script prints the number of movies where the character “Wedge Antilles” is present
 */

const req = require('request');
const url = process.argv[2];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let i = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          i++;
        }
      }
    }
    console.log(i);
  }
});
