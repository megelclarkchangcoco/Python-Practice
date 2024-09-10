# Polymorphism = Greek word that mean to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                Two ways to achieve POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

# Abstract base class Shape with an abstract method area
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Initialize radius attribute

    def area(self):
        return 3.14 * self.radius ** 2  # Calculate area of the circle

# Square class inheriting from Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side  # Initialize side attribute

    def area(self):
        return self.side ** 2  # Calculate area of the square

# Triangle class inheriting from Shape
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base  # Initialize base attribute
        self.height = height  # Initialize height attribute

    def area(self):
        return self.base * self.height * 0.5  # Calculate area of the triangle

# Pizza class inheriting from Circle
class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)  # Initialize radius attribute using Circle's constructor
        self.topping = toppings  # Initialize topping attribute

# Create a list of shape objects with different dimensions
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

# Iterate through the list of shapes and print the area of each shape
for shape in shapes:
    print(f"{shape.area()}")

