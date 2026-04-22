from Paintings import Paintings
from Painting import Painting
from Oil_painting import Oil_painting
from Watercolor_painting import Watercolor_painting

def main():
    paintings = Paintings()

    while True:
        print("Menu:")
        print("1. Add art piece")
        print("2. Remove art piece")
        print("3. Print art pieces by author")
        print("4. Find most expensive art pieces")
        print("5. Average price by author")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Adding a new art piece:")
            print("Choose type: 1. Painting 2. Oil Painting 3. Watercolor Painting")
            type_choice = input("Choose type: ")
            if type_choice == "1":
                art_piece = Painting()
            elif type_choice == "2":
                art_piece = Oil_painting()
            elif type_choice == "3":
                art_piece = Watercolor_painting()
            else:
                print("Invalid type, defaulting to Painting")
                art_piece = Painting()
            try:
                paintings.add_art_piece(art_piece)
                print("Art piece added successfully.")
            except ValueError as e:
                print(e)
        elif choice == "2":
            unique_number = input("Enter unique number to remove: ")
            paintings.remove_art_piece(unique_number)
        elif choice == "3":
            author = input("Enter author: ")
            paintings.print_by_author(author)
        elif choice == "4":
            paintings.find_most_expensive()
        elif choice == "5":
            author = input("Enter author: ")
            avg = paintings.average_price_by_author(author)
            print(f"Average price: {avg}")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()