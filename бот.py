import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot('7140814157:AAEDoHUWzU932NDiHngsI2--x_CHIZzDlFQ')
API = '704cf6c1b5b3a14fc7df20ef044673f2'


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>, чтобы перейти в меню задач, нажми на эту кнопку /help'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    website = types.KeyboardButton('/website_lms')
    tg = types.KeyboardButton('/tg')
    th = types.KeyboardButton('/technical_support')
    wt = types.KeyboardButton('/weather')
    markup.add(website, tg, th, wt)
    bot.send_message(message.chat.id, 'Так как этот сайт для участника, то тут все необходимое для него:'
                                      '1) Сайт яндекс лицея '
                                      '2) Телеграмм, где мы обсуждаем всякие вопросики '
                                      '3) Наш преподаватель', reply_markup=markup)


@bot.message_handler(commands=['website_lms'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://lms.yandex.ru"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


@bot.message_handler(commands=['tg'])
def tg(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить телеграмм канал", url="https://t.me/+T2lLeu4Zol05ZmRi"))
    bot.send_message(message.chat.id, 'Наш телергамм канал', reply_markup=markup)


@bot.message_handler(commands=['technical_support'])
def th(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Напиши, если не боишься", url="https://t.me/DmitriyShein"))
    bot.send_message(message.chat.id, 'Телефон босса', reply_markup=markup)


@bot.message_handler(commands=['weather'])
def wt(message):
    mess = 'Введи название города'
    bot.send_message(message.chat.id, mess, parse_mode='html')

    @bot.message_handler(content_types=['text'])
    def get_weather(message):
        city = message.text.strip().lower()
        res = requests.get(F'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
        if res.status_code == 200:
            data = json.loads(res.text)
            bot.reply_to(message, f'Сейчас погода: {data["main"]["temp_min"]}')
        else:
            bot.reply_to(message, 'Город указан не верно')


bot.polling(none_stop=True)
