from user import User

class Student(User):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

        self.my_grades = {}

    def add_grade_for_me(self, course_title, grade):
        if course_title not in self.my_grades:
            self.my_grades[course_title] = []
        self.my_grades[course_title].append(grade)