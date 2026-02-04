from circle import Circle
from rectangle import Rectangle

n = int(input())

for _ in range(n):
    data = input().split()

    if data[0] == "CIRCLE":
        r = float(data[1])
        shape = Circle(r)

    elif data[0] == "RECTANGLE":
        w = float(data[1])
        h = float(data[2])
        shape = Rectangle(w, h)

    print(f"{shape.area():.2f}")