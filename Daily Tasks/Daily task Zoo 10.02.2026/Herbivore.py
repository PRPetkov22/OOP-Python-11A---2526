from Animal import Animal

class Herbivore(Animal):
    def graze(self):
        return f"{self.name} яде трева"