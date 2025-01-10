import logging as log

version = '1.22.0'
log.basicConfig(filename='project.log' , filemode='w' , format=f'%(levelname)s - %(asctime)s - %(processName)s - {version} : %(message)s ')

log.critical('Starting ...')
import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
import streamlit as st
import time
import os
from DML import Insert_in_customer , Insert_to_vehicle , Insert_to_station , Insert_to_ticket 
from DQL import delete_fly , Edit_fly , get_from_vehicle , insert_into_customer , get_id_from_vehicle , get_from_customer , delete_from_customer 
log.critical('Importing ...')


API_TOKEN = 'Your token'


bot = telebot.TeleBot(API_TOKEN)
hideboard = ReplyKeyboardRemove()

lst_name = []
admins = [6728418988] 



command = {
    'start':'بات را شروع کنید',
    'buy':'خرید خود را آزاد کنید',
    'acount':'اطلاعات حساب خود را ببینید',
    'login':'حساب خود را بسازید',
    'Customer_Support':'پشتیبانی ۲۴ ساعته',
    'delete_acount':'اکانت خود را پاک کنید'
}

admins_commands = {
    'add_fly':'پرواز قابل رزرو جدیدی را اضافه کنید ',
    'delete_fly':'پروازی را حذف کنید',
    'edit_fly':'پروازی را تغییر دهید',
    'Technical_Support':'پشتیبانی برای مشکلات بوجود آمده یا سوالات'
}


message_id_channel = {
    'support'       :   2 ,
    'support_bug'   :   3
}


user_step = dict()


def listener(messages):   
    for m in messages:
        if m.content_type == 'text':
            print(f'{m.chat.first_name} [{m.chat.id}]: {m.text}') 
            
bot.set_update_listener(listener)


@bot.message_handler(commands=['start'])
def command_start_handler(message):
    cid = message.chat.id
    bot.send_message(cid, 'خوش آمدید', reply_to_message_id=message.message_id)
    log.critical('Starting bot ...')
    
    

@bot.message_handler(commands=['help'])
def command_help_handeler(message):
    cid = message.chat.id
    if cid not in admins:
        txt = 'لیست کامند ها:\n'
        for comm , desc in command.items():
            txt += f'/{comm:<18} - {desc}\n'
        bot.send_message(cid , txt)
    elif cid in admins:
        txt = 'لیست کامند ها:\n'
        for comman , des in command.items():
            txt += f'/{comman:<18} - {des}\n' 
        txt += "کامند های ادمین ها:\n"
        for comm , desc in admins_commands.items():
            txt += f'/{comm:<18} - {desc}\n'
        bot.send_message(cid , txt)


@bot.message_handler(commands= ['Customer_Support'])
def Customer_Support_handler(message):
    cid = message.chat.id
    ch_id = -1002395026478
    bot.copy_message(cid , ch_id , message_id_channel['support'])


@bot.message_handler(commands= ['Technical_Support'])
def Customer_Support_handler(message):
    cid = message.chat.id
    ch_id = -1002395026478
    bot.copy_message(cid , ch_id , message_id_channel['support_bug'])


@bot.message_handler(commands=['add_fly'])
def admin_add_fly_handler(message):
    cid = message.chat.id
    if cid in admins:
        bot.send_message(cid , 'لطفا کلاس هواپیما و اسم کمپانی و اسم هواپیما و تعداد سرنشینان را وارد اینگونه وارد کنید ...*...*...*... :')
        user_step[cid] = 'adm_add'
    elif cid not in admins:
        return


@bot.message_handler(func= lambda m : user_step.get(m.chat.id) == 'adm_add')
def admin_step_add_handler(message):
    cid = message.chat.id
    cls , com_name , plane_name , passengers = message.text.split('*')
    Insert_to_vehicle('plane' , cls , com_name , plane_name , int(passengers))
    bot.send_message(cid , 'با موفقیت ثبت شد')
    user_step[cid] = 0
    log.critical('Adding flies ...')

@bot.message_handler(commands=['delete_fly'])
def delete_fly_handler(message):
    cid = message.chat.id
    if cid not in admins:
        return
    bot.send_message(cid , 'لطفا آي دی پرواز مورد نطر را وارد کنید :')
    user_step[cid] = 'add_fl'


@bot.message_handler(func= lambda m : user_step.get(m.chat.id) == 'add_fl')
def add_fly_handler(message):
    cid = message.chat.id
    id_fly = message.text
    delete_fly(id_fly)
    bot.send_message(cid , 'با موفقیت حذف شد !')
    log.critical('Deleting flies ...')


