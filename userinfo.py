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
        name = bot.get_name(last_update)
        link_userid = bot.get_link_user_id(last_update)

        bot.send_message('name: {}\nuser_id: {}\nchat_id: {}\ntype: {}\nforward user_id: {}'.format(name, user_id, chat_id, type_upd, link_userid), chat_id)
        #bot.send_message(str(memb), chat_id)
        bot.send_message('полная структура ответа GetUpdates:\n{}'.format(str(last_update)), chat_id)
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
