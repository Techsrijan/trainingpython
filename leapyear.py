year=int(input("Enter any year"))
if year%100==0:
    if year%400==0:
        print("Leap year")
    else:
        print("not leap")
elif year%4==0:
    print("Leap year")
else:
    print("not leap")

