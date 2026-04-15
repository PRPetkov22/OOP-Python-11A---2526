class World:
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def simulate(self):
        print("=== НАЧАЛО НА ПРИКАЗКАТА ===\n")

        print("1. Всеки герой действа:")
        for character in self.characters:
            character.act()

        print("\n2. Появява се вълкът:")
        for character in self.characters:
            character.react("wolf_appears")

        print("\n3. Възниква опасност:")
        for character in self.characters:
            character.react("danger")

        print("\n4. Срещи между героите:")
        for i in range(len(self.characters)):
            for j in range(i + 1, len(self.characters)):
                self.characters[i].interact(self.characters[j])
                self.characters[j].interact(self.characters[i])
                print()

        print("=== КРАЙ НА ПРИКАЗКАТА ===")