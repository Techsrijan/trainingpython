from tkinter import *
root=Tk()
def msg():
    print("hi")
main_menu=Menu(root)
root.config(menu=main_menu)
#create file menu
file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="FILE",menu=file_menu)
file_menu.add_command(label="New",accelerator="Ctrl+O",command=msg)
file_menu.add_separator()
file_menu.add_command(label="Save",accelerator="Ctrl+S")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit")


#create edit menu
edit_menu=Menu(main_menu)
main_menu.add_cascade(label="EDIT",menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
root.geometry("800x600+120+120")
root.mainloop()