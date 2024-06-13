from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from loader import db


interviews_cbuttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="⬅️ Ortga"
            )
        ],
        [
            KeyboardButton(
                text="🏡 Bosh sahifa"
            )
        ]
    ],
    resize_keyboard=True
)
