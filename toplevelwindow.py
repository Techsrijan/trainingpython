from tkinter import *
from PIL import Image, ImageTk
root=Tk()
def open_new_window():
    top=Toplevel(root)
    btn22 = Button(top, text="Close", bg="yellow", fg="red", font=("Comic Sans Ms", "25", "bold")
                  , command=top.destroy)
    btn22.pack()
    top.geometry("800x600+120+120")
img=ImageTk.PhotoImage(file="images/exit.jpg")
btn1=Button(root,text="open new window",font=("Comic Sans Ms","25","bold")
            ,image=img,compound=BOTTOM,command =open_new_window)
btn1.pack()

btn2=Button(root,text="Exit",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
            ,command =quit)
btn2.pack()
root.geometry("800x600+120+120")
root.mainloop()