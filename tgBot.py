import db_fill as df
import createImage as cI
import conf

import telebot

from telebot import types
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage

state_storage = StateMemoryStorage()

bot = telebot.TeleBot('5345983938:AAHgFq1PgoRMn65P21gjrMJGIseV2DMb39Q',
state_storage= state_storage)
print('Бот запущен')
tempUserEdit = {}
class statesCRM(StatesGroup):
    menu = State()
    login = State()
    add = State()
    choice = State()
    update = State()
    table = State()
    whereSelect = State()
    delete = State()
    find = State()

@bot.message_handler(commands=['start'])
def start_user(message):
    bot.send_message(message.chat.id, 'Добро пожаловать введите пароль!')
    bot.set_state(message.from_user.id, statesCRM.login)
    with bot.retrieve_data(message.chat.id) as data:
        data['table'] = None
        data['ind'] = 0

@bot.message_handler(state = statesCRM.login)
def admin_check(password):
    if (password.text == '322'):
        tempUserEdit[password.from_user.username] = []
        bot.set_state(password.from_user.id, statesCRM.menu)
        menu(password)
    else:
        bot.send_message(password.chat.id, 'Пароль неверный!\nПовторите попытку')

@bot.message_handler(state = statesCRM.menu)
def menu(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
    markup_reply.add('История изменений', 'Поиск по первичному ключу')
    temp = []
    for i,tab in enumerate(df.tablesAll):
        if (i%(3) == 2):
            temp.append(df.tablesAll[tab].nameTable)
            markup_reply.add(temp[0], temp[1], temp[2], row_width=3)
            temp = []
        else:
            temp.append(df.tablesAll[tab].nameTable)
    markup_reply.add(temp[0])
    bot.send_message(message.chat.id, 'Выберите таблицу для взаимодействия.', reply_markup=markup_reply)
    bot.set_state(message.chat.id, statesCRM.table)

@bot.message_handler(state = statesCRM.table)
def table(message):
    if (message.text != 'История изменений' and message.text != 'Поиск по первичному ключу'):
        with bot.retrieve_data(message.chat.id) as data:
            data['table'] = df.tablesAll[message.text]
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup_reply.add(conf.buttons[0])
            markup_reply.add(conf.buttons[1], conf.buttons[2], conf.buttons[3], conf.buttons[4], conf.buttons[5], row_width=2)
            bot.send_message(message.chat.id, 'Выберите взаимодействие с таблицей', reply_markup=markup_reply)
            bot.set_state(message.chat.id, statesCRM.choice)
    elif (message.text == 'История изменений'):
        msg = "------------------------------------------\n"
        for i in tempUserEdit:
            for j in tempUserEdit[i]:
                msg += j + "\n------------------------------------------\n"
        bot.send_message(message.chat.id, msg)
        bot.set_state(message.from_user.id, statesCRM.menu)
        menu(message)
    elif (message.text == 'Поиск по первичному ключу'):
        bot.send_message(message.chat.id, "Введите название ключа и условие например\nID = 10")
        bot.set_state(message.from_user.id, statesCRM.find)
        


@bot.message_handler(state = statesCRM.whereSelect)
def whereSLC(message):
    with bot.retrieve_data(message.chat.id) as data:
        img = cI.createIMG(data['table'], message.text)
        bot.send_photo(message.chat.id, img, caption= data['table'].nameTable)
        tempUserEdit[message.from_user.username].append(F'@{message.from_user.username}: Запросил таблицу с условием ')
        bot.set_state(message.chat.id, statesCRM.choice)
        message.text = data['table'].nameTable
        table(message)

@bot.message_handler(state = statesCRM.find)
def findPK(message):
    check = False
    msg = bot.send_message(message.chat.id, "Начал поиск")
    for j,i in enumerate(df.tablesAll):
        temp = df.tablesAll[i].selectAll(where=message.text)
        if (temp is not None and len(temp)>0):
            try:
                img = cI.createIMG(df.tablesAll[i], message.text)
                bot.send_photo(message.chat.id, img, caption= df.tablesAll[i].nameTable)
                check = True
            except:
                print(df.tablesAll[i].nameTable)
    if (not check):
        bot.send_message(message.chat.id, "Данные не найдены")
    bot.set_state(message.from_user.id, statesCRM.menu)
    menu(message)



@bot.message_handler(state = statesCRM.update)
def updateVal(message):
    with bot.retrieve_data(message.chat.id) as data:
        if (data['ind'] == 0  or data['ind'] == 2):
            if (data['ind'] == 2):
                data['column'].append([0]*2)
                data['column'][0][0] = data['cln'][-1]
                data['column'][0][1] = message.text
                data['ind'] = 5
            
            if (data['ind'] == 0):
                data['column'] = []
                data['where'] = ''
                data['cln'] = []

            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
            if (data['ind'] == 5):
                markup_reply.add('Закончить')
            
            print(data['column'])
            data['ind'] = 1
            for tab in data['table'].atribute:
                if (not tab[0] in data['cln']):
                    markup_reply.add(tab[0])
            
            bot.send_message(message.chat.id, 'Добавьте изменяемую колонку', reply_markup=markup_reply)

        elif (data['ind'] == 1):
            if (message.text == 'Закончить'):
                bot.send_message(message.chat.id, "Введите условие! Пример:\nID > 10 AND NAME LIKE '%Данила%'", reply_markup=None)
                data['ind'] = 4
            else:
                data['cln'].append(message.text)
                data['ind'] = 2
                bot.send_message(message.chat.id, 'Введите новое значение Пример:\nСтрока\n999\n')

        elif (data['ind'] == 4):
            data['table'].updateValues(data['column'], where = message.text)
            tempUserEdit[message.from_user.username].append(F'@{message.from_user.username}: Изменил значение в таблице {data["table"].nameTable}\n{data["column"]=} {message.text}')
            bot.send_message(message.chat.id, "Изменения внесены", reply_markup=None)
            message.text = data['table'].nameTable
            table(message)


@bot.message_handler(state = statesCRM.add)
def addNewVal(message):
    with bot.retrieve_data(message.chat.id) as data:
        data['table'].insertIntoText(message.text)
        bot.send_message(message.chat.id, 'Элемент успешно добавлен')
        tempUserEdit[message.from_user.username].append(F'@{message.from_user.username}: Добавил значение в таблицу {data["table"].nameTable}\n{message.text}')
        bot.set_state(message.chat.id, statesCRM.choice)
        message.text = data['table'].nameTable
        table(message)

@bot.message_handler(state = statesCRM.delete)
def deletVal(message):
    with bot.retrieve_data(message.chat.id) as data:
        data['table'].deleteRow(message.text)
        bot.send_message(message.chat.id, 'Элемент успешно удалён')
        tempUserEdit[message.from_user.username].append(F'@{message.from_user.username}: Удалин значения в таблице {data["table"].nameTable}\n{message.text}')
        bot.set_state(message.chat.id, statesCRM.choice)
        message.text = data['table'].nameTable
        table(message)



@bot.message_handler(state = statesCRM.choice)
def choice(message):
    txt = message.text
    if (txt == conf.buttons[0]):
        menu(message)
    elif (txt == conf.buttons[1]):
        with bot.retrieve_data(message.chat.id) as data:
           img = cI.createIMG(data['table'])
           bot.send_photo(message.chat.id, img, caption= data['table'].nameTable)
           tempUserEdit[message.from_user.username].append(F'@{message.from_user.username}: Запросил картинку всей таблицы {data["table"].nameTable}')
    elif (txt == conf.buttons[2]):
        bot.send_message(message.chat.id, "Введите условие! Пример:\nID > 10 AND NAME LIKE '%Данила%'", reply_markup=None)
        bot.set_state(message.chat.id, state= statesCRM.whereSelect)
    elif (txt == conf.buttons[3]):
        bot.set_state(message.chat.id, state= statesCRM.update)
        updateVal(message)
    elif (txt == conf.buttons[4]):
       with bot.retrieve_data(message.chat.id) as data:
            msg = data['table'].atribute[1][0]
            for i in data['table'].atribute[2:]:
               msg += ', ' + i[0]
            msg += '\n' + (str('Число') if (data['table'].atribute[1][1] == 1) else 'Строка')
            for i in data['table'].atribute[2:]:
               msg += ', ' + (str('Число') if (i[1] == 1) else 'Строка')
            msg += '\n\nПример:\nДанила,322,13.09.2002'
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup_reply.add('Назад')
            bot.send_message(message.chat.id, 'Введите в формате\n' + msg, reply_markup=markup_reply)
            bot.set_state(message.chat.id, statesCRM.add)
    elif (txt == conf.buttons[5]):
        with bot.retrieve_data(message.chat.id) as data:
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
            markup_reply.add('Назад')
            bot.send_message(message.chat.id, "Введите условие! Пример:\nID > 10 AND NAME LIKE '%Данила%'", reply_markup= markup_reply)
            bot.set_state(message.chat.id, statesCRM.delete)
    else:
        bot.send_message(message.chat.id, 'Такой кнопки не существует!')
        with bot.retrieve_data(message.chat.id) as data:
            message.text = data['table'].nameTable
            table(message)

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling(skip_pending=True)