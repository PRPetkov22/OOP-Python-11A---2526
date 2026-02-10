class Zoo:
    def __init__(self):
        self.animals = {}

    def addAnimal(self, animal):
        self.animals[animal.name] = animal

    def listAnimals(self):
        if not self.animals:
            print("Zoo is empty.")
            return

        for a in self.animals.values():
            print(a.info())

    def feedAnimals(self):
        if not self.animals:
            print("Zoo is empty.")
            return

        for a in self.animals.values():
            if hasattr(a, "hunt"):
                print(a.hunt())
            if hasattr(a, "graze"):
                print(a.graze())

    def soundByName(self, name):
        if name not in self.animals:
            print("ERROR")
            return
        print(self.animals[name].makeSound())