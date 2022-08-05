from tkinter import *
root=Tk()

def left_click(event=""):
    print("left button is clicked")


root.bind("<Control-T>",left_click)
root.bind("<Control-t>",left_click)
btn=Button(root,text="left click",bg="yellow",fg="red",font=("Comic Sans Ms","25","bold")
           ,command=left_click)
btn.pack()


root.geometry("800x600+150+200")
root.resizable(0,0)
root.mainloop()