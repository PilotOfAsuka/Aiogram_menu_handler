from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_inline_keyboard_markup(buttons_list):
    menu_buttons = [[InlineKeyboardButton(text=button, callback_data=button)] for button in buttons_list]
    menu_keyboard = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    return menu_keyboard


main_menu_list = [
                "Test",
                "Test",
                "Test",
                "Test"
            ]

scrath_menu_list = [
    "test1",
    "test1"
]

main_menu_keyboard = generate_inline_keyboard_markup(main_menu_list)
scrath_menu_keyboard = generate_inline_keyboard_markup(scrath_menu_list)




