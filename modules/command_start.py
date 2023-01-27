import modules.creating_bot as c_bot
import modules.creating_keyboard as c_keyboard
import modules.send_message as s_message

@c_bot.bot.message_handler(commands = ["start"])
def bot_start(message):
    c_bot.bot.send_message(
        message.chat.id,
        "Hi User!",
        reply_markup=c_keyboard.keyboard
    )
    c_bot.bot.register_next_step_handler(message, s_message.send_message_user)