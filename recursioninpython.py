'''
recursion--when a function calls itself it is called recursion
'''
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(sys.getrecursionlimit()-500)
i=0
def greet():
    global i
    print("Good morning",i)
    i=i+1
    greet()


greet()