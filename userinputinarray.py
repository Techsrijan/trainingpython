from array import *
arr=array('i',[])  #empty array
n=int(input("how many students u have"))
print("no of student=",n)
for i in range(n):
    x=int(input("enter the marks of student"))
    arr.append(x)

print(arr)

search=int(input("Enter the number u want to search"))

pos=0
for i in arr:
    if i==search:
        print("Data mil gaya=",pos+1)
        break
    pos=pos+1
else:
    print("Not fonund")



# using python libray
print(arr.index(search))