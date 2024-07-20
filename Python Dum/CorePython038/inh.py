#  inhertitance : superclass,base class,parentclass--
#child class  subclass
#single level inh.
#parent --> child


class Vehicle: # parent class
    name = "toyota"
    model = "abc"
    year = "2003"
    def get_vehicledata(self):
        print("I am parent class method",self.name)

class Car(Vehicle): # child class
    print("this is chid class inherit attributes of parent class")
    print("car name is",Vehicle.name)


C= Car()
print(C.model,C.year)
C.get_vehicledata()

class Parent:
    surname = "Parmar" # attributes
    def get_property(self,property = 100000): # method,behaviour
        print("parents property",property)

class child(Parent):
    name = "suvidha"
    print("My name is:",name,Parent.surname)

ch = child()
ch.get_property() #
ch.get_property(200000)

# multilevel inheritance
class G_Parent:
    surname = "Parmar" # attributes
    def get_property(self,property = 100000): # method,behaviour
        print("parents property",property)
class Parent(G_Parent):
    middle_name = "john"

class child(Parent):
    name = "suvidha"
    print("My name is:",name,Parent.middle_name,Parent.surname)

ch1 = child()
print("my full name is:",ch1.name,ch1.middle_name,ch1.surname)