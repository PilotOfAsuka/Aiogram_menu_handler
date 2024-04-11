from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from misc import dp
from menu.menu import main_menu_keyboard, scrath_menu_keyboard, main_menu_list
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


async def back_button_handler(callback, user_id, states, mess_id, mess_text, r_markup):
    if callback.data == "to_back":
        if user_state.user_states.get(user_id) in states:
            await callback.message.edit_text(inline_message_id=mess_id, text=mess_text,
                                             reply_markup=r_markup)


async def menu_button_handler(callback, mess_id, mess_text, r_markup, user_id):
    await callback.message.edit_text(inline_message_id=mess_id, text=mess_text,
                                     reply_markup=r_markup)
    user_state.set_state(user_id, state=callback.data)
    pass


@dp.callback_query()
async def menu_handler(callback: CallbackQuery):
    message_id = str(callback.message.message_id)
    user_id = str(callback.from_user.id)

    await back_button_handler(callback=callback,
                              user_id=user_id,
                              mess_id=message_id,
                              states=main_menu_list,
                              mess_text="Главное меню",
                              r_markup=main_menu_keyboard)

    if callback.data in main_menu_list:
        if callback.data == main_menu_list[0]:
            await menu_button_handler(callback=callback,
                                      mess_id=message_id,
                                      user_id=user_id,
                                      r_markup=scrath_menu_keyboard,
                                      mess_text=main_menu_list[0],
                                      )


    pass



