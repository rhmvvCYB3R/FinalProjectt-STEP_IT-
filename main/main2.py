from tkinter import *
from PIL import Image, ImageTk #библеотека Pillow для добавление фоток, использовал так как библеотека Tkinter не даёт добавлять больше одного!
import webbrowser #чтобы сделать кнопку-фотку как svg файл!
from tkinter import messagebox #для того чтобы показать info,error,askquestions
from tkinter import ttk #для TreeView, еще чтобы более новый дизайн сделать(не получилась,т.к пришлось бы переделывать весь код)

datas = []  #пустой лист для того чтобы кидать данные туда. Используется для добавления,показа,редактирования,поиска,сортировки,удаления 
#элементов нашие StudentSchedule.тхт


#класс Расписания
class Schedule:
    def __init__(self, time, subject, group, room, count_student):
        self.time = time
        self.subject = subject
        self.group = group
        self.room = room
        self.count_student = count_student
    def __str__(self): #для того чтобы записать в файл в таком формате!
         return (f"{self.time},{self.subject},{self.group},{self.room},{self.count_student}\n")

 
    def create_schedule(self): #добавление расписания, остальная часть в admin frame
        path = "data/StudentSchedule.txt"
        with open(path, "a", encoding="utf=8") as file:
            file.write(str(self))


    def show_schedule(): #показать расписание, остальная часть в admin frame
        global datas
        datas.clear()
        with open("data/StudentSchedule.txt", 'r', encoding='utf-8') as file:
            for data in file:
                data = data.strip()
                schedule = data.split(",")
                time, subject, group,room,count_student = schedule
                list_s=[time,subject,group,room,count_student]
                datas.append(list_s)
        
          

    def del_schedule(): #удалить какой - либо расписание!, остальная часть в admin frame
        global datas
        datas.clear()
        with open("data/StudentSchedule.txt", 'r', encoding='utf-8') as file:
            for data in file:
                data = data.strip()
                schedule = data.split(",")
                time, subject, group,room,count_student = schedule
                list_s=[time,subject,group,room,count_student]
                datas.append(list_s)
        
    
    def edit_schedule(): #для того чтобы изменить расписание , остальная часть в admin frame
        global datas    
        datas.clear()
        with open("data/StudentSchedule.txt", 'r', encoding='utf-8') as file:
            for data in file:
                data = data.strip()
                schedule = data.split(",")
                time, subject, group,room,count_student = schedule
                list_s=[time,subject,group,room,count_student]
                datas.append(list_s)


    def save_schedule():#сохр.после редактирования ! 
        with open("data/StudentSchedule.txt", 'w', encoding='utf-8') as file:
            for schedule in datas:
                file.write(",".join(schedule) + "\n")

   
    def sorted_frame(): #сортируем наш списой по времени!
        global datas    
        datas.clear()
        with open("data/StudentSchedule.txt", 'r', encoding='utf-8') as file:
            for data in file:
                data = data.strip()
                schedule = data.split(",")
                time, subject, group,room,count_student = schedule
                list_s=[time,subject,group,room,count_student]
                datas.append(list_s)
        datas.sort(key=lambda x: x[0]) #сортируем одной лишь командой sort и лямбда. Очень удобно!!!


