from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from loader import db


main_dkb = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="📚 Kurslar"),
        KeyboardButton(text="🎙 Suhbat va loyihalar")
    ],
    [
        KeyboardButton(text="📝 Maqolalar")
    ]],
    resize_keyboard=True,
    input_field_placeholder="Habaringizni kiriting..."
)
