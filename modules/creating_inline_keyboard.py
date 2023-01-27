import telebot
import modules.creating_inline_button as c_inline_bt
import modules.creating_bot as c_bot


inline_list_keyboards = []

count = 0

for el in range(0, 10):
    if count <= 5:
        inline_keyboard = telebot.types.InlineKeyboardMarkup(row_width= 2)
        inline_list_keyboards.append(inline_keyboard)
    if count > 5 and count <= 10:
        for el in inline_list_keyboards:
            el.add(c_inline_bt.inline_bt, c_inline_bt.inline_list_button[count])
    count+= 1