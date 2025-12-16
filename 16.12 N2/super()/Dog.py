import Animal

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog")
        dog = Dog()
        dog.speak()