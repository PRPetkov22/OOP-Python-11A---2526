from abc import ABC, abstractmethod

class Art_piece(ABC):
    def __init__(self, name=None, author=None, price=None, year=None, unique_number=None):
        if name is None:
            self._name = input("Enter art piece name: ")
        else:
            self._name = name
        if author is None:
            self._author = input("Enter author: ")
        else:
            self._author = author
        if price is None:
            self._price = float(input("Enter price: "))
        else:
            self._price = price
        if year is None:
            self._year = int(input("Enter year: "))
        else:
            self._year = year
        if unique_number is None:
            self._unique_number = input("Enter unique number: ")
        else:
            self._unique_number = unique_number

    # Getters and setters for encapsulation
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_unique_number(self):
        return self._unique_number

    def set_unique_number(self, unique_number):
        self._unique_number = unique_number

    @abstractmethod
    def display_info(self):
        pass