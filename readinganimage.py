f=open("test.gif","rb")
g=open("rest.gif","wb")
for data in f:
    g.write(data)
''' 
for data in f:
    print(data)
    '''