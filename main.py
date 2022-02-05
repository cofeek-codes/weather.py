from pyowm import OWM
from pywebio.input import *
from pywebio.output import *

owm = OWM('aed1407ec32905a7a44f60f4cc6290f6')
# API = 'aed1407ec32905a7a44f60f4cc6290f6'
mgr = owm.weather_manager()

# interface
put_markdown(r""" # Погода by cofeek-codes""")
#  Search
place = input("Введите город ")
observation = mgr.weather_at_place(place)
w = observation.weather

# get

get__temp = w.temperature('celsius')["temp"]
get__wind = w.wind()["speed"]
get__rain = w.rain

# build
temp = 'В городе ' + place + ' сейчас ' + str(get__temp) + ' С'
# wind
if get__wind:
    wind = 'Ветер ' + str(get__wind) + ' м/с'
else:
    wind = 'Ветра нет'
# rain
if get__rain:
    rain = get__rain
else:
    rain = 'Дождя нет'

# out
put_text(temp)
put_text(wind)
# image check
cloudy_path = open('./img/cloudy.png', 'rb').read()
rain_path = open('./img/rain.png', 'rb').read()
sun_path = open('./img/sun.png', 'rb').read()
rain_image = put_image(rain_path, height='50px', width='50px')
sun_image = put_image(sun_path, height='50px', width='50px')
if get__rain:
    put_image(rain_path, height='50px', width='50px'), put_text(rain)

else:
    put_image(sun_path, height='50px', width='50px'), put_text(rain)
