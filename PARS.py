#Импорты
from tkinter import *
from PIL import ImageTk, Image
from tkinter import scrolledtext
from datetime import datetime
from selenium import webdriver
from time import sleep
import smtplib
import os
import mimetypes                                            # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders        
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication                          




#"http://90.157.4.4:88/"


#Создание окна
#_______________Создание окна_______________
window = Tk()
window.title('АЗС.Онлайн')
window.geometry('800x600')
frame = Frame(window)
frame.pack()

def add_file():
    file = open("Email.txt", "a")
    file = open("Site.txt", "a")
    file = open("Time.txt", "a")


#Главное окно
def main_window():
    global frame, btn_EditEmail, btn_EditSite, btn_EditSite
    #Начальные файлы
    add_file()
    #Сбор данных
    file = (open("Email.txt", "r")).read()
    file = (open("Site.txt", "r")).read()
    file = (open("Time.txt", "r")).read()
    #ФРЕЙМ
    frame.destroy()
    frame = Frame(window)
    frame.pack()
    #Вверхнее название
    title = Label(frame, text = "АЗС Онлайн", font="Arial 40", bg = "#b44d56", fg = "white").grid(row=0, column=0)
    #Кнопки
    #Запуск программы
    btn_Start = Button(frame, text = "Запуск", font="Arial 15", fg = "red", width = 28, height = 2, command = start_pars).grid(row = 1, column = 0)
    #Добавить почту
    btn_EditEmail = Button(frame, text = "Изменить почты", font="Arial 15", width = 28, height = 2, command = edit_Email).grid(row = 2, column = 0)
    #Изменить сайт
    btn_EditSite = Button(frame, text = "Изменить сайт", font="Arial 15", width = 28, height = 2, command = edit_Site).grid(row = 3, column = 0)
    #Изменить время
    btn_EditTime = Button(frame, text = "Изменить время", font="Arial 15", width = 28, height = 2, command = edit_Time).grid(row = 4, column = 0)
    
    #Изменить время
    label_ManuallyScreenshot = Label(frame, text = '', font="Arial 15", width = 28, height = 2).grid(row = 5, column = 0)
    btn_ManuallyScreenshot = Button(frame, text = "Сделать скриншот и отправить", font="Arial 15", fg = "green", width = 28, height = 2, command = screenshot_now).grid(row = 6, column = 0)
    

#Запуск программы
def start_pars():
    global frame, label_timer
    frame.destroy()
    frame = Frame(window)
    frame.pack()
    #Выход
    btn_exit = Button(frame, text = "Выход", font="Arial 15", command = exit).grid(row = 0, column = 0)
    #Открытие почты
    email = (open("Email.txt", "r")).read()
    #Открытие времени
    time = (open("Time.txt", "r")).read()
    #Открытие сайта
    site = (open("Site.txt", "r")).read()
    #Таймер
    label_timer_p2 = Label(frame, text = "", font="Arial 15").grid(row = 1, column = 0)
    label_timer_p = Label(frame, text = "Время на данный момент:", font="Arial 15").grid(row = 2, column = 0)
    label_timer = Label(frame, text = "время", font="Arial 20", width = 28, height = 1)
    label_timer.grid(row = 3, column = 0)
    frame.after(0,Timer)
    #Время отправки
    label_timer_p2 = Label(frame, text = "", font="Arial 15").grid(row = 4, column = 0)
    label_send_p = Label(frame, text = "Время отправки:", font="Arial 15").grid(row = 5, column = 0)
    label_send = Label(frame, text = time, font="Arial 15").grid(row = 6, column = 0)
    #Сайт отправки
    label_site_p2 = Label(frame, text = "", font="Arial 15").grid(row = 7, column = 0)
    label_site_p = Label(frame, text = "Сайт сбора:", font="Arial 15").grid(row = 8, column = 0)
    label_site = Label(frame, text = site, font="Arial 15").grid(row = 9, column = 0)
    #Почты для отправки
    label_site_p = Label(frame, text = "", font="Arial 15").grid(row = 10, column = 0)
    label_site_p = Label(frame, text = "Почты:", font="Arial 15").grid(row = 11, column = 0)
    label_emails= scrolledtext.ScrolledText(frame, width=40, height=10)
    label_emails.grid(column=0, row=12) 
    label_emails.insert(INSERT, str(email))


#Таймер
def Timer():
    global label_timer, frame
    #Получение времени
    data = str(datetime.now())
    time = (data.split(" "))[1]
    time = (time.split("."))[0]
    #Изменение времени
    label_timer.configure(text = str(time))
    check_time(time = time)
    frame.after(1000,Timer)
    

