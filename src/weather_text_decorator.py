"""Класс преобразовывающий полученную информацию в текст ответа"""


import json


class TextDecorator:
    @staticmethod
    def decorate_weather_info(location, temperature, wind, general_weather):
        with open('descriptions.json', encoding='utf-8-sig') as text_templates_file:
            descriptions_temp = json.load(text_templates_file)
        if general_weather in descriptions_temp:
            description = descriptions_temp[general_weather]
        else:
            description = general_weather

        return (f'Погода в {location}:\n\n'
                f'температура: {temperature}°C   ветер: {wind}\n'
                f'{description}')
