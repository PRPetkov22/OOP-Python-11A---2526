from Student_iterator import Student_iterator


class Student_group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_iterator(self):
        return Student_iterator(self.students)

    def print_students(self):
        print("Списък на студентите:")
        iterator = self.get_iterator()

        while iterator.has_next():
            print(iterator.next())

    def get_students_with_grade_above(self, min_grade):
        result = []
        iterator = self.get_iterator()

        while iterator.has_next():
            student = iterator.next()
            if student.grade >= min_grade:
                result.append(student)

        return result

    def get_average_grade(self):
        if len(self.students) == 0:
            return 0

        total = 0
        iterator = self.get_iterator()

        while iterator.has_next():
            total += iterator.next().grade

        return total / len(self.students)

    def get_best_student(self):
        if len(self.students) == 0:
            return None

        iterator = self.get_iterator()
        best_student = iterator.next()

        while iterator.has_next():
            current_student = iterator.next()
            if current_student.grade > best_student.grade:
                best_student = current_student

        return best_student