def person(name,age):
    print("name=",name)
    age=age+10
    print("age=",age)

#1. positioal argument
person("Ram",99)
#person(88,"rohit")

#2. keyword argument
person(name="Mohan",age=25)
person(age=44,name="gopi")



def add1(x,y,z): #here x and y are called formal argument
    c=x+y+z
    print("Addition=",c)
add1(8,9,4)

#3. variable length argument
def multinumberadd(x,*y):
    print(x)
    print(y)
    sum=x
    for i in y:
        sum=sum+i
    print("Sum=",sum)

multinumberadd(1,3,5,7,55,88,44,88,33)

def multinumberadd1(*y):
    print(y)
    sum=0
    for i in y:
        sum=sum+i
    print("Sum=",sum)

multinumberadd1(1,3,5,7,55,88,44,88,33)

#4 . keyword varable length argument
def persondata(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
persondata("ram",age=25,city='gkp',marks=63)