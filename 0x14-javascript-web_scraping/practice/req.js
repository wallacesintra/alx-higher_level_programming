#!/usr/bin/node

const req = require('request');

const url = "https://jsonplaceholder.typicode.com/posts/1"

req(url, (error, response, body) => {
    if (error){
        console.log(error);
    } else {
        console.log('code:', response.statusCode);
        console.log(body);
    }
})
