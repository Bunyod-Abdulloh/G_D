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
    all_tables = await db.select_all_tables()
    extract = extracter(all_medias=all_tables, delimiter=10)
    current_page = 1
    all_pages = len(extract)
    items = extract[current_page - 1]
    key = key_returner(
        items=items, current_page=current_page, all_pages=all_pages
    )
    text = str()
    for n in items:
        text += f"{n['table_number']}. {n['table_name']}\n"
    try:
        await db.add_user(telegram_id=telegram_id, full_name=full_name, username=username)
    except Exception as error:
        logger.info(error)
    await message.answer(f"Assalomu alaykum {full_name}! Botimizga xush kelibsiz!", reply_markup=main_dkb)
    await message.answer(text=text, reply_markup=key)


@router.callback_query(F.data.startswith("next:"))
async def start_next_page(call: types.CallbackQuery):
    await call.answer(cache_time=0)
    current_page = int(call.data.split(':')[1])
    tables = await db.select_all_tables()
    extract = extracter(all_medias=tables, delimiter=10)
    len_extract = len(extract)

    if current_page == len_extract:
        current_page = 1
    else:
        current_page += 1
    items = extract[current_page - 1]
    key = key_returner(
        items=items, current_page=current_page, all_pages=len(extract)
    )
    text = str()
    for n in items:
        text += f"{n['table_number']}. {n['table_name']}\n"
    await call.message.edit_text(
        text=text, reply_markup=key
    )


channels_list = [-1001917132582]


@router.callback_query(F.data.startswith("prev:"))
async def start_prev_page(call: types.CallbackQuery):
    await call.answer(cache_time=0)
    current_page = int(call.data.split(':')[1])
    tables = await db.select_all_tables()
    extract = extracter(all_medias=tables, delimiter=10)
    len_extract = len(extract)
    if current_page == 1:
        current_page = len_extract
    else:
        current_page -= 1
    items = extract[current_page - 1]
    key = key_returner(
        items=items, current_page=current_page, all_pages=len(extract)
    )
    text = str()
    for n in items:
        text += f"{n['table_number']}. {n['table_name']}\n"
    await call.message.edit_text(
        text=text, reply_markup=key
    )


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


@router.message(F.photo | F.audio | F.video | F.document)
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
