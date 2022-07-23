n=int(input("how many toffe u want"))
print(n)
stock=20
i=1
while i<=n:
    if i<=stock:
        print("Please Collect toffe=",i)
    else:
        print("Out of stock")
        break
    i=i+1
else:   #loop else will run when loop runs properly
    print("thank u please visit again")