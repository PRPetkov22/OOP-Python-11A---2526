from Painting import Painting

class Oil_painting(Painting):
    def display_info(self):
        print(f"Oil Painting - Name: {self._name}")
        print(f"Author: {self._author}")
        print(f"Price: {self._price}")
        print(f"Year: {self._year}")
        print(f"Unique Number: {self._unique_number}")
        print()