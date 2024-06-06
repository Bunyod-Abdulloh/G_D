from aiogram import Router, F, types

from handlers.functions.functions_one import extracter
from keyboards.inline.buttons import key_returner_projects
from loader import db

interviews_projects = Router()


@interviews_projects.message(F.text == "🎙 Suhbat va loyihalar")
async def interviews_projects_hr_one(message: types.Message):
    all_projects = await db.select_projects()
    extract = extracter(all_medias=all_projects, delimiter=10)
    current_page = 1
    all_pages = len(extract)
    items = extract[current_page - 1]
    projects = str()

    for index, n in enumerate(items):
        projects += f"{index + 1}. {n['category']}\n"
    markup = key_returner_projects(
        current_page=current_page, all_pages=all_pages
    )
    await message.answer(
        text=projects, reply_markup=markup
    )


@interviews_projects.callback_query(F.data.startswith("prev_projects:"))
async def interviews_projects_hr_prev(call: types.CallbackQuery):
    current_page = int(call.data.split(':')[1])
    if current_page == 1:
        await call.answer(
            text="Boshqa sahifa mavjud emas!", show_alert=True
        )
    else:
        all_projects = await db.select_projects()
        extract = extracter(
            all_medias=all_projects, delimiter=10
        )
        len_extract = len(extract)
        current_page -= 1

        await call.answer(
            cache_time=0
        )
        items = extract[current_page - 1]
        projects = str()

        for index, n in enumerate(items):
            projects += f"{index + 1}. {n['category']}\n"
        markup = key_returner_projects(
            current_page=current_page, all_pages=len_extract
        )
        await call.message.edit_text(
            text=projects, reply_markup=markup
        )


@interviews_projects.callback_query(F.data.startswith("alert_projects"))
async def interviews_projects_hr_alert(call: types.CallbackQuery):
    current_page = call.data.split(":")[1]
    await call.answer(
        text=f"Siz {current_page} - sahifadasiz", show_alert=True
    )


@interviews_projects.callback_query(F.data.startswith("next_projects"))
async def interviews_projects_hr_next(call: types.CallbackQuery):
    current_page = int(call.data.split(':')[1])
    if current_page == 1:
        await call.answer(
            text="Boshqa sahifa mavjud emas!", show_alert=True
        )
    else:
        all_projects = await db.select_projects()
        extract = extracter(
            all_medias=all_projects, delimiter=10
        )
        len_extract = len(extract)
        current_page += 1

        await call.answer(
            cache_time=0
        )
        items = extract[current_page - 1]
        projects = str()

        for index, n in enumerate(items):
            projects += f"{index + 1}. {n['category']}\n"
        markup = key_returner_projects(
            current_page=current_page, all_pages=len_extract
        )
        await call.message.edit_text(
            text=projects, reply_markup=markup
        )
