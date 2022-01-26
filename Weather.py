import requests
import json


# 74be05f6b9c8eea10478aa9a2bb0ecb3 - key
# https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang={lang}

# ids = {
#     #Thunderstorm
#     200: 'thunderstorm with light rain',
#     201: 'thunderstorm with rain',
#     202: 'thunderstorm with heavy rain'
#     210: 'light thunderstorm',
#     211: 'thunderstorm',
#     212: 'heavy thunderstorm',
#     221: 'ragged thunderstorm',
#     230: 'thunderstorm with light drizzle',
#     231: 'thunderstorm with drizzle',
#     232: 'thunderstorm with heavy drizzle'
#
#     #Drizzle
#     300: 'light intensity drizzle',
#     301: 'drizzle',
#     302: 'heavy intensity drizzle',
#     310: 'light intensity drizzle rain',
#     311: 'drizzle rain',
#     312: 'heavy intensity drizzle rain',
#     313: 'shower rain and drizzle',
#     314: 'heavy shower rain and drizzle',
#     321: 'shower drizzle'
#
#     #Rain
#     500: 'light rain',
#     501: 'moderate rain',
#     502: 'heavy intensity rain',
#     503: 'very heavy rain',
#     504: 'extreme rain',
#     511: 'freezing rain',
#     520: 'light intensity shower rain',
#     521: 'shower rain',
#     522: 'heavy intensity shower rain',
#     531: 'ragged shower rain',
#
#     #Snow
#     600: 'light snow',
#     601: 'Snow',
# }


class Observation:
    def __init__(self, response):
        self.resp = response
        self.absoluteNol = -273.15

    def get_temp(self, accurate=2):
        return round(float(self.resp['main']['temp']), accurate)

    def get_min_temp(self, accurate=2):
        return round(float(self.resp['main']['temp_min']), accurate)

    def get_max_temp(self, accurate=2):
        return round(float(self.resp['main']['temp_max']), accurate)

    def get_feels_like_temperature(self, accurate=2):
        return round(float(self.resp['main']['feels_like']), accurate)

    def get_humidity(self):
        return int(self.resp['main']['humidity'])

    def get_pressure(self):
        return int(self.resp['main']['pressure'])

    def get_main_weather(self):
        return self.resp['weather']['main']

    def get_weather_description(self):
        return self.resp['weather']['description']

    def get_coordinates(self): #широта, долгота
        return int(self.resp['coord']['lat']), int(self.resp['coord']['lot'])


class Weather:
    def __init__(self, key: str, lang='en', units='metric'):
        self.key = key
        self.lang = lang
        self.units = units
        self.url = '''https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang={lang}&units={units}'''

    def get_weather(self, city='London'):
        resp = requests.request(method='GET',
                                url=self.url.format(city=city, key=self.key, lang=self.lang, units=self.units))
        return Observation(resp.json())
