console.log('site.js running');

var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};

function findRarestValue(obj){
  ages = {
    // '22': 2,
    // '25': 4,
    // '20': 3
  }
    for (let name in obj) {
      age = obj[name]
      if (!(age in ages)){
        ages[age] = 1
      }else if (age in ages){
      ages[age] += 1
      }
    }

    // console.log(ages);
    var array_ages = Object.values(ages);
    // console.log(array_ages);

    lowest_value = Math.min.apply(null, array_ages);
    // console.log(lowest_value);

    for (let key in ages) {
      if (ages[key] === lowest_value){
          // console.log(key);
          //console.log(typeof key)
          var new_key = parseInt(key);
          //console.log(typeof new_key)
          return new_key;
      }
    }
}

function findRarestKeys (lowest_value_key){
  for (let key in namesToAges){
    if(namesToAges[key] === lowest_value_key){
      console.log(key);
    }
  }
}

lowest_value_key = findRarestValue(namesToAges);
// console.log(lowest_value_key);

findRarestKeys(lowest_value_key);
