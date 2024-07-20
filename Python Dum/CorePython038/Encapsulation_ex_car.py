"""Encapsulation is a fundamental concept in
object-oriented programming
that allows bundling of data (attributes) and methods (functions)
together within a class.

It promotes the idea of data hiding, where the internal details of a class
are hidden from external access,
and interactions with the class are done through a well-defined interface."""

# Python doesn't strictly enforce access modifiers like some other languages,
# but the use of naming conventions helps indicate the data hiding
class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        self.__mileage = 0 # private attribute
        #self.mileage = 0 # public Attribute
        #self._mileage = 0 # protected
    def get_make(self):
        return self._make
    def get_model(self):
        return self._model
    def get_year(self):
        return self._year
    def get_mileage(self):
        return self.__mileage #private
        #return self.mileage
        #return self._mileage #protected
    def drive(self, miles):
        if miles > 0:
            self.__mileage += miles #private
            #self.mileage+=miles # public
            #self._mileage +=miles # potected
        return self.__mileage

# Creating an instance of Car class
my_car = Car("Toyota", "Camry", 2021)
# Accessing private attributes using getter methods
print(my_car.get_make())  # Output: Toyota
print(my_car.get_model())  # Output: Camry
print(my_car.get_year())  # Output: 2021
print(my_car.get_mileage()) # 0
my_car._year = 2023
print("year:",my_car._year)
print("year:",my_car.get_year())
#here we access public attribute( self.mileage =0)

#print("first we initalize mileage =0:",my_car.__mileage) #Output 0
my_car.__mileage = 300 # Here we change atrribute outside the class using class object
print("we change public attribute ,mileage",my_car.get_mileage()) # output 300
print(my_car.drive(400))

                #protected----
# Now if you create atrribute as protected _ or private  __)
# (self._mileage)
# print("now we change mileage to protected_mileage:"
#       ,my_car._mileage)
# Output 0 (right first we initialize it)

# change attribute value
#my_car._mileage = -400 # its possible we use here protected

#my_car.drive
#print(my_car.get_mileage()) # its possible we use here proteceted
 # but its not way if your attributes are protected
  #then it can not change directly

# Modifying private attribute indirectly through a method
#my_car.drive(235)
#print("change value",my_car.get_mileage())


# Now make attribute private (__)
#print("private attribute",my_car.get_mileage()) # Output 0

# now i change atrribute value.xDW

#my_car.__mileage = 200 # change not possible
#print(my_car.__mileage) # it will show you 200 but its different thing in main attribute __mileagenot changed
#print("change private attributeas 200 and we got o/p: ",my_car.get_mileage())

#my_car.drive(345) # miles 345
#print("change private attributes through method (345) and we got o/p: ",my_car.get_mileage())



# name mangling:


'''
print("hello",my_car._Car__mileage) # this is how we get private attr.
# from object

#my_car._Car__mileage = 256

print(my_car._Car__mileage)
print(my_car.get_mileage())

'''

class vehicle(Car):
    def drive1(self):
        print("I am child class")

v1 = vehicle('toyota','x23',2023)
print("mileage",v1.get_mileage())
print("try to change mileage")
v1.__mileage= 300
print("Access mileage using get method")
print(v1.get_mileage())


my_car.__mileage=500
print(my_car.get_mileage())
my_car.drive(400)
print(my_car.get_mileage())
v1.drive(650)
print("call get_mileage",v1.get_mileage())
