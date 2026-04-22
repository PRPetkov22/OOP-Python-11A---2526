from Art_piece import Art_piece
from Painting import Painting
from Oil_painting import Oil_painting
from Watercolor_painting import Watercolor_painting

class Paintings:
    def __init__(self):
        self.art_pieces = []

    def get_art_pieces(self):
        return self.art_pieces

    def set_art_pieces(self, art_pieces):
        self.art_pieces = art_pieces

    def add_art_piece(self, art_piece):
        for p in self.art_pieces:
            if p.get_unique_number() == art_piece.get_unique_number():
                raise ValueError("Art piece with this unique number already exists.")
        self.art_pieces.append(art_piece)

    def remove_art_piece(self, unique_number):
        for p in self.art_pieces:
            if p.get_unique_number() == unique_number:
                self.art_pieces.remove(p)
                return
        print("Art piece with this unique number not found.")

    def print_by_author(self, author=""):
        if author == "":
            for p in self.art_pieces:
                p.display_info()
        else:
            for p in self.art_pieces:
                if p.get_author() == author:
                    p.display_info()

    def find_most_expensive(self):
        if not self.art_pieces:
            print("No art pieces.")
            return
        max_price = max(p.get_price() for p in self.art_pieces)
        expensive = [p for p in self.art_pieces if p.get_price() == max_price]
        for p in expensive:
            p.display_info()

    def average_price_by_author(self, author=""):
        if author == "":
            if not self.art_pieces:
                return 0
            total = sum(p.get_price() for p in self.art_pieces)
            return total / len(self.art_pieces)
        else:
            author_pieces = [p for p in self.art_pieces if p.get_author() == author]
            if not author_pieces:
                return 0
            total = sum(p.get_price() for p in author_pieces)
            return total / len(author_pieces)