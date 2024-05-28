from aiogram import Router, types, F
from aiogram.filters import Command
from data.config import ADMINS
from filters import IsBotAdminFilter
from keyboards.reply.admin_dkb import admin_main_dkb, admin_lessons_dkb

router = Router()


@router.message(IsBotAdminFilter(ADMINS), Command("admin"))
async def admin_main_router(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=admin_main_dkb
    )


@router.message(F.text == "Media bo'limi")
async def admin_media_main_router(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=admin_lessons_dkb
    )
