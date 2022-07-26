from numpy import *
#import numpy
arr=array([1,2,3,4,5.0])
print(arr)

print(arr.dtype)

arr=arr+5
print(arr)

arr2=array([1,2,3,4,5])

arr3=arr+arr2
print(arr3)

print(sum(arr3))