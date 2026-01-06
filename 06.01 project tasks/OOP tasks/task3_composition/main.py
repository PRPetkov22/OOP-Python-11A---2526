from teacher import Teacher
from student import Student
from course import Course

t = Teacher("Mr Ivanov")
c = Course("Math", t)

s1 = Student("David", 7)
s2 = Student("Boris", 12)

c.add_student(s1)
c.add_student(s2)

print("Course:", c.title)
print("Students:", c.list_students())