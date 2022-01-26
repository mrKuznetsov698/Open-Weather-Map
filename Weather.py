import requests
import json


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
