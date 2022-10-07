from Rectangle import Rectangle
from math import sqrt


class Hexagon(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def get_area(self):
        return (3 * sqrt(3) * self.side1 ** 2) / 2

    def __str__(self):
        return f"the area of the Hexagon is {self.get_area()}"