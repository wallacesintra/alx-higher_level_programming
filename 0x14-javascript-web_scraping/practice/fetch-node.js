const fetch = require('node-fetch');

fetch('https://jsonplaceholder.typicode.com/posts/3')
  .then(res => {
    if (!res.ok) {
      throw new Error(res.status);
    }
    return res.json();
  })
  .then(data => console.log(data))
  .catch(error => console.log('fetch error', error));
