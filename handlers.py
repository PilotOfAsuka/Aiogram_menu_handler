from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from misc import dp
from menu.menu import *
from modules import user_state


@dp.message(Command("start"))
async def start_handler(msg: Message):
    user_name = msg.from_user.username
    user_id = str(msg.from_user.id)
    # Отправляем приветственное сообщение
    await msg.answer(text=f"Главное меню", reply_markup=main_menu_keyboard)
    user_state.set_state(user_id, state="main_menu")


@dp.message()
async def message_handler(msg: Message):
    user_name = msg.from_user.username
    msg_text = msg.text
    await msg.answer(f"Сообщение от {user_name}, {msg_text}")


async def back_button_handler(callback, user_id, if_states, mess_id, mess_text, r_markup):  # TODO
    if callback.data == "to_back" and user_state.user_states.get(user_id) != "main_menu":
        if user_state.user_states.get(user_id) in if_states:
            await callback.message.edit_text(inline_message_id=mess_id, text=mess_text,
                                             reply_markup=r_markup)
            user_state.set_state(user_id, state="main_menu")


async def menu_button_handler(callback, mess_id, keyboard_dictanary, user_id, button_list):
    if callback.data in button_list:
        await callback.message.edit_text(inline_message_id=mess_id, text=callback.data,
                                         reply_markup=keyboard_dictanary.get(callback.data))
        user_state.set_state(user_id, state=callback.data)
        pass


@dp.callback_query()
async def menu_handler(callback: CallbackQuery):
    message_id = str(callback.message.message_id)
    user_id = str(callback.from_user.id)

    await back_button_handler(callback=callback, user_id=user_id, mess_id=message_id,
                              if_states=main_menu_buttons_list, mess_text="Главное меню", r_markup=main_menu_keyboard)
    await back_button_handler(callback=callback, user_id=user_id, mess_id=message_id,
                              if_states=menu1_buttons_list, mess_text="Главное меню", r_markup=main_menu_keyboard)

    await menu_button_handler(callback=callback, mess_id=message_id, user_id=user_id,
                              button_list=main_menu_buttons_list, keyboard_dictanary=main_menu_keyboards_dictanary)

    await menu_button_handler(callback=callback, mess_id=message_id, keyboard_dictanary=menu1_keyboards_dictanary, user_id=user_id, button_list=menu1_buttons_list)