#Дъщерен клас
from html.entities import name2codepoint

from Person import Person

class Student(Person):
    pass
def __init__(self, name, grade):
    super().__init__(name)
    self.grade = grade
    s=Student("Nikolai", 17)
    print(s.name, s.grade)
