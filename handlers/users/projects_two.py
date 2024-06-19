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
    audio = items[0]['audio_id']
    photo = items[0]['photo_id']
    video = items[0]['video_id']
    voice = items[0]['voice_id']
    document = items[0]['document_id']

    if audio:
        await call.message.answer_audio(
            audio=items[0]['audio_id'], caption=f"{items[0]['category']}\n\n{items[0]['caption']}", reply_markup=markup
        )
    if photo:
        await call.message.answer_photo(
            photo=items[0]['photo_id'], caption=f"{items[0]['category']}\n\n{items[0]['caption']}", reply_markup=markup
        )
    if video:
        await call.message.answer_video(
            video=items[0]['video_id'], caption=f"{items[0]['category']}\n\n{items[0]['caption']}", reply_markup=markup
        )
    if voice:
        await call.message.answer_voice(
            voice=items[0]['voice_id'], caption=f"{items[0]['category']}\n\n{items[0]['caption']}", reply_markup=markup
        )
    if document:
        await call.message.answer_document(
            document=items[0]['document_id'], caption=f"{items[0]['category']}\n\n{items[0]['caption']}",
            reply_markup=markup
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


@router.callback_query(F.data.startswith("prev_pts"))
async def projects_two_prev(call: types.CallbackQuery):
    await call.answer(
        cache_time=0
    )

    current_page = int(call.data.split(":")[1])
    id_ = int(call.data.split(":")[2])

    get_category = await db.select_project_by_id(
        id_=id_
    )
    select_category = await db.select_project_by_categories(
        category_name=get_category['category']
    )

    extract = extracter(
        all_medias=select_category, delimiter=5
    )

    all_pages = len(extract)

    if current_page == 1:
        current_page = all_pages
    else:
        current_page -= 1

    items = extract[current_page - 1]

    markup = interviews_first_ibuttons(
        items=items, current_page=current_page, all_pages=all_pages, selected=items[-1]['sequence']
    )

    audio = items[-1]['audio_id']
    document = items[-1]['document_id']
    photo = items[-1]['photo_id']
    video = items[-1]['video_id']
    caption = f"{items[-1]['category']}\n\n{items[-1]['caption']}"

    try:
        if audio:
            await call.message.edit_media(
                media=types.InputMediaAudio(
                    media=audio, caption=caption
                ), reply_markup=markup
            )
        if document:
            await call.message.edit_media(
                media=types.InputMediaDocument(
                    media=document, caption=caption
                ), reply_markup=markup
            )
        if photo:
            await call.message.edit_media(
                media=types.InputMediaPhoto(
                    media=photo, caption=caption
                ), reply_markup=markup
            )
        if video:
            await call.message.edit_media(
                media=types.InputMediaVideo(
                    media=video, caption=caption
                ), reply_markup=markup
            )
    except aiogram.exceptions.TelegramBadRequest:
        pass


@router.callback_query(F.data.startswith("select_pts:"))
async def projects_two_two(call: types.CallbackQuery):
    await call.answer(
        cache_time=0
    )
    id_ = int(call.data.split(":")[1])
    current_page = int(call.data.split(":")[2])

    get_data = await db.select_project_by_id(
        id_=id_
    )
    select_category = await db.select_project_by_categories(
        category_name=get_data['category']
    )

    extract = extracter(
        all_medias=select_category, delimiter=5
    )

    items = extract[current_page - 1]

    markup = interviews_first_ibuttons(
        items=items, current_page=current_page, all_pages=len(extract), selected=get_data['sequence']
    )

    audio = get_data['audio_id']
    photo = get_data['photo_id']
    video = get_data['video_id']
    document = get_data['document_id']
    caption = f"{get_data['category']}\n\n{get_data['caption']}"

    try:
        if audio:
            await call.message.edit_media(
                media=types.InputMediaAudio(
                    media=audio, caption=caption
                ), reply_markup=markup
            )
        if document:
            await call.message.edit_media(
                media=types.InputMediaDocument(
                    media=document, caption=caption
                ), reply_markup=markup
            )
        if photo:
            await call.message.edit_media(
                media=types.InputMediaPhoto(
                    media=photo, caption=caption
                ), reply_markup=markup
            )
        if video:
            await call.message.edit_media(
                media=types.InputMediaVideo(
                    media=video, caption=caption
                ), reply_markup=markup
            )
    except aiogram.exceptions.TelegramBadRequest:
        pass


@router.callback_query(F.data.startswith("alert_pts:"))
async def projects_two_alert(call: types.CallbackQuery):
    current_page = call.data.split(":")[1]
    await call.answer(
        text=f"Siz {current_page} - sahifadasiz", show_alert=True
    )


@router.callback_query(F.data.startswith("next_pts"))
async def projects_two_next(call: types.CallbackQuery):
    await call.answer(
        cache_time=0
    )

    current_page = int(call.data.split(":")[1])
    id_ = int(call.data.split(":")[2])

    get_category = await db.select_project_by_id(
        id_=id_
    )
    select_category = await db.select_project_by_categories(
        category_name=get_category['category']
    )

    extract = extracter(
        all_medias=select_category, delimiter=5
    )

    all_pages = len(extract)

    if current_page == all_pages:
        current_page = 1
    else:
        current_page += 1

    items = extract[current_page - 1]

    markup = interviews_first_ibuttons(
        items=items, current_page=current_page, all_pages=all_pages, selected=items[0]['sequence']
    )

    audio = items[0]['audio_id']
    document = items[0]['document_id']
    photo = items[0]['photo_id']
    video = items[0]['video_id']
    caption = items[0]['caption']

    try:
        if audio:
            await call.message.edit_media(
                media=types.InputMediaAudio(
                    media=audio, caption=caption
                ), reply_markup=markup
            )
        if document:
            await call.message.edit_media(
                media=types.InputMediaDocument(
                    media=document, caption=caption
                ), reply_markup=markup
            )
        if photo:
            await call.message.edit_media(
                media=types.InputMediaPhoto(
                    media=photo, caption=caption
                ), reply_markup=markup
            )
        if video:
            await call.message.edit_media(
                media=types.InputMediaVideo(
                    media=video, caption=caption
                ), reply_markup=markup
            )
    except aiogram.exceptions.TelegramBadRequest:
        pass
