from tkinter import *

root=Tk()
can=Canvas(root,bg="yellow",height="400" ,width="400")
cir=can.create_oval(200,200,300,300,fill="red")
can.pack()
root.geometry("800x600+120+120")
root.mainloop()