from Rectangle import Rectangle
from Circle import Circle

shapes = [
    Rectangle(4, 5),
    Circle(3),
    Rectangle(2, 7),
    Circle(1.5),
]

total_area = 0
for shape in shapes:
    total_area += shape.area()

print(f"Обща площ: {total_area:.2f}")