#класс юзера 
class Users:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def user_reg(self): #функция регистрации нового акк. Связано с register frame
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
    

    def admin_users_log_pass_check(login,password): #проверка логина, пароля пользователя и так же email и пароля!
        import admin_log #Быстро , удобно. 
        
        with open("data/users_data.txt", 'r') as file:
            for data in file:
                data = data.strip()#метод строки, который удаляет пробелы в начале и в конце строки.
                user_data = data.split(",")# разделяет очищенную строку на список элементов по запятым.
                username, user_password, email = user_data #происходит распаковка списка на несколько переменных.
                if login == username and password == user_password:
                    user_acc_frame()
                    return
                elif login == email and password ==user_password:
                    user_acc_frame()
                    return
        if login == admin_log.username and password == admin_log.password:
            admin_frame_win()
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

    #______________USERS_ACC_VIEWS____________________________________
    user_frame = Frame(mystat, width=1270, height=750, bg="white")
    user_frame.place(x=0, y=0)

    def find_btn_funk():   
        style = ttk.Style()
        style.configure("Fancy.TButton", foreground="black", background="red")
        Schedule.show_schedule()


        find_frame = Frame(user_frame, width=1270, height=750, bg="white")
        find_frame.place(x=65, y=55)

        search_text = ttk.Label(find_frame,text="Введите название группы или название предмета!")
        search_text.config(background="white",font=(("Arial"),13))
        search_text.place(x=30,y=437)
        search_entry = ttk.Entry(find_frame, style="Fancy.TButton")
        search_entry.place(x=30, y=460, width=300, height=30)
        columns = ("time", "subject", "group", "room", "count_student")
        tree = ttk.Treeview(user_frame, columns=columns, show="headings")
        tree.place(x=100, y=100, width=1100, height=350)

        tree.heading("time", text="Время")
        tree.heading("subject", text="Предмет")
        tree.heading("group", text="Группа")
        tree.heading("room", text="Комната")
        tree.heading("count_student", text="Колл-студента")
        
    
        def search_schedule(): #поиск расписания!
            info = search_entry.get().lower()  
            for row in tree.get_children():
                tree.delete(row)  

            
            for item in datas:
                if info in item[1].lower() or info in item[2].lower():  # Проверяем в предмете и группе
                    tree.insert("", END, values=item) 
                    
        find_Btn = ttk.Button(find_frame, text="Искать!", style="Fancy.TButton", command=search_schedule)
        find_Btn.place(x=870, y=460, width=300, height=30)



    
    def calendar_fr(): #для кнопки календаря
        calendar_frame = Frame(user_frame,width=1270, height=750, bg="white")
        calendar_frame.place(x=65,y=55)
        Schedule.show_schedule()

        columns = ("time", "subject", "group","room","count_student")    
        tree = ttk.Treeview(calendar_frame,columns=columns, show="headings")
        tree.place(x=0,y=0,width=1200,height=500)


        tree.heading("time", text="Время")
        tree.heading("subject", text="Предмет")
        tree.heading("group", text="Группа")
        tree.heading("room", text="Комната")
        tree.heading("count_student", text="Колл-студента")
        datas
        for info in datas:

            tree.insert("", END, values=info)

    def user_logo_frame():
        user_logo_fr = Frame(user_frame,width=1270, height=750, bg="white")
        user_logo_fr.place(x=65,y=55)

        user_info =Image.open("files/mainlabel.png")
        resized_user_info_in = user_info.resize((1210, 700))
        user_info_in = ImageTk.PhotoImage(resized_user_info_in)
        user_info_in_bg = Label(user_logo_fr, image=user_info_in, bd=0, bg = 'white')
        user_info_in_bg.place(x=0,y=0)
        user_info_in_bg.image = user_info_in

    def sort_btn_funk(): #сортировка нашиго расписание, сохраниние в лист datas и показ
        sorted_frame = Frame(user_frame, width=1270, height=750, bg="white")
        sorted_frame.place(x=65, y=55)
        Schedule.sorted_frame()
        style = ttk.Style()
        style.configure("Fancy.TButton", foreground="black", background="red")
        columns = ("time", "subject", "group", "room", "count_student")
        tree = ttk.Treeview(user_frame, columns=columns, show="headings")
        tree.place(x=100, y=100, width=1100, height=350)

        tree.heading("time", text="Время")
        tree.heading("subject", text="Предмет")
        tree.heading("group", text="Группа")
        tree.heading("room", text="Комната")
        tree.heading("count_student", text="Колл-студента")
        for info in datas:
            tree.insert("", END, values=info)


    design1 = Label(user_frame)
    design1.config(bg='white',padx=700,pady=20)
    design1.place(x=0,y=0)

    design2 = Label(user_frame)
    design2.config(bg='white',padx=30,pady=500)
    design2.place(x=0,y=0)
   
    mystat_text = Label(user_frame, text='MyStat')
    mystat_text.config(bg='white',
                        fg='#563bea',
                    font= ("Arial Black" , 15),bd=0)
    mystat_text.place(x=30,y=14)

    find_btn =Image.open("files/find_btn.png")
    resized_find_btn_in = find_btn.resize((55, 45))
    find_btn_in = ImageTk.PhotoImage(resized_find_btn_in)
    find_btn_in_bg = Button(user_frame, image=find_btn_in, bd=0, bg = 'white',command=find_btn_funk)
    find_btn_in_bg.place(x=5,y=245)
    find_btn_in_bg.image = find_btn_in

    sort_btn =Image.open("files/sort_btn.png")
    resized_sort_btn_in = sort_btn.resize((55, 45))
    sort_btn_in = ImageTk.PhotoImage(resized_sort_btn_in)
    sort_btn_in_bg = Button(user_frame, image=sort_btn_in, bd=0, bg = 'white',command=sort_btn_funk)
    sort_btn_in_bg.place(x=8,y=310)
    sort_btn_in_bg.image = sort_btn_in

    user_logo =Image.open("files/user_anonim.png")
    resized_user_logo_in = user_logo.resize((55, 55))
    user_logo_in = ImageTk.PhotoImage(resized_user_logo_in)
    user_logo_in_bg = Button(user_frame, image=user_logo_in, bd=0, bg = 'white',command=user_logo_frame )
    user_logo_in_bg.place(x=5,y=95)
    user_logo_in_bg.image = user_logo_in

    def go_back_btn_funk():
        options = messagebox.askquestion("Уже выходишь(?","Ты точно хочешь выйти из аккаунта ??", )
        if options == 'yes':
            main_view()


    quit_btn =Image.open("files/exitbtn.png")
    resized_quit_btn_in = quit_btn.resize((35, 35))
    quit_btn_in = ImageTk.PhotoImage(resized_quit_btn_in)
    quit_btn_in_btn = Button(user_frame, image=quit_btn_in, bd=0, bg = 'white',command=go_back_btn_funk )
    quit_btn_in_btn.place(x=1220,y=10)
    quit_btn_in_btn.image = quit_btn_in# Сохраняем ссылку на изображение



    calendar_btn =Image.open("files/calendar.png")
    resized_calendar_btn_in = calendar_btn.resize((55, 55))
    calendar_btn_in = ImageTk.PhotoImage(resized_calendar_btn_in)
    calendar_btn_in_bg = Button(user_frame, image=calendar_btn_in, bd=0, bg = 'white',command=calendar_fr)
    calendar_btn_in_bg.place(x=5,y=170)
    calendar_btn_in_bg.image = calendar_btn_in







