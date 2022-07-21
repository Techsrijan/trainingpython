a=int(input("Enter First No"))
b=int(input("Enter Second No"))
c=int(input("Enter Third No"))

if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("C is greatest")
elif b>c:
    print("B is greatest")
else:
    print("C is greatest")