
# created nodes for storing the book's info

class Node:
    def __init__(self, id, book_name, author):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.next = None

class Library:
    def __init__(self):
        self.head = None

# function for registering books

    def registerBook(self, id, name, author):
        newNode = Node(id, name, author)

        if self.head is None:
            self.head = newNode
            return True

        current_node = self.head
        while current_node.next:
            if current_node.book_name.lower() == name.lower() and current_node.author.lower() == author.lower():
                print("This book is already registered.")
                return False
            current_node = current_node.next

        current_node.next = newNode
        return True
    
# functions for searching books

    def searchBook(self, data):
        current_node = self.head
        found = False

        if current_node is None:
            print("Sorry, No Books Available")
            return

        data = data.lower()
        while current_node:
            if data in current_node.book_name.lower() or data in current_node.author.lower():
                print(f"\nBook Id: {current_node.id}, Book Name: {current_node.book_name}, Book Author: {current_node.author}")
                found = True
            current_node = current_node.next

        if not found:
            print("Book not found")
            
# functions for showing the books presenting in the library

    def showBooks(self):
        current_node = self.head

        if current_node is None:
            print("No Books Available")
            return

        while current_node:
            print(f"\nBook Id: {current_node.id}, Book Name: {current_node.book_name}, Book Author: {current_node.author}")
            current_node = current_node.next
            
# issue a book
            
    def issue(self, key):
        current_node = self.head
        prev_node = None
        found = False

        # Search for the book with the provided key
        while current_node:
            if str(current_node.id) == key:
                found = True
                break
            prev_node = current_node
            current_node = current_node.next

        # If the book is found, delete its information from the linked list
        if found:
            if prev_node is None:  # If the book to be deleted is the head node
                self.head = current_node.next
            else:
                prev_node.next = current_node.next
            print("Book issued successfully.")
        else:
            print("Book not found or already issued.")


# the main function for user interactions

def mainChoice():
    id = 0
    book = Library()

    while True:
        print("\n1. Register / Search\n2. Issue\n3. Show All Books\n4. Exit the Library\n")
        choice = input("\nChoose an Option: ")

        if choice.isdigit():
            choice = int(choice)
            
# operations for register and search of books

            if choice == 1:
                print("1. Register\n2. Search\n3. Go back\n")
                new_choice = input("Choose an Option: ")

                if new_choice.isdigit():
                    new_choice = int(new_choice)
                    
                # registration of books
                
                    if new_choice == 1:
                        book_name = input("Book's Name: ").strip().title()
                        book_author = input("Author's Name: ").strip().title()
                        id += 1
                        if book.registerBook(id, book_name, book_author):
                            print("Book registered successfully.")
                            
                # searching of books
                
                    elif new_choice == 2:
                        search = input("Enter book name/author name: ").strip().title()
                        book.searchBook(search)
                        
                    elif new_choice == 3:
                        continue
                    else:
                        print("Invalid choice")
                else:
                    print("Please enter a digit")
                    continue
                
# operations for issue and return books

            elif choice == 2:
                key = input("Enter the book key: ")
                book.issue(key)
                
# opeartions for showing all existing books

            elif choice == 3:
                book.showBooks()
                
# operations for exiting the program

            elif choice == 4:
                confirm_exit = input("Are you sure you want to exit the library? (yes/no): ").strip().lower()
                if confirm_exit == "yes":
                    break
                elif confirm_exit != "no":
                    print("Invalid choice. Please enter 'yes' or 'no'.")
            else:
                print("Invalid choice")
        else:
            print("Please enter a digit")
            continue

# calling the mainchoice function

if __name__ == "__main__":
    mainChoice()
