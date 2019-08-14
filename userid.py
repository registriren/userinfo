#!/usr/bin/python
# -*- coding: utf-8 -*-


from botapitamtam import BotHandler
import json

config = 'config.json'
with open(config, 'r', encoding='utf-8') as c:
    conf = json.load(c)
    token = conf['access_token']

bot = BotHandler(token)

def main():

    while True:
        last_update = bot.get_updates()
        if last_update == None: #проверка на пустое событие, если пусто - возврат к началу цикла
            continue
        type_upd = bot.get_update_type(last_update)
        chat_id = bot.get_chat_id(last_update)
        user_id = bot.get_user_id(last_update)
        
        bot.send_message('user_id: {}\nchat_id: {}\ntype: {}'.format(user_id, chat_id, type_upd), chat_id)
        
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
