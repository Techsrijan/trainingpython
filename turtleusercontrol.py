from turtle import *
t=Turtle()
sc=Screen()
def move_x():
    t.forward(100)

def move_y():
    t.bk(100)

def move_left():
    t.left(90)

def move_right():
    t.right(90)

sc.listen()
sc.onkey(move_x,"Up")
sc.onkey(move_y,"D")
sc.onkey(move_left,"Left")
sc.onkey(move_right,"Right")
#done()
sc.mainloop()