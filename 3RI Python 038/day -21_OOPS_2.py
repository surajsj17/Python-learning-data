# class Vehicale:
#     def drive(self):
#         print("Vehicle is being drive")
# class Engine:
#     def drive(self):
#         print("Vechice is being drive")
#     def start(self):
#         print("Vehicle is starting")
# class Child(Vehicale ,Engine):
#     def honk(self):
#         print("car is honking")
#         self.start()
#         super().start()
        
# car1 = Child()
# car1.drive()
# car1.start()
# car1.honk()


# # class A:
# #      def drive(self):
# #         print("BMW is being drive")
# # class B(A):
# #     def drive1(self):
# #         print("AUDI is being drive")
# # class C(B):
# #     def drive2(self):
# #         print("LAMBO is being drive")

# # a = A()
# # a.drive()

# # b = B()
# # b.drive1()
# # b.drive()

# c = C()
# c.drive2()


# for row in range(0, 5):
#     for col in range(0,row+1):
#       print("*",end= " ")
#     print()




# superclass shape  --> method (area)
# cricle (shape) --> area () --> (must create constructor)
#rectangle (shape) --> area () --> (must create constructor) l*w
# square (rectangle) --> find area of square 
# used(super) method to call rectangle constructor
# and also call area method of rectangle

# Define the superclass Shape with an area method
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        pi = 3.14
        return pi * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def area(self):
        return super().area()

# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 5)
square = Square(4)

print(f"Area of circle: {circle.area()}")
print(f"Area of rectangle: {rectangle.area()}")
print(f"Area of square: {square.area()}")
