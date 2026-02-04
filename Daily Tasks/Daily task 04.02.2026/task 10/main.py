from upper import Upper
from lower import Lower
from reverse import Reverse
from vowelstostar import VowelsToStar

n = int(input())

for _ in range(n):
    data = input().split(maxsplit=1)
    cmd = data[0]
    text = data[1] if len(data) > 1 else ""

    if cmd == "UP":
        transformer = Upper()
    elif cmd == "LOW":
        transformer = Lower()
    elif cmd == "REV":
        transformer = Reverse()
    elif cmd == "VOW":
        transformer = VowelsToStar()

    print(transformer.transform(text))