from tkinter import *
root=Tk()


def reset():
    i.set("")
    j.set("")
def add():
    a=int(i.get())
    b=j.get()
    x=a+b
    k.set(x)

label=Label(root,text="Enter First Number",
            bg="yellow",fg="red",font=("Comic Sans Ms","13","bold"))
label.place(x=100,y=200)
i=StringVar()
ent=Entry(root,font=("Comic Sans Ms","13","bold"),textvariable=i)
ent.place(x=400,y=200)

label1=Label(root,text="Enter Second Number",
            bg="yellow",fg="red",font=("Comic Sans Ms","13","bold"))
label1.place(x=100,y=300)
j=IntVar()
ent1=Entry(root,font=("Comic Sans Ms","13","bold"),bd=5,textvariable=j)

ent1.place(x=400,y=300)


btn=Button(root,text="click me",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=add)
btn.place(x=250,y=400)

btn2=Button(root,text="Reset",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=reset)
btn2.place(x=500,y=400)

btn3=Button(root,text="Exit",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=quit)
btn3.place(x=700,y=400)

k=IntVar()
label11=Label(root,
            font=("Comic Sans Ms","13","bold"),textvariable=k)
label11.place(x=250,y=500)
root.wm_iconbitmap("c.ico")
root.geometry("800x600+150+200")
root.resizable(0,0)
root.mainloop()