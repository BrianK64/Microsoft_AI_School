// get weekday based on weekday as a number between 0 and 6.
let week = 0;
let day;

switch (week)
{
    case 0:
        day = "Sunday";
        break;
    case 1:
        day = "Monday";
        break;
    case 2:
        day = "Tuesday";
        break;
    case 3:
        day = "Wednesday";
        break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
        break;
    case 6:
        day = "Saturday";
}

console.log(day)


// the number of days on different months
let year = 2024;
let month = 2;
let days, cond1, cond2, cond3;

switch (month)
{
    case 1:
        days = 31;
        break;
    case 2:
        cond1 = year % 4 === 0;
        cond2 = year % 100 === 0;
        cond3 = year % 400 == 0;
        days = ((cond1 && !cond2) || cond3) ? 29 : 28;
        break;
    case 3:
        days = 31;
        break;
    case 4:
        days = 30;
        break;
    case 5:
        days = 31;
        break;
    case 6:
        days = 30;
        break;
    case 7:
        days = 31;
        break;
    case 8:
        days = 31;
        break;
    case 9:
        days = 30;
        break;
    case 10:
        days = 31;
        break;
    case 11:
        days = 30;
        break;
    case 12:
        days = 31;
        break;
    default:
        days = "Invalid Month"
}

console.log(`
year : ${year}
month : ${month}
days : ${days}`)