console.log("########## Counting Backwards ##########")
for (let i = 5; i >= 1; i--)
{
    console.log(i)
}

console.log("########## Series Summation ##########")
let start = 1;
let end = 100;
let sum = 0;
for (let i = start; i <= end; i ++)
{
    sum += i
}
console.log(`The summation of the series from 1 to 100 is ${sum}`)