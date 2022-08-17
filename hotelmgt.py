from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
taz=Tk()
user_icon=ImageTk.PhotoImage(Image.open('images/user.png'))

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()

#### database Connection ################
def db_connect():
    global mycursor, connection
    connection = pymysql.connect(user="root", host="127.0.0.1", db="summer")
    mycursor = connection.cursor()
#### main heading ###########
def mainheading():
    label=Label(taz,text="Hotel Management System" ,bg="yellow",
                fg="red",font=("Comic Sans Ms","48","bold"),padx=130)
    label.grid(row=0,column=0,columnspan=5)

######### welcome window #############
def welcomewindow():
    remove_all_widgets()
    mainheading()

usernameVar = StringVar()
passwordVar = StringVar()

def  adminlogin():
    a=usernameVar.get()
    b=passwordVar.get()
    if a=='' or b=='':
        messagebox.showerror("Login Error", " Please Enter Both Fields")
    else:
        db_connect()
        que = "select * from login_info where binary username=%s and binary password=%s"
        val = (a,b)
        mycursor.execute(que, val)
        data = mycursor.fetchall()
        flag = False
        for row in data:
            flag = True

        connection.close()
        if flag == True:
            welcomewindow()

        else:
            messagebox.showerror("Invalid User Credential", 'either User Name or Password is incorrect')
            passwordVar.set('')
            usernameVar.set('')

########## login window ######################
def loginwindow():
    mainheading()
    loginLabel = Label(taz, text="Admin Login", image=user_icon, compound=LEFT, font="Arial 30")
    loginLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)


    passwordEntry = Entry(taz, show='#', textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)

    loginButton = Button(taz, text="Login", width=20, height=2, fg="green", bd=10, command=adminlogin)
    loginButton.grid(row=4, column=1, columnspan=2)



width=taz.winfo_screenwidth()
height=taz.winfo_screenheight()
#print(width,height)

loginwindow()
taz.title("Hotel Management System")
taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()

