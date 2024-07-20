'''
Hybrid inheritance can be achieved in Python by combining multiple forms
of inheritance,such as single, multiple, hierarchical, and multilevel
inheritance.
'''
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")

# Multiple Inheritance
class ElectricVehicle:
    def charge(self):
        print("Electric vehicle is charging.")

# Hierarchical Inheritance
class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving.")

class Bicycle(Vehicle):
    def ride(self):
        print(f"{self.brand} bicycle is riding.")

# Multilevel Inheritance
class ElectricCar(Car, ElectricVehicle):
    def drive(self):
        print(f"{self.brand} electric car is driving.")

# Hybrid Inheritance
class ElectricBike(Bicycle, ElectricVehicle):
    def ride(self):
        print(f"{self.brand} electric bike is riding.")

# Create instances and demonstrate hybrid inheritance
car = Car("Toyota") # vehicle --> brand value
bike = Bicycle("Schwinn")
electric_car = ElectricCar("Tesla")
electric_bike = ElectricBike("e-Bike")

car.start()
car.drive()

bike.start()
bike.ride()

electric_car.start()
electric_car.drive()
electric_car.charge()

electric_bike.start()
electric_bike.ride()
electric_bike.charge()
