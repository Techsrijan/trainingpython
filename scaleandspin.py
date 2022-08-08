from tkinter import *

root=Tk()
def showdata():
   print(s.get())
   print(spin.get())
s=Scale(root,from_=1,to=500, orient=HORIZONTAL,length=300,sliderlength=50,width=50)
s.set(200)
s.pack()

spin=Spinbox(root,from_=1,to=5,)
spin.pack()
btn=Button(root,text="click me",bg="yellow",fg="red",font=("Comic Sans Ms","13","bold")
           ,command=showdata)
btn.pack()
root.geometry("800x600+150+200")
root.resizable(0,0)
root.mainloop()