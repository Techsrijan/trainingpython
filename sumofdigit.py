n=int(input("enetr any number"))
print(n)

sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("sum of digit=",sum)
