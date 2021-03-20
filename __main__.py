import telebot
import matplotlib.pyplot as plt
from telebot import types
import time
import matplotlib
import mysql.connector
import cairo
import io
from PIL import Image

bot = telebot.TeleBot('1707466910:AAHPoEcNJkLJ3au0fj_BMlBwH3cnC4L3Fqs')
keyboard1 = telebot.types.ReplyKeyboardMarkup()

keyboard1.row('Графики', 'Формулы')

@bot.message_handler(commands=['start'])
def start_message(message):
    stike = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, stike)
    bot.send_message(message.chat.id, 'Салам малейкум', reply_markup=keyboard1)
    bot.edit_message_reply_markup(False)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text.lower().strip() == "графики":
        # Пишем приветствие

        bot.send_message(message.chat.id, "Witch func do you want?")

        keyboard = types.InlineKeyboardMarkup()

        key_lineykx = types.InlineKeyboardButton(text='Line | y = kx', callback_data='lineFunc')

        # И добавляем кнопку на экран
        keyboard.add(key_lineykx)
        key_lineykxb = types.InlineKeyboardButton(text='Линейная | y = kx + b', callback_data='zodiac')
        keyboard.add(key_lineykxb)
        key_yx2 = types.InlineKeyboardButton(text='Квадратичная | y = x^2', callback_data='zodiac')
        keyboard.add(key_yx2)
        key_yx2bxc = types.InlineKeyboardButton(text='Квадратичная | y = ax^2 + bx + c', callback_data='zodiac')
        keyboard.add(key_yx2bxc)
        key_yx3 = types.InlineKeyboardButton(text='Степенная | y = x^3', callback_data='zodiac')
        keyboard.add(key_yx3)
        key_yx12 = types.InlineKeyboardButton(text='Степенная | y = x^1/2', callback_data='zodiac')
        keyboard.add(key_yx12)
        key_stepykx = types.InlineKeyboardButton(text='Степенная | y = k/x', callback_data='zodiac')
        keyboard.add(key_stepykx)
        key_yex = types.InlineKeyboardButton(text='Показательная | y = e^x', callback_data='zodiac')
        keyboard.add(key_yex)
        key_yax = types.InlineKeyboardButton(text='Показательная | y = a^x', callback_data='zodiac')
        keyboard.add(key_yax)
        key_ylnx = types.InlineKeyboardButton(text='Логарифмическая | y = lnx', callback_data='zodiac')
        keyboard.add(key_ylnx)
        key_ylogax = types.InlineKeyboardButton(text='Логарифмическая | y = logax', callback_data='zodiac')
        keyboard.add(key_ylogax)
        key_ysinx = types.InlineKeyboardButton(text='Синус | y = sinx', callback_data='zodiac')
        keyboard.add(key_ysinx)
        key_ycosx = types.InlineKeyboardButton(text='Косинус | y = cosx', callback_data='zodiac')
        keyboard.add(key_ycosx)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.chat.id, text='Выбери функцию для построения', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Напиши Привет")
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "lineFunc":
            operator(message)


def operator(message):
    msg = bot.send_message(message.chat.id, 'Введи данные в формате  >>  y  =  k  *  x. Например  -  (5  =  1  *  5)') #reply_markup= )
    #bot.send_message(message.from_user.id, 'Введи данные в формате  >>  y  =  k  *  x. Например  -  (5  =  1  *  5)')
    bot.register_next_step_handler(msg, graph)
    print(msg.text)

def graph(msg):
    mes = msg.text.split(' ')
    print(msg)
    try:
        y = float(mes[0])
        k = float(mes[2])
        x = float(mes[4])
        isX = abs(y) * 1.2
        print(mes)
        plt.figure()
        plt.axis([-isX, isX, -isX, isX])
        plt.grid(True)
        plt.plot((x, -x), (y, -y))
        plt.plot([x, -x], [y, -y], 'ro')
        plt.plot((0, 0), (isX, -isX), color='#ff7f0e')
        plt.plot((-isX, isX), (0, 0), color='#ff7f0e')
        plt.ylabel('Линейная функция')
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        im = Image.open(buf)
        im.show()
        buf.close()
        bot.send_photo(msg.chat.id, photo=im)
    except ValueError:
        bot.send_message(msg.chat.id, 'Пошел нахуй')
    except IndexError:
        bot.send_message(msg.chat.id, 'Пошел нахуй')

bot.polling(none_stop=True, interval=0)

while True:
    time.sleep(1)