@bot.message_handler(commands= ['acount'])
def watch_acount_handler(message):
    cid = message.chat.id
    image = bot.get_user_profile_photos(cid)
    l_image = image.photos[-1][-1]
    f_id = l_image.file_id
    if get_from_customer(cid) != 'er':
        bot.send_photo(cid , f_id , caption= f'{get_from_customer(cid)} \nبرای پاک کردن حساب خود : /delete_acount')
    else :
        bot.send_message(cid , 'شما اکانتی ندارید لطفا اول اکانت بسازید ! /login برای ساخت اکانت .')


@bot.message_handler(commands= ['delete_acount'])
def delete_acount_handler(message):
    cid = message.chat.id
    if get_from_customer(cid) == 'er':
        bot.send_message(cid , 'شما اکانتی برای حذف کردن ندارید ! \n برای ساخت اکانت : /login')
    else :
        delete_from_customer(cid)
        bot.send_message(cid , 'اکانت شما با موفقیت حذف شد . در حال گرفتن اطلاعات ...')
        bot.send_message(cid , 'لطفا اسم و فامیلی و شماره تلفن خود را اینگونه وارد کنید اسم-فامیلی-شماره')
        user_step[cid] = 'Nn'
        log.critical('Deleteing acount ...')



@bot.message_handler(commands= ['login'])
def login_customer(message):
    cid = message.chat.id
    bot.send_message(cid , 'لطفا اسم و فامیلی و شماره تلفن خود را اینگونه وارد کنید اسم-فامیلی-شماره')
    user_step[cid] = 'Nn'



@bot.message_handler(func= lambda m : user_step.get(m.chat.id) == 'Nn')
def login_customer_handler(message):
    cid = message.chat.id
    fname , lname , pnum = message.text.split('-')
    user_step[cid] = None
    if len(pnum) == 11 :
        if get_from_customer(cid) == 'er':
            insert_into_customer(cid , fname , lname , pnum)
            bot.send_message(cid , 'اکانت شما ذخیره شد !')
            bot.send_message(cid , 'برای دیدن مشخصات خود /acount')
            user_step[cid] = None
        else :  
            bot.send_message(cid , 'شما از قبل اکانت دارید ! برای دیدن اکانت خود : /acount')
            user_step[cid] = None
    else :
        bot.send_message(cid , 'لطفا یک شماره تلفن معتبر وارد نمایید !')
        user_step[cid] == 'Nn'
        log.critical('Logining ...')
   


@bot.message_handler(commands=['buy'])                       
def button_flight_handler(message):
    cid = message.chat.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('پرواز ✈')
    bot.send_message(cid, 'انتخاب کنید :', reply_markup = markup)


@bot.message_handler(commands=['edit_fly'])
def edit_fly_handler(message):
    cid = message.chat.id
    if cid not in admins:
        return
    bot.send_message(cid , 'لطفا آي دی پرواز مورد نظر را وارد کنید و بخش مورد نظر برای تغییر را اینگونه وارد کنید آی دی*ستون*مقدار :')
    user_step[cid] = 'ade_fl'


@bot.message_handler(func= lambda m : user_step.get(m.chat.id) == 'ade_fl')
def admin_step_edit_fly_handler(message):
    cid = message.chat.id
    id_fly , column , amount = message.text.split('*')
    if column == 'sarneshinan':
        Edit_fly(int(amount), column , int(id_fly))
    else :
        Edit_fly(amount, column , int(id_fly))
    bot.send_message(cid , 'ذخیره شد !')
    user_step[cid] = None
    log.critical('Editing flies ...')
 
    

@bot.message_handler(func= lambda m : m.text == 'پرواز ✈')
def button_person_handler(message):
    cid = message.chat.id
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('تک نفره 👤')
    bot.send_message(cid , 'انتخاب کنید :' , reply_markup=markup)


@bot.message_handler(func= lambda m : m.text == 'تک نفره 👤')
def button_person_pressed_handler(message):
    cid = message.chat.id
    get_from_customer(cid)
    if get_from_customer(cid) == 'er':
        bot.send_message(cid , ' /login شما اکانتی ندارید لطفا اول اکانت بسازید !' , reply_markup= hideboard)
        user_step[cid] = 'Nn'
    else :
        bot.send_chat_action(cid , 'typing')
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add('رفت','رفت و برگشت','برگشت')
        bot.send_message(cid, 'انتخاب کنید :', reply_markup= markup)


@bot.message_handler(func= lambda m : m.text == 'رفت' or m.text == 'رفت و برگشت' or m.text == 'برگشت')                          
def user_step_chandtarafe(message):
    cid = message.chat.id
    chandtarafe = message.text
    bot.send_message(cid , 'لطفا شهر مبدا خود را وارد کنید :', reply_markup=hideboard)
    user_step[cid] = 'mabdae'

