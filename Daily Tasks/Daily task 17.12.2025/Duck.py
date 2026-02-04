from Swim import Swim
from Fly import Fly

class Duck(Fly, Swim):
    def swim(self):
        print("swim")
        d = Duck()
        d.fly()
        d.swim()