def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


num=int(input("enter any number for which u want factorial"))
x=factorial(num)
print(x)