#from calendar import *
import calendar
#print(month(2100,2))
#print(calendar.calendar(2022))
print(calendar.isleap(2100))
print(calendar.month(2100,2))
print(calendar.leapdays(2015,2022))
s=calendar.weekday(2002,12,14)
print(calendar.weekday(2002,12,14))
if s==0:
    print("Monday")
elif s==1:
    print("Tuesday")
elif s==2:
    print("Wednesday")
elif s==3:
    print("Thursday")
elif s==4:
    print("Friday")
elif s==5:
    print("Saturday")
else:
    print("sunday")




