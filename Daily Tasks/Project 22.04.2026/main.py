from Paintings import Paintings
from Painting import Painting

def main():
    paintings = Paintings()

    while True:
        print("Menu:")
        print("1. Add painting")
        print("2. Remove painting")
        print("3. Print paintings by author")
        print("4. Find most expensive paintings")
        print("5. Average price by author")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Adding a new painting:")
            painting = Painting()
            try:
                paintings.add_painting(painting)
                print("Painting added successfully.")
            except ValueError as e:
                print(e)
        elif choice == "2":
            unique_number = input("Enter unique number to remove: ")
            paintings.remove_painting(unique_number)
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