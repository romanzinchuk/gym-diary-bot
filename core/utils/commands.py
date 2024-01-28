from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='початок роботи'
        ),
        BotCommand(
            command='help',
            description='30 grn'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
