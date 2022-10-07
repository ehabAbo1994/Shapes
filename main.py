from calculator import Shape
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle
from Circle import Circle
from Hexagon import Hexagon

def main():
    r = Rectangle(5, 5)
    print(r)
    s = Square(5)
    print(s)
    t = Triangle(5,5)
    print(t)
    c = Circle(15)
    print(c)
    h = Hexagon(3)
    print(h)


if __name__ == '__main__':
    main()
