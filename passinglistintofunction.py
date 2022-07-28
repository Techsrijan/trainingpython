#l=[1,2,3,4,5,5,7,8]

def listuse(lst):
    sum_of_even=0
    sum_of_odd=0
    for i in lst:
        if i%2==0:
            sum_of_even=sum_of_even+i
        else:
            sum_of_odd=sum_of_odd+i
    return sum_of_even,sum_of_odd


#run time user input a list or tuple
l=list()
l=eval(input("enter the elment of list"))
print(l)
c,d=listuse(l)
print("sum of even=",c)
print("sum of odd=",d)