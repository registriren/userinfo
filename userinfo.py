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
        #type_upd = bot.get_update_type(last_update)
        chat_id = bot.get_chat_id(last_update)
        user_id = bot.get_user_id(last_update)
        name = bot.get_name(last_update)
        link_userid = bot.get_link_user_id(last_update)
        link_name = bot.get_link_name(last_update)
        link_chatid = bot.get_link_chat_id(last_update)

        if link_userid != None:
            bot.send_message('forward name: {}\nforward user_id: {}\nforward chat_id: {}\n'.format(link_name, link_userid, link_chatid), chat_id)
        elif link_chatid != None:
            bot.send_message('forward name: {}\nforward user_id: {}\nforward chat_id: {}\n'.format(link_name, link_userid, link_chatid), chat_id)
        else:    
            bot.send_message('name: {}\nuser_id: {}\nchat_id: {}\n'.format(name, user_id, chat_id), chat_id)
        bot.send_message('полная структура ответа GetUpdates:\n{}'.format(str(last_update)), chat_id)
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
