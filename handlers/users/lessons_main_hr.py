from aiogram import Router, F, types

from handlers.functions.functions_one import extracter
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
    ibutton = key_returner_selected(
        items=items, current_page=current_page, all_pages=all_pages, selected=1, table_name=table_name
    )
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
    await call.message.answer_video(
        video=items[0]['video_id'], caption=items[0]['caption'], reply_markup=ibutton
    )


@lessons.callback_query(F.data.startswith("id:"))
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
