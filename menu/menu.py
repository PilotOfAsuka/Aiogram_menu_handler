from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def generate_inline_keyboard_markup(buttons_list, back_button=False):
    menu_buttons = [[InlineKeyboardButton(text=button, callback_data=button)] for button in buttons_list]
    if back_button:
        menu_buttons.append([InlineKeyboardButton(text="Назад", callback_data="to_back")])
        pass
    menu_keyboard = InlineKeyboardMarkup(inline_keyboard=menu_buttons)
    return menu_keyboard


def generate_keyboards_dictanary(in_menu_button_list, to_menu_button_list):
    keyboards_dictanary = {}
    for button_label, submenu_buttons in zip(in_menu_button_list, to_menu_button_list):
        keyboards_dictanary[button_label] = submenu_buttons
    return keyboards_dictanary
    pass


main_menu_buttons_list = [
    "Menu1",
    "Menu2",
    "Menu3",
    "Menu4"
]

menu1_buttons_list = [
    "Test_button1_in_menu1",
    "Test_button2_in_menu1"
]

menu2_buttons_list = [
    "Test_button1_in_menu2",
    "Test_button2_in_menu2"
]

menu1_submenu1_buttons_list = [
    "Test_button1_in_submenu1",
    "Test_button2_in_submenu1"
]

main_menu_keyboards_list = [
    generate_inline_keyboard_markup(menu1_buttons_list, back_button=True),
    generate_inline_keyboard_markup(menu2_buttons_list, back_button=True)
]

menu1_submenu_keyboards_list = [
    generate_inline_keyboard_markup(menu1_submenu1_buttons_list, back_button=True)
]

main_menu_keyboard = generate_inline_keyboard_markup(main_menu_buttons_list)


main_menu_keyboards_dictanary = generate_keyboards_dictanary(main_menu_buttons_list, main_menu_keyboards_list)

menu1_keyboards_dictanary = generate_keyboards_dictanary(menu1_buttons_list, menu1_submenu_keyboards_list)

