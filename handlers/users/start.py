from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.client.session.middlewares.request_logging import logger
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
    await message.answer(f"Assalomu alaykum {full_name}!\n\nBotimizga xush kelibsiz!", reply_markup=main_dkb)


@router.message(F.text == "🏡 Bosh sahifa")
async def back_main_menu(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=main_dkb
    )


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
# pandas==2.1.0
