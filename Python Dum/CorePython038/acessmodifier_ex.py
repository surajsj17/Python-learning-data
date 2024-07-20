
class Vehicle: #parent _class
    _secret = "SECRET" # protected
    __pvt = "PRIVATE" # private
    public = "public_attribute"
    def drive(self):
        print("Vehicle is being driven.")
    def get_pvt(self):
        return self.__pvt

class Car(Vehicle): # child_class  inhetit the parent class name - this is inheritance
    def honk(self):
        print("Car is honking.")

# vehicle object
V = Vehicle()
print(V.public)
print(V._secret)
V._secret ="protected12"
#print(V.__pvt) # not possible its private
#Now make object of inherite class
c = Car()
c.drive() # Output: Vehicle is being driven.
c.honk() # Output: Car is honking.
print("before changing public",c.public)
c.public = "change public attribute value"
print("after changing",c.public)
print(c._secret) # __
c._secret = "not secret"
print(c._secret)
# # now access private attibute
print(c.__pvt) # we are trying to acess private method. not possible
# #print(car._Car__pvt)
# print(c.get_pvt())




