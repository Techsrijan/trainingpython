from tkinter import *
from tkinter import filedialog,colorchooser
root=Tk()
def changebk():
    col=colorchooser.askcolor()
    print(col)
    t.config(background=col[1])

def changefore():
    col = colorchooser.askcolor()
    print(col)
    t.config(foreground=col[1])
f=''
def openfile():
    global f
    f=filedialog.askopenfile(initialdir="/",title="select file to open",
                           filetypes=(("TEXT FILE","*.txt"),("ALL FILES","*.*")))
    print(f.name)

    for data in f:
        #print(data)
        t.insert(INSERT,data)

def savefile():
    fw=open(f.name,"w")
    data=t.get(1.0,END)
    fw.write(data)
def saveAsfile():
    g=filedialog.asksaveasfile()
    data1 = t.get(1.0, END)
    g.write(data1)
t=Text(root,height=10,width=20,wrap=WORD,selectbackground="red")
t.pack()


btn3=Button(root,text="open file dialog",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=openfile)
btn3.pack()

btn4=Button(root,text="save file dialog(file already open)",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=savefile)
btn4.pack()

btn5=Button(root,text="save AS file dialog(create duplicate copy or new file)",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=saveAsfile)
btn5.pack()


btn6=Button(root,text="Background Color",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=changebk)
btn6.pack()

btn7=Button(root,text="Foreground Color",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=changefore)
btn7.pack()
root.geometry("800x600+150+200")

root.mainloop()