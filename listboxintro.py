from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
def showdata():
    print(l.curselection())
    for item in l.curselection():
        print(l.get(item))

def delete():
    print(l.curselection())
    for item in l.curselection():
        print(l.delete(item))

f=Frame(root)
scroll=Scrollbar(f)

l=Listbox(f,height=5,selectmode=EXTENDED,yscrollcommand=scroll.set)
'''
l.insert(1,"C++")
l.insert(2,"C")
l.insert(3,"Java")
l.insert(4,"C#")'''
for i in range(20):
    l.insert(i,i+1)
l.pack(side=LEFT)
scroll.config(command=l.yview)
scroll.pack(side=RIGHT,fill=Y)
f.pack()

btn=Button(root,text="click me",bg="yellow",fg="red",font=("Comic Sans Ms","13","bold")
           ,command=showdata)
btn.pack()


btn2=Button(root,text="Delete",bg="yellow",fg="red",font=("Comic Sans Ms","13","bold")
           ,command=delete)
btn2.pack()

root.geometry("800x600+150+200")
root.resizable(0,0)
root.mainloop()