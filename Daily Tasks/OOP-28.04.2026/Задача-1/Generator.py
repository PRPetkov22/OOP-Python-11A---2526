def even_numbers(n):
    """
    Генератор, който връща четни числа до N
    Generator that returns even numbers up to N
    """
    for i in range(2, n + 1, 2):
        yield i
        
if __name__ == "__main__":
    print("Even numbers up to 10:")
    for num in even_numbers(10):
        print(num, end=" ")
    print("\n")
    
    print("Even numbers up to 20 as list:")
    result = list(even_numbers(20))
    print(result)
