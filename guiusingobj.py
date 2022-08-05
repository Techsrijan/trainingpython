from tkinter import *

root=Tk()




class MyWindow:
    def __init__(self,window):
        self.label = Label(root, text="Enter First Number",
                      font=("Comic Sans Ms", "13", "bold"))
        self.label.grid(row=0, column=0)


w=MyWindow(root)
root.mainloop()