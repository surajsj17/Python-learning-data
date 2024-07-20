# Hierarchical Inheritance:
"""
Hierarchical inheritance involves multiple classes inheriting from
a single parent class.
This allows for specialization of different child classes
 based on a common parent class.
"""
# one parent two child
# parent : vehicle --method (drive)
# child: car (honk),bike (speed),truck  (load)
class Vehicle: # single parents
    def drive(self):
        print("Vehicle is being driven.")

class Car(Vehicle):
    def honk(self):
        print("Car is honking.")

class Truck(Vehicle):
    def load(self):
        print("Truck is being loaded.")
class bike(Vehicle):
    pass
car = Car()
car.drive()  # Output: Vehicle is being driven.
car.honk()  # Output: Car is honking.

truck = Truck()
truck.drive()  # Output: Vehicle is being driven.
truck.load()  # Output: Truck is being loaded.

list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)


l1 = [1,2,3,4,5]
print(l1[7])

