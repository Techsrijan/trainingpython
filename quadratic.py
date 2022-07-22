import math
a,b,c=-6,3,2
d=b*b-4*a*c
print(d)
if d==0:
    print("roots are real and equal")
    x1=x2=-b/(2*a)
    print("x1=",x1,"x2=",x2)
elif d>0:
    print("roots are real unequal")
    x1=(-b+math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1=", x1, "x2=", x2)
else:
    print("roots are imaginary")