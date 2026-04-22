from Art_piece import Art_piece

class Painting(Art_piece):
    def __init__(self, name=None, author=None, price=None, year=None, unique_number=None):
        super().__init__(name, author, price, year, unique_number)

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Author: {self._author}")
        print(f"Price: {self._price}")
        print(f"Year: {self._year}")
        print(f"Unique Number: {self._unique_number}")
        print()