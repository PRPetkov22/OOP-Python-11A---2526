from Herbivore import Herbivore

class Cow(Herbivore):
    def __init__(self, name, age):
        super().__init__(name, age, "Мууу")