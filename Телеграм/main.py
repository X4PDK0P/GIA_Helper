from Add1 import *


@bot.message_handler(commands=['start', 'menu'])
def hello(message):
    menu(message)


@bot.message_handler(content_types='text')
def main(massege):
    vibor(massege)


bot.polling(none_stop=True)
