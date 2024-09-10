# super() = Function used in child class to class methods from a parent class(super class)
#            Allows you to extend the functuibakuty if the inherited methods

# super() = Function used in child class to call methods from a parent class (super class)
#            Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        # Initialize the Shape class with color and is_filled attributes
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        # Print a description of the shape, indicating its color and whether it is filled
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):  # Inherit from Shape
    def __init__(self, color, is_filled, radius):
        # Initialize the Circle class, calling the parent class (Shape) initializer
        super().__init__(color, is_filled)
        # Set the radius attribute specific to Circle
        self.radius = radius

    def describe(self):
        # Print a description of the circle, including its area
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")
        # Call the describe method of the parent class (Shape)
        super().describe()

class Square(Shape):  # Inherit from Shape
    def __init__(self, color, is_filled, width):
        # Initialize the Square class, calling the parent class (Shape) initializer
        super().__init__(color, is_filled)
        # Set the width attribute specific to Square
        self.width = width

    def describe(self):
        # Print a description of the square, including its area
        print(f"It is a square with an area of {self.width * self.width}")
        # Call the describe method of the parent class (Shape)
        super().describe()

class Triangle(Shape):  # Inherit from Shape
    def __init__(self, color, is_filled, width, height):
        # Initialize the Triangle class, calling the parent class (Shape) initializer
        super().__init__(color, is_filled)
        # Set the width and height attributes specific to Triangle
        self.width = width
        self.height = height

    def describe(self):
        # Print a description of the triangle, including its area
        print(f"It is a triangle with an area of {self.width * self.height / 2}")
        # Call the describe method of the parent class (Shape)
        super().describe()

# Create an instance of Circle with color "Red", filled status True, and radius 5
circle = Circle("Red", True, 5)
# Create an instance of Square with color "Blue", filled status False, and width 6
square = Square("Blue", False, 6)
# Create an instance of Triangle with color "Yellow", filled status True, width 7, and height 8
triangle = Triangle("Yellow", True, 7, 8)

# Print the color of the circle instance
print(circle.color)
# Print the color of the square instance
print(square.color)
# Print the width of the square instance with "cm" appended
print(f"{square.width}cm")

# Call the describe method of the circle instance
circle.describe()
