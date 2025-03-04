// let
let l1; // variable declaration
console.log("l1: ", l1);    // doesn't throw an error since variable is declared with undefined value
l1 = 1; // value assignment
console.log("l1: ", l1);

//console.log("l2: ", l2);    // throws an error because variable is not declared
let l2 = 2; // declare and assign a value to a variable
console.log("l2: ", l2)

// let variable allows value reassignment
l1 = 3
console.log("l1: ", l1)

// but does not allow value redeclaration using let in the same scope
// let l1 = 6;
// console.log("l1: ", l1);    // throws an error