@bot.message_handler(func= lambda m : user_step.get(m.chat.id) == 'mabdae')
def user_step_mabdae(message):
    cid = message.chat.id
    bg = message.text
    bot.send_message(cid , 'لطفا شهر مقصد خود را وارد کنید :')
    user_step[cid] = 'maghsad'

@bot.message_handler(func= lambda m : user_step.get(m.chat.id) == 'maghsad')
def user_step_mabdae(message):
    cid = message.chat.id
    des = message.text
    bot.send_message(cid , 'لطفا تاریخ مورد نظر را وارد کنید اینگونه روز/ماه/سال :')
    user_step[cid] = 'HO'



@bot.message_handler(func= lambda m : user_step.get(m.chat.id) == 'HO')                      
def user_step_mabdae(message):
    if 'q' not in st.session_state:
        st.session_state.q = 0
    cid = message.chat.id
    Tarikh = message.text   
    day , month , year = Tarikh.split('/')
    print(int(day) , int(month) , int(year))
    if int(day) > 30 or int(day) < int(time.strftime('%e')) or int(month) > 12 or int(month) < int(time.strftime('%m')) or int(year) > int(time.strftime('%Y')) or int(year) < int(time.strftime('%Y')):
        bot.send_message(cid , 'لطفا یک تاریخ معتبر وارد کنید .')
        user_step[cid] = 'HO'
    else :
        user_data[cid] = {'Tarikh' : Tarikh}
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton('-->' , callback_data='+'))                       
        markup.add(InlineKeyboardButton('✅' , callback_data='✅'))
        lst_id = get_from_vehicle(x= 'no' , y= None , z= None)
        dict_fly = get_from_vehicle(x= 'yes' , y= st.session_state.q , z= lst_id[st.session_state.q])               
        bot.send_message(cid , f"model : {dict_fly.get('model_vehicle')} \nclass : {dict_fly.get('class_vehicle')} \ncompany : {dict_fly.get('company_name')} \nmodel plane : {dict_fly.get('plane_name')} \ntedad sarneshinan : {dict_fly.get('sarneshinan')}" , reply_markup= markup)


@bot.callback_query_handler(func= lambda call: True)
def callback_handler(call):
    if 's' not in st.session_state:
        st.session_state.s = 0
    print(st.session_state.s)
    id = call.id
    cid = call.message.chat.id
    mid = call.message.message_id
    data = call.data
    try : 
        if data == '+':
            st.session_state.s += 1
            lst_id = get_from_vehicle(x= 'no' , y= None , z= None)
            dict_fly = get_from_vehicle(x= 'yes' , y= st.session_state.s , z= lst_id[st.session_state.s])
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton('<--' , callback_data='-') , InlineKeyboardButton('-->' , callback_data='+'))                 
            markup.add(InlineKeyboardButton('✅' , callback_data='✅'))
            bot.edit_message_text(f"model : {dict_fly.get('model_vehicle')} \nclass : {dict_fly.get('class_vehicle')} \ncompany : {dict_fly.get('company_name')} \nmodel plane : {dict_fly.get('plane_name')} \ntedad sarneshinan : {dict_fly.get('sarneshinan')}" , chat_id= cid , message_id= mid , reply_markup = markup)
            
            
        if data == '-':
            st.session_state.s -= 1
            lst_id = get_from_vehicle(x= 'no' , y= None , z= None)
            dict_fly = get_from_vehicle(x= 'yes' , y= st.session_state.s , z= lst_id[st.session_state.s])
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton('<--' , callback_data='-') , InlineKeyboardButton('-->' , callback_data='+'))                
            markup.add(InlineKeyboardButton('✅' , callback_data='✅'))
            bot.edit_message_text(f"model : {dict_fly.get('model_vehicle')} \nclass : {dict_fly.get('class_vehicle')} \ncompany : {dict_fly.get('company_name')} \nmodel plane : {dict_fly.get('plane_name')} \ntedad sarneshinan : {dict_fly.get('sarneshinan')}" , chat_id= cid , message_id= mid , reply_markup = markup)
                
            
        if data == '✅':
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add('رزرو')
            bot.send_message(cid, 'انتخاب کنید :', reply_markup = markup)
            user_step[cid] = 'cont'

    except :
        pass

@bot.message_handler(func= lambda m : user_step.get(m.chat.id) == 'cont')
def continue_handler(message):
    cid = message.chat.id
    bot.send_message(cid , 'عملیات با موفقیت انجام شد!' , reply_markup= hideboard)


@bot.message_handler(func= lambda message: True)
def other_messages(message):
    bot.reply_to(message , 'کاربر گرامی این یک ربات تلگرام است\nیک چت خصوصی یا گروه یا کانال نیست\nلطفا دستوری معتبر وارد کنید')


bot.infinity_polling()