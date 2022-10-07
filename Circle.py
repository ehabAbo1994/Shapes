from calculator import Shape
from math import pi


class Circle(Shape):
    def __init__(self,radios):
        self.radius = radios

    def get_area(self):
        return pi * (self.radius ** 2)

    def __str__(self):
        return f"the area of this circle is {self.get_area()} "