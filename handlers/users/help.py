from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.bot_commands import bot_commands


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ['Список команд: \nВведите @shop_329_bot для поиска товаров ']
    text.extend([f'{command.command} - {command.description}' for command in bot_commands])
    await message.answer("\n".join(text))
