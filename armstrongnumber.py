n=int(input("enter any number"))
print(n)
orig=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit*digit*digit
    n=n//10

print(n)
print(orig)
print(sum)
if orig==sum:
    print("Number is armstrong")
else:
    print("not armstrong")
