from aiogram import Router  # full ???
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from utils.matrix_ops import *

matrix_router = Router()


class MatrixFSM(StatesGroup):
    waiting_first_matrix = State()
    waiting_second_matrix = State()


@matrix_router.callback_query(lambda c: c.data == "transpose")
async def transpose_button(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MatrixFSM.waiting_first_matrix)
    await state.update_data(operation="transpose")
    await callback.message.answer("Send matrix:\nRows — new line\nNumbers — space")
    await callback.answer()


@matrix_router.callback_query(lambda c: c.data == "determinant")
async def determinant_button(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MatrixFSM.waiting_first_matrix)
    await state.update_data(operation="determinant")
    await callback.message.answer("Send matrix:\nRows — new line\nNumbers — space")
    await callback.answer()


@matrix_router.callback_query(lambda c: c.data == "inverse")
async def inverse_button(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MatrixFSM.waiting_first_matrix)
    await state.update_data(operation="inverse")
    await callback.message.answer("Send matrix:\nRows — new line\nNumbers — space")
    await callback.answer()


@matrix_router.callback_query(lambda c: c.data == "add")
async def add_button(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MatrixFSM.waiting_first_matrix)
    await state.update_data(operation="add")
    await callback.message.answer(
        "Send first matrix:\nRows — new line\nNumbers — space"
    )
    await callback.answer()


@matrix_router.callback_query(lambda c: c.data == "multiply")
async def multiply_button(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MatrixFSM.waiting_first_matrix)
    await state.update_data(operation="multiply")
    await callback.message.answer(
        "Send first matrix:\nRows — new line\nNumbers — space"
    )
    await callback.answer()


@matrix_router.message(MatrixFSM.waiting_first_matrix)
async def handle_first_matrix(message: Message, state: FSMContext):
    try:
        matrix = parse_matrix(message.text)
        data = await state.get_data()
        operation = data["operation"]

        if operation == "transpose":
            result = transpose(matrix)
            text = "\n".join(" ".join(map(str, row)) for row in result)
            await message.answer(f"Result:\n{text}")
            await state.clear()
            return

        if operation == "determinant":
            result = determinant(matrix)
            await message.answer(f"Result:\n{result}")
            await state.clear()
            return

        if operation == "inverse":
            result = inverse(matrix)
            text = "\n".join(" ".join(map(str, row)) for row in result)
            await message.answer(f"Result:\n{text}")
            await state.clear()
            return

        await state.update_data(matrix1=matrix)
        await state.set_state(MatrixFSM.waiting_second_matrix)
        await message.answer("Send second matrix:\nRows — new line\nNumbers — space")

    except ValueError as e:
        await message.answer(f"Error: {e}\nTry again:")


@matrix_router.message(MatrixFSM.waiting_second_matrix)
async def handle_second_matrix(message: Message, state: FSMContext):
    try:
        data = await state.get_data()
        matrix1 = data["matrix1"]
        operation = data["operation"]
        matrix2 = parse_matrix(message.text)

        if operation == "add":
            result = add(matrix1, matrix2)
        elif operation == "multiply":
            result = multiply(matrix1, matrix2)
        else:
            raise ValueError("Unknown operation")

        text = "\n".join(" ".join(map(str, row)) for row in result)
        await message.answer(f"Result:\n{text}")
        await state.clear()

    except ValueError as e:
        await message.answer(
            f"Error: {e}\n" "Send second matrix again or choose another operation."
        )
