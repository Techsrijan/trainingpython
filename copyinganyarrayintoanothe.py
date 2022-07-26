from numpy import *
#import numpy
arr=array([1,2,3,4,5])
print(arr,"id of arr=",id(arr))

arr1=arr  #aliasing
print(arr1,"id of arr1=",id(arr1))

arr[0]=1000
print(arr,"id of arr=",id(arr))
print(arr1,"id of arr1=",id(arr1))

#what if u want two different address
arr3=array([1,2,3,4,5])
print(arr3,"id of arr3=",id(arr3))
arr4=arr3.view() #shallow copy
print(arr4,"id of arr4=",id(arr4))
arr3[0]=5000
print(arr3,"id of arr3=",id(arr3))
print(arr4,"id of arr4=",id(arr4))

#what if u want two different address and change in one does not affect other

arr5=array([1,2,3,4,5])
print(arr5,"id of arr3=",id(arr5))
arr6=arr5.copy() #deep copy
print(arr6,"id of arr6=",id(arr6))
arr5[0]=8000
print(arr5,"id of arr5=",id(arr5))
print(arr6,"id of arr6=",id(arr6))