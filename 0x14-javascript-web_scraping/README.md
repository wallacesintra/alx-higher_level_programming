# Web Scraping - JavaScript

## Manipulating JSON data

### Converting JSON to JS object

convert a JSON string into a JS object, use `JSON.parse()`

```Javascript
const jsonString = '{"name": "John", "age": 30}';
const jsObject = JSON.parse(jsonString);

console.log(jsObject.name); // Output: John
console.log(jsObject.age); // Output: 30
```

### Converting JS object to JSON

convert a JS object into a JSON string, use `JSON.stringify()`

```Javascript
const person = { name: 'John', age: 30 };
const jsonString = JSON.stringify(person);

console.log(jsonString); // Output: {"name":"John","age":30}
```

### Accessing and Modifying JSON data

```Javascript
const jsonString = '{"name": "John", "age": 30}';
const person = JSON.parse(jsonString);

console.log(person.name); // Output: John

// Modify property
person.age = 35;

// Add new property
person.city = 'New York';

// Convert back to JSON string
const updatedJsonString = JSON.stringify(person);
console.log(updatedJsonString); // Output: {"name":"John","age":35,"city":"New York"}
```

### Iterating over JSON data

```Javascript
const jsonString = '[{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]';
const persons = JSON.parse(jsonString);

persons.forEach(person => {
    console.log(`${person.name} is ${person.age} years old.`);
});
```

### Nested JSON data

JSON can contain nested objects and arrays. Access nested properties using dot notation or square brackets:

```Javascript
const jsonString = '{"name": "John", "address": {"city": "New York", "zip": 10001}}';
const person = JSON.parse(jsonString);

console.log(person.name); // Output: John
console.log(person.address.city); // Output: New York
console.log(person['address']['zip']); // Output: 10001
```

### Error handling

parsing JSON strings, handling potential error using `try...catch`

```Javascript
const invalidJsonString = '{name: "John", age: 30}';

try {
    const person = JSON.parse(invalidJsonString);
    console.log(person);
} catch (error) {
    console.error('Error parsing JSON:', error.message);
}
```

## Request and Fetch API

### using 'request' (Node.js)

#### installation

```bash
npm install request
```

#### making a GET request

```Javascript
const request = require('request')

const url = 'https://api.example.com/data'

request(url, (error, response, body) => {
    if (error) {
        console.log("Error: ", error)
    } else {
        console.log('status code: ', response.statusCode)
        console.log('body: ', body)
    }
})
```

### using 'fetch' API(web browser and node.js)

#### make a GET request

in a web browser:

```Javascript
fetch('https://api.example.com/data')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error('Fetch Error:', error));
```

in node.js(with `node-fetch`):

```Javascript
const fetch = require('node-fetch');

fetch('https://api.example.com/data')
    .then(response => {
        if (!response.ok) {
            throw new Error('HTTP status ' + response.status);
        }
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error('Fetch Error:', error));
```

#### making other types of requests(POST, PUT, DELETE)

```Javascript
fetch('https://api.example.com/data', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ key: 'value' })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Fetch Error:', error));

```

## File System(FS) module

The Node.js file system module allows you to work with the file system on your computer

use for FS:

* read files
* create files
* update files
* delete files
* rename files

### read file

use `fs.readFile()`

```Javascript
const fs = require('fs');

const filePath = 'path/to/your/file.txt';

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }
    console.log('File contents:', data);
});
```

### create file

use `fs.writeFile()`

```Javascript
const fs = require('fs');

const filePath = 'path/to/your/newfile.txt';
const dataToWrite = 'Hello, this is some data to write to the file!';

fs.writeFile(filePath, dataToWrite, 'utf8', (err) => {
    if (err) {
        console.error('Error writing to file:', err);
        return;
    }
    console.log('File created and data written successfully!');
});

```

### update files

use `fs.writeFile()` or `fs.appendFile()`

appending data:

```Javascript
const fs = require('fs');

const filePath = 'path/to/your/file.txt';
const newData = '\nThis is new data to append.';

fs.appendFile(filePath, newData, 'utf8', (err) => {
    if (err) {
        console.error('Error appending to file:', err);
        return;
    }
    console.log('Data appended to file successfully!');
});
```

overwriting data:

```Javascript
const fs = require('fs');

const filePath = 'path/to/your/file.txt';
const newData = 'This is updated content.';

fs.writeFile(filePath, newData, 'utf8', (err) => {
    if (err) {
        console.error('Error updating file:', err);
        return;
    }
    console.log('File updated successfully!');
});
```

### delete file

use `fs.unlink()`

```Javascript
const fs = require('fs');

const filePath = 'path/to/your/file.txt';

fs.unlink(filePath, (err) => {
    if (err) {
        console.error('Error deleting file:', err);
        return;
    }
    console.log('File deleted successfully!');
});
```

### renaming files

use `fs.rename()`

```Javascript
const fs = require('fs');

const oldFilePath = 'path/to/your/oldfile.txt';
const newFilePath = 'path/to/your/newfile.txt';

fs.rename(oldFilePath, newFilePath, (err) => {
    if (err) {
        console.error('Error renaming file:', err);
        return;
    }
    console.log('File renamed successfully!');
});
```
