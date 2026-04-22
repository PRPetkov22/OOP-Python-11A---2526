class Student_iterator:
    def __init__(self, students):
        self.students = students
        self.position = 0

    def has_next(self):
        return self.position < len(self.students)

    def next(self):
        if self.has_next():
            student = self.students[self.position]
            self.position += 1
            return student
        return None

    def __iter__(self):
        return self

    def __next__(self):
        student = self.next()
        if student is None:
            raise StopIteration
        return student