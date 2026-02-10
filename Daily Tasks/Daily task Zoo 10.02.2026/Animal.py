class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def makeSound(self):
        return f"{self.name} ({self.age} г. издава звука: {self.sound})"

    def info(self):
        return f"{self.__class__.__name__}: {self.name}, {self.age} г."