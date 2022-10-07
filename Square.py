from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return "a square is just a rectangle whose four sides are all equal"
