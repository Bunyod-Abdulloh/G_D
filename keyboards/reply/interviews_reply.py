from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

interviews_cbuttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="⬅️ Ortga"
            ),
            KeyboardButton(
                text="🏡 Bosh sahifa"
            )
        ]
    ],
    resize_keyboard=True
)
