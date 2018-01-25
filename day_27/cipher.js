console.log('cipher.js running');
var MAX_KEY_SIZE = 26;

// console.log("f".charCodeAt(0));

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

function getTranslatedMessage(mode, message, key){
	// Wrap the amount
	if (mode === 'd'){
        key = -key;
    }
    if (key < 0)
		key += 26;
	// Make an output variable
	var output = '';
	// Go through each character
	for (var i = 0; i < message.length; i ++) {
		// Get the character we'll be appending
		var c = message[i];
		// If it's a letter...
		if (c.match(/[a-z]/i)) {

			// Get its code
			var code = message.charCodeAt(i);

			// Uppercase letters
			if ((code >= 65) && (code <= 90))
				c = String.fromCharCode(((code - 65 + key) % 26) + 65);

			// Lowercase letters
			else if ((code >= 97) && (code <= 122))
				c = String.fromCharCode(((code - 97 + key) % 26) + 97);
		}
		// Append
		output += c;
	}
	// All done!
	return output;
};

var mode = getMode();
var message = getMessage();
var key = getKey();

console.log(getTranslatedMessage(mode, message, key));

