# JavaScript

## **Create variables and constants**

**with 'var'**:
have function scope or global scope depending on where they are declared.

```javascript
var myVariable = "Hello";
myVariable = "World";
```

**with let**: (block-scoped)
they are only accessible within the block they are defined in(e.g within a loop or if statement)

```javascript
let myVariable = 'Hello'; // Declares a variable named myVariable
myVariable = 'World'; // Reassigns the value of myVariable
```

**constants with const**: constants can't be assigned once they're initialized. they must be assigned a value when declared.

```javascript
// Variable example
let age = 30;
console.log(age); // Output: 30

// Constant example
const PI = 3.14;
console.log(PI); // Output: 3.14

// Attempting to reassign a constant will result in an error
// PI = 3.14159; // This will throw an error
```

## Data types

### **Primitive data type**

* number - rep numeric values.
* string - rep textual data
* Boolean - rep true or false values
* Undefined - rep a variable that has been declared but not assigned a value.
* Null - rep an intentional absence of any object value.
* Symbol - rep unique identifiers, introduced in ECMAScript(ES6)

### **Non-primitive data types**

* Object: rep a collection of key-value pairs(properties and methods)
* Array: rep a list-like collection of elements
* Function: rep a reusable block of code.
* Date: rep specific moment in time.
* RegExp: rep regular expressions for pattern matching.
* map, set, weakMap, weakSet: more specialized way to store data. introduced in ES6.

## **if**

allow you to conditionally execute blocks of code based on certain conditions.

```javascript
let x = 10;

if (x > 5) {
    console.log("x is greater than 5");
}
```

```javascript
let x = 10;

if (x > 5) {
    console.log("x is greater than 5");
} else {
    console.log("x is not greater than 5");
}
```

```javascript
let x = 10;

if (x > 10) {
    console.log("x is greater than 10");
} else if (x < 10) {
    console.log("x is less than 10");
} else {
    console.log("x is equal to 10");
}
```

```javascript
let x = 10;
let y = 5;

if (x > 5) {
    if (y > 2) {
        console.log("x is greater than 5 and y is greater than 2");
    }
}
```

## **while**

### while loop

executes a block of code as long as a specified condition is true:

```javascript
let count = 0;

while (count < 5) {
    console.log(count);
    count++;
}
```

### do...while

the condition is checked after executing the block of code, meaning the block is always executed at least once.

```javascript
let count = 0;

do {
    console.log(count);
    count++;
} while (count < 5);
```

## **for**

The for loop repeats a block of code a specified number of times.

```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

## **break**

The break statement is used to exit the loop prematurely, regardless of whether the loop condition evaluates to true or false.

```javascript
for (let i = 0; i < 10; i++) {
    console.log(i);
    if (i === 5) {
        break; // Exit the loop when i is 5
    }
}
```

This loop will print numbers from 0 to 5, and then exit the loop when i becomes 5.

## **continue**

The continue statement is used to skip the current iteration of the loop and proceed to the next iteration.

```javascript
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        continue; // Skip iteration when i is 5
    }
    console.log(i);
}
```

This loop will print numbers from 0 to 9, skipping the iteration where i is 5.

## **functions**

function is a block of reusable code that performs a specific task.

### defining a function

function using the function keyword followed by the function name, a list of parameters (if any), and the code block to be executed when the function is called.

```javascript
function greet(name) {
    console.log("Hello, " + name + "!");
}
```

### calling a function

To execute a function, you simply write its name followed by parentheses () and provide any required arguments inside the parentheses.

```javascript
greet("Alice"); // Output: Hello, Alice!
```

### return statement

Functions can also return values using the return statement. The returned value can then be used elsewhere in your code.

```javascript
function add(a, b) {
    return a + b;
}

let result = add(3, 5);
console.log(result); // Output: 8
```

### function expression

can also define functions using function expressions, which are assigned to variables.

```javascript
const multiply = function(a, b) {
    return a * b;
};

console.log(multiply(4, 6)); // Output: 24
```

### Arrow functions(ES6+)

```javascript
const divide = (a, b) => a / b;

console.log(divide(10, 2)); // Output: 5
```

if a function does not use any return statement, it implicitly returns undefined. This means that when the function is called and executed, if no return statement is encountered, the function will automatically return undefined.

## **manipulating dictionary**

dictionaries are typically represented using objects. Objects in JavaScript are collections of key-value pairs, where each key is unique.

### Accessing values

access the value associated with a specific key using either dot notation or square bracket notation.

```javascript
let person = {
    name: "John",
    age: 30,
    city: "New York"
};

console.log(person.name); // Output: John
console.log(person['age']); // Output: 30
```

### Adding or Modifying key-value pairs

can add new key-value pairs to an object or modify existing ones by assigning a value to a new or existing key.

```javascript
let person = {
    name: "John",
    age: 30,
    city: "New York"
};

person.age = 35; // Modifying existing value
person.job = "Engineer"; // Adding new key-value pair

console.log(person); // Output: { name: 'John', age: 35, city: 'New York', job: 'Engineer' }
```

### deleting key-value pairs

can delete a key-value pair from an object using the delete keyword.

```javascript
let person = {
    name: "John",
    age: 30,
    city: "New York"
};

delete person.city;

console.log(person); // Output: { name: 'John', age: 30 }
```

### iterating over key-value pairs

can iterate over the keys of an object using a for...in loop.

```javascript
let person = {
    name: "John",
    age: 30,
    city: "New York"
};

for (let key in person) {
    console.log(key + ": " + person[key]);
}
```

## **Import a file**

importing files depends on the environment in which you're working.

### Node.js

can use the require() function to import files.

```javascript
// myModule.js
function myFunction() {
    console.log("Hello from myModule.js");
}

module.exports = myFunction;
```

can import this module into another file like this:

```javascript
// main.js
const myFunction = require('./myModule.js');

myFunction(); // Output: Hello from myModule.js
```

### browser(frontend)

Can use `<script> </script>` tags to include JavaScript files in your HTML.

```javascript
// script.js
function greet() {
    console.log("Hello, world!");
}
```

```htm
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Import Example</title>
    <script src="script.js"></script>
</head>
<body>
    <script>
        greet(); // Output: Hello, world!
    </script>
</body>
</html>
```

### in ES6 and later

there's support for module syntax (import and export) in both Node.js and the browser, but it requires using tools like Webpack or Babel to transpile and bundle your code for browser compatibility.

```javascript
// myModule.js
export function myFunction() {
    console.log("Hello from myModule.js");
}
```

```javascript
// main.js
import { myFunction } from './myModule.js';

myFunction(); // Output: Hello from myModule.js
```

to use ES6 module syntax in Node.js, you need to use the .mjs file extension for your modules or explicitly specify "type": "module" in your package.json file.
