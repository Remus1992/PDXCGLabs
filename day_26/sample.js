'use strict';

// fruit = {
//   'apple': 1.99
//   'pear': 0.99
// }

// function Animal(kind, noise, fur){
//     this.kind = type;
//     this.fur = fur;
//     this.speak = function(){
//       console.log(noise)
//     }
// }
//
// var cat = new Animal('Cat', 'Meow', true);
// var dog = new Animal('Dog', 'Woof', false);

// var animal = {
//   type: 'dog',
//   fur: true,
//   speak: function (noise) {
//     console.log(noise)
//   }
// };

function BankAccount (balance, name) {
  this.balance = balance;
  this.name = name;
  this.withdraw = function (amount) {
    if (this.balance - amount > 0) {
      this.balance -= amount;
      console.log('Thank you. Your balance is $' + this.balance + '.')
    } else {
      console.log('I\'m sorry ' + this.anme + '. You do not have enough funds. Your balance is $' + this.balance + '.')
    }
  };
  this.deposit = function (amount) {
    this.balance += amount;
    console.log('Thank you ' + this.name + '. Your balance is $' + this.balance + '.')
  };
}

var chris = new BankAccount(100, 'Chris');
