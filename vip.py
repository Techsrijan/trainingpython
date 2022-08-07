from tkinter import *

root=Tk()


def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnclear():
    global val
    val=""
    data.set("")

def btnEquals():
    global val
    result=str(eval(val))
    data.set(result)
def btnDot():
    global val
    result=float(eval(val))
    data.set("")
val=''
root.title("my calculator")
root.resizable(0,0)
#root.geometry("360x380+300+200")
data=StringVar()
display=Entry(root,bd=28,justify='right',bg="powder blue",font=("Ariel",20),textvariable=data)
display.grid(row=0,columnspan=5)

btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(9))
btn9.grid(row=1,column=2)
btn_div=Button(root,text="/",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick('/'))
btn_div.grid(row=1,column=3)
btn_C=Button(root,text="C",bg="medium sea green",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=btnclear)
btn_C.grid(row=1,column=4)

btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(6))
btn6.grid(row=2,column=2)
btn_mul=Button(root,text="",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(''))
btn_mul.grid(row=2,column=3)
btn=Button(root,text="(",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick('('))
btn.grid(row=2,column=4)

btn1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(3))
btn3.grid(row=3,column=2)
btn_sub=Button(root,text="-",bg="blue",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick('-'))
btn_sub.grid(row=3,column=3)
btn=Button(root,text=")",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(')'))
btn.grid(row=3,column=4)

btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(0))
btn0.grid(row=4,column=0)
btn00=Button(root,text="00",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick(00))
btn00.grid(row=4,column=1)
btn_Dot=Button(root,text=".",bg="deeppink",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick)
btn_Dot.grid(row=4,column=2)
btn_add=Button(root,text="+",bg="yellow",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=lambda:btnClick('+'))
btn_add.grid(row=4,column=3)
btn_Equals=Button(root,text="=",bg="pink",font=("Ariel",12,"bold"),bd=12,height=2,width=4,command=btnEquals)
btn_Equals.grid(row=4,column=4)




root.mainloop()