#Проверка времени
def check_time(time):
    global label_timer
    times = (open("Time.txt", "r")).read()
    times = times.split(",")
    times.pop(len(times) - 1)
    if len(times) == 1:
        if str(time) == str(times[0]+":00"):
            screenshot_now()
    elif len(times) == 2:
        if str(time) == str(times[0]+":00") or str(time) == str(times[1]+":00"):
            screenshot_now()
    elif len(times) == 3:
        if str(time) == str(times[0]+":00") or str(time) == str(times[1]+":00") or  str(time) == str(times[2]+":00"):
            screenshot_now()
    elif len(times) == 4:
        if str(time) == str(times[0]+":00") or str(time) == str(times[1]+":00") or str(time) == str(times[2]+":00") or str(time) == str(times[3]+":00"):
            screenshot_now()
    elif len(times) == 5:
        if str(time) == str(times[0]+":00") or str(time) == str(times[1]+":00") or str(time) == str(times[2]+":00") or str(time) == str(times[3]+":00") or str(time) == str(times[4]+":00"):
            screenshot_now()
    elif len(times) == 6:
        if str(time) == str(times[0]+":00") or str(time) == str(times[1]+":00") or str(time) == str(times[2]+":00") or str(time) == str(times[3]+":00") or str(time) == str(times[4]+":00") or str(time) == str(times[5]+":00"):
            screenshot_now()
    elif len(times) == 7:
        if str(time) == str(times[0]+":00") or str(time) == str(times[1]+":00") or str(time) == str(times[2]+":00") or str(time) == str(times[3]+":00") or str(time) == str(times[4]+":00") or str(time) == str(times[5]+":00") or str(time) == str(times[6]+":00"):
            screenshot_now()
    elif len(times) == 8:
        if str(time) == str(times[0]+":00") or str(time) == str(times[1]+":00") or str(time) == str(times[2]+":00") or str(time) == str(times[3]+":00") or str(time) == str(times[4]+":00") or str(time) == str(times[5]+":00") or str(time) == str(times[6]+":00") or str(time) == str(times[7]+":00"):
            screenshot_now()
    elif len(times) == 9:
        if str(time) == str(times[0]+":00") or str(time) == str(times[1]+":00") or str(time) == str(times[2]+":00") or str(time) == str(times[3]+":00") or str(time) == str(times[4]+":00") or str(time) == str(times[5]+":00") or str(time) == str(times[6]+":00") or str(time) == str(times[7]+":00") or str(time) == str(times[8]+":00"):
            screenshot_now()
    elif len(times) == 10:
        if str(time) == str(times[0]+":00") or str(time) == str(times[1]+":00") or str(time) == str(times[2]+":00") or str(time) == str(times[3]+":00") or str(time) == str(times[4]+":00") or str(time) == str(times[5]+":00") or str(time) == str(times[6]+":00") or str(time) == str(times[7]+":00") or str(time) == str(times[8]+":00") or str(time) == str(times[8]+":00"):
            screenshot_now()
    



#Выход 
def exit():
    main_window()


#Изменить почту
def edit_Email():
    global frame, entry_email, emails
    #Открытие файла
    file = (open("Email.txt", 'r')).read()
    #Фрейм
    frame.destroy()
    frame = Frame(window)
    frame.pack()
    #Выход
    btn_exit = Button(frame, text = "Выход", font="Arial 15", command = exit).grid(row = 0, column = 0)
    #Добавить почту
    label_email_p = Label(frame, text = "Почта", width = 28, height = 2, font="Arial 15").grid(row = 1, column = 0)
    entry_email = Entry(frame, width = 28, font="Arial 15", fg = "green")
    entry_email.grid(row = 2, column = 0)
    btn_email = Button(frame, text = "Добавить", width = 28, height = 1, font="Arial 15", fg = "green", command = add_Email).grid(row = 3, column = 0)
    label_email_p = Label(frame, text = "", width = 28, height = 2, font="Arial 15").grid(row = 4, column = 0)
    #Почты
    label_email = Label(frame, text = "Уже добавленные почты", width = 28, height = 2, font="Arial 18").grid(row = 5, column = 0)
    emails= scrolledtext.ScrolledText(frame, width=40, height=10)
    emails.grid(column=0, row=6) 
    #Вставка с прошлого файла
    emails.insert(INSERT, str(file))
    #Кнопка обновить
    btn_update = Button(frame, text = "Обновить", width = 30, height = 2, font="Arial 15", fg = "green", command = edit_Email)
    btn_update.grid(row = 7, column = 0)
    btn_delete = Button(frame, text = "Удалить", width = 30, height = 2, font="Arial 15", fg = "#b44d56", command = clear_Email)
    btn_delete.grid(row = 8, column = 0)


#Очистить почты
def clear_Email():
    file = open("Email.txt", 'w+')
    edit_Email()

 
#Добавить почту
def add_Email():
    global entry_email, frame
    wr_email= "{}".format(entry_email.get())
    wr_email=str(wr_email)
    file = open("Email.txt", "a")
    file.write(wr_email)
    file.write(",")
    entry_email.delete(0, 'end')
    

