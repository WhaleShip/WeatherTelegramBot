"""Класс парсера страницы с погодой"""

from bs4 import BeautifulSoup


class WeatherParser:
    def __init__(self, soup):
        self.bs = BeautifulSoup(soup, features="html.parser")

    def is_weather_found(self):
        return self.bs.find(name='div', attrs={'id': 'wob_wc'}) is not None

    def get_city_name(self):
        return self.bs.find(name='span', attrs={'class': 'BBwThe'}).text

    def get_temperature(self):
        return self.bs.find(name='span', attrs={'id': 'wob_tm'}).text

    def get_general_weather(self):
        return self.bs.find(name='span', attrs={'id': 'wob_dc'}).text

    def get_wind(self):
        wind = self.bs.find(name='span', attrs={'id': 'wob_ws'}).text
        wind = wind.replace(' ', '')
        return wind
