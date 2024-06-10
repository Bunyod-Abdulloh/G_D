from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import db

inline_keyboard = [[
    InlineKeyboardButton(text="✅ Yes", callback_data='yes'),
    InlineKeyboardButton(text="❌ No", callback_data='no')
]]
are_you_sure_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def key_returner(items, current_page, all_pages):
    keys = InlineKeyboardBuilder()
    for item in items:
        keys.add(
            InlineKeyboardButton(
                text=f"{item['table_number']}",
                callback_data=f"courses:{item['table_number']}:{current_page}"
            )
        )
    keys.adjust(5)
    keys.row(
        InlineKeyboardButton(
            text="◀️",
            callback_data=f"courses_prev:{current_page}"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"courses_alert:{current_page}"
        ),
        InlineKeyboardButton(
            text="▶️",
            callback_data=f"courses_next:{current_page}"
        )
    )
    return keys.as_markup()


def key_returner_selected(items, table_name, current_page, all_pages, selected):
    keys = InlineKeyboardBuilder()
    for item in items:
        if selected == item['lesson_number']:
            keys.add(
                InlineKeyboardButton(
                    text=f"[ {item['lesson_number']} ]",
                    callback_data=f"id:{item['lesson_number']}:{current_page}:{table_name}"
                )
            )
        else:
            keys.add(
                InlineKeyboardButton(
                    text=f"{item['lesson_number']}",
                    callback_data=f"id:{item['lesson_number']}:{current_page}:{table_name}"
                )
            )
    keys.row(
        InlineKeyboardButton(
            text="◀️",
            callback_data=f"prev:{current_page}:{table_name}"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"alertmessage:{current_page}:{table_name}"
        ),
        InlineKeyboardButton(
            text="▶️",
            callback_data=f"next:{current_page}:{table_name}"
        )
    )
    return keys.as_markup()


def key_returner_articles(current_page, all_pages):
    keys = InlineKeyboardBuilder()
    keys.row(
        InlineKeyboardButton(
            text="◀️",
            callback_data=f"prev_articles:{current_page}"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"alertarticles:{current_page}"
        ),
        InlineKeyboardButton(
            text="▶️",
            callback_data=f"next_articles:{current_page}"
        )
    )
    return keys.as_markup()


def key_returner_projects(items, current_page, all_pages):
    keys = InlineKeyboardBuilder()
    for item in items:
        keys.add(
            InlineKeyboardButton(
                text=f"{item['rank']}",
                callback_data=f"projects:{item['id']}"
            )
        )
    keys.adjust(5)
    keys.row(
        InlineKeyboardButton(
            text="◀️",
            callback_data=f"prev_projects:{current_page}:{all_pages}"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"alert_projects:{current_page}"
        ),
        InlineKeyboardButton(
            text="▶️",
            callback_data=f"next_projects:{current_page}:{all_pages}"
        )
    )
    return keys.as_markup()

# async def tables_menu(callback_text):
#     all_tables = await db.select_all_tables()
#
#     builder = keyboard.InlineKeyboardBuilder()
#
#     for table in all_tables:
#         builder.add(
#             InlineKeyboardButton(
#                 text=f"{table['table_name']}", callback_data=f"{callback_text}_{table['id']}"
#             )
#         )
#     builder.adjust(1)
#     return builder.as_markup()
