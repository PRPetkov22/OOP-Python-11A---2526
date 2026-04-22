from Painting import Painting

class Watercolor_painting(Painting):
    def display_info(self):
        print(f"Watercolor Painting - Name: {self._name}")
        print(f"Author: {self._author}")
        print(f"Price: {self._price}")
        print(f"Year: {self._year}")
        print(f"Unique Number: {self._unique_number}")
        print()