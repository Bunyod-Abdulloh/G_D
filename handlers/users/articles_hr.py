from aiogram import Router, F, types

from handlers.functions.functions_one import extracter
from keyboards.inline.buttons import key_returner_articles
from loader import db

articles = Router()


@articles.message(F.text == "📝 Maqolalar")
async def articles_hr_one(message: types.Message):
    all_articles = await db.select_all_articles()
    extract = extracter(all_medias=all_articles, delimiter=10)
    current_page = 1
    all_pages = len(extract)
    extracted_articles = extract[current_page - 1]
    articles = str()

    for n in extracted_articles:
        articles += f"{n['articles_number']}. <a href='{n['link']}'>{n['file_name']}</a>\n"

    await message.answer(
        text=articles, reply_markup=key_returner_articles(
            current_page=current_page, all_pages=all_pages
        ), disable_web_page_preview=True
    )
