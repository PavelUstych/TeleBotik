import modules.creating_buttons as c_buttons
import telebot

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.add(c_buttons.button_new)
keyboard.add(c_buttons.button_sale)
keyboard.add(c_buttons.button_discounts)