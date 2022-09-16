import telebot
from telebot import types

bot = telebot.TeleBot("1962353179:AAGnamAnCNgOLsKrlsgssejjRKQQB3mZMvU")


def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('ОГЭ')
    button2 = types.KeyboardButton('ЕГЭ')
    button3 = types.KeyboardButton('Устный русский')
    button4 = types.KeyboardButton('Итоговое сочинение(изложение)')
    markup.add(button1, button2, button3, button4)
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Привет, ученик, что тебе надо из нижеперечисленного:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Ученик, что тебе надо из нижеперечисленного:', reply_markup=markup)


def oge(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn01 = types.KeyboardButton('/menu')
    markup.add(itembtn01)
    bot.send_message(message.chat.id, 'Вот тебе информация по ОГЭ', reply_markup=markup)


def ege(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn01 = types.KeyboardButton('/menu')
    markup.add(itembtn01)
    bot.send_message(message.chat.id, 'Вот тебе информация по ОГЭ', reply_markup=markup)


def sochinenie(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn01 = types.KeyboardButton('/menu')
    markup.add(itembtn01)
    bot.send_message(message.chat.id, 'Держи информацию по поводу сочинеия', reply_markup=markup)


def ystni(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn01 = types.KeyboardButton('/menu')
    markup.add(itembtn01)
    bot.send_message(message.chat.id, 'Держи информацию по поводу устного русского', reply_markup=markup)


def vibor(message):
    if message.text == 'ОГЭ':
        oge(message)
    if message.text == 'ЕГЭ':
        ege(message)
    if message.text == 'Итоговое сочинение(изложение)':
        sochinenie(message)
    if message.text == 'Устный русский':
        ystni(message)
