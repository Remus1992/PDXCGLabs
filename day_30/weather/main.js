$('body').css('background-image', 'url(portland.jpg)');

var method_search = function (e) {
    e.preventDefault();
    //$('body').css('background-image', 'url(rain.jpg)');

    var new_search = document.getElementById("search_box").value;
    var api_object;
    // console.log(isNaN(new_search));

    if (isNaN(new_search)){
        api_object = {
            url: 'https://api.openweathermap.org/data/2.5/weather?',
            type: 'GET',
            data: {
                APPID: '56fff62ecf26c959b7fb917cb1bf1f99',
                q: new_search
            },
        success: function(data) {
            web_data(data)
        }
    }} else {
        api_object = {
            url: 'https://api.openweathermap.org/data/2.5/weather?',
            type: 'GET',
            data: {
                APPID: '56fff62ecf26c959b7fb917cb1bf1f99',
                zip: new_search
            },
            success: function (data) {
                web_data(data)
            }
        }}
        $.ajax(api_object)

    };
var city_search = document.getElementById("btn-search");
city_search.addEventListener('click', method_search);



function web_data (data) {
            console.log(data);
            var current_weather = data.weather[0]['main'];
            console.log("The Weather is: " + current_weather);
            document.getElementById("forecast_result").innerHTML = "The Current Weather is: " + current_weather;
            var current_tempf = Math.ceil(data.main['temp']  * (9/5) - 459.67);
            var current_tempc = Math.ceil(data.main['temp']  - 273);
            console.log("Farenheit: " + current_tempf);
            document.getElementById("temp-celsius").innerHTML = current_tempc + ' °C';
            console.log("Celcius: " + current_tempc);
            document.getElementById("temp-fahrenheit hidden").innerHTML = current_tempf + ' °F';
            var location_name = data.name;
            document.getElementById("city_name").innerHTML = "City Name: " + location_name;

            if (current_weather === 'Rain') {
                $('body').css('background-image', 'url(rain.jpg)')
            } else if (current_weather === 'Clouds') {
                $('body').css('background-image', 'url(cloudy.jpg)')
            } else if (current_weather === 'Clear') {
                $('body').css('background-image', 'url(sun.jpg)')
            } else if (current_weather === 'Snow') {
                $('body').css('background-image', 'url(snow.jpg)')
            }  else if (current_weather === 'Haze') {
                $('body').css('background-image', 'url(haze.jpg)')
            }

            // if (current_weather === 'Rain'){
            //     document.body.style.backgroundImage = 'url(rain.jpg)';
            // }
        }





// var request = new XMLHttpRequest();
// request.onreadystatechange = function () {
//     if (request.readyState === 4) {
//         console.log('ready state 4');
//         if (request.status === 200) {
//             console.log('ready state 4');
//             console.log(response.responseText);
//         } else {
//             console.log('There was an error')
//         }
//     }
// };
//
// request.open('GET', 'URL');
//
// request.send('APPID=');

