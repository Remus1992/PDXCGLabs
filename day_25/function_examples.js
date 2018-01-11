console.log('function_examples.js running');


var two = 2

function add2 (x) {
  if (arguments.length < 1) {
    throw 'The function add2 takes at least one argument. None given.'
  }
  for (var i=0; i<arguments.length; i++) {
    console(arguments[i])
  }
  // var two = 2
  return two + x
}

// console.log(two);
// console.log(add2(5));


try {
  add2()
} catch (ex) {
  console.log(ex)
}
