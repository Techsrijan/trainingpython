s={}
print(type(s))

se=set()
print(type(se))

p={1,2,3,4,3,4,3,2}
print(p)

p.add(100)
print(p)

p.remove(2)
print(p)

print(5 in p)  # in is membership operator
print(1 in p)
'''
se=eval(input("enter the elements of set"))
print(se)
'''
a={1,2,3,4}
b={5,6,3,8}

print(a|b)  #union

print(a&b) #intersection

print(a-b)  # which are in a but not in b

print(a^b) #symmetric differnence