from functools import reduce
l=[1,2,4,5,6,7,98]

f=list(filter(lambda n:n%2==0,l))
print(f)

m=list(map(lambda a:a+5,f))
print(m)

t=reduce(lambda a,b:a+b,m)
print(t)