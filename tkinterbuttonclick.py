from tkinter import *
root=Tk()

def left_click(event=""):
    print("left button is clicked")


def middle_click(event=""):
    print("middle button is clicked")


def right_click(event=""):
    print("right button is clicked")

root.bind("<Button-1>",left_click)
root.bind("<Button-2>",middle_click)
root.bind("<Button-3>",right_click)
btn=Button(root,text="left click",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=left_click)
btn.pack()

btn1=Button(root,text="middle click",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
            ,command = middle_click)
btn1.pack()


btn2=Button(root,text="right click",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=right_click)
btn2.pack()
root.geometry("800x600+150+200")
root.resizable(0,0)
root.mainloop()