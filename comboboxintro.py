from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
def showdata():
    print(c.get())
l=[1,2,3,4,5,6]
c=Combobox(root,value=l)
c.set('Select Date')
c.pack()

btn=Button(root,text="click me",bg="yellow",fg="red",font=("Comic Sans Ms","13","bold")
           ,command=showdata)
btn.pack()
root.geometry("800x600+150+200")
root.resizable(0,0)
root.mainloop()