#!/usr/bin/node

/**
 * prints all characters of a Star Wars movie
*/

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      req(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
