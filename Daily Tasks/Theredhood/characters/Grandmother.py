from characters.Character import Character


class Grandmother(Character):
    def __init__(self, name="Бабата"):
        super().__init__(name)

    def act(self):
        print(f"{self.name} си почива и чака Червената шапчица.")

    def react(self, event):
        if event == "wolf_appears":
            print(f"{self.name} се ужасява и вика за помощ.")
        elif event == "danger":
            print(f"{self.name} е беззащитна и трепери от страх.")
        else:
            print(f"{self.name} се чуди дали всичко е наред.")

    def interact(self, other):
        print(f"{self.name} среща {other.name}.")
        if other.__class__.__name__ == "RedRidingHood":
            print(f"{self.name} се радва, че внучката ѝ е дошла.")
        elif other.__class__.__name__ == "Wolf":
            print(f"{self.name} разбира, че е в беда.")
        else:
            print(f"{self.name} говори спокойно с {other.name}.")