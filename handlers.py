from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from misc import dp
from aiogram import F
from menu.menu import main_menu_keyboard, scrath_menu_keyboard, main_menu_list


@dp.message(Command("start"))
async def start_handler(msg: Message):
    user_name = msg.from_user.username
    user_id = str(msg.from_user.id)
    # Отправляем приветственное сообщение
    await msg.answer(text=f"Главное меню", reply_markup=main_menu_keyboard)


@dp.message()
async def message_handler(msg: Message):
    user_name = msg.from_user.username
    msg_text = msg.text
    await msg.answer(f"Сообщение от {user_name}, {msg_text}")


@dp.callback_query(F.data == main_menu_list[0])
async def main_menu_handler(callback: CallbackQuery):
    await callback.message.edit_reply_markup(inline_message_id=str(callback.message.message_id),
                                             reply_markup=scrath_menu_keyboard)
    pass

