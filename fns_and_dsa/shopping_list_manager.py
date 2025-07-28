def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice): ")
        
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item cannot be empty. Please try again.")
        elif choice == '2':
            print("Current shopping list:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")
        elif choice == '3':
            print("Your shopping list:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
            print()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
# This code defines a simple shopping list manager that allows users to add, remove, and view their shopping list items through a command-line interface.
