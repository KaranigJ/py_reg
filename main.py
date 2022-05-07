from CONFIG import bot
from CONFIG import link
from CONFIG import chat
from telebot import types
import csv_func as csv

сurators = []
csv.read('members.csv', сurators)

allus = []
csv.read('alluser.csv', allus)

crmen = '👨‍🏫Меню куратора👨‍🏫‍'

menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
cmenu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
course = types.KeyboardButton('Инструкции к выполнению курса')
dz = types.KeyboardButton('Инструкции к выполнению ДЗ')
info = types.KeyboardButton('Информационный канал')
table = types.KeyboardButton('Расписание')
again = types.KeyboardButton('На старт!')
rate = types.KeyboardButton('Рейтинг')
curator = types.KeyboardButton(crmen)
curator_сh = types.KeyboardButton('Куратор')

menu.add(course, dz, info, table, rate, curator_сh, again)
cmenu.add(course, dz, info, table, rate, curator_сh, curator, again)

markup_check = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
yes_button = types.KeyboardButton('Да')
no_button = types.KeyboardButton('Нет')
markup_check.add(yes_button, no_button)

text = 'Уважаемый куратор! Статистика ответов по 1 заданию и баллы обновлены.' \
       ' Вы можете найти всю информацию в "меню куратора" по кнопкам "Мои участники" меню.'

@bot.message_handler(commands=['send'])
def send(message):
    for i in range(len(сurators)):
        print(сurators[i][0])
        bot.send_message(сurators[i][1], text)

@bot.message_handler(commands=['start'])
def start(message):
    member = [f'{message.from_user.first_name} {message.from_user.last_name}', f'{message.from_user.id}', f'{message.from_user.username}']
    mes = f'Добро пожаловать на курс, {member[0]}!\nУ вас уже есть приложение Getcourse.ru?'

    bot.send_message(message.chat.id, mes, reply_markup=markup_check)
    if member not in allus:
        allus.append(member)
        csv.write('alluser.csv', allus)

