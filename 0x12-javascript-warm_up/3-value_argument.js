#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
  console.log('No argument');
}

for (const i of args) {
  if (i === args[0] || i === args[1]) {
    continue;
  }
  console.log(i);
}
