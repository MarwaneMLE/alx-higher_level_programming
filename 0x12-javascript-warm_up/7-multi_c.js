#!/usr/bin/node
// prints x times “C is fun”

const prog_lang = "C is fun";

if (isNaN(process.argv[2])) {
	console.log("Missing number of occurrences");
}
else {
	for (let i = 0; i < parseInt(process.argv[2]); i++) {
		console.log(prog_lang);
	}
}
