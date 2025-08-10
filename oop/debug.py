print("Testing imports...")
from polymorphism_demo import Shape, Rectangle, Circle
import math
print("Imports successful!")

print("\nTesting Rectangle...")
rect = Rectangle(10, 5)
print(f"Rectangle: {rect}")
print(f"Area: {rect.area()}")

print("\nTesting Circle...")
circle = Circle(7)
print(f"Circle: {circle}")
print(f"Area: {circle.area()}")

print("\nTesting polymorphism...")
shapes = [rect, circle]
for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
