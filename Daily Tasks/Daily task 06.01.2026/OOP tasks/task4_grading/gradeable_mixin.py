class GradeableMixin:
    def __init__(self):
        self.grades = {}

    def add_grade(self, course_title, grade):
        if grade < 2 or grade > 6:
            raise ValueError("Grade must be between 2 and 6.")

        if course_title not in self.grades:
            self.grades[course_title] = []

        self.grades[course_title].append(grade)

    def average(self, course_title):
        if course_title not in self.grades or len(self.grades[course_title]) == 0:
            return 0

        total = sum(self.grades[course_title])
        count = len(self.grades[course_title])
        return total / count

    def overall_average(self):
        all_grades = []
        for course_list in self.grades.values():
            all_grades.extend(course_list)

        if len(all_grades) == 0:
            return 0

        return sum(all_grades) / len(all_grades)