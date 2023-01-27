import modules.creating_bot as c_bot

@c_bot.bot.callback_query_handler(func= lambda callback: callback.data)

def request_processing(callback):
    if callback.data == "замовити":
        c_bot.bot.send_message(
            callback.message.chat.id,
            "Замовлення прийнято до обробки\nОчікуйте зворотній зв'язок"
        )