from tkinter import *
root=Tk()

def msg():
    print("are wah click ho gaya")
def msg2():
    print("dekho bhai")
root.title("My Project")

label=Label(root,text="Enter First Number",
            bg="yellow",fg="red",font=("Comic Sans Ms","25","bold"))
label.pack(side=TOP,fill=X)

label1=Label(root,text="Enter Second Number",
            bg="yellow",fg="red",font=("Comic Sans Ms","25","bold"))
label1.pack(side=BOTTOM,fill=X)

btn=Button(root,text="click me",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold"),
           command=msg)
btn.pack(side=LEFT,fill=Y)
btn1=Button(root,text="click me",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold"),
            command=msg2)
btn1.pack(side=RIGHT,fill=Y)

root.wm_iconbitmap("c.ico")
root.geometry("800x600+150+200")
root.resizable(0,0)
root.mainloop()