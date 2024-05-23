"""Класс получения информации о погоде"""

from urllib.parse import quote

import aiohttp

from weather_parser import WeatherParser
from weather_text_decorator import TextDecorator


class Weather:
    def __init__(self):
        self.host = 'https://www.google.com/search?q='
        self.session = aiohttp.ClientSession()

    @property
    def headers(self):
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }

    async def make_request(self, url):
        async with self.session.get(url, headers=self.headers) as resp:
            return await resp.text()

    async def get_weather(self, city):
        """
        находит информацию о погоде в заданом городе и возвращает оформленный ответ
        :return: оформленное сообщение
        """
        url = self.host + quote(f'погода в + {city}')
        soup = await self.make_request(url)
        pars = WeatherParser(soup)

        if not pars.is_weather_found():
            return 'Ошибка❗️ Бот не понял где смотреть погоду. Попробуй ввести запрос иначе.'

        location = pars.get_city_name()
        temperature = pars.get_temperature()
        general = pars.get_general_weather()
        wind = pars.get_wind()

        return TextDecorator.decorate_weather_info(location, temperature, wind, general_weather=general)
