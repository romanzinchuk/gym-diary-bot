from core.handlers.basic import get_start
from aiogram import Bot, Dispatcher, MagicFilter, F
from aiogram.filters import Command
import asyncio
import os
from dotenv import load_dotenv
from core.handlers.basic import get_new_workout, get_privat
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")



bot = Bot(BOT_TOKEN)
dp = Dispatcher()

async def start():

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.message.register(get_start, Command(commands='start'))
    dp.message.register(get_new_workout, Command(commands='new'))
    dp.message.register(get_privat, F.text == 'Можна на приват кинути?')


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
