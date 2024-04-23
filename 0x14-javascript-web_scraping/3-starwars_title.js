#!/usr/bin/node

/**
 * fetch the title of a Star Wars movie where the episode number matches a given integer
 */

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
