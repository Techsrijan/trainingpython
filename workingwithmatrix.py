from numpy import *
arr=array([[1,2,3,4],
          [3,4,5,6],
          [5,6,7,8]])
print(arr)

print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)

print(arr.flatten())

arr2=arr.reshape(4,3)
print(arr2)

a=array([[1,2,3,4],
          [3,4,5,6],
          [5,6,7,8]])

b=array([[1,2,3,4],
          [3,4,5,6],
          [5,6,7,8],
         [5, 6, 7, 8]])

print(b.min())
print(b.max())

#print(a+b)

d=a@b
print(d)

x=dot(a,b)
print(x)

print(diagonal(d))