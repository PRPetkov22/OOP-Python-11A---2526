from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    """
    Клас за представяне на ученик с име и оценка
    Class to represent a student with name and grade
    """
    name: str
    grade: float
    
    def __repr__(self):
        return f"Student(name='{self.name}', grade={self.grade})"


def sort_students(students: List[Student]) -> List[Student]:
    """
    Сортира списък от ученици по:
    1. Оценка (низходящо - от висока към ниска)
    2. Име (възходящо - по азбучен ред)
    
    Sorts a list of students by:
    1. Grade (descending - from high to low)
    2. Name (ascending - alphabetically)
    """
    return sorted(students, key=lambda student: (-student.grade, student.name.lower()))

if __name__ == "__main__":
    students = [
        Student("Alice", 5.5),
        Student("Bob", 4.0),
        Student("Charlie", 5.5),
        Student("Diana", 4.5),
        Student("Eve", 5.5),
        Student("Frank", 4.0),
        Student("Grace", 4.5),
    ]
    
    print("Original list:")
    for student in students:
        print(f"  {student.name:15} -> {student.grade}")
    
    sorted_students = sort_students(students)
    
    print("\n\nSorted by grade (descending) then by name (ascending):")
    for student in sorted_students:
        print(f"  {student.name:15} -> {student.grade}")
    
    print("\n\n--- Bulgarian Students Example ---")
    bulgarian_students = [
        Student("Иван", 5.0),
        Student("Мария", 5.5),
        Student("Петър", 5.0),
        Student("Анна", 4.5),
        Student("Таня", 5.5),
        Student("Борис", 4.5),
    ]
    
    print("Original list:")
    for student in bulgarian_students:
        print(f"  {student.name:15} -> {student.grade}")
    
    sorted_bulgarian = sort_students(bulgarian_students)
    
    print("\nSorted by grade (descending) then by name (ascending):")
    for student in sorted_bulgarian:
        print(f"  {student.name:15} -> {student.grade}")
