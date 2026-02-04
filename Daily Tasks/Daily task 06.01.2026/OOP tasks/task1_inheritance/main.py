from person import Person
from student import Student

p = Person("Milko", 32)
s1 = Student("Plamen", 17, 11, "High School")
s2 = Student("Misho", 11, 5, "Primary School")

print(p.get_info())
print(s1.get_info())
print(s2.get_info())

print("\nBirthday:")
p.birthday()
s1.birthday()

print(p.get_info())
print(s1.get_info())