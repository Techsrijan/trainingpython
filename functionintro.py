#function definition
def puncherwala():
    print("puncher ban jayega")


#function call
puncherwala()
puncherwala()

def add():
    a,b=5,6
    c=a+b
    print("Sum=",c)

add()
add()

def add1(x,y): #here x and y are called formal argument
    c=x+y
    print("Addition=",c)
add1(8,9)
add1(20,10)

p=int(input("enetr first number"))
q=int(input("enetr second number"))
add1(p,q)   #here p and q are called actual argument

def add2(x,y):
    c=x+y
    return c

a=add2(8,7)
print(a)
print("The sum of x and y is =",a)

def calc(x,y):
    c=x+y
    d=x-y
    return c,d

addw,sub=calc(25,20)
print(addw)
print(sub)

add()