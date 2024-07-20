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

circle.area()