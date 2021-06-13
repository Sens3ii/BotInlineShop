from aiogram import types

from utils.bot_commands import bot_commands


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [command for command in bot_commands]
    )
