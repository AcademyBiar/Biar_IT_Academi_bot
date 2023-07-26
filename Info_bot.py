import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot import types
import sqlite3

bot = telebot.TeleBot('6586474561:AAFBDSvUjnXsL85bYwH42oLKbvH7sf7-p3M')

menu1 = ReplyKeyboardMarkup(resize_keyboard=True)
menu1.row('Обучение.')
menu1.row('Консультация.')
menu1.row('Курсы.')
menu1.row('Вебинары.')
menu1.row('Получить скидку.')
menu1.row('Я студент и у меня есть вопрос.')
menu1.row('Хочу подарок!')
menu1.row('Это интересно.')
menu2 = ReplyKeyboardMarkup(resize_keyboard=True)
menu2.row('Основное меню.')


@bot.message_handler()
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Я - бот European IT Academy Biar. Помогу:'
                                          'Найти ответы на вопросы.'
                                          'Выбрать и оплатить курс.'
                                          'Что вас интересует?', reply_markup=menu1)

        # def create_table_user():
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
        # while True:
        bot.register_next_step_handler(message, choice)
        # create_table_user()


def choice(message):
    if message.text == 'Обучение.':
        bot.send_message(message.chat.id, 'Обучение\n'
                                          'Для начала обучения необходимо зарегистрироваться на сайте '
                                          '(через эл. почту/Google/Facebook). Выберите вариант обучения '
                                          '(light, standard, premium) и, следуя инструкциям на сайте, '
                                          'произведите оплату курса.​Обратите внимание, '
                                          'что зачисление денежных средств осуществляется в течение 3-5 дней.\n'
                                          '\nНачало занятий.\n'
                                          'После подтверждения оплаты выбранного вами курса, на вашу электронную почту'
                                          ' придет письмо-подтверждение и откроется доступ к курсу. Вы сможете '
                                          'открывать занятия на платформе и изучать материал в удобное для себя время.'
                                          '\n'
                                          '\nПрохождение занятий.\n'
                                          'Проходить занятия следует друг за другом. Для отработки полученных знаний, '
                                          'предлагаются практические задачи и домашние задания, выполнение которых '
                                          'обязательно для успешного освоения курса . Для положительной динамики '
                                          'обучения соблюдайте дедлайн (1 неделя) по выполнению домашних заданий.',
                         reply_markup=menu2)
        bot.register_next_step_handler(message, study)
    elif message.text == 'Консультация.':
        bot.send_message(message.chat.id, 'Text', reply_markup=menu2)
        bot.register_next_step_handler(message, consult)
    elif message.text == 'Курсы.':
        bot.send_message(message.chat.id, 'Text', reply_markup=menu2)
        bot.register_next_step_handler(message, course)
    elif message.text == 'Вебинары.':
        bot.send_message(message.chat.id, 'Text', reply_markup=menu2)
        choice_veb = types.InlineKeyboardMarkup()
        veb1 = types.InlineKeyboardButton(text='Гайд по изучению английского языка', url='https://www.radiorecord.ru/')
        veb2 = types.InlineKeyboardButton(text="Бесплатный урок английского", url='https://www.radiorecord.ru/')
        veb3 = types.InlineKeyboardButton(text='Гайд по изучению английского языка', url='https://www.radiorecord.ru/')
        veb4 = types.InlineKeyboardButton(text="Бесплатный урок английского", url='https://www.radiorecord.ru/')
        choice_veb.row(veb1, veb2)
        choice_veb.row(veb3, veb4)
        bot.send_message(message.chat.id, 'Какой подарок вы бы хотели получить?', reply_markup=choice_veb)
        bot.register_next_step_handler(message, veb)
    elif message.text == 'Получить скидку.':
        bot.send_message(message.chat.id, 'Text', reply_markup=menu2)
        bot.register_next_step_handler(message, discount)
    elif message.text == 'Я студент и у меня есть вопрос.':
        bot.send_message(message.chat.id, 'Text', reply_markup=menu2)
        bot.register_next_step_handler(message, quest)
    elif message.text == 'Хочу подарок!':
        choice_gift = types.InlineKeyboardMarkup()
        gift1 = types.InlineKeyboardButton(text='Гайд по изучению английского языка', url='https://www.radiorecord.ru/')
        gift2 = types.InlineKeyboardButton(text="Бесплатный урок английского", url='https://www.radiorecord.ru/')
        choice_gift.add(gift1, gift2)
        bot.send_message(message.chat.id, 'Какой подарок вы бы хотели получить?', reply_markup=choice_gift)
        bot.register_next_step_handler(message, gift)
    elif message.text == 'Это интересно.':
        bot.send_message(message.chat.id, 'Полезные статьи тут: https://www.itbiar.com/%D1%80%D0%B5%D0%B3%D0%'
                                          'B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-'
                                          '%D0%BD%D0%B0-%D0%BA%D1%83%D1%80%D1%81\n'
                                          '\n'
                                          '**Наши соц.сети:**\n'
                                          '\n'
                                          'Инстаграм - https://www.instagram.com/it_akademy_biar/\n'
                                          'Фейсбук - https://www.facebook.com/it.akademy.biar', reply_markup=menu2)
        bot.register_next_step_handler(message, interest)
    else:
        bot.send_message(message.chat.id, 'Такой команды не существует. Пожалуйста, повторите ввод.',
                         reply_markup=menu1)


def study(message):
    if message.text == 'Основное меню.':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=menu1)


def consult(message):
    if message.text == 'Основное меню.':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=menu1)


def course(message):
    if message.text == 'Основное меню.':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=menu1)


def veb(message):
    if message.text == 'Основное меню.':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=menu1)


def discount(message):
    if message.text == 'Основное меню.':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=menu1)


def quest(message):
    if message.text == 'Основное меню.':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=menu1)


def gift(message):
    if message.text == 'Основное меню.':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=menu1)


def interest(message):
    if message.text == 'Основное меню.':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=menu1)


bot.polling()
