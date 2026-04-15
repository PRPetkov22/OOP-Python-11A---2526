from characters.Character import Character


class Wolf(Character):
    def __init__(self, name="Вълкът"):
        super().__init__(name)

    def act(self):
        print(f"{self.name} се промъква тихо между дърветата и търси плячка.")

    def react(self, event):
        if event == "wolf_appears":
            print(f"{self.name} се усмихва хитро знаейки ,че е опасността.")
        elif event == "danger":
            print(f"{self.name} става още по-агресивен и настъпателен.")
        else:
            print(f"{self.name} наблюдава внимателно всичко наоколо.")

    def interact(self, other):
        print(f"{self.name} среща {other.name}.")
        if other.__class__.__name__ == "RedRidingHood":
            print(f"{self.name} я заблуждава с мили думи и измамни въпроси.")
        elif other.__class__.__name__ == "Grandma":
            print(f"{self.name} напада {other.name} и заема мястото ѝ.")
        else:
            print(f"{self.name} гледа подозрително {other.name}.")