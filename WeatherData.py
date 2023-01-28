import requests
import os
from datetime import datetime

user_api = os.environ['API_key']

loc = input('Enter the city name:\t')

link = f"https://api.openweathermap.org/data/2.5/weather?q={loc}&appid={API_key}"

api_link = requests.get(link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print('City not found')
else:
    #variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-------------------------------------------------------------")
    print("Weather Stats for - {}  || {}".format(loc.upper(), date_time))
    print("-------------------------------------------------------------")
    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current weather desc  :",weather_desc)
    print("Current Humidity      :",hmdt, '%')
    print("Current wind speed    :",wind_spd ,'kmph')

