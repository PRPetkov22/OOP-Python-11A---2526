from add import Add
from sub import Sub
from mul import Mul
from div import Div

n = int(input())

for _ in range(n):
    data = input().split()
    op = data[0]
    a = float(data[1])
    b = float(data[2])

    if op == "ADD":
        operation = Add()
    elif op == "SUB":
        operation = Sub()
    elif op == "MUL":
        operation = Mul()
    elif op == "DIV":
        operation = Div()

    result = operation.apply(a, b)
    print(result)