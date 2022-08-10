from tkinter import *
from tkinter import messagebox
root=Tk()
def openmsgbox():
    #res=messagebox.askyesno("Question?","Do You want To join Our Trainingg Program?")
    res = messagebox.askyesnocancel("Question?", "Do You want To join Our Traini")
    print(res)
    if res==True:
        print("Good")
    else:
        print("Bad")
btn=Button(root,text="click me",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=openmsgbox)
btn.place(x=250,y=400)
root.geometry("800x600+150+200")
root.resizable(0,0)
root.mainloop()