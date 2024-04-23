#!/usr/bin/node

/**
 * script that prints all characters of a Star Wars movie
 * Display one character name by line in the same order of the list “characters”
 * in the /films/ response
 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getCharacters (character) {
  return new Promise((resolve, reject) => {
    request(character, (err, _res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

request(url, async (err, _res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      console.log(await getCharacters(characters[i]));
    }
  }
});
