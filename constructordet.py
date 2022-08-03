'''
constructor is a special member function which can
be invoked(call) automatically when the object of associated
class is created.
It is used to initialiize the data member of the class
variable-data member
'''

class Student:
    def student_info(self):
        print("this will print student information")
        self.a=5
        self.b=55

    def __init__(self):  #constructor
        print("Mein bade kamal ka function hoon")
        self.a=5
        self.b=10
        self.citizenship="india"

    def add(self):
        print(self.a+self.b)



#how to create object of a class
s=Student() # call constructor
s.student_info()
t=Student()
#t.student_info()
t.add()
