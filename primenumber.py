n=int(input("Enter any number"))
i=2
while i<=n-1:
    if n%i==0:
        print("not prime")
        break

    i=i+1
else:
     print("prime no")