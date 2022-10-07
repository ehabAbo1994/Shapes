from calculator import Shape


class Rectangle(Shape):

    def __init__(self, side1, side2):
        super().__init__()
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2

    def __str__(self):
        return f'The area of this {self.__class__.__name__} is: {self.get_area()}'
