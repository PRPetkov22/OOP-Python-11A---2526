from student import Student
from gradeable_mixin import GradeableMixin

class GradedStudent(Student, GradeableMixin):
    def __init__(self, name, age, grade):
        Student.__init__(self, name, age, grade)
        GradeableMixin.__init__(self)