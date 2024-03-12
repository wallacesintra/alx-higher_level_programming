# **Objects**

## **creating a object**

### Using Object Literal Notation

define the object properties and methods within curly braces {}.

```javascript
// Creating an object using object literal notation
const person = {
  firstName: "John",
  lastName: "Doe",
  age: 30,
  greet: function() {
    console.log("Hello, my name is " + this.firstName + " " + this.lastName);
  }
};

// Accessing object properties
console.log(person.firstName); // Output: John

// Accessing object method
person.greet(); // Output: Hello, my name is John Doe
```

### Using Constructor Functions

can define a constructor function and then create new instances of the object using the new keyword.

```javascript
// Constructor function for creating Person objects
function Person(firstName, lastName, age) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.age = age;

  // Method definition inside constructor function
  this.greet = function() {
    console.log("Hello, my name is " + this.firstName + " " + this.lastName);
  };
}

// Creating a new instance of the Person object
const person1 = new Person("John", "Doe", 30);

// Accessing object properties
console.log(person1.firstName); // Output: John

// Accessing object method
person1.greet(); // Output: Hello, my name is John Doe
```

### Using ES6 Classes

ES6 introduced the class syntax which makes object-oriented programming more familiar to developers coming from other languages.

```javascript
// ES6 Class for creating Person objects
class Person {
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }

  // Method definition inside class
  greet() {
    console.log("Hello, my name is " + this.firstName + " " + this.lastName);
  }
}

// Creating a new instance of the Person object
const person2 = new Person("Jane", "Smith", 25);

// Accessing object properties
console.log(person2.firstName); // Output: Jane

// Accessing object method
person2.greet(); // Output: Hello, my name is Jane Smith
```

## **this**

the this keyword refers to the current context within which code is executed.

### Inside a Method of an Object

When this is used inside a method of an object (such as a function defined as a property of an object), this refers to the object that the method is called on.

```javascript
const person = {
  firstName: "John",
  lastName: "Doe",
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};

console.log(person.fullName()); // Output: John Doe
```

### Inside a Constructor Function

When this is used inside a constructor function, it refers to the specific instance of the object that is being created with the new keyword.

```javascript
function Person(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.fullName = function() {
    return this.firstName + " " + this.lastName;
  };
}

const john = new Person("John", "Doe");
console.log(john.fullName()); // Output: John Doe
```

### Global Context

In the global context (outside of any function or object), this refers to the global object. In a web browser, the global object is window.

```javascript
console.log(this === window); // Output: true
```

### Inside Arrow Functions

Arrow functions do not have their own this binding. Instead, they inherit the this value from the surrounding lexical context.

```javascript
const obj = {
  foo: function() {
    console.log(this === obj); // Output: true
    const arrowFunc = () => {
      console.log(this === obj); // Output: true
    };
    arrowFunc();
  }
};

obj.foo();
```

## **Closure**

A closure is a fundamental concept in JavaScript that allows functions to retain access to variables from their containing (enclosing) lexical scope, even after the parent function has finished executing. In simpler terms, a closure gives you access to an outer function's scope from an inner function.

breakdown of what closures are and how they work:

### Lexical Scope

JavaScript has lexical scoping, which means that the scope of a variable is determined by its location within the code. When you define a function inside another function, the inner function has access to the variables declared in the outer (enclosing) function's scope.

### Function Definition vs. Function Invocation

When a function is defined inside another function, it forms a closure. This means that the inner function retains access to the variables and parameters of the outer function, even after the outer function has finished executing.

### Access to Outer Variables

Closures have access to variables in three scopes:

* Variables declared in their own scope
* Variables declared in the parent function's scope
* Variables declared in the global scope

### Use Cases

* Private Variables: Closures are commonly used to create private variables and functions in JavaScript. By defining variables within a closure, they are inaccessible from outside the closure, providing data encapsulation and information hiding.
* Callbacks: Closures are frequently used with callback functions to maintain access to variables in the parent scope when the callback is invoked asynchronously.
* Iterators and Generators: Closures can be used to create iterators and generators, enabling the creation of functions that maintain their own state.

```javascript
function outerFunction() {
  let outerVariable = "I'm in the outer function";

  function innerFunction() {
    console.log(outerVariable); // Accessing outerVariable from the outer function's scope
  }

  // Returning innerFunction, which forms a closure over outerVariable
  return innerFunction;
}

const closureExample = outerFunction();
closureExample(); // Output: I'm in the outer function
```

In this example, innerFunction forms a closure over the outerVariable declared in outerFunction, allowing innerFunction to access outerVariable even after outerFunction has finished executing.
