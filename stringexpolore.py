'''
st="welcome To Python"
print(st.upper())
print(st.lower())
print(st.title())
print(st.capitalize())
print(st.swapcase())

name=input("enter your name")
print(name)
if name.isalpha():
    print(name)
else:
    print("Please Enter Valid name")
'''
x="26abc"
print(type(x))
if x.isdigit():
    print(x)
else:
    print("not valid")

enroll="2020"
if enroll.isalnum():
    print("Valid")
else:
    print("Invalid")

str1="Techsrijan, consultancy, Services, Pvt, Ltd"
l=str1.split(',')
for i in l:
    print(i)

st2="!!!!!!!ashwani!!!!!!!"
print(st2,end="")
print("kumar")
print(st2.lstrip('!'),end="")   #lstrip rstrip strip
print("hello")

st3="Her name is tamanna and tamanna is good girl"
search=input("enter the string u want search")
print(st3.find(search))
if st3.find(search)!=-1:
    rep = input("enter the string u want replace")
    print(st3.replace(search,rep))
else:
    print("The string not matched")


print("kitnibar=",st3.count(search))
print("ant",st3.endswith('l'))

print(st3[-1])
