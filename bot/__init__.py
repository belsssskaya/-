import telebot
from telebot import types

bot=telebot.TeleBot('6747087696:AAEv_H_IiVg_Q-bS40ceekhRuULj5xpkhgc')


@bot.message_handler(commands=['start'])

def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Меня зовут Alice, я являюсь простейшим чатботом. Мои умения заканчиваются на приветствии и прощании с Вами. Чтобы перейти на умную версию меня, нажмите на кнопку "smart". Напишите мне "пока", чтобы попрощаться!!!')

@bot.message_handler(commands=['Пока'])

def info(message):
    bot.reply_to(message, f'До свидания,  {message.from_user.first_name}!')

@bot.message_handler(commands=['smart'])

def smart(message):
    bot.reply_to(message, f'На связи умный бот Alice! Я знаю отличные курсы по созданию телеграмм-ботов и веб-разработке. {message.from_user.first_name}, могу я Вам помочь?!')
@bot.message_handler(content_types=['text'])

def prod(message):
    markup=types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Связаться с моим разработчиком', url='https://vk.com/belskayaaaaaa'))
    markup.add(types.InlineKeyboardButton('Научиться создавать телеграмм-ботов', url='https://www.youtube.com/watch?v=ObwoMskHDoA&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&pp=iAQB'))
    markup.add(types.InlineKeyboardButton('Научиться создавать сайты', url='https://www.youtube.com/watch?v=UIKyAKC0ab8&list=PLNaJj8xMY1XQgYzVhLEFD4WSKqEhj4Sx1&pp=iAQB'))
    markup.add(types.InlineKeyboardButton('Далее', callback_data='enter'))

    bot.reply_to(message, "Хорошо! Выберите, что вам подходит больше... \n Нажмите 'Далее', если выбор сделан!", reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)

def callback_message(callback):
    if callback.data=='enter':
        bot.send_message(callback.message.chat.id, f'Отлично! Надеюсь вам будут полезны данные курсы! При возникновении вопросов, вы всегда можете обратиться к создателю бота...')












bot.polling(none_stop=True)