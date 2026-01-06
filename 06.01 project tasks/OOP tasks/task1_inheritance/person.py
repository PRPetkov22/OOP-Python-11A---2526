class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return "| Name: " + self.name + " | Age: " + str(self.age)

    def birthday(self):
        self.age += 1