#Изменить сайт
def edit_Site():
    global frame, entry_site
    #Взятие данных
    file = (open("Site.txt", "r")).read()
    #Фрейм
    frame.destroy()
    frame = Frame(window)
    frame.pack()
    #Выход
    btn_exit = Button(frame, text = "Выход", font="Arial 15", command = exit).grid(row = 0, column = 0)
    #Ввод 
    label_site_p = Label(frame, text = "", width = 28, height = 1, font="Arial 15").grid(row = 1, column = 0)
    label_site_p2 = Label(frame, text = "Сайт на данный момент:", width = 28, height = 2, font="Arial 18").grid(row = 2, column = 0)
    label_site = Label(frame, text = file, width = 28, height = 2, font="Arial 15").grid(row = 3, column = 0)
    entry_site = Entry(frame, width = 28, font="Arial 15", fg = "green")
    entry_site.grid(row = 4, column = 0)
    btn_site = Button(frame, text = "Перезаписать", width = 28, height = 1, font="Arial 15", fg = "green", command= overwrite_site)
    btn_site.grid(row = 5, column = 0)
    

#Перезаписать сайт
def overwrite_site():
    global wr_site
    wr_site= "{}".format(entry_site.get())
    wr_site=str(wr_site)
    file = open("Site.txt", "+w")
    file.write(str(wr_site))
    entry_site.delete(0, 'end')
    edit_Site()
    label_site = Label(frame, text = wr_site, width = 28, height = 2, font="Arial 15").grid(row = 3, column = 0)
    


#Изменить время
def edit_Time():
    global frame, entry_time, label_time
    #Сбор данных
    file = (open("Time.txt", "r")).read()
    #Фрейм
    frame.destroy()
    frame = Frame(window)
    frame.pack()
    #Выход
    btn_exit = Button(frame, text = "Выход", font="Arial 15", command = exit).grid(row = 0, column = 0)
    #
    label_time_p = Label(frame, text = "", width = 28, height = 1, font="Arial 15").grid(row = 1, column = 0)
    label_time_p2 = Label(frame, text = "В какое время отправлять:", width = 28, height = 2, font="Arial 18").grid(row = 2, column = 0)
    label_time = Label(frame, text = file, width = 28, height = 2, font="Arial 15").grid(row = 3, column = 0)
    entry_time = Entry(frame, width = 28, font="Arial 15", fg = "green")
    entry_time.grid(row = 4, column = 0)
    btn_time = Button(frame, text = "Записать", width = 28, height = 1, font="Arial 15", fg = "green", command = add_time)
    btn_time.grid(row = 5, column = 0)
    btn_time = Button(frame, text = "Удалить", width = 28, height = 1, font="Arial 15", fg = "#b44d56", command = del_time)
    btn_time.grid(row = 6, column = 0)


#Добавить время
def add_time():
    global wr_time, entry_time
    wr_time= "{}".format(entry_time.get())
    wr_time=str(wr_time)
    file = open("Time.txt", "a")
    file.write(str(wr_time))
    file.write(",")
    entry_time.delete(0, 'end')
    file = (open("Time.txt", "r")).read()
    label_time = Label(frame, text = file, width = 28, height = 2, font="Arial 15")
    edit_Time()

    
#Удалить время
def del_time():
    global label_time
    file = open("Time.txt", "+w")
    file.write("")
    edit_Time()
    file = (open("Time.txt", "r")).read()
    label_time = Label(frame, text = file, width = 28, height = 2, font="Arial 15").grid(row = 3, column = 0)
    entry_time = Entry(frame, width = 28, font="Arial 15", fg = "green")



#Скрин сайта
def screenshot_site(site, name):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument(f'window-size={1080},{1800}')
    options.add_argument('hide-scrollbars')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(site)
    sleep(1)
    browser.save_screenshot("Screenshots/" + name)
    
    
#Отправка по почте
def send_email(addr_to, files):
    addr_from = "bot_azs@mail.ru"                         # Отправитель
    password  = "454565leo"                               # Пароль
    date = datetime.now()
    date = str(date).split(' ')
    date[1] = (date[1].split("."))[0]
    date = date[0] + "_" +date[1]
    

    msg = MIMEMultipart()                                   # Создаем сообщение
    msg['From']    = addr_from                              # Адресат
    msg['To']      = addr_to                                # Получатель
    msg['Subject'] = "АЗС сводка " + str(date)                               # Тема сообщения

    body = "files"                                         # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))                     # Добавляем в сообщение текст

    part = MIMEApplication(open(files, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=files)
    msg.attach(part)

    
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)    # Создаем объект SMTP           # Создаем объект SMTP
    #server.set_debuglevel(True)                         # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    #server.starttls()                                   # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                   # Получаем доступ
    server.send_message(msg)                            # Отправляем сообщение
    server.quit()                                       # Выходим                                      # Выходим                                         # Выходим
    


def screenshot_now():
    #Открытие почт
    file = (open("Email.txt", "r")).read()
    email = file.split(",")
    email.pop(len(email) - 1)
    #Открытие сайта
    site = (open("Site.txt", "r")).read()
    #Получение времени
    data = str(datetime.now()).split(' ')
    mounth = data[0]
    time = data[1]
    time = (time.split("."))[0]
    time = time.split(":")
    time = time[0] + "." + time[1] +"."+ time[2]
    data = mounth + "_" + time + ".png"
    #Отправка
    screenshot_site(site = site, name = str(data))
    for i in email:
        send_email(addr_to = i, files = str("Screenshots/" + data))
    


main_window()

#Луп
window.mainloop()