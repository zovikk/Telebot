import telebot
from telebot import types

bot = telebot.TeleBot("5655462618:AAFOlq_VrbgGBbFY9vlINBcKpEhDA_bUNyI", parse_mode=None)

# Клавиатура главного меню
keyboard1 = types.ReplyKeyboardMarkup(True, True)
item1 = types.KeyboardButton('Расписание 🗓')
item2 = types.KeyboardButton('Программы 💾')
item3 = types.KeyboardButton('О проекте  🛠')
keyboard1.add(item1, item2)
keyboard1.add(item3)
# Клавиатура раздела "О проекте"
keyboard2 = types.ReplyKeyboardMarkup(True, True)
item4 = types.KeyboardButton('💰 Поддержать проект 💰')
item5 = types.KeyboardButton('Назад')
keyboard2.add(item4, item5)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бета-версия парсера гороскопа', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'О проекте  🛠':
        bot.send_message(message.chat.id, 'Бета-версия парсера-гороскопа', reply_markup=keyboard2)
    elif message.text == 'Программы 💾':
        bot.send_message(message.chat.id, 'Здесь будет отображаться список програм для скачивания')
    elif message.text == 'Расписание 🗓':
        bot.send_message(message.chat.id, 'Здесь будет отображаться расписание занятий')
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Вы вышли в главное меню', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Назад':
        bot.send_message(message.chat.id, 'Вы вышли в главное меню', reply_markup=keyboard1)


bot.polling()