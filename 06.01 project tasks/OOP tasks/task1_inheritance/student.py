from person import Person

class Student(Person):
    def __init__(self, name, age, grade, school):
        super().__init__(name, age)
        self.grade = grade
        self.school = school

    def get_info(self):
        return super().get_info() + " | Grade: " + str(self.grade) + " | School: " + self.school