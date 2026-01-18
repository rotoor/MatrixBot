import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Message

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        import asyncio

        asyncio.run(main())
    except KeyboardInterrupt:
        pass
