from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_main_dkb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Media bo'limi"),
            KeyboardButton(text="Foydalanuvchilar bo'limi")
        ],
        [
            KeyboardButton(text="Bosh sahifa")
        ]
    ],
    resize_keyboard=True
)


admin_lessons_dkb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yangi dars qo'shish"),
            KeyboardButton(text="Dars nomini o'zgartirish")
        ],
        [
            KeyboardButton(text="Darsni o'chirish"),
            KeyboardButton(text="Dars ro'yxatini ko'rish")
        ],
        [
            KeyboardButton(text="Admin paneliga qaytish")
        ]
    ],
    resize_keyboard=True
)
