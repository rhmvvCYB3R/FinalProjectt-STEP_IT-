from tkinter import *
from PIL import Image, ImageTk #чтобы можно было добавить фотки
import webbrowser #добавил чтобы мог управлять ссылками
from tkinter import messagebox

adminka = {"admin":"admin"}
usernew_acc = {}

class Schedule:
    def __init__(self, time, subject, group, room, count_student):
        self.time = time
        self.subject = subject
        self.group = group
        self.room = room
        self.count_student = count_student
    def __str__(self):
        
        return (f"\nВремя -- {self.time} \nНазвание предмета -- {self.subject} \nНазвание группы -- {self.group} \nНазвание кабинета -- {self.room} \nКолл.студента -- {self.count_student}")

list_schedule = [
    Schedule("10:00","Python","12a", "6", "13"),
    Schedule("12:00","Cybersecurity", "10b","5","15"),
    Schedule("14:00","DevOps","11e","3",'10')
    
]    

class Administrator:
    

    def add_schedule():
        print("\t\t\tДобавление расписания!")
        time = input("Введите время -- ")
        subject = input("Введите название предмета -- ")
        group = input("Введите название группы-- ")
        room = input("Введите номер кабинета -- ")
        count_student = input("Введите колл-во студентов -- ")
        adder = Schedule(time,subject,group,room,count_student)
        list_schedule.append(adder)
        print("\nУспешно добавлено!")

        

    # def remove_schedule():
    #     print("\t\t\tУдаление расписания!")
    #     subject = input("Введите название предмета -- ")
    #     global list_schedule
    #     found = False
    #     for i in list_schedule:
    #         if i.subject == subject:
    #             list_schedule.remove(i)
    #             print(f"\n{subject} -- Удалено!")
    #             found = True
    #             break
    #     if not found:
    #         print(f"\n{subject} -- Не найдено")
           
               
            
                
    # def change_room():
    #     print("\t\t\tИзменить кабинет по времени")
    #     time = input("\nВведите время урока, чтобы найти кабинет --  ")
    #     change_room = input("Введите новый номер кабинета -- ")
    #     for schedule in list_schedule:
    #         if schedule.time == time:
    #             schedule.room = change_room
    #             print(f"\nКабинет успешно поменян на {change_room}")
    #             print("__________________________")
    #             print(schedule)
    #             return
    #     print(f"\nНе \nнайден время предмета -- {time} ")

    # def search_by_time():
    #     print("\t\t\tПоиск расписания по времени")
    #     search_time = input("\nВведите время для поиска расписания -- ")
    #     found = False
    #     for schedule in list_schedule:
    #         if schedule.time == search_time:
    #             print(schedule)
    #             found = True
    #     if not found:
    #         print(f"\nРасписание на {search_time} не найдено")

    

    # def show_schedule2():
    #     for i in list_schedule:
    #         print("__________________________")
    #         print(i)

    # def logout():
    #     input = "Нажмите на что то, чтобы выйти  -- "
    #     main()



mystat = Tk()
mystat.title('Mystat')
mystat.geometry("1270x750+140+20")
mystat.resizable(False,False)
mystat.iconbitmap("files/logo.ico")
mystat.config(background="#FFFFFF")

#user_ACC_FRAME_____________
def user_acc_frame():
    user_frame = Frame(mystat, width=1270, height=750, bg="#FFFFFF")
    user_frame.place(x=0, y=0)




