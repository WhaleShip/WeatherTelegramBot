"""Класс обработчика сообщений"""

from aiogram import types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold


class MessageHandler:
    def __init__(self, bot):
        self.bot = bot
        self.bot.dp.message.register(self.start_handler, CommandStart())
        self.bot.dp.message.register(self.message_handler)

    async def message_handler(self, message: types.Message):
        """
        Обрабатывает все входящие сообщения от пользователя
        """
        try:
            weather = await self.bot.weather.get_weather(message.text)
            await message.answer(weather)
        except Exception:
            await message.answer("❌Ошибка со стороны сервера!❌")

    async def start_handler(self, message: types.Message):
        """
        Ответ на команду /start
        """
        await message.answer(f'Привет, {hbold(message.from_user.full_name)}! 👋')