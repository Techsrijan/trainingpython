def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def mul(x,y):
    print(x*y)

print(__name__)  #predefined variable

if __name__=='__main__':
    def msg():
        print("This is original file")
    msg()
else:
    print("This message is copy write message")


