from tkinter import *
from PIL import Image, ImageTk

root=Tk()
can=Canvas(root,bg="yellow",height="400" ,width="600")
lin=can.create_line(0,0,400,400,width=5,fill='red')
rec=can.create_rectangle(200,200,300,300,fill='green')
rec=can.create_rectangle(200,200,500,300,fill='blue')
cir=can.create_oval(200,200,300,300,fill="red",outline="white",width="5")
can.create_arc(200,200,300,300,fill="white",extent=-180)
#can.create_text()
img=ImageTk.PhotoImage(file="rest.gif")
can.create_image(0,0,image=img,anchor=NW)
points=[250,110,480,200,280,280,250,110]

poly=can.create_polygon(points,fill="blue",outline="white",width=5)
can.pack()
root.geometry("800x600+120+120")
root.mainloop()