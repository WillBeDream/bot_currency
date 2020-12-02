from settings.SETTINGS import *
from parse.Parse import Parse 
from parse.dataPy import Data 



@BOT.message_handler(commands = ["start"])
def start_message(message):
    BOT.send_message(message.chat.id, "Что вас интересует", reply_markup = KEYBOARD_START)

@BOT.message_handler(content_types = ["text"])
def get_text_messages(message):
    
    global site,values

    if message.text == BUTTON_USD:
        site = Parse(URL_USD).get_content()        
        BOT.send_message(message.chat.id, "Что вас интересует", reply_markup = KEYBOARD_CHOICE)
    
    elif message.text == BUTTON_EUR:
        site = Parse(URL_EUR).get_content()
        BOT.send_message(message.chat.id, "Что вас интересует", reply_markup = KEYBOARD_CHOICE)


    elif message.text == BUTTON_GET_ALL_LIST:
        values = Data(site) 
        BOT.send_message(message.chat.id, values.get_all_list(), reply_markup = KEYBOARD_CHOICE)

    elif message.text == BUTTON_BEST_BUY_VALUE:
        values = Data(site) 
        BOT.send_message(message.chat.id, values.get_best_bye_value(), reply_markup = KEYBOARD_CHOICE)

    elif message.text == BUTTON_BEST_SELL_VALUE:
        values = Data(site) 
        BOT.send_message(message.chat.id, values.get_best_sell_value(), reply_markup = KEYBOARD_CHOICE)

    elif message.text == BUTTON_START:
        start_message(message)
    

    else:
        BOT.send_message(message.chat.id, "я тебя не понимаю! Напиши, пожалуйста, /start")


BOT.polling()

