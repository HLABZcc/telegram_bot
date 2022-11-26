import telebot
from telebot import types

bot = telebot.TeleBot('       ')

name = ''
age = 0
rost = 0
we = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Send Bot 'Hi'")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Hi' or message.text == 'hi':
        bot.send_message(message.from_user.id, 'Hello! What is your name?')
        bot.register_next_step_handler(message, bname)


def bname(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, name + 'How tall are you? For example: 1.60')
    bot.register_next_step_handler(message, brost)


def brost(message):
    global rost
    try:
        rost = float(message.text)
        bot.send_message(message.from_user.id, name + 'What is your weight?')
        bot.register_next_step_handler(message, bwe)
    except Exception:
        bot.send_message(message.from_user.id, name + 'How tall are you? For example: 1.60')
        bot.register_next_step_handler(message, brost)


def bwe(message):
    global we
    try:
        we = float(message.text)
        bmi = int(we) / float(rost) ** 2
        bmi = round(bmi, 1)

        if bmi < 18.5:
            bot.send_message(message.from_user.id, name+', your weight index = ' + str(bmi)+'\nYou, below the normal weight.')
        elif 18.5 <= bmi < 25:
            bot.send_message(message.from_user.id, name+', your weight index = ' + str(bmi)+'\nYou have a normal weight.')
        elif 25 <= bmi < 30:
            bot.send_message(message.from_user.id, name+', your weight index = ' + str(bmi)+'\nYou are overweight.')
        elif 30 <= bmi < 35:
            bot.send_message(message.from_user.id, name+', your weight index = ' + str(bmi)+'\nYou have first-degree obesity.')
        elif 35 <= bmi < 40:
            bot.send_message(message.from_user.id, name+', your weight index = ' + str(bmi)+'\nYou have Grade II obesity.')
        elif 40 <= bmi:
            bot.send_message(message.from_user.id, name+', your weight index = ' + str(bmi)+'\nYou have Grade III obesity.')

        bot.send_message(message.from_user.id, "\n_________________\nSend 'Hi' to start over")
    except Exception:
        bot.send_message(message.from_user.id, name + ', What is your weight? 55')
        bot.register_next_step_handler(message, bwe)


bot.polling()
