"""Класс бота а так же его стандартных конфигураций"""

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from pydantic_settings import BaseSettings

from weather import Weather
from handler import MessageHandler


class BotConfig(BaseSettings):
    token: str

    class Config:
        env_file = '.env'
        env_prefix = 'BOT_'


class WeatherTeleBot:
    def __init__(self, config):
        self.config = config
        self.dp = Dispatcher()
        self.weather = Weather()
        self.bot = Bot(config.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.message_handler = MessageHandler(self)

    async def start(self):
        await self.dp.start_polling(self.bot)
