from Person import Person

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def info(self):
        return f"{super().info()}, Grade: {self.grade}"