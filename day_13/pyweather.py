
import requests
city = input ("Enter City: ")
payload = {'APPID': '56fff62ecf26c959b7fb917cb1bf1f99','q': city}

r = requests.post ('https://api.openweathermap.org/data/2.5/weather?', params=payload)
data = r.json()
tempf = data['main']['temp'] * (9/5) - 459.67
tempc = data['main']['temp'] - 273
print(r.url)
print ("Farenheit:\t", tempf)
print ("Celcius:\t", tempc)
