import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers.commands import user_router
from handlers.matrix_handlers import matrix_router

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(user_router, matrix_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        import asyncio

        asyncio.run(main())
    except KeyboardInterrupt:
        pass
