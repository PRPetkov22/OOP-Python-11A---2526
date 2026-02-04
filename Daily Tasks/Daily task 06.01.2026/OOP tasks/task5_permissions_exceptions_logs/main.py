from logger import Logger
from admin import Admin
from teacher import Teacher
from student import Student
from course import Course
from exceptions import PermissionDeniedError, NotEnrolledError

def main():
    logger = Logger()

    admin = Admin("Admin", 50)
    teacher1 = Teacher("Mr Ivanov", 40, "French")
    teacher2 = Teacher("Mrs Kumanova", 38, "History")

    students = [
        Student("Student 1", 14, 8),
        Student("Student 2", 17, 11),
        Student("Student 3", 12, 6),
        Student("Student 4", 18, 12),
        Student("Student 5", 13, 7),
    ]

    course1 = Course("French Course", teacher1, logger)
    course2 = Course("History Course", teacher2, logger)

    course1.add_student(teacher1, students[0])
    course1.add_student(admin, students[1])
    course2.add_student(teacher2, students[2])

    try:
        course1.add_student(students[0], students[3])
    except PermissionDeniedError as e:
        print("Expected error:", e)

    try:
        course1.set_grade(teacher1, students[4], 6)
    except NotEnrolledError as e:
        print("Expected error:", e)

    course1.set_grade(teacher1, students[0], 6)
    course1.set_grade(admin, students[1], 5)

    print("\nStudent 1 grades:", students[0].my_grades)
    print("Student 2 grades:", students[1].my_grades)

    print("\n  - LOGS -  ")
    logger.show_logs()

if __name__ == "__main__":
    main()