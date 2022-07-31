from turtle import *
import time
t=Turtle()
s=Screen()
s.setup(width=1000,height=600)

#t.circle(100,steps=10)

t.shape('turtle')
j=2
for i in range(50):
    t.stamp()
    #t.setheading(25+j)
    t.setposition(30,30)
    t.forward(j)
    j=j+2
    time.sleep(1)
done()