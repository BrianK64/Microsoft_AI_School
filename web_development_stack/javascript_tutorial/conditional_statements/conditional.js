// making decisions based on temperature
let temperature = 20;

let decision;
if (temperature == 30)
{
    decision = "home";
}

else if (temperature >= 20)
{
    decision = "the park";
}

else if (temperature >= 10)
{
    decision = "the cafe";
}

else if (temperature < 10)
{
    decision = "the movie theatre";
}

console.log(`Since it is ${temperature} degrees outside, I will be at ${decision} today.`)


// score
let score = 40;
let result = score >= 60 ? "pass" : "fail";
console.log(result);