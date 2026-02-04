from car import Car
from bus import Bus
from bike import Bike

n = int(input())

for _ in range(n):
    data = input().split()
    transport = data[0]
    km = float(data[1])

    if transport == "CAR":
        t = Car()
    elif transport == "BUS":
        t = Bus()
    elif transport == "BIKE":
        t = Bike()

    print(f"{t.cost(km):.2f}")