from tkinter import *
from tkinter import messagebox
root=Tk()
def getdata():
   print(t.get(1.0,END))
def getselecteddata():
    res=t.selection_get()
    print(res)
    pos=t.search(res,1.0,stopindex=END)
    print(pos)
def deletedata():
    t.delete(1.0,END)


def getfileddata():
    f=open("ram.txt","r")
    for data in f:
        print(data)
        t.insert(INSERT,data)
t=Text(root,height=10,width=20,wrap=WORD,selectbackground="red")
t.pack()
#t.pack(fill=BOTH,expand=1)
#t.insert(INSERT,'fdsfsdfsd')
btn=Button(root,text="Get Data",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=getdata)
btn.pack()

btn1=Button(root,text="Get selected Data",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=getselecteddata)
btn1.pack()


btn2=Button(root,text="clear Data",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=deletedata)
btn2.pack()

btn3=Button(root,text="Get file Data",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=getfileddata)
btn3.pack()
root.geometry("800x600+150+200")

root.mainloop()