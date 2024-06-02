from aiogram import Router, F, types

from handlers.functions.check_subscription import extracter
from keyboards.inline.buttons import key_returner_selected
from loader import db

lessons = Router()


@lessons.callback_query(F.data.startswith("table:"))
async def lessons_hr_one(call: types.CallbackQuery):
    await call.message.delete()
    table_id = int(call.data.split(":")[1])
    table_name = f"medias_table{table_id}"
    select_table = await db.select_all_media(table_name=table_name)
    extract = extracter(all_medias=select_table, delimiter=6)

    current_page = 1
    all_pages = len(extract)
    items = extract[current_page - 1]
    # key = key_returner_selected(
    #     items=items, current_page=current_page, all_pages=all_pages, selected=1, table_name=table_name
    # )
    if items[0]['audio_id']:
        await call.message.answer_photo(
            photo="AgACAgIAAxkBAAMqZlc4GfY4Jm5098grcklYcF0LAAElAAKHzzEbtn6YSyHJaUdbA3WNAQADAgADeQADNQQ",
            caption=items[0]['caption']
        )
