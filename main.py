#74be05f6b9c8eea10478aa9a2bb0ecb3 - key
import Weather
weather = Weather.Weather('74be05f6b9c8eea10478aa9a2bb0ecb3')
observ = weather.get_weather()
print(observ.get_temp())