a,b,c,d,e=40,42,40,56,88
tot=a+b+c+d+e
print(tot)
per=(tot*100)/500
print(per)
if per<33:
    print("fail")
elif per>=33 and per<45:
    print("thrid division")
elif per>=45 and per<60:
    print("second division")
elif per>=60:
    print("first division")