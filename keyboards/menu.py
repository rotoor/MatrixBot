from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Transpose', callback_data='transpose')],
        [InlineKeyboardButton(text='Determinant', callback_data='determinant')],
        [InlineKeyboardButton(text='Add',callback_data='add')],
        [InlineKeyboardButton(text='Multiply',callback_data='multiply')],
        [InlineKeyboardButton(text='Inverse',callback_data='inverse')]
    ]
)