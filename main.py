import requests
import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        print(f"Песочная грязь в : {city}\nТемпратура: {cur_weather}C\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind}\n"
              f"Восход солнца: {sunrise_timestamp}\n"
              f"  Я думаю пивка тяпнуть все равно можно"
              )

    except Exception as ex:
        print(ex)
        print("Проверься брат: ")


def main():
    city = input("Брат, набери свой город, пиво не ждет: ")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()