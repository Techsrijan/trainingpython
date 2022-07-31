'''from turtle import *
import time
t=Turtle()
t.speed(1)
t.pu()
t.goto(200,-100)
t.pd()
t.circle(100)

done()
'''
# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('white')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)
