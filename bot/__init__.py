import telebot

bot=telebot.TeleBot('6747087696:AAEv_H_IiVg_Q-bS40ceekhRuULj5xpkhgc')


@bot.message_handler(commands=['start'])

def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Меня зовут Alice, я являюсь простейшим чатботом. Мои умения заканчиваются на приветствии и прощании с Вами. Напишите мне "пока", чтобы попрощаться!!!')

@bot.message_handler()
def info(message):
    if message.text.lower()== 'пока':
        bot.reply_to(message, f'До свидания,  {message.from_user.first_name}!')
    elif message.text.lower()== 'привет':
        bot.reply_to(message, f'Привет,  {message.from_user.first_name}!')




bot.polling(none_stop=True)