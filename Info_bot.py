import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot import types
import sqlite3

bot = telebot.TeleBot('6284976456:AAE7rXYkLmBg2FYDSKuz5VoxHASo_jedJdA')

menu1 = ReplyKeyboardMarkup(resize_keyboard=True)
menu1.row('Обучение.', 'Консультация.')
menu1.row('Бесплатное занятие.', 'Курсы.')
menu1.row('Вебинары.', 'Получить скидку.')
menu1.row('Хочу подарок!', 'Это интересно.')
menu2 = ReplyKeyboardMarkup(resize_keyboard=True)
menu2.row('Основное меню.')


@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, '<b>Я - бот European IT Academy Biar. Помогу:</b>\n'
                                          '\n🤔 Найти ответы на вопросы.'
                                          '\n💰 Выбрать и оплатить курс.'
                                          '\n✍️ Что вас интересует?',
                         parse_mode='HTML',
                         reply_markup=menu1)

        first_name = message.from_user.first_name
        user_name = message.from_user.username
        user_id = message.from_user.id
        con = sqlite3.connect('sqlite.db')
        cur = con.cursor()
        cur.execute('DROP TABLE users')
        cur.execute('CREATE TABLE IF NOT EXISTS users ('
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                    'first_name varchar,'
                    'user_name varchar,'
                    'user_id varchar)')
        id_data = cur.execute('SELECT user_id FROM users').fetchall()
        id_data = [u_id[0] for u_id in id_data]
        if str(user_id) not in id_data:
            # print(1)
            cur.execute(f'''INSERT INTO users (first_name, user_name, user_id)
                                    values('{first_name}','{user_name}', '{user_id}')''')
        else:
            pass
        # cur.execute('DROP TABLE users')   # Delete table
        con.commit()
        con.close()
        bot.register_next_step_handler(message, choice)


@bot.message_handler(func=lambda message: message.text)
def no_start(message):
    bot.register_next_step_handler(message, choice)


