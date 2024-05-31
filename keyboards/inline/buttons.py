from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import db

inline_keyboard = [[
    InlineKeyboardButton(text="✅ Yes", callback_data='yes'),
    InlineKeyboardButton(text="❌ No", callback_data='no')
]]
are_you_sure_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


async def lessons_main_ikb():
    all_lessons = await db.select_all_tables()
    builder = InlineKeyboardBuilder()
    for lesson in all_lessons:
        builder.add(
            InlineKeyboardButton(
                text=lesson['table_name'], callback_data=f"table:{lesson['table_number']}"
            )
        )
    builder.adjust(1)
    # builder.add(
    #     InlineKeyboardButton(
    #         text="⬅️ Ortga", callback_data="back_main"
    #     )
    # )
    return builder.as_markup()
