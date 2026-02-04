from fulltime import FullTime
from parttime import PartTime
from intern import Intern

n = int(input())

for _ in range(n):
    data = input().split()
    emp_type = data[0]

    if emp_type == "FULLTIME":
        emp = FullTime()
    elif emp_type == "PARTTIME":
        hours = int(data[1])
        emp = PartTime(hours)
    elif emp_type == "INTERN":
        emp = Intern()

    print(emp.salary())