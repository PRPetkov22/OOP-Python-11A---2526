from Painting import Painting

class Paintings:
    def __init__(self):
        self.paintings = []

    def get_paintings(self):
        return self.paintings

    def set_paintings(self, paintings):
        self.paintings = paintings

    def add_painting(self, painting):
        for p in self.paintings:
            if p.get_unique_number() == painting.get_unique_number():
                raise ValueError("Painting with this unique number already exists.")
        self.paintings.append(painting)

    def remove_painting(self, unique_number):
        for p in self.paintings:
            if p.get_unique_number() == unique_number:
                self.paintings.remove(p)
                return
        print("Painting with this unique number not found.")

    def print_by_author(self, author=""):
        if author == "":
            for p in self.paintings:
                p.print_info()
        else:
            for p in self.paintings:
                if p.get_author() == author:
                    p.print_info()

    def find_most_expensive(self):
        if not self.paintings:
            print("No paintings.")
            return
        max_price = max(p.get_price() for p in self.paintings)
        expensive = [p for p in self.paintings if p.get_price() == max_price]
        for p in expensive:
            p.print_info()

    def average_price_by_author(self, author=""):
        if author == "":
            if not self.paintings:
                return 0
            total = sum(p.get_price() for p in self.paintings)
            return total / len(self.paintings)
        else:
            author_paintings = [p for p in self.paintings if p.get_author() == author]
            if not author_paintings:
                return 0
            total = sum(p.get_price() for p in author_paintings)
            return total / len(author_paintings)