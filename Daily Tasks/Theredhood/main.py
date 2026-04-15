from characters.Theredhood import Theredhood
from characters.Wolf import Wolf
from characters.Grandmother import Grandmother
from Story_world import World


def main():
    girl = Theredhood()
    wolf = Wolf()
    grandma = Grandmother()

    world = World()
    world.add_character(girl)
    world.add_character(wolf)
    world.add_character(grandma)

    world.simulate()


if __name__ == "__main__":
    main()