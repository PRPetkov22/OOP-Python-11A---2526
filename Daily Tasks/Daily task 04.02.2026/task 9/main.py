from warrior import Warrior
from mage import Mage
from archer import Archer

n = int(input())
total_attack = 0

for _ in range(n):
    char_type = input().strip()

    if char_type == "WARRIOR":
        character = Warrior()
    elif char_type == "MAGE":
        character = Mage()
    elif char_type == "ARCHER":
        character = Archer()

    atk = character.attack()
    print(atk)
    total_attack += atk

print(total_attack)