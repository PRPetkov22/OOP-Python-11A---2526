from teacher import Teacher
from course import Course
from graded_student import GradedStudent
from student import Student

def main():
    t = Teacher("Mr. Petrov", 40, "Math")
    course = Course("Math", t)

    gs = GradedStudent("Ivan", 16, 10)
    normal_student = Student("Maria", 15, 9)

    course.add_student(gs)
    course.add_student(normal_student)

    course.set_grade(gs, 4)
    course.set_grade(gs, 6)
    course.set_grade(gs, 5)
    course.set_grade(gs, 6)

    print("Plamen's grades:", gs.grades)
    print("Plamen's Math average:", gs.average("Math"))
    print("Plamen's overall average:", gs.overall_average())

    print("\n  - Testing error for normal student -  ")
    try:
        course.set_grade(normal_student, 6)
    except Exception as e:
        print("Error [", e)

if __name__ == "__main__":
    main()