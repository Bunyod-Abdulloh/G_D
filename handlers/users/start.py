from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.client.session.middlewares.request_logging import logger

from handlers.functions.functions_one import extracter
from keyboards.inline.buttons import key_returner
from keyboards.reply.main_dkb import main_dkb
from loader import db

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    telegram_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    try:
        await db.add_user(telegram_id=telegram_id, full_name=full_name, username=username)
    except Exception as error:
        logger.info(error)
    await message.answer(f"Assalomu alaykum {full_name}! Botimizga xush kelibsiz!", reply_markup=main_dkb)


@router.message(F.text == "salom")
async def samplerr(message: types.Message):
    # checker = await check_channel_subscription(
    #     user_id=message.from_user.id, channel_id=channels_list[0]
    # )
    # if checker:
    #     print("Sizga dars ochiq")
    # else:
    #     print("Siz darsga ro'yxatdan o'tmagansiz! Admin bilan bog'laning")
    await db.alter_type()
    print("o'zgardi")


@router.message(F.photo | F.audio | F.video | F.document | F.voice)
async def get_media(message: types.Message):
    if message.photo:
        await message.answer(
            text=f"<code>{message.photo[-1].file_id}</code>"
        )
    if message.audio:
        await message.answer(
            text=f"<code>{message.audio.file_id}</code>"
        )
    if message.video:
        await message.answer(
            text=f"<code>{message.video.file_id}</code>"
        )
    if message.document:
        await message.answer(
            text=f"<code>{message.document.file_id}</code>"
        )
    if message.voice:
        await message.answer(
            text=f"<code>{message.voice.file_id}</code>"
        )