from turtle import *
t=Turtle()
l=['red','yellow','blue','orange','pink']
for i in range(200):
    t.forward(i)
    t.pencolor(l[i%5])
    t.pensize(i%5)
    t.left(0+i)
done()