#______________USERS_ACC_VIEWS_END________________

#___________Admin__ACCOUNT____FRAME_____
def admin_frame_win():



    #______ADMIN_ACC_VIEWS
    admin_frame = Frame(mystat, width=1270, height=750, bg="#DCDCDC")
    admin_frame.place(x=0, y=0)

    def calendar_add_frame():
        calendar_frame = Frame(admin_frame, width=1250, height=800, bg="#7545ff")
        calendar_frame.place(x=67, y=100)
        
        design3 = Label(admin_frame)
        design3.config(bg='#46394b',padx=700,pady=20)
        design3.place(x=67,y=60)
        #_____________________________________
         




         #SHOW_BUTTON_AND_FUNK______
        def show_btn_funk():
            add_frame = Frame(admin_frame, width=1250, height=580, bg="#7545ff")
            add_frame.place(x=67, y=120)
            Schedule.show_schedule()

            columns = ("time", "subject", "group","room","count_student")    
            tree = ttk.Treeview(admin_frame,columns=columns, show="headings")
            tree.place(x=100,y=140,width=1000,height=500)


            tree.heading("time", text="Время")
            tree.heading("subject", text="Предмет")
            tree.heading("group", text="Группа")
            tree.heading("room", text="Комната")
            tree.heading("count_student", text="Колл-студента")
            datas
            for info in datas:

                tree.insert("", END, values=info)
                
            

        show_btn = Button(admin_frame, text="Показать",command=show_btn_funk)
        show_btn.config(padx=15,pady=14)
        show_btn.place(x=80,y=65)

        #_________END___________________
    




        #___________ADD_BUTTON_AND_FUNK______
        def add_btn_frame():
            add_frame = Frame(admin_frame, width=1250, height=580, bg="#7545ff")
            add_frame.place(x=67, y=120)
            #______________ENTRIES_________________
            time_add = Entry(add_frame)
            time_add.config(font=("Arial",16),bg="#f9e6f6",fg="black")
            time_add.place(x=50,y=50,height=35,width=220)

            subject_add = Entry(add_frame)
            subject_add.config(font=("Arial",16),bg="#f9e6f6",fg="black")
            subject_add.place(x=50,y=100,height=35,width=220)
           
            group_add = Entry(add_frame)
            group_add.config(font=("Arial",16),bg="#f9e6f6",fg="black")
            group_add.place(x=50,y=150,height=35,width=220)

            room_add = Entry(add_frame)
            room_add.config(font=("Arial",16),bg="#f9e6f6",fg="black")
            room_add.place(x=50,y=200,height=35,width=220)

            count_stn_add = Entry(add_frame)
            count_stn_add.config(font=("Arial",16),bg="#f9e6f6",fg="black")
            count_stn_add.place(x=50,y=250,height=35,width=220)


            #______________TEXT_LABELS______________________________-
            time_add_text = Label(add_frame, text="--Время урока")
            time_add_text.config(font=("Arial",16),bg="#7545ff",fg="white")
            time_add_text.place(x=300,y=50)

            subject_add_text = Label(add_frame, text="--Название предмета")
            subject_add_text.config(font=("Arial",16),bg="#7545ff",fg="white")
            subject_add_text.place(x=300,y=100)

            group_add_text = Label(add_frame, text="--Группа")
            group_add_text.config(font=("Arial",16),bg="#7545ff",fg="white")
            group_add_text.place(x=300,y=150)

            room_add_text = Label(add_frame, text="--Комната")
            room_add_text.config(font=("Arial",16),bg="#7545ff",fg="white")
            room_add_text.place(x=300,y=200)

            count_stn_text = Label(add_frame, text="--Колличество студентов")
            count_stn_text.config(font=("Arial",16),bg="#7545ff",fg="white")
            count_stn_text.place(x=300,y=250)
            
            
            def create_schedule():
                time = time_add.get()
                subject = subject_add.get()
                group = group_add.get()
                room = room_add.get()
                count_student = count_stn_add.get()
                if time in [""] or subject in [""] or group in [""] or room in [""] or count_student in [""]:
                    messagebox.showerror("Ошибка", "Введите данные!")
                else: 
                    new_schedule_add = Schedule(time, subject, group, room, count_student)
                    new_schedule_add.create_schedule()
                    messagebox.showinfo("Успех", "Записано!")
                
                

            schedule_add = Button(add_frame, text="Добавить",command=create_schedule)
            schedule_add.config(padx=15,pady=14)
            schedule_add.place(x=180,y=310)
            


        add_btn = Button(admin_frame, text="Создать",command=add_btn_frame)
        add_btn.config(padx=15,pady=14)
        add_btn.place(x=190,y=65)

    

        #______ADD_BUTTON_AND_FUNK___END___________________



        #______DELETE_BUTTON_AND_FUNK______
        def delete_btn_funk():
            delete_btn_frame = Frame(admin_frame, width=1250, height=580, bg="#7545ff")
            delete_btn_frame.place(x=67, y=120)
            Schedule.del_schedule()
            
            columns = ("time", "subject", "group","room","count_student")    
            tree = ttk.Treeview(admin_frame,columns=columns, show="headings")
            tree.place(x=100,y=140,width=1000,height=500)


            tree.heading("time", text="Время")
            tree.heading("subject", text="Предмет")
            tree.heading("group", text="Группа")
            tree.heading("room", text="Комната")
            tree.heading("count_student", text="Колл-студента")
            datas
            for info in datas:
                tree.insert("", END, values=info)
            
            def delete_selected():
                selected_item = tree.selection()
                if selected_item:
                    values = tree.item(selected_item)['values']
                    time_to_delete = values[0]
                    subject_to_delete = values[1]
                    for data in datas:
                        if data[0] == time_to_delete and data[1] == subject_to_delete:
                            datas.remove(data)
                            break
                    
                    with open("data/StudentSchedule.txt", 'w', encoding='utf-8') as file:
                        for data in datas:
                            file.write(",".join(data) + "\n")
                    messagebox.showinfo("Успех","Успешно удалено!")
                    tree.delete(selected_item)

            del_chosed_btn = Button(delete_btn_frame, text="Удалить выбранное!",command=delete_selected)
            del_chosed_btn.config(padx=15,pady=14)
            del_chosed_btn.place(x=1040,y=467)     
           
            


        delete_btn = Button(admin_frame, text="Удалить",command=delete_btn_funk)
        delete_btn.config(padx=15,pady=14)
        delete_btn.place(x=300,y=65)


        #______DELETE_BUTTON_AND_FUNK___END___________________



        #________EDIT_BUTTON_AND_FUNK______

        def edit_btn_funk():
            style = ttk.Style()
            style.configure("Fancy.TButton", foreground="black", background="red")

            edit_frame = Frame(admin_frame, width=1250, height=580, bg="#7545ff")
            edit_frame.place(x=67, y=120)

            Schedule.edit_schedule()

            columns = ("time", "subject", "group", "room", "count_student")
            tree = ttk.Treeview(admin_frame, columns=columns, show="headings")
            tree.place(x=100, y=140, width=1000, height=350)

            tree.heading("time", text="Время")
            tree.heading("subject", text="Предмет")
            tree.heading("group", text="Группа")
            tree.heading("room", text="Комната")
            tree.heading("count_student", text="Колл-студента")
            
            for info in datas:
                tree.insert("", END, values=info)

            # Поля ввода для изменения данных
            time_change = ttk.Entry(edit_frame, style="Fancy.TButton")
            time_change.place(x=30, y=400, width=200, height=30)

            subject_change = ttk.Entry(edit_frame, style="Fancy.TButton")
            subject_change.place(x=240, y=400, width=200, height=30)

            group_change = ttk.Entry(edit_frame, style="Fancy.TButton")
            group_change.place(x=450, y=400, width=200, height=30)

            room_change = ttk.Entry(edit_frame, style="Fancy.TButton")
            room_change.place(x=660, y=400, width=200, height=30)

            cnt_student_change = ttk.Entry(edit_frame, style="Fancy.TButton")
            cnt_student_change.place(x=870, y=400, width=200, height=30)

            # Функция для заполнения полей при выборе строки, делим по значением, время = 0 индекс, предмет = 1 индекс и т.д
            def select_item(event):
                selected_item = tree.selection()[0]
                values = tree.item(selected_item, 'values')

                time_change.delete(0, END)
                time_change.insert(0, values[0])

                subject_change.delete(0, END)
                subject_change.insert(0, values[1])

                group_change.delete(0, END)
                group_change.insert(0, values[2])

                room_change.delete(0, END)
                room_change.insert(0, values[3])

                cnt_student_change.delete(0, END)
                cnt_student_change.insert(0, values[4])

            tree.bind('<<TreeviewSelect>>', select_item)

            def apply_changes():
                selected_item = tree.selection()[0]
                time = time_change.get()
                subject = subject_change.get()
                group = group_change.get()
                room = room_change.get()
                cnt_student = cnt_student_change.get()

                # Обновляем данные в списке datas
                for i in range(len(datas)):
                    if datas[i][0] == tree.item(selected_item)['values'][0]:  # Поиск строки по времени
                        datas[i] = [time, subject, group, room, cnt_student]  
                        Schedule.save_schedule()  
                        tree.item(selected_item, values=[time, subject, group, room, cnt_student])  # Обновление таблицы
                        break
                messagebox.showinfo("Успех","Изменено!")
            change_btn = ttk.Button(edit_frame, text="Изменить!", style="Fancy.TButton", command=apply_changes)
            change_btn.place(x=870, y=460, width=200, height=30)

                    

        edit_btn = Button(admin_frame, text="Редактировать",command=edit_btn_funk)
        edit_btn.config(padx=15,pady=14)
        edit_btn.place(x=400,y=65) 


        #____EDIT_BUTTON_AND_FUNK___END___________________
        
        

        #_________Find_BUTTON_AND_FUNK______


        def find_btn_funk():   
            style = ttk.Style()
            style.configure("Fancy.TButton", foreground="black", background="red")
            Schedule.show_schedule()


            find_frame = Frame(admin_frame, width=1250, height=580, bg="#7545ff")
            find_frame.place(x=67, y=120)
            search_text = ttk.Label(find_frame,text="Введите название группы или название предмета!")
            search_text.config(background="#7545ff",font=(("Arial"),13))
            search_text.place(x=30,y=437)
            search_entry = ttk.Entry(find_frame, style="Fancy.TButton")
            search_entry.place(x=30, y=460, width=300, height=30)
            columns = ("time", "subject", "group", "room", "count_student")
            tree = ttk.Treeview(admin_frame, columns=columns, show="headings")
            tree.place(x=100, y=140, width=1000, height=350)

            tree.heading("time", text="Время")
            tree.heading("subject", text="Предмет")
            tree.heading("group", text="Группа")
            tree.heading("room", text="Комната")
            tree.heading("count_student", text="Колл-студента")
            
        
            def search_schedule():
                info = search_entry.get().lower()  
                for row in tree.get_children():
                    tree.delete(row)  

                
                for item in datas:
                    if info in item[1].lower() or info in item[2].lower():  # Проверяем в предмете и группе
                        tree.insert("", END, values=item) 
                        
            find_Btn = ttk.Button(find_frame, text="Искать!", style="Fancy.TButton", command=search_schedule)
            find_Btn.place(x=870, y=460, width=200, height=30)

        # Кнопка "Поиск" на главном фрейме
        find_btn = Button(admin_frame, text="Поиск", command=find_btn_funk)
        find_btn.config(padx=15, pady=14)
        find_btn.place(x=540, y=65)
                


        def sort_btn_funk():
            sorted_frame = Frame(admin_frame, width=1250, height=580, bg="#7545ff")
            sorted_frame.place(x=67, y=120)
            Schedule.sorted_frame()
            style = ttk.Style()
            style.configure("Fancy.TButton", foreground="black", background="red")
            columns = ("time", "subject", "group", "room", "count_student")
            tree = ttk.Treeview(admin_frame, columns=columns, show="headings")
            tree.place(x=100, y=140, width=1000, height=350)

            tree.heading("time", text="Время")
            tree.heading("subject", text="Предмет")
            tree.heading("group", text="Группа")
            tree.heading("room", text="Комната")
            tree.heading("count_student", text="Колл-студента")
            for info in datas:
                tree.insert("", END, values=info)


        sort_btn = Button(admin_frame, text="Сортировка",command=sort_btn_funk)
        sort_btn.config(padx=15,pady=14)
        sort_btn.place(x=630,y=65)
        




        #______FIND_BUTTON_AND_FUNK___END___________________



    #________ADMIN_FRAME_VIEWS
    design1 = Label(admin_frame)
    design1.config(bg='#7545ff',padx=700,pady=20)
    design1.place(x=0,y=0) 

    design2 = Label(admin_frame)
    design2.config(bg='#7545ff',padx=32,pady=500)
    design2.place(x=0,y=0)

    calendar_add =Image.open("files/calendar_add.png")
    resized_calendar_add_in = calendar_add.resize((55, 55))
    calendar_add_in = ImageTk.PhotoImage(resized_calendar_add_in)
    calendar_add_in_bg = Button(admin_frame, image=calendar_add_in, bd=0, bg = '#7545ff', command=calendar_add_frame)
    calendar_add_in_bg.place(x=7,y=200)
    calendar_add_in_bg.image = calendar_add_in# Сохраняем ссылку на изображение

    admin_text = Label(admin_frame, text='admin')
    admin_text.config(bg='#7545ff',
                        fg='#2e0b93',
                    font= ("Ubuntu" , 13),bd=0)
    admin_text.place(x=85,y=35)

    mystat_text = Label(admin_frame, text='MyStat')
    mystat_text.config(bg='#7545ff',
                        fg='#2e0b93',
                    font= ("Arial Black" , 14),bd=0)
    mystat_text.place(x=75,y=9)

    step_logo =Image.open("files/step_logo2.png")
    resized_step_logo_in = step_logo.resize((60, 75))
    step_logo_in = ImageTk.PhotoImage(resized_step_logo_in)
    step_logo_in_bg = Button(admin_frame, image=step_logo_in, bd=0, bg = '#7545ff',command=admin_frame_win )
    step_logo_in_bg.place(x=0,y=0)
    step_logo_in_bg.image = step_logo_in# Сохраняем ссылку на изображение
    
    admin_logo =Image.open("files/admin_anonim.png")
    resized_admin_logo_in = admin_logo.resize((55, 55))
    admin_logo_in = ImageTk.PhotoImage(resized_admin_logo_in)
    admin_logo_in_bg = Button(admin_frame, image=admin_logo_in, bd=0, bg = '#7545ff',command=admin_frame_win )
    admin_logo_in_bg.place(x=5,y=95)
    admin_logo_in_bg.image = admin_logo_in# Сохраняем ссылку на изображение

    def go_back_btn_funk():
        options = messagebox.askquestion("Уже выходишь(?","Ты точно хочешь выйти из аккаунта ??", )
        if options == 'yes':
            main_view()

    quit_btn =Image.open("files/exitbtn.png")
    resized_quit_btn_in = quit_btn.resize((35, 35))
    quit_btn_in = ImageTk.PhotoImage(resized_quit_btn_in)
    quit_btn_in_btn = Button(admin_frame, image=quit_btn_in, bd=0, bg = '#7545ff',command=go_back_btn_funk )
    quit_btn_in_btn.place(x=1220,y=15)
    quit_btn_in_btn.image = quit_btn_in# Сохраняем ссылку на изображение
