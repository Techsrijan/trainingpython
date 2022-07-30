from turtle import *
t=Turtle()
t.speed(1)
t.pencolor('red')
t.fillcolor('yellow')
def shape():
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
'''
for i in range(4):
    t.forward(100)
    t.left(90)
'''
shape()
t.right(90)
t.pu()
t.fd(100)
t.pd()
shape()
done()