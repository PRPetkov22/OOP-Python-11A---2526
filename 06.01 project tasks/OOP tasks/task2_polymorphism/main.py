from student import Student
from teacher import Teacher
from utils import print_people

people = [
    Student("Mariq", 15, 9),
    Teacher("Mr Petrov", 58, "English"),
    Student("Denis", 18, 12)
]

print_people(people)