from tkinter import *
root=Tk()



def add():
    a=int(i.get())
    b=j.get()
    x=a+b
    print(x)

label=Label(root,text="Enter First Number",
           font=("Comic Sans Ms","13","bold"))
label.grid(row=0,column=0)
i=StringVar()
ent=Entry(root,font=("Comic Sans Ms","13","bold"),textvariable=i)
ent.grid(row=0,column=1)

label1=Label(root,text="Enter Second Number",
           font=("Comic Sans Ms","13","bold"))
label1.grid(row=1,column=0)
j=IntVar()
ent1=Entry(root,font=("Comic Sans Ms","13","bold"),bd=5,textvariable=j)

ent1.grid(row=1,column=1)

btn=Button(root,text="click me",bg="yellow",fg="red",font=("Comic Sans Ms","13","bold")
           ,command=add)
btn.grid(row=2,columnspan=2)



root.wm_iconbitmap("c.ico")
#root.geometry("800x600+150+200")
root.resizable(0,0)
root.mainloop()