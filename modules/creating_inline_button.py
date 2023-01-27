import telebot
inline_bt = telebot.types.InlineKeyboardButton(text= "Замовити", callback_data = "замовити")

inline_bt1 = telebot.types.InlineKeyboardButton(
    text= "Перейти до сайту", 
    url = "https://rozetka.com.ua/zte-zte-v40-6-128gb-blue/p357873492/"
)
inline_bt2 = telebot.types.InlineKeyboardButton(
    text = "Перейти до сайту", 
    url = "https://rozetka.com.ua/apple_iphone_13_128gb_midnight/p318463663/"
)
inline_bt3 = telebot.types.InlineKeyboardButton(
    text = "Перейти до сайту",
    url = "https://rozetka.com.ua/motorola-950888/p361481661/"
)
inline_bt4 = telebot.types.InlineKeyboardButton(
    text = "Перейти до сайту",
    url = "https://rozetka.com.ua/samsung-sm-m135flbdsek/p347516328/"
)
inline_bt5 = telebot.types.InlineKeyboardButton(
    text = "Перейти до сайту",
    url = "https://rozetka.com.ua/nokia_719901148421/p294450473/"
)

inline_list_button = []
inline_list_button.append(1)
inline_list_button.append(1)
inline_list_button.append(1)
inline_list_button.append(1)
inline_list_button.append(1)
inline_list_button.append(inline_bt1)
inline_list_button.append(inline_bt2)
inline_list_button.append(inline_bt3)
inline_list_button.append(inline_bt4)
inline_list_button.append(inline_bt5)
