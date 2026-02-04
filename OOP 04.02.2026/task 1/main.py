from dog import Dog
from cat import Cat
from cow import Cow

n = int(input())

for _ in range(n):
    animal = input().strip().upper()

    if animal == "DOG":
        Dog().speak()
    elif animal == "CAT":
        Cat().speak()
    elif animal == "COWC":
        Cow().speak()