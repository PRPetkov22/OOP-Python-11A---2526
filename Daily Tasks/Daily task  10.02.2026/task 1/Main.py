from Person import Person
from Student import Student

def solve():
    n = int(input())
    people = {}
    for _ in range(n):
        data = input().split()
        if data[0] == "Person":
            person = Person(data[1], int(data[2]))
            print(person.info())
        elif data[0] == "Student":
            student = Student(data[1], int(data[2]), data[3])
            print(student.info())
        elif data[0] == "Info":
            name = data[1]
        if name not in people:
            print('ERROR')
        else:
            print(people[name].info())

def main():
    solve()

if __name__ == "__main__":
    main()