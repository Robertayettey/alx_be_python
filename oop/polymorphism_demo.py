import math

class Shape:
    """Base class for different shapes."""
    
    def area(self):
        """Method to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """Class to represent a rectangle."""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """Override area method to calculate the area of a rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Class to represent a circle."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Override area method to calculate the area of a circle."""
        return math.pi * self.radius ** 2

