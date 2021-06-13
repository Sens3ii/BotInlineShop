from aiogram import types

bot_commands = []

bot_commands.extend(
    [
        types.BotCommand('/start', 'Запуск бота'),
        types.BotCommand('/help', 'Показать справку'),
        types.BotCommand('/items', 'Показать товары'),
    ]
)

