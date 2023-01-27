import modules.creating_bot as c_bot
import modules.file_search_path as s_path
import modules.creating_inline_keyboard as c_inline_keyboard

def send_message_user(message):
    if message.text.lower() == "new" or message.text.lower() == "sale" or message.text.lower() == "discounts":
        path_file = s_path.path_search("images/1.jpeg")
        c_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Телефон ZTE",
            reply_markup= c_inline_keyboard.inline_keyboard1
        )
        path_file = s_path.path_search("images/2.jpeg")
        c_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Телефон iPhone",
            reply_markup= c_inline_keyboard.inline_keyboard2
        )
        path_file = s_path.path_search("images/3.jpeg")
        c_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Телефон Motorola",
            reply_markup= c_inline_keyboard.inline_keyboard3
        )
        path_file = s_path.path_search("images/4.jpeg")
        c_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Телефон Samsung Galaxy",
            reply_markup= c_inline_keyboard.inline_keyboard4
        )
        path_file = s_path.path_search("images/5.jpeg")
        c_bot.bot.send_photo(
            message.chat.id,
            open(path_file, "rb"),
            "Телефон Nokia",
            reply_markup= c_inline_keyboard.inline_keyboard5
        )