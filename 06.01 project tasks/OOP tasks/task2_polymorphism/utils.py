from student import Student
from teacher import Teacher

def print_people(people):
    for p in people:
        print(p.get_info())

        if isinstance(p, Teacher):
            print(" ", p.teach())

        if isinstance(p, Student):
            print("  - Student in grade", p.grade)