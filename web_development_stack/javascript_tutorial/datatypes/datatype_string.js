console.log(typeof "hello");

let name = "John Doe"
let carName = "BMW i8"
let sentence = "His name is 'John Doe' and he drives 'BMW i8'"

console.log(sentence)

// multiline string using backticks(`)
console.log("##### multiline #####")
let s1 = `Hello
World!`;
console.log(s1);

// Template Strings
console.log("##### Template Strings #####")
console.log(`His name is ${name} and he drives ${carName}`);    // variable substitutions

// String methods
console.log("##### length and indexing #####")
const message = "Hello, World!";
console.log(message.length);
console.log(message[0]);
console.log(message[100]);  // undefined (out of range)

console.log("##### indexOf() #####")
console.log(message.indexOf("W"));
console.log(message.indexOf("a"));  // not included character

console.log("##### includes() #####")
console.log(message.includes("Hello"));

// slicing
console.log("##### substring() #####")
console.log(message.substring(0, 5));
console.log(message.substring(7));

// upper case lower case
console.log("##### toUpperCase() & toLowerCase() #####")

console.log(message.toUpperCase());
console.log(message.toLowerCase());

// replacing
console.log("##### replace() #####")

console.log(message.replace("World!", "JavaScript!"));

// split
console.log("##### split() #####")

console.log(message.split(","));

// start & end
console.log("##### startsWith() & endsWith() #####")

console.log(message.startsWith("He"));
console.log(message.endsWith("?"));

// trimming
console.log("##### trim() #####")
const message2 = "          hello world          "
console.log(message2.trim());

// repeat()
console.log("##### repeat() #####")
const message3 = "ha";
console.log(message3.repeat(3));