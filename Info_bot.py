import time
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
        bot.send_message(message.chat.id, '<b>Я - бот European IT Academy Biar. Помогу:</b>'
                                          '\nНайти ответы на вопросы.'
                                          '\nВыбрать и оплатить курс.'
                                          '\nЧто вас интересует?', parse_mode='HTML',reply_markup=menu1)

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
        bot.send_message(message.chat.id, '<b>Обучение.</b>\n'
                                          'Для начала обучения необходимо зарегистрироваться на сайте '
                                          '(через эл. почту/Google/Facebook). Выберите вариант обучения '
                                          '(light, standard, premium) и, следуя инструкциям на сайте, '
                                          'произведите оплату курса.​Обратите внимание, '
                                          'что зачисление денежных средств осуществляется в течение 3-5 дней.\n'
                                          '\n<b>Начало занятий.</b>\n'
                                          'После подтверждения оплаты выбранного вами курса, на вашу электронную почту'
                                          ' придет письмо-подтверждение и откроется доступ к курсу. Вы сможете '
                                          'открывать занятия на платформе и изучать материал в удобное для себя время.'
                                          '\n'
                                          '\n<b>Прохождение занятий.</b>\n'
                                          'Проходить занятия следует друг за другом. Для отработки полученных знаний, '
                                          'предлагаются практические задачи и домашние задания, выполнение которых '
                                          'обязательно для успешного освоения курса . Для положительной динамики '
                                          'обучения соблюдайте дедлайн (1 неделя) по выполнению домашних заданий.',
                         parse_mode='HTML',
                         reply_markup=menu2)
        time.sleep(3)
        bot.send_message(message.chat.id, '<b>Экзамен.</b>\n'
                                          'В конце обучения проходит экзамен для контроля усвоения знаний. '
                                          'Экзамен состоит из теоретической и практической частей, что позволяет '
                                          'качественно проверить весь диапазон изученного материала на курсе.\n'
                                          '<b>\nОбратная связь.\n</b>'
                                          'После экзамена мы предоставляем обратную связь по результатам обучения и '
                                          'рекомендации для дальнейшего профессионального роста студента.\n'
                                          '<b>\nСертификат.\n</b>'
                                          'Финальный шаг успешного обучения - сертификат, который высылаем студенту на '
                                          'электронную почту.',
                         parse_mode='HTML')
        bot.register_next_step_handler(message, back)
    elif message.text == 'Консультация.':
        choice_faq = types.InlineKeyboardMarkup()
        faq_button = types.InlineKeyboardButton(text='FAQ',
                                                url='https://www.itbiar.com/question')
        choice_faq.add(faq_button)
        bot.send_message(message.chat.id, 'Ответы на 90% вопросов к Biar собраны в разделе FAQ',
                         reply_markup=choice_faq)
        bot.register_next_step_handler(message, choice)
    elif message.text == 'Курсы.':
        choice_course = types.InlineKeyboardMarkup()
        course1 = types.InlineKeyboardButton(text='Программирование',
                                             url='https://www.itbiar.com/our-courses-programming')
        course2 = types.InlineKeyboardButton(text="Тестирование",
                                             url='https://www.itbiar.com/our-courses-qa')
        course3 = types.InlineKeyboardButton(text='Дизайн',
                                             url='https://www.itbiar.com/our-courses-design')
        course4 = types.InlineKeyboardButton(text="HR рекрутинг",
                                             url='https://www.itbiar.com/our-courses-hr')
        choice_course.row(course1, course2)
        choice_course.row(course3, course4)
        bot.send_message(message.chat.id, '<b>Наши курсы.</b>\n'
                                          'Просто выберите программу, на которой хотите пройти обучение'
                                          'и станьте на шаг ближе ко входу в мир IT:',
                         parse_mode='HTML',
                         reply_markup=choice_course)
        bot.register_next_step_handler(message, choice)
    elif message.text == 'Вебинары.':
        choice_veb = types.InlineKeyboardMarkup()
        veb1 = types.InlineKeyboardButton(text='Программирование',
                                          url='https://www.itbiar.com/our-courses-programming')
        veb2 = types.InlineKeyboardButton(text="Тестирование",
                                          url='https://www.itbiar.com/our-courses-qa')
        veb3 = types.InlineKeyboardButton(text='Дизайн',
                                          url='https://www.itbiar.com/our-courses-design')
        veb4 = types.InlineKeyboardButton(text="HR рекрутинг",
                                          url='https://www.itbiar.com/our-courses-hr')
        choice_veb.row(veb1, veb2)
        choice_veb.row(veb3, veb4)
        bot.send_message(message.chat.id, '<b>Вебинары.\n</b>'
                                          'Выберите направление, которое Вас интересует:',
                         parse_mode='HTML',
                         reply_markup=choice_veb)
        bot.register_next_step_handler(message, choice)
    elif message.text == 'Получить скидку.':
        choice_ans = types.InlineKeyboardMarkup()
        ans1 = types.InlineKeyboardButton(text='Да', callback_data='yes')
        ans2 = types.InlineKeyboardButton(text="Нет", callback_data='no')
        choice_ans.add(ans1, ans2)
        bot.send_message(message.chat.id, '<b>Получить скидку.\n</b>'
                                          'Вы уже проходите или проходили курсы Biar?',
                         parse_mode='HTML',
                         reply_markup=choice_ans)

        @bot.callback_query_handler(func=lambda callback: callback)
        def disc_show(callback):
            if callback.data == 'no':
                bot.send_message(callback.message.chat.id,
                                 'Введите промокод NEXT при оформлении покупки курса на сайте и получите скидку 15%')
            else:
                pass
        bot.register_next_step_handler(message, choice)
    elif message.text == 'Я студент и у меня есть вопрос.':
        bot.send_message(message.chat.id, '<b>Если Вы уже учитесь у нас и у Вас есть вопросы:</b>'
                                          'Отправьте свой вопрос нам на почту - biaritacademy@gmail.com\n'
                                          'Мы ответим так быстро, насколько это возможно\n'
                                          '\nСпасибо, что выбрали Biar.',
                         parse_mode='HTML',
                         reply_markup=menu2)
        bot.register_next_step_handler(message, back)
    elif message.text == 'Хочу подарок!':
        choice_gift = types.InlineKeyboardMarkup()
        gift1 = types.InlineKeyboardButton(text='Гайд по изучению английского языка',
                                           url='https://www.itbiar.com/')
        gift2 = types.InlineKeyboardButton(text="Бесплатный урок английского",
                                           url='https://www.itbiar.com/')
        choice_gift.row(gift1)
        choice_gift.row(gift2)
        bot.send_message(message.chat.id, '<b>Подарки.\n</b>'
                                          'Какой подарок вы бы хотели получить?',
                         parse_mode='HTML',
                         reply_markup=choice_gift)
        bot.register_next_step_handler(message, choice)
    elif message.text == 'Это интересно.':
        bot.send_message(message.chat.id, '<b>Полезные статьи тут:</b> https://www.itbiar.com/%D1%80%D0%B5%D0%B3%D0%'
                                          'B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-'
                                          '%D0%BD%D0%B0-%D0%BA%D1%83%D1%80%D1%81\n'
                                          '\n'
                                          '<b>Наши соц.сети:</b>\n'
                                          'Инстаграм - https://www.instagram.com/it_akademy_biar/\n'
                                          'Фейсбук - https://www.facebook.com/it.akademy.biar',
                         parse_mode='HTML',
                         reply_markup=menu2)
        bot.register_next_step_handler(message, back)
    else:
        bot.send_message(message.chat.id, 'Такой команды не существует. Пожалуйста, повторите ввод.',
                         reply_markup=menu1)


def back(message):
    if message.text == 'Основное меню.':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=menu1)
        bot.register_next_step_handler(message, choice)


bot.polling()
