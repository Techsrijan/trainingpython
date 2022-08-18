from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
taz=Tk()
#user_icon=ImageTk.PhotoImage(Image.open('images/user.png'))

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
                fg="red",font=("Comic Sans Ms","48","bold"),padx=270)
    label.grid(row=0,column=0,columnspan=5)

def hmanage():
    remove_all_widgets()
    mainheading()

    HotalmanagementLabel = Label(taz, text="Hotel Management", compound=LEFT, bg='red', font="Arial 34 bold")
    HotalmanagementLabel.grid(row=1, column=1, padx=(60, 0), columnspan=2, pady=50)

    logoutButton = Button(taz, text="LogOut", font="Arial 20 bold", fg="green", bd=3,bg='pink',
                          command=loginwindow)
    logoutButton.grid(row=1, column=3)

    backButton = Button(taz, text="<- Back", font="Arial 20 bold", fg="green", bd=3,bg='pink',
                          command=welcomewindow)
    backButton.grid(row=1, column=0)

    ItemnameLabel = Label(taz, text="Item-Name", compound=LEFT, bg='cyan', font="Arial 20")
    ItemnameLabel.grid(row=2, column=1, pady=10)

    ItemrateLabel = Label(taz, text="Item-Rate", compound=LEFT, bg='cyan', font="Arial 20")
    ItemrateLabel.grid(row=3, column=1, padx=(50, 0), pady=10)

    ItemtypeLabel = Label(taz, text="Item-Type", compound=LEFT, bg='cyan', font="Arial 20")
    ItemtypeLabel.grid(row=4, column=1, padx=(50, 0), pady=10)

    ItemnameEntry = Entry(taz, textvariable=ItemnameLabel, font="Arial 20")
    ItemnameEntry.grid(row=2, column=2, pady=10)

    ItemrateEntry = Entry(taz, textvariable=ItemrateLabel, font="Arial 20")
    ItemrateEntry.grid(row=3, column=2, pady=10)

    ItemtypeEntry = Entry(taz, textvariable=ItemtypeLabel, font="Arial 20")
    ItemtypeEntry.grid(row=4, column=2, pady=10)

    insertButton = Button(taz, text="Insert", font="Arial 24 bold", fg="green", bd=2,bg='light green',
                          command=loginwindow)
    insertButton.grid(row=7, column=0, pady=130)

    updateButton = Button(taz, text="Update", font="Arial 24 bold", fg="green", bd=2,bg='light green',
                          command=loginwindow)
    updateButton.grid(row=7, column=1, columnspan=2, pady=130)

    deleteButton = Button(taz, text="Delete", font="Arial 24 bold", fg="green", bd=2,bg='light green',
                          command=loginwindow)
    deleteButton.grid(row=7, column=3, pady=130)

######### welcome window #############
def welcomewindow():
    remove_all_widgets()
    mainheading()
    WelcomeLabel = Label(taz, text="Welcom To Home Page", compound=LEFT, font="Arial 30")
    WelcomeLabel.grid(row=1, column=1, padx=(50, 0), columnspan=2, pady=50)

    HmanageButton = Button(taz, text="Hotel Management", font="Arial 15", width=25, height=3, fg="green", bd=3,command=hmanage)
    HmanageButton.grid(row=4, column=0)

    billButton = Button(taz, text="Bill Generation", font="Arial 15", width=25, height=3, fg="green", bd=3)
    billButton.grid(row=4, column=1)

    logoutButton = Button(taz, text="LogOut", font="Arial 15", width=25, height=3, fg="green", bd=3,command=loginwindow)
    logoutButton.grid(row=4, column=2)

usernameVar = StringVar()
passwordVar = StringVar()

def  adminlogin():
    remove_all_widgets()
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
    passwordVar.set('')
    usernameVar.set('')
    remove_all_widgets()
    mainheading()
    loginLabel = Label(taz, text="Admin Login", compound=LEFT, font="Arial 30")
    loginLabel.grid(row=1, column=1, padx=(70, 0),columnspan=2 , pady=50)

    usernameLabel = Label(taz, text="Username", font="Arial 15")
    usernameLabel.grid(row=2, column=1, pady=5)

    passwordLabel = Label(taz, text="Password", font="Arial 15")
    passwordLabel.grid(row=3, column=1, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar, font="Arial 15")
    usernameEntry.grid(row=2, column=2, pady=5)


    passwordEntry = Entry(taz, show='#', textvariable=passwordVar, font="Arial 15")
    passwordEntry.grid(row=3, column=2, pady=5)

    loginButton = Button(taz, text="Login", font="Arial 15", width=25, height=3, fg="green", bd=3, command=adminlogin)
    loginButton.grid(row=4, column=1, columnspan=2)



width=taz.winfo_screenwidth()
height=taz.winfo_screenheight()
#print(width,height)

loginwindow()
taz.title("Hotel Management System")
taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()