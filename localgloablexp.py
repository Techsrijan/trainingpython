y=50  #global

def msg():
    global z
    z=500
    y=500
    x=10 #local variable
    print("Local=",x)
    print(y) #always print local
    print(z)
    f=globals()['y']
    print("global to local=",f)

msg()
print("global=",y)
print(z)
