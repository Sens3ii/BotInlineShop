import asyncio
import os

import django
os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "admin_side.admin_side.settings"
    )
os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
django.setup()


from utils.db_api.db_commands import add_user, add_item, get_users, get_user, get_items, get_item


async def fill_db():
    # print('Добавляю пользователей')
    # await add_user(123, 'Alex', 'alex1')
    # await add_user(124, 'Daniil', 'daniil1')
    # await add_user(125, 'Melisa', 'melisa1')
    # await add_user(126, 'Sofia', 'sofa1')
    # print('Добавляю товар')
    # await add_item(name='Товар1', photo='url_1', price=1500, description='Описание 1')
    # await add_item(name='Товар2', photo='url_2', price=2500, description='Описание 2')
    # await add_item(name='Товар3', photo='url_3', price=3500, description='Описание 3')
    # await add_item(name='Товар4', photo='url_4', price=4500, description='Описание 4')
    # await add_item(name='Товар5', photo='url_5', price=5500, description='Описание 5')
    # await add_item(name='Товар6', photo='url_6', price=6500, description='Описание 6')
    # await add_item(name='Товар7', photo='url_7', price=7500, description='Описание 7')
    # await add_item(name='Товар8', photo='url_8', price=8500, description='Описание 8')
    # users = await get_users()


    # user = await get_user(124)
    # print(f'Все юзеры: {users}')
    # print(f'Юзер с id 124: {user}')
    # items = await get_items()
    # for item in items:
    #     print(item.id, item.name, item.price, item.photo, item.description)
    # item = await get_item(2)
    # print(f'Все items: {items}')
    # print(f'Item 2: {item}')


asyncio.run(fill_db())
