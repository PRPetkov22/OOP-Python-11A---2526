def sort_by_last_letter(names):
    """
    Сортира списък от имена по последна буква
    Sorts a list of names by their last letter
    """
    return sorted(names, key=lambda name: name[-1].lower())

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]
    print("Original list:")
    print(names)
    
    sorted_names = sort_by_last_letter(names)
    print("\nSorted by last letter:")
    print(sorted_names)
    
    bulgarian_names = ["Иван", "Мария", "Петър", "Анна", "Таня", "Борис"]
    print("\n\nBulgarian names:")
    print(bulgarian_names)
    
    sorted_bulgarian = sort_by_last_letter(bulgarian_names)
    print("Sorted by last letter:")
    print(sorted_bulgarian)
    
    print("\n\nNames with their last letters:")
    for name in sorted_names:
        print(f"{name:15} -> last letter: '{name[-1]}'")
