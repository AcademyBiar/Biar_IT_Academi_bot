import telebot
from telebot.types import ReplyKeyboardMarkup
import sqlite3

bot = telebot.TeleBot('6586474561:AAFBDSvUjnXsL85bYwH42oLKbvH7sf7-p3M')


@bot.message_handler()
def start(message):
    if message.text == '/start':
        menu1 = ReplyKeyboardMarkup(resize_keyboard=True)
        menu1.row('Ответы на частые вопросы')
        menu1.row('Получить уроки бесплатно')
        menu1.row('Акции и скидки')
        menu1.row('Получить подарок')
        bot.send_message(message.chat.id, 'Я- бот European IT Academy Biar. Помогу:'
                                          'Найти ответы на вопросы.'
                                          'Выбрать и оплатить курс.'
                                          'Что вас интересует?', reply_markup=menu1)

        def create_table_user():
            con = sqlite3.connect('sqlite.db')
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS users ('
                        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                        'first_name varchar,'
                        'user_name varchar,'
                        'user_id varchar)')
            cur.execute(f'''INSERT INTO users (first_name, user_name, user_id)
            values('{message.from_user.first_name}','{message.from_user.username}', '{message.from_user.id}')''')
            # cur.execute('DROP TABLE users')
            con.commit()
            con.close()

        create_table_user()


bot.polling()
