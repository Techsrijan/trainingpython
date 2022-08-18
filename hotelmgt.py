from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
import pymysql
taz=Tk()
user_icon=ImageTk.PhotoImage(Image.open('images/user.png'))
tazTV = ttk.Treeview(height=10, columns=('Item Name''Rate','Type'))

############# validation ######################
def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False
callback1 = taz.register(only_numeric_input)  # registers a Tcl to Python callback

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


def logout():
    loginwindow()
######### welcome window #############
def welcomewindow():
    remove_all_widgets()
    mainheading()
    additemwindow()

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
def OnDoubleClick(event):
    item = tazTV.selection()
    itemNameVar1 = tazTV.item(item, "text")
    item_detail = tazTV.item(item, "values")
    #print(itemNameVar1)
    #print(item_detail)
    itemnameVar.set(itemNameVar1)
    itemrateVar.set(item_detail[0])
    itemTypeVar.set(item_detail[1])
########## login window ######################
def loginwindow():
    remove_all_widgets()
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

###### get item in tree view ######
def getItemInTreeView():
    # to delete already inserted item
    records = tazTV.get_children()

    for element in records:
        tazTV.delete(element)

    # insert data in treeview
    conn = pymysql.connect(host="localhost", user="root", db="summer")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select * from itemlist"
    mycursor.execute(query)
    data = mycursor.fetchall()
    #print(data)

    for row in data:
        tazTV.insert('', 'end', text=row['item_name'], values=(row["item_rate"], row["item_type"]))
    tazTV.bind("<Double-1>", OnDoubleClick)
    conn.close()
################## add item window ##################
itemnameVar=StringVar()
itemrateVar=StringVar()
itemTypeVar=StringVar()
def additem():
    print(itemnameVar.get(),itemrateVar.get(),itemTypeVar.get())
    x=itemnameVar.get()
    y=itemrateVar.get()
    z=itemTypeVar.get()
    print(x,y,z)
    if x=='' or y=='' or z=='':
        messagebox.showerror("Insertion Error", " Please Enter All Fields")
    else:
        db_connect()
        quei="insert into itemlist(item_name,item_rate,item_type)values(%s,%s,%s)"
        val=(x,y,z)
        mycursor.execute(quei,val)
        connection.commit()
        messagebox.showinfo("Data Insertion","Data Interted successfully")
        getItemInTreeView()
        itemnameVar.set('')
        itemrateVar.set('')
        itemTypeVar.set('')

def updateitem():
    x = itemnameVar.get()
    y = itemrateVar.get()
    z = itemTypeVar.get()
    print(x, y, z)
    db_connect()
    queup = "update itemlist set item_rate=%s, item_type=%s where item_name=%s"
    val = (y,z,x)
    mycursor.execute(queup, val)
    connection.commit()
    messagebox.showinfo("Data Updation", "Data Updated successfully")
    getItemInTreeView()

def deleteitem():
    x = itemnameVar.get()
    y = itemrateVar.get()
    z = itemTypeVar.get()
    print(x, y, z)
    db_connect()
    queup = "delete from itemlist  where item_name=%s"
    val = (x)
    mycursor.execute(queup, val)
    connection.commit()
    messagebox.showinfo("Data Deletion", "Data Deleted successfully")
    getItemInTreeView()
def additemwindow():
    remove_all_widgets()
    mainheading()

    itemnameLabel = Label(taz, text="ITEM DETAILS", font="Arial 30")
    itemnameLabel.grid(row=1, column=2, padx=(50, 0), columnspan=1, pady=10)

    ###############################
    billButton = Button(taz, text="Back", width=20, height=2, fg="green", bd=10, )
    billButton.grid(row=1, column=0, columnspan=1)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=3, column=0, columnspan=1)

    ###########################

    itemnameLabel = Label(taz, text="Item name")
    itemnameLabel.grid(row=2, column=1, padx=20,  pady=5)


    itemrateLabel = Label(taz, text="Item Rate")
    itemrateLabel.grid(row=3, column=1, padx=20, pady=5)

    itemTypeLabel = Label(taz, text="Item Type")
    itemTypeLabel.grid(row=4, column=1, padx=20, pady=5)

    itemnameEntry = Entry(taz, textvariable=itemnameVar)
    itemnameEntry.grid(row=2, column=2, padx=20, pady=5)
    #itemnameEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

    itemrateEntry = Entry(taz, textvariable=itemrateVar)
    itemrateEntry.grid(row=3, column=2, padx=20, pady=5)
    itemrateEntry.configure(validate="key", validatecommand=(callback1, "%P"))  # enables validation

    itemTypeEntry = Entry(taz, textvariable=itemTypeVar)
    itemTypeEntry.grid(row=4, column=2, padx=20, pady=5)
    #itemTypeEntry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation
    '''global itemType
    #l = ["BreakFast", "Lunch", "Dinner"]
    itemType = Combobox(taz, values=l, height=2)
    itemType.set("Select Item type")
    itemType.grid(row=4, column=3, padx=20, pady=5)'''

    label = Label(taz)
    label.grid(row=5, column=2, padx=20, pady=5)

    additemButton = Button(taz, text="Add Item", width=20, height=2, fg="green", bd=10,command=additem)
    additemButton.grid(row=3, column=3, columnspan=1)

    updateButton = Button(taz, text="UpDate Item", width=20, height=2, fg="green", bd=10,command=updateitem )
    updateButton.grid(row=1, column=3, columnspan=1)

    deleteButton = Button(taz, text="Delete Item", width=20, height=2, fg="green", bd=10,command=deleteitem)
    deleteButton.grid(row=6, column=3, columnspan=1)

    ###############################################
    tazTV.grid(row=7, column=0, columnspan=3)
    style = ttk.Style(taz)
    style.theme_use('clam')
    style.configure("Treeview", fieldbackground="green")
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV.yview)
    scrollBar.grid(row=7, column=2, sticky="NSE")

    tazTV.configure(yscrollcommand=scrollBar.set)

    tazTV.heading('#0', text="Item Name")
    tazTV.heading('#1', text="Rate")
    tazTV.heading('#2', text="Type")

    getItemInTreeView()



width=taz.winfo_screenwidth()
height=taz.winfo_screenheight()
#print(width,height)

loginwindow()
taz.title("Hotel Management System")
taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()

