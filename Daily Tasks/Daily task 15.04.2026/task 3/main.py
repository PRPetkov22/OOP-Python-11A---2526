from Square import Square
from Circle import Circle
from Triangle import Triangle


def main():
    square = Square(4)
    circle = Circle(3)
    triangle = Triangle(3, 4, 5)

    print(f"Square area: {square.area()}, perimeter: {square.perimeter()}")
    print(f"Circle area: {circle.area():.2f}, perimeter: {circle.perimeter():.2f}")
    print(f"Triangle area: {triangle.area():.2f}, perimeter: {triangle.perimeter()}")


if __name__ == "__main__":
    main()
