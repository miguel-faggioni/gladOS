import requests, json

API_KEY = '99f5445ca903b62336be09d7507236b9'
CITY = 'Barão Geraldo, Campinas'

base_url = 'http://api.openweathermap.org/data/2.5/weather?'
complete_url = base_url + 'appid=' + API_KEY + '&q=' + CITY


def GetTemperature(content):
    response = requests.get(complete_url)
    response_json = response.json()
  
    if response_json['cod'] == '404':
        return 'eita, não sei, deu ruim'

    response_content = response_json['main']
  
    current_temperature = response_content['temp'] - 273.15
    current_temperature_feeling = response_content['feels_like'] - 273.15
    current_pressure = response_content['pressure']
    current_humidity = response_content['humidity']
  
    current_weather = response_json['weather']
    weather_description = current_weather[0]['description']

    print('temperatura ')
    print(current_temperature)
    print('sensação térmica ')
    print(current_temperature_feeling)
    print('humidade ')
    print(current_humidity)
    print('clima')
    print(weather_description)

    return response_json