#______________REGISTARTION FRAME
def registration_menu():
    mystat_reg = Frame(mystat, width=1270, height=750, bg="#FFFFFF")
    mystat_reg.place(x=0, y=0)
    
    fon = Image.open("files/reg_menu_fon.png")
    resized_fon = fon.resize((1000, 750))
    reg_fon = ImageTk.PhotoImage(resized_fon)
    reg_fon_label = Label(mystat_reg, image=reg_fon, bd=0)
    reg_fon_label.place(x=460, y=0)
    reg_fon_label.image = reg_fon # Сохранение ссылки на изображение

    def clear_newlogin(event):
        if newlogin.get() == "Введите логин*: ":
            newlogin.delete(0, "end")
            newlogin.config(fg="black")   
    def clear_newpass(event):        
        if newpass_input.get() == "Введите пароль*: ":
            newpass_input.delete(0, "end")
            newpass_input.config(fg="black")
    def clear_newemail(event):    
        if new_gmail.get() == "Введите E-mail*: ":
            new_gmail.delete(0, "end")
            new_gmail.config(fg="black")
        
    register_text = Label(mystat_reg, text="Регистрация аккаунта:")
    register_text.config(bg='#FFFFFF',
                    fg='#0000FF',
                font= ("Arial Black" , 18))
    register_text.place(x=35,y=30)
    





    newlogin = Entry(mystat, validate="key",bd=0.5,justify="left", fg= "black")
    newlogin.config(
            bg="#FFFFFF",
            fg="grey",
            font= ("Times" , 12), )
    newlogin.insert(0,"Введите логин*: ")
    newlogin.place(x=50, y= 130,height=30,width=280)
    newlogin.bind("<FocusIn>", clear_newlogin)

    newpass_input = Entry(mystat, validate="key",bd=0.5,justify="left", fg= "black")
    newpass_input.config(
                bg="#FFFFFF",
                fg="grey",
                font= ("Times" , 12), )
    newpass_input.insert(0,"Введите пароль*: ")
    newpass_input.place(x=50, y= 180,height=30,width=280)
    newpass_input.bind("<FocusIn>", clear_newpass)

    new_gmail = Entry(mystat, validate="key",bd=0.5,justify="left", fg= "black")
    new_gmail.config(
                bg="#FFFFFF",
                fg="grey",
                font= ("Times" , 12), )
    new_gmail.insert(0,"Введите E-mail*: ")
    new_gmail.place(x=50, y= 230,height=30,width=280)
    new_gmail.bind("<FocusIn>", clear_newemail)
    #Create_Acc_____________________
    def register_user():
        global usernew_acc
        username = newlogin.get()
        password = newpass_input.get()
        email = new_gmail.get()
        
        if username in ["", "Введите логин*: "] or password in ["", "Введите пароль*: "] or email in ["", "Введите E-mail*: "]:
            messagebox.showerror("Ошибка", "Введите данные!")
            return
        if len(password) < 8:
            messagebox.showerror("Ошибка", "Пароль должен содержать больше 8-ми символов!")
            return
        
        usernew_acc = {username:password,
                      email:password
                                         }
        
        messagebox.showinfo("Успех", "Вы успешно зарегистрированы!")
        print(usernew_acc)


    sign_up_fon = Image.open("files/sign_up.png")
    resized_sign_up = sign_up_fon.resize((300, 60))
    sign_up = ImageTk.PhotoImage(resized_sign_up)
    sign_up_btn = Button(mystat_reg, image=sign_up, bd=0, bg='#FFFFFF')
    sign_up_btn.image = sign_up # Сохраняем ссылку на изображение чтобы сборщик мусора не удалял!
    sign_up_btn.config(command=register_user)
    sign_up_btn.place(x=45, y=280)

    go_back_fon = Image.open("files/go_back1.png")
    resized_go_back = go_back_fon.resize((160, 60))
    go_back = ImageTk.PhotoImage(resized_go_back)
    go_back_btn = Button(mystat_reg, image=go_back, bd=0, bg='#FFFFFF',command=main_view)
    go_back_btn.image = go_back # Сохраняем ссылку на изображение чтобы сборщик мусора не удалял!
    go_back_btn.place(x=12, y=660)
    
        




