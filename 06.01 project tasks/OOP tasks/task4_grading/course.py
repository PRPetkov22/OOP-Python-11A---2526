from gradeable_mixin import GradeableMixin

class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def set_grade(self, student, grade):
        if student not in self.students:
            raise ValueError("Student isn't enrolled in this course! ]")

        if not isinstance(student, GradeableMixin):
            raise TypeError("This student can't receive grades! ]")

        student.add_grade(self.title, grade)