from . import *

def get_weather(s_city="Київ"):
    appid = "c4bb700a457b50d5c8702a4cb696837b"
    
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()

    city_id = data['list'][0]['id']

    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                        params={'id': city_id, 'units': 'metric', 'lang': 'ua', 'APPID': appid})
    data = res.json()
    list_for_week = []
    temperature = 0
    for i in data['list']:
        temperature = int(i['main']['temp'])
        weather = i['weather'][0]['description']
        if i['dt_txt'][12] != '2': continue
        try: weather = textToSmile[weather]
        except: ...
        list_for_week.append((weather, temperature, f'{i["wind"]["speed"]} м/с'))
    return list_for_week