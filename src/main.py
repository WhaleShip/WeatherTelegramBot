"""Точка входа"""

import asyncio
import logging
import sys

from dotenv import load_dotenv

from bot import BotConfig, WeatherTeleBot


async def main():
    load_dotenv()
    config = BotConfig()
    bot = WeatherTeleBot(config)
    await bot.start()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
