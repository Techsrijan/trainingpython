from numpy import *
#import numpy
arr=array([1,2,3,4,5])
print(arr)

'''
There are 6 ways to create an array using numpy
1. array
2. linspace
3. logspace
4. arange
5. zeros
6. ones
'''

#1 array
arr=array([1,2,3,4,5])
print(arr)

#2 linspace
arr3=linspace(1,15)
print(arr3)

#2 linspace
arr4=logspace(1,15)
print(arr4)

arr5=arange(1,15,2)
print(arr5)

#arr6=array([0,0,0,0,0,0,0,0,0])
arr6=zeros(10,int)
print(arr6)

arr7=ones(100)
print(arr7)