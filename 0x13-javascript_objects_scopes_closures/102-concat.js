#!/usr/bin/node
/**
 * concatenate 2 files.
 * @param {String} file1 - The first file to be concatenated.
 * @param {String} file2 - The second file to be concatenated.
 * @param {String} file3 - The file to be written.
*/
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];

const data1 = fs.readFileSync(file1, 'utf8');
const data2 = fs.readFileSync(file2, 'utf8');
fs.writeFileSync(file3, data1 + data2);
