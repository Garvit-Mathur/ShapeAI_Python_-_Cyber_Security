import requests
#import os
from datetime import datetime

api_key = '769ac46120204dc8d4223330f5517e15'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')


l1 = "-------------------------------------------------------------"
l2 = "Weather Stats for - {}  || {}".format(location.upper(), date_time)
l3 = "-------------------------------------------------------------"

l4 = "Current temperature is: {:.2f} deg C".format(temp_city)
l5 = "Current weather desc  :", weather_desc
l6 = "Current Humidity      :", hmdt, '%'
l7 = "Current wind speed    :", wind_spd, 'kmph'

with open('WeatherForecasting.txt','w') as out:
    out.writelines('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(l1,l2,l3,l4,l5,l6,l7))

