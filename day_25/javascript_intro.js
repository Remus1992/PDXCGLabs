"use strict";
console.log("javascript_intro.js is running");
// // Data Types
//
// // int and float
// 1
// 2.3
//
// // strings
// "string"
// 'string'
//
// // won't work in python
// // string = "I'm a string"
// // print(string + 1)
//
// // will work in Javascript
// var string = 'I am a string!';
// console.log(string + ' ' +  1);
//
// //booleans
// true
// false
//
// null

// //JavaScript Objects (Notation) or JSON
// // dictionaries are like Python dictionaries but only use single quotes
// var value = 'lalala';
// var obj {key:'value'};
// console.log(obj);

// // arrays
// var arr = ['string', 1, 3, 12.2];
// console.log(arr);

// // variables
// var name = 'Remington';
// var fruitPrice = {'apple':2.99};
// var FEET_PER_MILE = 5280; // global constant due to all caps
// const INCHES_PER_FOOT = 12;

// var fruitPrices = {
//   apple: 0.99,
//   pear: 1.50,
//   kiwi: 2.50
// };
// console.log(fruitPrices['apple']);
// console.log(fruitPrices.apple]);

// var store = {
//   aisle1: {
//       apple: 0.99,
//       pear: 1.50,
//       kiwi: 2.50
//   },
//   aisle2: {
//     crackers: 1.99,
//     cookies: 5.99,
//     'ice cream': 0.99
//   }
// };
// console.log(store.aisle1.pear);
// console.log(store['aisle1']['pear']);

// //reassignment
// store.aisle1.apple = 1.99;
// console.log(store.aisle1.apple);
//
// var fruit = ['apple', 'banana', 'grape'];
// console.log(fruit[1]);
// fruit[1] = 'BANANA';
// console.log(fruit[1]);

// console.log(1 + 2);
// console.log(10 % 3);
// console.log('Hi, ' + 'Remington');
// var x = 99;
// console.log(x + 1);
// console.log(x += 1);
// console.log(x ++);
// x --;
// console.log(x --);

// // booleans
// console.log(1==1);
// console.log('1'=='1');
// console.log('1'==1); // this will come out as true also so use three equal signs instead
// console.log('1'===1);
// console.log('1'!==1);

// // and operator
// console.log('1'==='1' && 1 === 1);

// // or operator
// console.log('1'==='1' || 1 === 1);

// // not operator
// console.log('1'!==1);

// var temp = parseInt(prompt('What is the temp?'));
// var forecast;
// if (temp > 90) {
//   forecast = 'Hot!'
// } else if (temp > 70) {
//   forecast = 'Nice!'
// } else {
//   forecast = 'So Cold!'
// }
// console.log(forecast);

// var fruit = ['Banana', 'Apple', 'Pear', 'Grape'];
//
// for (var i = 0; i < fruit.length; i++) {
//   console.log(fruit[i])
// }

var num = 0;

while (num < 10){
  num += 1
  console.log(num)
}
