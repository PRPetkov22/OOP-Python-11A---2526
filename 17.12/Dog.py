from Animals import Animals

class Dog(Animals):

    def speak(self):
        super().speak()
        print("Dog is speaking")
        dog = Dog()
        dog.speak()