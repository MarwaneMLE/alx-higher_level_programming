#!/usr/bin/node
// script that concats 2 files.

const file = require('fs');
const fileA = file.readFileSync(process.argv[2], 'utf8');
const fileB = file.readFileSync(process.argv[3], 'utf8');
file.writeFileSync(process.argv[4], fileA + fileB);
