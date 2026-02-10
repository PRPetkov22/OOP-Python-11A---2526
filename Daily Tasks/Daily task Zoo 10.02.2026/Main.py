from Zoo import Zoo
from Lion import Lion
from Cow import Cow
from Bear import Bear


def print_help():
    print("Commands:")
    print("  add lion <name> <age>")
    print("  add cow <name> <age>")
    print("  add bear <name> <age>")
    print("  list")
    print("  feed")
    print("  sound <name>")
    print("  help")
    print("  exit")


def main():
    zoo = Zoo()
    print("Zoo console started. Type help for commands")

    while True:
        line = input("> ").strip()
        if not line:
            continue

        parts = line.split()
        cmd = parts[0]
        if cmd == "help":
            print_help()

        elif cmd == "exit":
            break

        elif cmd == "add":
            if len(parts) != 4:
                print("ERROR")
                continue

            animal_type = parts[1]
            name = parts[2]
            age = parts[3]

            if animal_type == "lion":
                zoo.addAnimal(Lion(name, age))
            elif animal_type == "cow":
                zoo.addAnimal(Cow(name, age))
            elif animal_type == "bear":
                zoo.addAnimal(Bear(name, age))
            else:
                print("ERROR")

        elif cmd == "list":
            zoo.listAnimals()

        elif cmd == "feed":
            zoo.feedAnimals()

        elif cmd == "sound":
            if len(parts) != 2:
                print("ERROR")
                continue
            zoo.soundByName(parts[1])

        else:
            print("Unknown command. Type help")

    print("Bye!")


if __name__ == "__main__":
    main()