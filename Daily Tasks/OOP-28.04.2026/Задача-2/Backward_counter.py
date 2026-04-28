class BackwardCounter:
    """
    Клас итератор, който брои назад от N до 1
    Iterator class that counts backwards from N to 1
    """
    
    def __init__(self, n):
        """
        Инициализира итератора с крайна стойност
        Initialize the iterator with the maximum value
        """
        self.n = n
        self.current = n
    
    def __iter__(self):
        """
        Връща самия обект като итератор
        Returns the object itself as an iterator
        """
        return self
    
    def __next__(self):
        """
        Връща следващата стойност (намаляваща)
        Returns the next value (decreasing)
        """
        if self.current < 1:
            raise StopIteration
        
        result = self.current
        self.current -= 1
        return result

if __name__ == "__main__":
    print("Counting backwards from 5 to 1:")
    for num in BackwardCounter(5):
        print(num, end=" ")
    print("\n")
    
    print("Counting backwards from 10 to 1 using next():")
    counter = BackwardCounter(10)
    try:
        while True:
            print(next(counter), end=" ")
    except StopIteration:
        print("\nDone!")
    
    print("\nAs a list from 7 to 1:")
    result = list(BackwardCounter(7))
    print(result)
