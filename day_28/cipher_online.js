console.log('cipher_online.js running');
//
// var caesarShift = function(str, amount) {
// 	// Wrap the amount
// 	if (amount < 0)
// 		return caesarShift(str, amount + 26);
// 	// Make an output variable
// 	var output = '';
//
//     //charCodeAt() gets the char code in a string
//     //Upper and lower bounds for upper case characters
//     var upperBoundUpper = "A".charCodeAt(0);
//     var lowerBoundUpper = "Z".charCodeAt(0);
//     //Upper and lower bounds for lower case characters
//     var upperBoundLower = "a".charCodeAt(0);
//     var lowerBoundLower = "z".charCodeAt(0);
//
// 	// Go through each character
//     for (var i = 0; i < str.length; i++) {
//       // Get the character we'll be appending
//       var c = str[i];
//       // Get its code
// 	  var code = str.charCodeAt(i);
// 	  if (code <= upperBoundUpper && code >= lowerBoundUpper) {
//           c = String.fromCharCode(((code - 65 + amount) % 26) + 65);
//       }else if (code <= upperBoundLower && code >= lowerBoundLower) {
//           var code = str.charCodeAt(i);
//           c = String.fromCharCode(((code - 97 + amount) % 26) + 97);
//           //Check for space
//       }else if (str[i] == " ") {
//           continue;
//       }else{  //Not recognized character - not valid
// 		alert("Invalid name");
// 		break;
// 	  }
// 	  // Append
// 	  output += c;
// 	}
//
// 	// All done!
// 	return output;
//
// };
//
// caesarShift('Attack', 12);


var caesarShift = function(str, amount) {

	// Wrap the amount
	if (amount < 0)
		return caesarShift(str, amount + 26);

	// Make an output variable
	var output = '';

	// Go through each character
	for (var i = 0; i < str.length; i ++) {

		// Get the character we'll be appending
		var c = str[i];

		// If it's a letter...
		if (c.match(/[a-z]/i)) {

			// Get its code
			var code = str.charCodeAt(i);

			// Uppercase letters
			if ((code >= 65) && (code <= 90))
				c = String.fromCharCode(((code - 65 + amount) % 26) + 65);

			// Lowercase letters
			else if ((code >= 97) && (code <= 122))
				c = String.fromCharCode(((code - 97 + amount) % 26) + 97);

		}
		// Append
		output += c;

	}
	// All done!
	return output;

};

console.log(caesarShift('Mffmow mf pmiz!', -12));    // Returns "Attack at dawn!"

// function getTranslatedMessage(mode, message, key){
//   var translated = '';
//   if (mode === 'd'){
//     key = -key
//   }
//     for (symbol in message){
//       if (symbol is a letter){
//           num = symbol.charCodeAt(0);
//           num += key
//         }
//         {
//             if (symbol is uppercase){
//                 if (num > "Z".charCodeAt(0)){
//                     num -= 26
//                 } else if (num < "A".charCodeAt(0))
//         }
//         }
//     }
//
// }