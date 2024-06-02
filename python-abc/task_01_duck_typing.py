#!/usr/bin/python3

"""Defines Shape abstract class and concrete classes Circle and Rectangle."""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter of the shape."""
        pass

class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Returns the area of the circle, handling negative radius."""
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """Returns the perimeter of the circle, handling negative radius."""
        return 2 * math.pi * abs(self.radius)

class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Prints the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
