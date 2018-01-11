console.log('vowels.js running');
/**
var input = prompt('Enter a character');

alert('The character you entered is a vowel');

['a'].indexOf('a') // 0
['a'].indexOf('b') // -1

**/

/**
var input = prompt('Enter a letter');

function vowel_finder (input) {
  if (input === 'a' || input === 'e' || input === 'i' || input === 'o' || input === 'u') {
    alert('This is a vowel')
  } else if (input === 'y') {
    alert('Only Sometimes.')
  } else {
    alert('That was not a valid entry')
  }
}
vowel_finder(input)
**/


var letter = prompt('Enter a letter');
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for (let element of alphabet) {
  if (alphabet.indexOf(letter) === 0 || alphabet.indexOf(letter) === 4 || alphabet.indexOf(letter) === 8 || alphabet.indexOf(letter) === 14 || alphabet.indexOf(letter) === 20){
    alert('this is a vowel')
    break
  } else if (alphabet.indexOf(letter) === 24) {
    alert('this is sometimes a vowel')
    break
  } else if (alphabet.indexOf(letter) === -1) {
    alert('that is not a valid entry')
    break
  } else {
    alert('that is a consonant')
    break
  }
}
