from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_inline_keyboard_markup(buttons_list, back_button=False):
    menu_buttons = [[InlineKeyboardButton(text=button, callback_data=button)] for button in buttons_list]
    if back_button:
        menu_buttons.append([InlineKeyboardButton(text="Назад", callback_data="to_back")])
        pass
    menu_keyboard = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    return menu_keyboard


main_menu_list = [
    "Меню1",
    "Меню2",
    "Меню3",
    "Меню4"
]

scrath_menu_list = [
    "Тест0",
    "Тест1"
]

main_menu_keyboard = generate_inline_keyboard_markup(main_menu_list)
scrath_menu_keyboard = generate_inline_keyboard_markup(scrath_menu_list, back_button=True)




