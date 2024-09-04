from tkinter import *
from PIL import Image, ImageTk #чтобы можно было добавить фотки
import webbrowser #добавил чтобы мог управлять ссылками
from tkinter import messagebox


class Users:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def __str__(self): #Сам не понял для чего я это создал!, но пусть пока остаётся
        return f'''
______________________________

Имя - {self.name}
Пароль - {self.password}            
Э-почта - {self.email}
__________________________

'''

    def user_reg(self):
        username = self.name
        password = self.password
        email = self.email
        
        if username in ["", "Введите логин*: "] or password in ["", "Введите пароль*: "] or email in ["", "Введите E-mail*: "]:
            messagebox.showerror("Ошибка", "Введите данные!")
            return
        if len(password) < 8:
            messagebox.showerror("Ошибка", "Пароль должен содержать больше 8-ми символов!")
            return

        with open("data/users_data.txt", 'a') as file:
            file.write(f"{username},{password},{email}\n")
            messagebox.showinfo("Успех","Вы успешно создали аккаунт!")
    
    def admin_users_log_pass_check(login,password):
        import admin_log
        
        with open("data/users_data.txt", 'r') as file:
            for data in file:
                data = data.strip()#метод строки, который удаляет пробелы в начале и в конце строки.
                user_data = data.split(",")# разделяет очищенную строку на список элементов по запятым.
                username, user_password, email = user_data #происходит распаковка списка или кортежа на несколько переменных.
                if login == username or login == email and password == user_password:
                    user_acc_frame()
                    return

        if login == admin_log.username and password == admin_log.password:
            admin_frame()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль.")
   
    
        

mystat = Tk()
mystat.title('Mystat')
mystat.geometry("1270x750+140+20")
mystat.resizable(False,False)
mystat.iconbitmap("files/logo.ico")
mystat.config(background="#FFFFFF")

#____________user_ACC_FRAME_____________
def user_acc_frame():
    user_frame = Frame(mystat, width=1270, height=750, bg="#DCDCDC")
    user_frame.place(x=0, y=0)



#___________Admin__ACCOUNT____FRAME_____
def admin_frame():
    admin_frame = Frame(mystat, width=1270, height=750, bg="#DCDCDC")
    admin_frame.place(x=0, y=0)

    design1 = Label(admin_frame)
    design1.config(bg='#D3D3D3',padx=700,pady=20)
    design1.place(x=0,y=0)

    design2 = Label(admin_frame)
    design2.config(bg='#D3D3D3',padx=30,pady=500)
    design2.place(x=0,y=0)


    admin_text = Label(admin_frame, text='admin')
    admin_text.config(bg='#D3D3D3',
                        fg='#563bea',
                    font= ("Ubuntu" , 13),bd=0)
    admin_text.place(x=85,y=35)


    mystat_text = Label(admin_frame, text='MyStat')
    mystat_text.config(bg='#D3D3D3',
                        fg='#563bea',
                    font= ("Arial Black" , 14),bd=0)
    mystat_text.place(x=75,y=9)

    step_logo =Image.open("files/step_logo2.png")
    resized_step_logo_in = step_logo.resize((65, 75))
    step_logo_in = ImageTk.PhotoImage(resized_step_logo_in)
    step_logo_in_bg = Label(admin_frame, image=step_logo_in, bd=0, bg = '#D3D3D3' )
    step_logo_in_bg.place(x=0,y=0)
    step_logo_in_bg.image = step_logo_in# Сохраняем ссылку на изображение
    
    admin_logo =Image.open("files/admin_anonim.png")
    resized_admin_logo_in = admin_logo.resize((55, 55))
    admin_logo_in = ImageTk.PhotoImage(resized_admin_logo_in)
    admin_logo_in_bg = Label(admin_frame, image=admin_logo_in, bd=0, bg = '#D3D3D3' )
    admin_logo_in_bg.place(x=5,y=95)
    admin_logo_in_bg.image = admin_logo_in# Сохраняем ссылку на изображение

    def go_back_btn_funk():
        options = messagebox.askquestion("Уже выходишь(?","Ты точно хочешь выйти из аккаунта ??", )
        if options == 'yes':
            main_view()


    quit_btn =Image.open("files/exitbtn.png")
    resized_quit_btn_in = quit_btn.resize((35, 35))
    quit_btn_in = ImageTk.PhotoImage(resized_quit_btn_in)
    quit_btn_in_btn = Button(admin_frame, image=quit_btn_in, bd=0, bg = '#D3D3D3',command=go_back_btn_funk )
    quit_btn_in_btn.place(x=1220,y=15)
    quit_btn_in_btn.image = quit_btn_in# Сохраняем ссылку на изображение



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
    
    def register():
        username = newlogin.get()
        password = newpass_input.get()
        email = new_gmail.get()
        
        user = Users(username, password, email)
        user.user_reg()

    sign_up_fon = Image.open("files/sign_up.png")
    resized_sign_up = sign_up_fon.resize((300, 60))
    sign_up = ImageTk.PhotoImage(resized_sign_up)
    sign_up_btn = Button(mystat_reg, image=sign_up, bd=0, bg='#FFFFFF')
    sign_up_btn.image = sign_up # Сохраняем ссылку на изображение чтобы сборщик мусора не удалял!
    sign_up_btn.config(command=register)
    sign_up_btn.place(x=45, y=280)

    
    

    go_back_fon = Image.open("files/go_back1.png")
    resized_go_back = go_back_fon.resize((160, 60))
    go_back = ImageTk.PhotoImage(resized_go_back)
    go_back_btn = Button(mystat_reg, image=go_back, bd=0, bg='#FFFFFF',command=main_view)
    go_back_btn.image = go_back # Сохраняем ссылку на изображение чтобы сборщик мусора не удалял!
    go_back_btn.place(x=12, y=660)
#__________-REGISTRATION_FRAME_END_______________
    
        

#______________MAIN VIEW________________________
def main_view():
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


    #__________ПРОВЕРКА ЛОГИНА И ПАРОЛЯ ЧЕРЕЗ КЛАСС User и его метод!
    def log_pass_check():
        login = name_input.get()
        password = password_input.get()
        Users.admin_users_log_pass_check(login,password)




    
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
    sign_in_btn = Button(main, image=sign_in, bd=0, bg = '#fafafa', command=log_pass_check)
    sign_in_btn.place(x=110,y=390)
    sign_in_btn.image = sign_in# Сохраняем ссылку на изображение

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
    google_play_button.image = google_play# Сохраняем ссылку на изображение

    apple = Image.open("files/Appstore_logo.png")
    resized_apple = apple.resize((135, 45))
    apple_store = ImageTk.PhotoImage(resized_apple)
    apple_store_button = Button(main, image=apple_store, bd=0, command=open_apple_store,bg = '#fafafa')
    apple_store_button.place(x=270, y=550)
    apple_store_button.image = apple_store# Сохраняем ссылку на изображение
    #_______________Main___VIEW____END________________________________________





main_view()
mystat.mainloop()


