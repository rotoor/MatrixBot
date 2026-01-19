from aiogram import Router #full ???
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from utils.matrix_ops import parse_matrix, transpose

matrix_router = Router()

class MatrixFSM(StatesGroup):
    waiting_matrix = State()

# Нажали кнопку "transpose"
@matrix_router.callback_query(lambda c: c.data == "transpose")
async def transpose_button(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MatrixFSM.waiting_matrix)
    await callback.message.answer(
        "Send matrix:\nRows — new line\nNumbers — space"
    )
    await callback.answer()


# Прислали матрицу
@matrix_router.message(MatrixFSM.waiting_matrix)
async def handle_matrix(message: Message, state: FSMContext):
    try:
        matrix = parse_matrix(message.text)
        result = transpose(matrix)

        text = "\n".join(
            " ".join(map(str, row)) for row in result
        )

        await message.answer(f"Result:\n{text}")

    except ValueError:
        await message.answer("Wrong matrix format")

    await state.clear()