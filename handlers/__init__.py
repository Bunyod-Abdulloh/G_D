from aiogram import Router

from filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import start, lessons_main_hr
    from .errors import error_handler
    from .admin import main

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    start.router.message.filter(ChatPrivateFilter(chat_type=["private"]))
    #  Users
    router.include_routers(start.router, error_handler.router, lessons_main_hr.lessons)
    # Admins
    router.include_routers(main.router)
    return router
