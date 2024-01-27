
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")



bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def get_start(message: Message, bot: Bot):

    await bot.send_message(message.from_user.id, f'Hello, {message.from_user.first_name}, dai 35 grn')
    await message.answer(f'sorry, {message.from_user.first_name}, nema zdachi')
    await message.reply(f'Privat? {message.from_user.first_name}, idi nahuy')


async def start():

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
