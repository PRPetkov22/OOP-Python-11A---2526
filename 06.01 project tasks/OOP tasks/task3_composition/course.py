class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        if student not in self.students and len(self.students) < 30:
            self.students.append(student)

    def list_students(self):
        names = []
        for s in self.students:
            names.append(s.name)
        return sorted(names)