#______________ADMIN_FRAME_VIEWS_END________________





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
            newpass_input.config(fg="black",show="*")
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
                font= ("Times" , 12))
    newpass_input.insert(0,"Введите пароль*: ") 
    newpass_input.place(x=50, y= 180,height=30,width=280)
    newpass_input.bind("<FocusIn>", clear_newpass)

    passw_show = IntVar()
    def show_password_funk():
        if passw_show.get() == 1:
            newpass_input.config(show="")
        else:
            newpass_input.config(show="*")


    password_show_btn = Image.open("files/password_show.png")
    resized_password_show_btn = password_show_btn.resize((20, 15))
    password_show_btn = ImageTk.PhotoImage(resized_password_show_btn)
    password_show_btn_button = Checkbutton(mystat, image=password_show_btn, bd=0, command=show_password_funk, variable= passw_show, bg = '#FFFFFF')
    password_show_btn_button.place(x=310, y=187)
    password_show_btn_button.image = password_show_btn# Сохраняем ссылку на изображение




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
            password_input.config(fg="black",show="*")
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

    passw_show2 = IntVar()
    def show_password_funk2():
        if passw_show2.get() == 1:
            password_input.config(show="")
        else:
            password_input.config(show="*")

    password_show_btn2 = Image.open("files/password_show.png")
    resized_password_show_btn2 = password_show_btn2.resize((20, 15))
    password_show_btn2 = ImageTk.PhotoImage(resized_password_show_btn2)
    password_show_btn2_button = Checkbutton(mystat, image=password_show_btn2, bd=0, command=show_password_funk2, variable= passw_show2, bg = '#FFFFFF')
    password_show_btn2_button.place(x=378, y=317)
    password_show_btn2_button.image = password_show_btn2# Сохраняем ссылку на изображение
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



# user_acc_frame()
# admin_frame_win()
main_view()
mystat.mainloop()


