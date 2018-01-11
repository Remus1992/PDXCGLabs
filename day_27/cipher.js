console.log('cipher.js running');
var MAX_KEY_SIZE = 26;

console.log(ord(26))
function getMode(){
  let x = true
  while (x) {
    var mode = prompt('Do you wish to encrypt(e) or decrypt(d) a message?');
    if (mode === 'e' || mode === 'd'){
      return mode
    } else {
      console.log('Enter either \'e\' for encrypt or \'d\' for decrypt.')
    }
  }
}

function getMessage(){
  var message = prompt('Enter your message: ')
  return message
}

function getKey(){
  var key_string = 0
  let x = true
  while (x) {
    key_string = prompt('Enter the key number (1-26)')
    key = parseInt(key_string)
    if (key >= 1 && key <= MAX_KEY_SIZE){
      return key
    }
  }
}

// function getTranslatedMessage(mode, message, key){
//   var translated = '';
//   if (mode === 'd'){
//     key = -key
//   }
//     for (symbol in message){
//       if (sy)
//     }
//
// }

getMode();
// getMessage()
console.log(getMessage());
console.log(getKey());
