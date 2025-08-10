import math

class Shape:
    """Base class for shapes"""
    
    def area(self):
        """Base area method that raises NotImplementedError"""
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""
    
    def __init__(self, length: float, width: float):
        """Initialize rectangle with length and width"""
        self.length = length
        self.width = width
    
    def area(self):
        """Override area method to calculate rectangle area: length × width"""
        return self.length * self.width


class Circle(Shape):
    """Circle class inheriting from Shape"""
    
    def __init__(self, radius: float):
        """Initialize circle with radius"""
        self.radius = radius
    
    def area(self):
        """Override area method to calculate circle area: π × radius²"""
        return math.pi * (self.radius ** 2)