def main_view():
    #______________MAIN VIEW
    main = Frame(mystat, width=1270, height=750, bg="#FFFFFF")
    main.place(x=0, y=0)
    
    image1 = PhotoImage(file="files/bg_photo.png")
    image1_label = Label(main, image=image1,bd=0,width=800)
    image1_label.place(x=550,y=0)
    image1_label.image = image1  # Сохраняем ссылку на изображение

    mystat_text = Label(main, text='MyStat')
    mystat_text.config(bg='#FFFFFF',
                        fg='#563bea',
                    font= ("Arial Black" , 14))
    mystat_text.place(x=20,y=20)

    language_text = Label(main, text='🌐 AZ')
    language_text.config(bg='#FFFFFF',
                        fg='black',
                    font= ("Sans-serif" , 11))
    language_text.place(x=465,y=25)

    entry_text = Label(main, text='Вход')
    entry_text.config(bg='#FFFFFF',
                        fg='black',
                    font= ("Ubuntu" , 14))
    entry_text.place(x=225,y=200)

    #_____Очистка Поля ВВОДА ЛОГИН И ПАРОЛЬ!
    def clear_name(event):
        if name_input.get() == "Введите E-mail или Логин*: ":
            name_input.delete(0, "end")
            name_input.config(fg="black")

    def clear_password(event):
        if password_input.get() == "Пароль*: ":
            password_input.delete(0, "end")
            password_input.config(fg="black")
    #event: Параметр event передается автоматически, 
    #когда функция привязана к событию через метод bind. Он содержит информацию о событии (например, какой виджет вызвал событие).
    #_______________________________________

    #___________Ввод логин
    name_input = Entry(main, validate="key",bd=0.5,justify="left", fg= "black")
    name_input.config(
                bg="#fafafa",
                fg="grey",
                font= ("Times" , 12), )
    name_input.insert(0,"Введите E-mail или Логин*: ")
    name_input.place(x=115, y= 260,height=30,width=280)
    name_input.bind("<FocusIn>", clear_name)
    #________________________________________
    #bind("<FocusIn>", clear_name): Этот метод привязывает обработчик события
    #clear_name к событию "<FocusIn>", которое происходит, когда виджет получает фокус 
    # (например, пользователь щелкает на виджете или переключается на него с помощью клавиатуры).
    #_____________________________________________________________________________________________

    #____________________________Ввод пароля
    password_input = Entry(main, validate="key",bd=0.5,justify="left", fg= "black")
    password_input.config(
                bg="#fafafa",
                fg="grey",
                font= ("Times" , 12), )
    password_input.insert(0,"Пароль*: ")
    password_input.place(x=115, y= 310,height=30,width=280)
    password_input.bind("<FocusIn>", clear_password)
    #___________________________________________________

    def admin_log_pass_check():
        global adminka
        global usernew_acc
        login = name_input.get()
        password = password_input.get()
        if login in adminka and adminka[login] == password:
            admin_frame()  # Открываем админ фрейм
        elif login in usernew_acc and usernew_acc[login] == password: #["Пароль"] - извлекает значение по ключу "Пароль" из словаря
            user_acc_frame() #открываем юзер фрейм
       
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")
        

    
    #_____________Кнопка для создания нового аккаунта!
    create_acc_btn = Button(main, text='Нет аккаунта?',bd=0,command=registration_menu)
    create_acc_btn.config(bg='#fafafa',
                        fg='#696969',
                    font= ("Ubuntu" , 11))
    create_acc_btn.place(x=295,y=345)
    #______________________
    #_________________Кнопка для входа
    sign =Image.open("files/singin_button.png")
    resized_sign_in = sign.resize((290, 45))
    sign_in = ImageTk.PhotoImage(resized_sign_in)
    sign_in_btn = Button(main, image=sign_in, bd=0, bg = '#fafafa', command=admin_log_pass_check )
    sign_in_btn.place(x=110,y=390)
    sign_in_btn.image = sign_in

    #___ФОТКИ КАК КНОПКИИ_______________
    def open_google_play():
        webbrowser.open("https://play.google.com/store/apps/details?id=com.reactmystat&hl=")

    def open_apple_store():
        webbrowser.open("https://apps.apple.com/gb/app/mystat/id1404383586?l=")

    google = Image.open("files/icon_googleplay.png")
    resized_google = google.resize((135, 45))
    google_play = ImageTk.PhotoImage(resized_google)
    google_play_button = Button(main, image=google_play, bd=0, command=open_google_play, bg = '#fafafa')
    google_play_button.place(x=115, y=550)
    google_play_button.image = google_play

    apple = Image.open("files/Appstore_logo.png")
    resized_apple = apple.resize((135, 45))
    apple_store = ImageTk.PhotoImage(resized_apple)
    apple_store_button = Button(main, image=apple_store, bd=0, command=open_apple_store,bg = '#fafafa')
    apple_store_button.place(x=270, y=550)
    apple_store_button.image = apple_store
    #__________________________________________________________________




#___________Admin__ACCOUNT____FRAME_____
def admin_frame():
    admin_frame = Frame(mystat, width=1270, height=750, bg="#FFFFFF")
    admin_frame.place(x=0, y=0)
    mystat_text = Label(admin_frame, text='MyStat')
    mystat_text.config(bg='#FFFFFF',
                        fg='#563bea',
                    font= ("Arial Black" , 14))
    mystat_text.place(x=20,y=20)

    quit_btn =Image.open("files/exitbtn.png")
    resized_quit_btn_in = quit_btn.resize((35, 35))
    quit_btn_in = ImageTk.PhotoImage(resized_quit_btn_in)
    quit_btn_in_btn = Button(admin_frame, image=quit_btn_in, bd=0, bg = '#fafafa',command=main_view )
    quit_btn_in_btn.place(x=1220,y=15)
    quit_btn_in_btn.image = quit_btn_in

main_view()
mystat.mainloop()


