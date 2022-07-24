try:
    print("fridge is open")
    a = int(input("Enetr any number"))
    b = int(input("Enetr any number"))
    d=a/b
    print("div=",d)
    #print("fridge is close") #hammesa execute

except  ValueError:
    print("You have enter a character not a number")
    #print("fridge is close")  # hammesa execute
except ZeroDivisionError:
    print("value of second number cant be zero")
   # print("fridge is close")  # hammesa execute
except Exception:
    print("something went wrong")
    #print("fridge is close")  # hammesa execute
finally:  #always executes
    print("fridge is close")  # hammesa execute