def choice(message):
    if message.text == 'Обучение.':
        bot.send_message(message.chat.id, '*Обучение 📌*\n'
                                          '☑️Выбираете вариант обучения (light, standard или premium).\n'
                                          '☑️Нажимаете «Записаться на курс».\n'
                                          '☑️Вводите данные банковской карты и email для оформления покупки курса.\n'
                                          '☑️ Ожидаете зачисление денежных средств в течение 3-5 дней.\n'
                                          # 'Для начала обучения необходимо зарегистрироваться на сайте '
                                          # '(через эл. почту/Google/Facebook). Выберите вариант обучения '
                                          # '(light, standard, premium) и, следуя инструкциям на сайте, '
                                          # 'произведите оплату курса.Обратите внимание, '
                                          # 'что зачисление денежных средств осуществляется в течение 3-5 дней.\n'
                                          '\n*Начало занятий 📚*\n'
                                          '✔️ Получаете на указанный email письмо-подтверждение.'
                                          '\n✔️ Регистрируетесь на [сайте](https://www.itbiar.com/)\n'
                                          '✔️ Вам открывается доступ к материалам курса.\n',
                                          # 'После подтверждения оплаты выбранного вами курса, на вашу электронную почту'
                                          # ' придет письмо-подтверждение и откроется доступ к курсу. Вы сможете '
                                          # 'открывать занятия на платформе и изучать материал в удобное для себя время.'
                                          # '\n'

                                          # 'Проходить занятия следует друг за другом. Для отработки полученных знаний, '
                                          # 'предлагаются практические задачи и домашние задания, выполнение которых '
                                          # 'обязательно для успешного освоения курса . Для положительной динамики '
                                          # 'обучения соблюдайте дедлайн (1 неделя) по выполнению домашних заданий.',
                         parse_mode='Markdown',
                         reply_markup=menu2)
        bot.send_message(message.chat.id, '\n<b>Прохождение занятий 🎓</b>\n'
                                          '☑️Изучаете материал на платформе в любое удобное время.'
                                          '\n☑️ Выполняете практические задания, получаете обратную связь и '
                                          'закрепляете знания.\n'
                                          '☑️Общаетесь с преподавателем.'
                                          '<b>Экзамен 🛎 </b>\n'
                                          '✔️ В конце курса сдаете экзамен для проверки изученного материала '
                                          'на курсе.\n',
                         parse_mode='HTML')
        bot.send_message(message.chat.id,
                                          # 'В конце обучения проходит экзамен для контроля усвоения знаний. '
                                          # 'Экзамен состоит из теоретической и практической частей, что позволяет '
                                          # 'качественно проверить весь диапазон изученного материала на курсе.\n'
                                          '<b>\nОбратная связь📍\n</b>'
                                          '☑️ Получаете обратную связь по результатам обучения.\n'
                                          '☑️ Рекомендации для дальнейшего профессионального роста.\n'
                                          # 'После экзамена мы предоставляем обратную связь по результатам обучения и '
                                          # 'рекомендации для дальнейшего профессионального роста студента.\n'
                                          '<b>\nСертификат 🏆\n</b>'
                                          '✔️ Получаете сертификат об окончании курса.\n'
                                          '✔️ Дополняете портфолио выполненными практическими заданиями '
                                          'с реальными кейсами.',
                                          # 'Финальный шаг успешного обучения - сертификат, который высылаем студенту на '
                                          # 'электронную почту.',
                         parse_mode='HTML')
        bot.register_next_step_handler(message, back)
    elif message.text == 'Консультация.':
        choice_faq = types.InlineKeyboardMarkup()
        faq_button = types.InlineKeyboardButton(text='FAQ',
                                                url='https://www.itbiar.com/question')
        quest_button = types.InlineKeyboardButton(text='Задать вопрос', url='https://tinyurl.com/ypnatmp8')
        choice_faq.add(faq_button, quest_button)
        bot.send_message(message.chat.id, 'Ответы на 90% вопросов к Biar собраны в разделе FAQ'
                                          '\nЕсли Вы не нашли ответ на свой вопрос:\n'
                                          'Отправьте его нам на почт\n'
                                          'Мы ответим так быстро, насколько это возможно'
                         ,
                         reply_markup=choice_faq)
        bot.send_message(message.chat.id, 'Для выхода в главное меню нажмите кнопку "Основное меню."',
                         reply_markup=menu2)
        bot.register_next_step_handler(message, back)
    elif message.text == 'Бесплатное занятие.':
        free_link = types.InlineKeyboardMarkup()
        link = types.InlineKeyboardButton(text='Бесплатные уроки тут', url='https://www.itbiar.com/lesson-example')
        free_link.add(link)
        bot.send_message(message.chat.id, '<b>Бесплатное занятие.\n</b>'
                                          'Программирование. Тестирование. Дизайн. Рекрутинг. Всё:\n'
                                          '\nPython JavaScript Ruby\n'
                                          'QA Engineer (Trainee)\n'
                                          'QA Engineer (Junior)\n'
                                          'UX/UI дизайн\n'
                                          'Figma\n'
                                          'IT рекрутинг', parse_mode='HTML', reply_markup=free_link)
        bot.send_message(message.chat.id, 'Для выхода в главное меню нажмите кнопку "Основное меню."',
                         reply_markup=menu2)
        bot.register_next_step_handler(message, back)
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
        bot.send_message(message.chat.id, 'Для выхода в главное меню нажмите кнопку "Основное меню."',
                         reply_markup=menu2)
        bot.register_next_step_handler(message, back)
    elif message.text == 'Вебинары.':
        choice_veb = types.InlineKeyboardMarkup()
        veb1 = types.InlineKeyboardButton(text='Программирование',
                                          url='https://www.itbiar.com/webinars')
        veb2 = types.InlineKeyboardButton(text="Тестирование",
                                          url='https://www.itbiar.com/webinars')
        veb3 = types.InlineKeyboardButton(text='Дизайн',
                                          url='https://www.itbiar.com/webinars')
        veb4 = types.InlineKeyboardButton(text="HR рекрутинг",
                                          url='https://www.itbiar.com/webinars')
        choice_veb.row(veb1, veb2)
        choice_veb.row(veb3, veb4)
        bot.send_message(message.chat.id, '<b>Вебинары.\n</b>'
                                          'Выберите направление, которое Вас интересует:',
                         parse_mode='HTML',
                         reply_markup=choice_veb)
        bot.send_message(message.chat.id, 'Для выхода в главное меню нажмите кнопку "Основное меню."',
                         reply_markup=menu2)
        bot.register_next_step_handler(message, back)
    elif message.text == 'Получить скидку.':
        choice_ans = types.InlineKeyboardMarkup()
        ans1 = types.InlineKeyboardButton(text='✅ Да', callback_data='yes')
        ans2 = types.InlineKeyboardButton(text="❌ Нет", callback_data='no')
        choice_ans.add(ans1, ans2)
        bot.send_message(message.chat.id, '<b>Получить скидку.\n</b>'
                                          'Вы уже проходите или проходили курсы Biar?',
                         parse_mode='HTML',
                         reply_markup=choice_ans)

        @bot.callback_query_handler(func=lambda callback: callback)
        def disc_show(callback):
            if callback.data == 'no':
                guide_inline = types.InlineKeyboardMarkup()
                guide_button = types.InlineKeyboardButton(text='🔥 Гайд по входу в IT 2023 тут', url='https://'
                                                                                                    'e03dc1fb-f21c-'
                                                                                                    '4092-bd5c-'
                                                                                                    '4d20cea1e3fb.'
                                                                                                    'usrfiles.com/ugd/'
                                                                                                    'e03dc1_eabcfb672d7'
                                                                                                    '24305b71b979d3701'
                                                                                                    '7438.pdf')
                guide_inline.add(guide_button)
                bot.send_message(callback.message.chat.id,
                                 '<b>Для Вас мы подготовили:</b>\n'
                                 '\n1) промокод BOTBIAR на скидку 20% при оформлении покупки курса на сайте\n'
                                 '2) Ваш гайд по входу в IT в 2023 году прямо по ссылке:',
                                 parse_mode='HTML',
                                 reply_markup=guide_inline)
            elif callback.data == 'yes':
                bot.send_message(callback.message.chat.id, '<b>Для Вас мы подготовили:</b>\n'
                                                           '\nПромокод BOTBIAR на скидку 20% при оформлении покупки '
                                                           'курса на сайте', parse_mode='HTML')

        bot.send_message(message.chat.id, 'Для выхода в главное меню нажмите кнопку "Основное меню."',
                         reply_markup=menu2)
        bot.register_next_step_handler(message, back)
    # elif message.text == 'Задать вопрос.':
    #     bot.send_message(message.chat.id, '<b>Если Вы уже учитесь у нас и у Вас есть вопросы:</b>'
    #                                       'Отправьте свой вопрос нам на почту - biaritacademy@gmail.com\n'
    #                                       'Мы ответим так быстро, насколько это возможно\n'
    #                                       '\nСпасибо, что выбрали Biar.',
    #                      parse_mode='HTML',
    #                      reply_markup=menu2)
    #     bot.register_next_step_handler(message, back)
    elif message.text == 'Хочу подарок!':
        choice_gift = types.InlineKeyboardMarkup()
        gift1 = types.InlineKeyboardButton(text='🔥 Гайд по обучению в IT',
                                           url='https://e03dc1fb-f21c-4092-bd5c-4d20cea1e3fb.usrfiles.com/ugd/'
                                               'e03dc1_eabcfb672d724305b71b979d37017438.pdf')
        gift2 = types.InlineKeyboardButton(text="🇬🇧 Английский язык для IT 🇺🇸",
                                           url='https://e03dc1fb-f21c-4092-bd5c-4d20cea1e3fb.usrfiles.com/ugd/'
                                               'e03dc1_3d5a08a54006468d93f1ab910aee9dcb.pdf')
        choice_gift.row(gift1)
        choice_gift.row(gift2)
        bot.send_message(message.chat.id, '<b>Подарки.\n</b>'
                                          'Какой подарок вы бы хотели получить?',
                         parse_mode='HTML',
                         reply_markup=choice_gift)
        bot.send_message(message.chat.id, 'Для выхода в главное меню нажмите кнопку "Основное меню."',
                         reply_markup=menu2)
        bot.register_next_step_handler(message, back)
    elif message.text == 'Это интересно.':
        text = '*Статьи:*\n' \
               '[Полезные статьи тут 📚](https://www.itbiar.com/%D1%80%D0%B5%D0%B3%D0%' \
               'B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-' \
               '%D0%BD%D0%B0-%D0%BA%D1%83%D1%80%D1%81)\n' \
               '\n' \
               '*Наши соц.сети:*\n' \
               '[Instagram 📌](https://www.instagram.com/it_akademy_biar/)\n' \
               '[Facebook 👌](https://www.facebook.com/it.akademy.biar)'
        bot.send_message(message.chat.id, text,
                         parse_mode='Markdown',
                         reply_markup=menu2)
        bot.register_next_step_handler(message, back)
    elif message.text == '/biar__admin':
        message = bot.send_message(message.chat.id, 'Введите сообщение для рассылки всем пользователм:')
        bot.register_next_step_handler(message, mailing)
    else:
        bot.send_message(message.chat.id, 'Такой команды не существует. Пожалуйста, повторите ввод.',
                         reply_markup=menu1)
        bot.register_next_step_handler(message, choice)


def mailing(message):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    id_data = cur.execute('SELECT user_id FROM users').fetchall()
    id_data = [u_id[0] for u_id in id_data]
    con.close()
    # print(id_data)
    for user_id in id_data:
        bot.send_message(user_id, f'{message.text}', parse_mode='HTML')
    bot.register_next_step_handler(message, choice)


def back(message):
    if message.text == 'Основное меню.':
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню.', reply_markup=menu1)
        bot.register_next_step_handler(message, choice)


bot.polling()
