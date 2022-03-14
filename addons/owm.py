from pyowm import OWM
from pyowm.utils.config import get_default_config
from config import OWM_API


def ReturnWeather(place):
    try:
        owm = OWM(OWM_API)
        mgr = owm.weather_manager()
        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        observation = mgr.weather_at_place(place)
        w = observation.weather
        clouds = w.detailed_status
        wind_speed = w.wind()['speed']
        hum = w.humidity
        temp = w.temperature('celsius')['temp']
        f_like = w.temperature('celsius')['feels_like']
        rains = w.rain
        if len(rains) == 0:
            rains = 0
        else:
            rains = rains['1h'] * 100
        return f'Погода в городе {place}\nтучи: {clouds}\nскорость ветра: {wind_speed}м/с\nВлажность: {hum}%\nТемпература: {temp}, ощущается как: {f_like}\nВероятность дождя в ближайший час: {rains}%'
    except:
        return "Вы ошиблись в названии города, попробуйте еще раз"
