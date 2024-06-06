from aiogram import Router, F, types

from handlers.functions.functions_one import extracter
from keyboards.inline.buttons import key_returner_selected, key_returner
from loader import db

courses = Router()


@courses.message(F.text == "📚 Kurslar")
async def courses_hr_one(message: types.Message):
    all_courses = await db.select_all_tables(
        table_type='kurs'
    )
    extract = extracter(all_medias=all_courses, delimiter=10)
    current_page = 1
    all_pages = len(extract)
    items = extract[current_page - 1]
    key = key_returner(
        items=items, current_page=current_page, all_pages=all_pages
    )
    text = str()
    for n in items:
        text += f"{n['table_number']}. {n['table_name']}\n"
    await message.answer(
        text=text, reply_markup=key
    )


@courses.callback_query(F.data.startswith("courses_prev:"))
async def start_prev_page(call: types.CallbackQuery):
    tables = await db.select_all_tables(
        table_type='kurs'
    )
    extract = extracter(
        all_medias=tables, delimiter=10
    )
    current_page = int(call.data.split(':')[1])
    all_pages = len(extract)

    if current_page == all_pages:
        await call.answer(
            text="Boshqa sahifa mavjud emas!", show_alert=True
        )
    else:
        await call.answer(
            cache_time=0
        )
        current_page -= 1
        items = extract[current_page - 1]
        key = key_returner(
            items=items, current_page=current_page, all_pages=all_pages
        )
        text = str()
        for n in items:
            text += f"{n['table_number']}. {n['table_name']}\n"
        await call.message.edit_text(
            text=text, reply_markup=key
        )


@courses.callback_query(F.data.startswith("courses_next:"))
async def start_next_page(call: types.CallbackQuery):
    tables = await db.select_all_tables(
        table_type='kurs'
    )
    extract = extracter(
        all_medias=tables, delimiter=10
    )
    current_page = int(call.data.split(':')[1])
    all_pages = len(extract)

    if current_page == all_pages:
        await call.answer(
            text="Boshqa sahifa mavjud emas!", show_alert=True
        )
    else:
        await call.answer(
            cache_time=0
        )
        current_page += 1
        items = extract[current_page - 1]
        key = key_returner(
            items=items, current_page=current_page, all_pages=len(extract)
        )
        text = str()
        for n in items:
            text += f"{n['table_number']}. {n['table_name']}\n"
        await call.message.edit_text(
            text=text, reply_markup=key
        )


channels_list = [-1001917132582]


@courses.callback_query(F.data.startswith("courses:"))
async def lessons_hr_one(call: types.CallbackQuery):
    await call.answer(
        text="Bo'lim hozircha ishga tushirilmadi!"
    )

    # table_id = int(call.data.split(":")[1])
    # table_name = f"medias_table{table_id}"
    # select_table = await db.select_all_media(
    #     table_name=table_name
    # )
    # extract = extracter(
    #     all_medias=select_table, delimiter=6
    # )
    # current_page = 1
    # all_pages = len(extract)
    # items = extract[current_page - 1]
    # ibutton = key_returner_selected(
    #     items=items, current_page=current_page, all_pages=all_pages, selected=1, table_name=table_name
    # )
    #
    # if items[0]['photo_id']:
    #     await call.message.answer_photo(
    #         photo=items[0]['photo_id'], protect_content=True
    #     )
    # if items[0]['audio_id']:
    #     await call.message.answer_audio(
    #         audio=items[0]['audio_id'], protect_content=True
    #     )
    # if items[0]['document_id']:
    #     await call.message.answer_document(
    #         document=items[0]['document_id'], protect_content=True
    #     )
    # if items[0]['video_id']:
    # await call.message.answer_video(
    #     video=items[0]['video_id'], caption=items[0]['caption'], reply_markup=ibutton
    # )


@courses.callback_query(F.data.startswith("id:"))
async def get_id_and_selected(call: types.CallbackQuery):
    await call.answer(
        cache_time=0
    )
    lesson_number = int(call.data.split(":")[1])
    current_page = int(call.data.split(":")[2])
    table_name = call.data.split(":")[3]
    all_medias = await db.select_all_media(
        table_name=table_name
    )
    extract = extracter(
        all_medias=all_medias, delimiter=6
    )
    items = extract[current_page - 1]
    ibutton = key_returner_selected(
        items=items, current_page=current_page, all_pages=len(extract), selected=lesson_number, table_name=table_name
    )
    selected_media = await db.db_get_media_by_id(
        table_name=table_name, lesson_number=lesson_number
    )
    # if selected_media['photo_id']:
    #     await call.message.answer_photo(
    #             photo=selected_media['photo_id'], protect_content=True
    #     )
    # if selected_media['audio_id']:
    #     await call.message.answer_audio(
    #         audio=selected_media['audio_id'], protect_content=True)
    # if selected_media['document_id']:
    #     await call.message.answer_document(
    #         document=selected_media['document_id'], protect_content=True
    #     )
    # if selected_media['video_id']:
    await call.message.edit_media(
        media=types.InputMediaVideo(
            media=selected_media['video_id'],
            caption=selected_media['caption']
        ), reply_markup=ibutton
    )
