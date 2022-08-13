class Room:   #parent base
    def area(self,l,b):
        self.l=l
        self.b=b
        print("area=",self.l*self.b)

class GuestRoom(Room):  # child derived
    def msg(self):
        print("This is GuestRoom")



#r=Room()
#r.area(5,7)

g=GuestRoom()
g.area(55,2)
g.msg()