from aiogram import types

from loader import dp
from utils.db_api.db_commands import get_items, get_items_by_query


@dp.inline_handler(text='')
async def empty_query(query: types.InlineQuery):
    items_list = await get_items()
    results = await get_inline_query_results(items_list)
    await query.answer(results=results)


@dp.inline_handler()
async def inline_query(query: types.InlineQuery):
    text = query.query
    items_list = await get_items_by_query(text)
    results = await get_inline_query_results(items_list)
    await query.answer(results=results)


async def get_inline_query_results(items_list):
    results = []
    for item in items_list:
        results.append(types.InlineQueryResultArticle(
            id=str(item.id),
            title=item.name,
            input_message_content=types.InputTextMessageContent(
                message_text=f"Показать описание {item.name}:\n"
                             f"t.me/shop_329_bot?start={str(item.id)}\n"
                             f"(Перейди по ссылке к боту, и нажми кнопку Start)",
                parse_mode="HTML",
                disable_web_page_preview=True
            ),
            thumb_url=item.photo,
            description=f'{str(item.price)} тг.',
            url=f't.me/shop_329_bot?start={item.id}',
            hide_url=True
        )
        )
    return results
