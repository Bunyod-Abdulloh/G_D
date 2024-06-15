import aiogram.exceptions
from aiogram import Router, F, types

from handlers.functions.functions_one import extracter
from keyboards.inline.buttons import interviews_first_ibuttons
from loader import db

router = Router()


@router.callback_query(F.data.startswith("projects:"))
async def interviews_projects_hr_projects(call: types.CallbackQuery):
    category_id = int(call.data.split(":")[1])
    get_category = await db.select_project_name(
        id_=category_id
    )
    select_category = await db.select_project_by_categories(
        category_name=get_category['category']
    )
    extract = extracter(
        all_medias=select_category, delimiter=5
    )
    current_page = 1
    all_pages = len(extract)
    items = extract[current_page - 1]
    markup = interviews_first_ibuttons(
        items=items, current_page=current_page, all_pages=all_pages, selected=1
    )
    await call.message.delete()
    await call.message.answer_audio(
        audio=items[0]['audio_id'], caption=f"{items[0]['category']}\n\n{items[0]['caption']}", reply_markup=markup
    )


@router.callback_query(F.data.startswith("content_projects:"))
async def projects_two_one(call: types.CallbackQuery):
    current_page = int(call.data.split(':')[1])
    category = call.data.split(':')[2]
    get_category = await db.select_project_by_categories(
        category_name=category
    )
    extract = extracter(all_medias=get_category, delimiter=5)
    items = extract[current_page - 1]

    content = str()
    for item in items:
        content += f"{item['subcategory']}\n"

    await call.answer(
        text=content, show_alert=True
    )


@router.callback_query(F.data.startswith("select_projects:"))
async def projects_two_two(call: types.CallbackQuery):
    await call.answer(cache_time=0)
    id_ = int(call.data.split(":")[1])
    current_page = int(call.data.split(":")[2])
    get_audio = await db.select_project_by_id(
        id_=id_
    )
    select_category = await db.select_project_by_categories(
        category_name=get_audio['category']
    )
    extract = extracter(
        all_medias=select_category, delimiter=5
    )
    items = extract[current_page - 1]
    markup = interviews_first_ibuttons(
        items=items, current_page=current_page, all_pages=len(extract), selected=get_audio['sequence']
    )
    try:
        await call.message.edit_media(
            media=types.InputMediaAudio(
                media=get_audio['audio_id'], caption=f"{get_audio['category']}\n\n{get_audio['caption']}"
            ), reply_markup=markup
        )
    except aiogram.exceptions.TelegramBadRequest:
        pass


@router.callback_query(F.data.startswith("prev_pts"))
async def projects_two_prev(call: types.CallbackQuery):
    await call.answer(
        cache_time=0
    )
    current_page = int(call.data.split(":")[1])
    all_pages = int(call.data.split(":")[2])
    id_ = int(call.data.split(":")[3])

    if current_page == 1:
        current_page = all_pages
    else:
        current_page -= 1

    get_audio = await db.select_project_by_id(
        id_=id_
    )
    select_category = await db.select_project_by_categories(
        category_name=get_audio['category']
    )
    extract = extracter(
        all_medias=select_category, delimiter=5
    )
    items = extract[current_page - 1]
    markup = interviews_first_ibuttons(
        items=items, current_page=current_page, all_pages=len(extract), selected=items[-1]['sequence']
    )
    try:
        await call.message.edit_media(
            media=types.InputMediaAudio(
                media=items[-1]['audio_id'], caption=f"{items[-1]['category']}\n\n{items[-1]['caption']}"
            ), reply_markup=markup
        )
    except aiogram.exceptions.TelegramBadRequest:
        pass
