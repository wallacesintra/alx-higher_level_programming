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
