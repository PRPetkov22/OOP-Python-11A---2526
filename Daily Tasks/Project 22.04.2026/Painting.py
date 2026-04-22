class Painting:
    def __init__(self, name=None, author=None, price=None, year=None, unique_number=None):
        if name is None:
            self.name = input("Enter painting name: ")
        else:
            self.name = name
        if author is None:
            self.author = input("Enter author: ")
        else:
            self.author = author
        if price is None:
            self.price = float(input("Enter price: "))
        else:
            self.price = price
        if year is None:
            self.year = int(input("Enter year: "))
        else:
            self.year = year
        if unique_number is None:
            self.unique_number = input("Enter unique number: ")
        else:
            self.unique_number = unique_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_unique_number(self):
        return self.unique_number

    def set_unique_number(self, unique_number):
        self.unique_number = unique_number

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        print(f"Year: {self.year}")
        print(f"Unique Number: {self.unique_number}")
        print()