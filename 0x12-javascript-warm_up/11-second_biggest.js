#!/usr/bin/node
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  const array = args.slice(2);
  array.sort(function (a, b) { return b - a; });
  console.log(array[1]);
}
