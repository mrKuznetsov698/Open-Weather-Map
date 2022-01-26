import requests


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

    def get_wind_speed(self):
        return int(self.resp['wind']['speed'])

    def get_wind_deg(self):
        return int(self.resp['wind']['deg'])

    def get_clouds_all(self):
        return int(self.resp['clouds']['all'])

    def get_rain_volume_1h(self):
        return int(self.resp['rain']['1h'])

    def get_rain_volume_3h(self):
        return int(self.resp['rain']['3h'])

    def get_snow_volume_1h(self):
        return int(self.resp['snow']['1h'])

    def get_snow_volume_3h(self):
        return int(self.resp['snow']['3h'])


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
