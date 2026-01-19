from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
from keyboards.menu import menu

user_router = Router()


@user_router.message(CommandStart())
@user_router.message(Command("menu"))
async def cmd_start(message: Message):
    await message.answer(
        "Choose an action:",
        reply_markup=menu)
