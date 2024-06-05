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
