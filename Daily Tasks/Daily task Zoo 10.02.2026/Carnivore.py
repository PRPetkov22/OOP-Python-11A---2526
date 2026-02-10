from Animal import Animal

class Carnivore(Animal):
    def hunt(self):
        return f"{self.name} яде месо"