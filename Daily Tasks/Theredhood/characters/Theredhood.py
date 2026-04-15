from characters.Character import Character


class Theredhood(Character):
    def __init__(self, name="Червената шапчица"):
        super().__init__(name)

    def act(self):
        print(f"{self.name} весело си върви през гората с кошница.")

    def react(self, event):
        if event == "wolf_appears":
            print(f"{self.name} се изненадва, но започва да говори доверчиво с вълка.")
        elif event == "danger":
            print(f"{self.name} се уплашва и не знае какво да направи.")
        else:
            print(f"{self.name} не разбира напълно какво се случва.")

    def interact(self, other):
        print(f"{self.name} среща {other.name}.")
        if other.__class__.__name__ == "Wolf":
            print(f"{self.name} наивно разказва на вълка къде отива.")
        else:
            print(f"{self.name} поздравява {other.name} учтиво.")