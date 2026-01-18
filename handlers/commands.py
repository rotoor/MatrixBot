from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart, Command
from keyboards.menu import menu

user = Router()


@user.message(CommandStart())
@user.message(Command("menu"))
async def cmd_start(message: Message):
    await message.answer(
        "Choose an action:",
        reply_markup=menu)
