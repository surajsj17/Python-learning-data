""" Inheritance is a fundamental concept in (OOP)
that allows you to create new classes based on existing classes.
It enables you to define a new class by extending an existing
class,there by inheriting its attributes and methods.
The class being inherited from is called the "parent class" or
"superclass,"
 and the class inheriting from it is called the "child class" or "subclass." """

#Single level : one parent one child.
from inh1_ex import Parent1

class A(Parent1):
    pass
obj = A()
print(obj.surname)
# print()


class parent:
    surname = 'Parmar' # attribute
    def parent_m(self,name):
        print("I am parent class",name,self.surname)
class child(parent)  :
    print("I am child class")
    def child_m(self,name):
        print("My name is:",name,self.surname)
ch1 = child()
ch1.child_m('suvidha')
ch1.parent_m('abcd')

#p1 = parent()
ch1.parent_m('john')
ch1.surname="king"
ch1.child_m('abc')
ch1.parent_m('steven')

class Vehicle: #parent _class
    def drive(self):
        print("Vehicle is being driven.")

class Car(Vehicle): # child_class
    def honk(self):
        print("Car is honking.")

car1 = Car()
car1.drive()  # Output: Vehicle is being driven.
car1.honk()  # Output: Car is honking.

print("*"*200)
# SUPER() METHOD EXAMPLE
# used to give access to methods and properties
# of parent class.
class Vehicle:    
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"The {self.brand} is driving.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  #  its call base class(superclass)
                               # init method
        self.model1 = model
    def drive(self):
        super().drive()
        # Call parent class's drive method
        # O/p:The Toyota is driving.
        print(f"The {self.brand} {self.model1} is driving.")

    def honk(self):
        print("Beep! Beep!")

# Creating instances of the child class
car1 = Car("Toyota", "Camry")

# Accessing the inherited attribute
#print("child class",car1.brand)  # Output: Toyota #super class attribute print

# Calling the inherited method
car1.drive()  # Output: The Toyota Camry is driving.
# Calling the method specific to the child class
car1.honk()  # Output: Beep! Beep!


# superclass  shape --> method (area)
# circle (shape) --> area () (must create constructor)
# rectangle(shape) --> area() constructor (l*w)  --> (l*l)
# square  (rectangle) --> find area of square
# used(super) method to call rectangle constructor
# and also call area method of rectangle.

import math

class Shape:
    def area(self):
        print("I am main area class")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        super().area() # 3.14 *r *r
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width # 4 * 4

class Square(Rectangle): # side *side
    def __init__(self, side): # 10
        super().__init__(side, side) #


# Example usage
circle = Circle(5)
print(f"Area of the circle: {circle.area()}")

rectangle = Rectangle(4, 6)
print(f"Area of the rectangle: {rectangle.area()}")

square = Square(4)
print(f"Area of the square: {square.area()}")





