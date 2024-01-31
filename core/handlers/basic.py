from aiogram import Bot
from aiogram.types import Message

from core.keyboards.reply import reply_keyboard
from core.utils.commands import set_commands


async def get_start(message: Message, bot: Bot):

    await message.reply(f'Zdorov, {message.from_user.first_name}, дай 35 грн',)

async def get_privat(message: Message, bot: Bot):

    await message.reply(f'Privat?{message.from_user.first_name}, idi nahuy ', reply_markup=reply_keyboard)

async def get_new_workout(message: Message, bot: Bot):

    await message.answer('Дата: ')