@bot.message_handler(content_types=['text'])
def get_text(message):
    def check(text):
        if mem in сurators:
            bot.send_message(message.chat.id,
                            text,
                             reply_markup=cmenu)
        else:
            bot.send_message(message.chat.id,
                             text,
                             reply_markup=menu)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    mem = [f'{message.from_user.first_name} {message.from_user.last_name}', f'{message.from_user.id}']

    if message.chat.id == 443257481:
        txt = message.text
        for i in range(len(allus)):
            bot.send_message(allus[i][1], txt)

    if message.text == 'Да':
        step = 0
        next = types.KeyboardButton(f'{step+1})Авторизация Далее➡')
        markup.add(next)
        bot.send_message(message.chat.id, 'Первый шаг к авторизации.\n\n Если вы перепутали кнопку, дойдите до конца регистрации не выполняя пунктов,'
                                          ' а затем выберите кнопку "На старт!"', reply_markup=markup)
    elif message.text == 'Нет':
        step = 0
        next = types.KeyboardButton(f'{step + 1})Регистрация Далее➡')
        markup.add(next)
        bot.send_message(message.chat.id, 'Первый шаг к регистрации.\n\n Если вы перепутали кнопку, дойдите до конца регистрации не выполняя пунктов,'
                                          ' а затем выберите кнопку "На старт!"')
        markup_get = types.InlineKeyboardMarkup()
        markup_get.add(types.InlineKeyboardButton('Перейти к регистрации', url=link))
        bot.send_message(message.chat.id, 'Перейдите по ссылке для начала ругистрации.', reply_markup=markup_get)
        bot.send_message(message.chat.id, 'Нажмите далее чтобы получить следующий шаг', reply_markup=markup)

    def next_but_a(markup, count):
        step = count
        next = types.KeyboardButton(f'{step + 1})Авторизация Далее➡')
        markup.add(next)
        if count == 1:
            bot.send_message(message.chat.id, 'Нажмите кнопку "Авторизоваться и найти"', reply_markup=markup)
            file = open('Photo/12.png', 'rb')
            bot.send_photo(message.chat.id, file)
        elif count == 2:
            bot.send_message(message.chat.id, 'Нажмите кнопку "Войти по почте"', reply_markup=markup)
            file = open('Photo/13.png', 'rb')
            bot.send_photo(message.chat.id, file)
        elif count == 3:
            bot.send_message(message.chat.id, 'Введите вашу электронную почту и нажмите "получить ссылку для входа"', reply_markup=markup)
            file = open('Photo/14.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/3.mp4', 'rb')
            bot.send_video(message.chat.id, vid)

        elif count == 4:
            bot.send_message(message.chat.id, 'Перейдите в почту и найдите там письмо от Chatium.\n'
                                              'Если его нет в основных письмах проверьте папку спам.\n'
                                              'Если его нет и там, проверьте правильность почты и попробуйте ещё раз.\n'
                                              'В письме есть ссылка, нажав на которую вы увидите код, который необходимо запомнить.',
                             reply_markup=markup)
            file = open('Photo/3.png', 'rb')
            file1 = open('Photo/4.png', 'rb')
            file2 = open('Photo/5.png', 'rb')

            bot.send_photo(message.chat.id, file)
            bot.send_photo(message.chat.id, file1)
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/4.mp4', 'rb')
            bot.send_video(message.chat.id, vid)

        elif count == 5:
            bot.send_message(message.chat.id, 'Возвращаемся в Getcourse и вводим полученый код в специальное поле',
                             reply_markup=markup)
            file = open('Photo/6.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/5.mp4', 'rb')
            bot.send_video(message.chat.id, vid)

        elif count == 6:
            bot.send_message(message.chat.id, 'Открываем меню избранного')
            file = open('Photo/8.png', 'rb')
            file1 = open('Photo/9.png', 'rb')
            file2 = open('Photo/10.png', 'rb')
            bot.send_photo(message.chat.id, file)
            bot.send_message(message.chat.id,
                             'Находим кнопку настройка избранного и ставим галочку напротив practicumtk',
                             reply_markup=markup)
            bot.send_photo(message.chat.id, file1)
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/7.mp4', 'rb')
            bot.send_video(message.chat.id, vid)

        elif count == 7:
            bot.send_message(message.chat.id,
                             'Возвращаемся назад в избранное при помощи стрелки назад на телефоне и находим там курс',
                             reply_markup=markup)
            file2 = open('Photo/11.png', 'rb')
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/8.mp4', 'rb')
            bot.send_video(message.chat.id, vid)

    def next_but_r(markup, count):
        step = count
        next = types.KeyboardButton(f'{step + 1})Регистрация Далее➡')
        markup.add(next)
        if count == 1:
            bot.send_message(message.chat.id, 'Найдите кнопку скачать приложение', reply_markup=markup)
            file = open('Photo/1.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/1.mp4', 'rb')
            bot.send_document(message.chat.id, vid)

        elif count == 2:
            bot.send_message(message.chat.id, 'Установите приложение', reply_markup=markup)
            vid = open('Vid/2.mp4', 'rb')
            bot.send_document(message.chat.id, vid)

        elif count == 3:
            bot.send_message(message.chat.id, 'Введите вашу электронную почту и нажмите "получить ссылку для входа"', reply_markup=markup)
            file = open('Photo/2.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/3.mp4', 'rb')
            bot.send_document(message.chat.id, vid)

        elif count == 4:
            bot.send_message(message.chat.id, 'Перейдите в почту и найдите там письмо от Chatium.\n'
                                              'Если его нет в основных письмах проверьте папку спам.\n'
                                              'Если его нет и там, проверьте правильность почты и попробуйте ещё раз.\n'
                                              'В письме есть ссылка, нажав на которую вы увидите код, который необходимо запомнить.', reply_markup=markup)
            file = open('Photo/3.png', 'rb')
            file1 = open('Photo/4.png', 'rb')
            file2 = open('Photo/5.png', 'rb')

            bot.send_photo(message.chat.id, file)
            bot.send_photo(message.chat.id, file1)
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/4.mp4', 'rb')
            bot.send_document(message.chat.id, vid)

        elif count == 5:
            bot.send_message(message.chat.id, 'Возвращаемся в Getcourse и вводим полученый код в специальное поле', reply_markup=markup)
            file = open('Photo/6.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/5.mp4', 'rb')
            bot.send_document(message.chat.id, vid)

        elif count == 6:
            bot.send_message(message.chat.id, 'Нажимаем кнопку зарегистрироваться с помощью email', reply_markup=markup)
            file = open('Photo/7.png', 'rb')
            bot.send_photo(message.chat.id, file)
            vid = open('Vid/6.mp4', 'rb')
            bot.send_document(message.chat.id, vid)

        elif count == 7:
            bot.send_message(message.chat.id, 'Открываем меню избранного')
            file = open('Photo/8.png', 'rb')
            file1 = open('Photo/9.png', 'rb')
            file2 = open('Photo/10.png', 'rb')
            bot.send_photo(message.chat.id, file)
            bot.send_message(message.chat.id, 'Находим кнопку настройка избранного и ставим галочку напротив practicumtk', reply_markup=markup)
            bot.send_photo(message.chat.id, file1)
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/7.mp4', 'rb')
            bot.send_document(message.chat.id, vid)

        elif count == 8:
            bot.send_message(message.chat.id, 'Возвращаемся назад в избранное при помощи стрелки назад на телефоне и находим там курс', reply_markup=markup)
            file2 = open('Photo/11.png', 'rb')
            bot.send_photo(message.chat.id, file2)
            vid = open('Vid/8.mp4', 'rb')
            bot.send_document(message.chat.id, vid)

    if message.text == '1)Авторизация Далее➡':
        next_but_a(markup, 1)
    elif message.text == '2)Авторизация Далее➡':
        next_but_a(markup, 2)
    elif message.text == '3)Авторизация Далее➡':
        next_but_a(markup, 3)
    elif message.text == '4)Авторизация Далее➡':
        next_but_a(markup, 4)
    elif message.text == '5)Авторизация Далее➡':
        next_but_a(markup, 5)
    elif message.text == '6)Авторизация Далее➡':
        next_but_a(markup, 6)
    elif message.text == '7)Авторизация Далее➡':
        next_but_a(markup, 7)
        check('Поздравляю с авторизацией на курсе!')


    if message.text == '1)Регистрация Далее➡':
        next_but_r(markup, 1)
    elif message.text == '2)Регистрация Далее➡':
        next_but_r(markup, 2)
    elif message.text == '3)Регистрация Далее➡':
        next_but_r(markup, 3)
    elif message.text == '4)Регистрация Далее➡':
        next_but_r(markup, 4)
    elif message.text == '5)Регистрация Далее➡':
        next_but_r(markup, 5)
    elif message.text == '6)Регистрация Далее➡':
        next_but_r(markup, 6)
    elif message.text == '7)Регистрация Далее➡':
        next_but_r(markup, 7)
    elif message.text == '8)Регистрация Далее➡':
        next_but_r(markup, 8)
        check('Поздравляю с регистрацией на курсе!\n\nЯ ваш помощник! Вы всегда можешь обратиться ко мне за помощью😉')


    back = types.KeyboardButton('Назад')
    if message.text == 'Назад':
        check('Основное меню')


    if message.text == 'Инструкции к выполнению курса':
        print('course')
        bot.send_message(message.chat.id,'У вас будет на выбор несколько заданий, каждое из которых принесёт вам определённое количество баллов(2, 4, 8 баллов).\n\n'
                                        'Для получения бОльшего количества баллов, рекомендуется выполнять все задаия.\n\n'
                                        'Если задание выполнено не полностью или некорректно, то количество баллов уменьшается пропорционально количеству неточностей.\n\n'
                                        'Ответ отправляется ТОЛЬКО 1 РАЗ. Повторные ответы учитываться не будут.\n\n'
                                        'Количество набранных баллов будет суммироваться и участвововать в рейтинге всех участников марафона.\n\n'
                                        'Кураторы не участвуют в начислении баллов.\n\n'
                                        'Крайний срок выполнения задания — до выхода следующего урока(дата следующего урока указана в боте марафона и на платформе Getcourse)\n\n'
                                        'Есть возможность дополнительного получения баллов, о которой вы можете узнать у кураторов.\n\n',
                                        parse_mode='html')
    elif message.text == 'Инструкции к выполнению ДЗ':
        dz_markap = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        dz1 = types.KeyboardButton('Домашнее задание номер 1')
    #    dz2 = types.KeyboardButton('Домашнее задание номер 2')
    #    dz3 = types.KeyboardButton('Домашнее задание номер 3')
    #    dz4 = types.KeyboardButton('Домашнее задание номер 4')
        dz_markap.add(dz1, back)
        bot.send_message(message.chat.id, 'Выберете интструкцию к какому заданию хотите получить', reply_markup=dz_markap)
    elif message.text == 'Информационный канал':
        ch_markup = types.InlineKeyboardMarkup()
        ch_markup.add(types.InlineKeyboardButton('Информационный канал', url=chat))
        bot.send_message(message.chat.id, 'Марафон "Кризис. Зона роста."', reply_markup=ch_markup)
    elif message.text == 'Расписание':
        bot.send_message(message.chat.id, '<b>25 апреля:</b> Кризис и главный фактор риска\n<b>28 апреля:</b> Кризис и финансы\n'
                                          '<b>02 мая:</b> Кризис. Трамплин к мечте\n<b>04 мая:</b> Кризис. Прорыв\n<b>05 мая:</b> Кризис. За линией страха',
                         parse_mode='html')
    if message.text == 'На старт!':
        bot.send_message(message.chat.id, 'У вас уже есть приложение Getcourse.ru?', reply_markup=markup_check)

    if message.text == 'Куратор':
        all_cur = types.InlineKeyboardMarkup(row_width=1)
        gi = types.InlineKeyboardButton('Гребнева Ирина', url='https://t.me/+_Prgd1rS2Uc3MTQy')
        mm = types.InlineKeyboardButton('Троц Марина', url='https://t.me/+uxYWaMlr5RoxOTBi')
        tk = types.InlineKeyboardButton('Кислая Татьяна', url=link)
        el = types.InlineKeyboardButton('Вайнилович Елена', url='https://t.me/+JTyr8ADNZ_E0ZDEy')
        nt = types.InlineKeyboardButton('Трусь Наталья', url='https://t.me/+F29DwEh9J0Q5MGUy')
        sv = types.InlineKeyboardButton('Евтушик Святослав', url='https://t.me/sonarostaes')
        kl = types.InlineKeyboardButton('Котусова Людмила', url='https://t.me/LiudmilaKotusova')
        dk = types.InlineKeyboardButton('Кислый Денис', url=link)
        ma = types.InlineKeyboardButton('Левкович Матвей', url=link)
        all_cur.add(gi, mm, el, nt, sv, kl)
        bot.send_message(message.chat.id, 'Выберите вашего куратора', reply_markup=all_cur)

    all = []
    csv.read('Curator/All.csv', all)

    if message.text == 'Рейтинг':
        bot.send_message(message.chat.id, 'Место: Участник : Баллы')
        for i in range(len(all)):
            text = f'{i+1}: {all[i][0]} : {float(all[i][1])}'
            bot.send_message(message.chat.id, text)


    curmenu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    mymem = types.KeyboardButton('Мои участники')
    curinfo = types.KeyboardButton('Информация📚')
    curmenu.add(mymem, curinfo, back)

    if message.text == crmen:
        print('Curator')
        bot.send_message(message.chat.id, 'Меню кураторов', reply_markup=curmenu)

    greb = []
    csv.read('Curator/Гребнева.csv', greb)
    troc = []
    csv.read('Curator/Троц.csv', troc)
    evtu= []
    csv.read('Curator/Евтушик.csv', evtu)
    trus = []
    csv.read('Curator/Трусь.csv', trus)
    vain = []
    csv.read('Curator/Вайнилович.csv', vain)
    kots = []
    csv.read('Curator/Котусова.csv', kots)

    if message.text == 'Мои участники':
        if message.chat.id == 742739821: #Гребнева
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1P_wW6kwpj5QXOPYWAmc2NyuOjj7SnQ-4u42fM6KJ8bI/edit?usp=sharing')
            for i in range(len(greb)):
                text = f'{greb[i][0]} : {float(greb[i][1])}'
                bot.send_message(message.chat.id, text)
    if message.text == 'Мои участники':
        if message.chat.id == 531433683: #Котусова
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1P_wW6kwpj5QXOPYWAmc2NyuOjj7SnQ-4u42fM6KJ8bI/edit?usp=sharing')
            for i in range(len(kots)):
                text = f'{kots[i][0]} : {float(kots[i][1])}'
                bot.send_message(message.chat.id, text)
        elif message.chat.id == 1383469137:#Троц
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1_vUmD-MiKx2Kpubvies9-qym6mdRp2sZqZURe_QLjkg/edit?usp=sharing')
            for i in range(len(troc)):
                text = f'{troc[i][0]} : {float(troc[i][1])}'
                bot.send_message(message.chat.id, text)
        elif message.chat.id == 1121927226:#Евтушик
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1z8F433XA4pqMscGHmP9h_sWgbkAIYgNX03SLGO_AQU8/edit?usp=sharing')
            for i in range(len(evtu)):
                text = f'{evtu[i][0]} : {float(evtu[i][1])}'
                bot.send_message(message.chat.id, text)
        elif message.chat.id == 650172724:#Трусь
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1WIZdBedtZvAkXD1xSnbVjgFM2q2cII0oQYKHQO5iips/edit?usp=sharing')
            for i in range(len(trus)):
                text = f'{trus[i][0]} : {float(trus[i][1])}'
                bot.send_message(message.chat.id, text)
        elif message.chat.id == 315332801:#Вайнилович
            bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1577Jea9eSXLxc7Zs7FTm4loSs63uleGf7iacRNmNgWI/edit?usp=sharing')
            for i in range(len(vain)):
                text = f'{vain[i][0]} : {float(vain[i][1])}'
                bot.send_message(message.chat.id, text)
        elif message.chat.id == 405934214:#Я
           bot.send_message(message.chat.id,
                             'https://docs.google.com/spreadsheets/d/1577Jea9eSXLxc7Zs7FTm4loSs63uleGf7iacRNmNgWI/edit?usp=sharing')
           for i in range(len(greb)):
               text = f'{greb[i][0]} : {float(greb[i][1])}'
               bot.send_message(message.chat.id, text)

    elif message.text == 'Информация📚':
        bot.send_message(message.chat.id, 'Дополнительное начисление баллов за приобретённую продукцию:\n'
                                            '1. пакет Начальный – 20 баллов\n'
                                            '2. пакет Стандарт – 40 баллов\n'
                                            '3. пакет Вип – 60 баллов\n'
                                            '4. пакет Инвестор – 100 баллов\n'
                                            '5. пакет Инвестор 2 – 150 баллов\n'
                                            '6. пакет Инвестор 3 – 300 баллов\n'
                                            '7. пакет Инвестор Премиум – 500 баллов\n'
                                            '8. Бизнес-вход Молодёжный – 120 баллов\n'
                                            '9. Бизнес-вход Базовый – 160 баллов\n'
                                            '10. Бизнес-вход Быстрый старт – 360 баллов\n'
                                            '11. Годовая бизнес активность – 20 баллов\n')

    if message.text == 'Домашнее задание номер 1':
        v = open('Vid/9.mp4', 'rb')
        bot.send_message(message.chat.id, 'Подождите пока придёт файл.')
        bot.send_video(message.chat.id, v)

print('start')
bot.polling(none_stop=True)
print('stop')