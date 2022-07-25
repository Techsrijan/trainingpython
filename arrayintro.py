from array import *
arr=array('f',[1,2,3,4.7])
print(arr)

for i in arr:
    print(i)

print("index of=",arr[1])

for i in range(len(arr)):
    print(arr[i])

#print(id(arr))
print(arr.buffer_info())

arr.reverse()
print(arr)