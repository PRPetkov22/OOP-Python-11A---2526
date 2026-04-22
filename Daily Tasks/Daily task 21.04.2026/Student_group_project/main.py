from Student import Student
from Student_group import Student_group


def main():
    student1 = Student("Пламен", 5.90)
    student2 = Student("Борис", 5.25)
    student3 = Student("Димитър", 4.50)
    student4 = Student("Михаил", 5.75)
    student5 = Student("Евгени", 4.80)

    group = Student_group()
    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)
    group.add_student(student4)
    group.add_student(student5)

    group.print_students()

    average = group.get_average_grade()
    print(f"\nСреден успех: {average:.2f}")

    best_student = group.get_best_student()
    if best_student is not None:
        print(f"Най-добър студент: {best_student}")
    else:
        print("Най-добър студент: None")

    print("\nСтуденти с оценка поне 5.50:")
    students_above = group.get_students_with_grade_above(5.50)

    for student in students_above:
        print(student)


if __name__ == "__main__":
    main()