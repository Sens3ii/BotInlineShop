from re import compile

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.inline_buy import buy_keyboard, paid_keyboard
from loader import dp
from utils.db_api.db_commands import get_item


@dp.message_handler(CommandStart(deep_link=compile(r"\d+")))
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!', deep_link_args)
    item = await get_item(deep_link_args)
    caption = """
Название: {title}
<i>Описание:</i>
{description}
<b>Цена:</b> {price:.2f} <b>тг</b>
"""
    await message.answer_photo(
        photo=item.photo,
        caption=caption.format(
            title=item.name,
            description=item.description,
            price=item.price,
        ),
        reply_markup=buy_keyboard(item_id=item.id),
    )


@dp.callback_query_handler(text_contains="buy")
async def create_invoice(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    item_id = call.data.split(":")[-1]
    item = await get_item(item_id)
    await call.message.answer(
        f"Переведите не менее {item.price:.2f} тг. с помощью Kaspi-перевода.\n"
        f"Номер Kaspi: +77772221177",
        reply_markup=paid_keyboard)
    await state.set_state("purchase")
    await call.message.edit_reply_markup()


@dp.callback_query_handler(text="cancel", state="purchase")
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Заказ отменен")
    await state.finish()


@dp.callback_query_handler(text="paid", state="purchase")
async def approve_payment(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Проверка транзакций..\n"
                              "Оплата успешно проведена")
    await call.message.edit_reply_markup()
    await state.finish()


@dp.message_handler(CommandStart(deep_link=None))
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Я чат-бот магазин, в пару кликов ты сможешь купить нужный для тебя товар. \n'
                         f'Введи @shop_329_bot для списка товаров')
