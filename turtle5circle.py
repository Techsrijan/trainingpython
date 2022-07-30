from turtle import *
t=Turtle()
s=Screen()
s.setup(width=1000,height=600)
l=['red','yellow','blue','orange','pink']
t.penup()
t.forward(400)
t.pd()
t.pensize(5)
for i in range(8):
    t.pd()
    t.pencolor(l[i%5])
    t.circle(50)
    t.pu()
    t.backward(100)
#t.circle(-100)
done()