import os

FILE_NAME = "books.txt"

# --- Node for the Linked List ---
class BookNode:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.next = None
        self.prev = None

# --- Linked List for Inventory ---
class BookLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_book(self, title, author, is_borrowed=False):
        new_node = BookNode(title, author, is_borrowed)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def get_all_books(self):
        books = []
        current = self.head
        while current:
            books.append(current)
            current = current.next
        return books

# --- Main Application ---
class ELibraryApp:
    def __init__(self):
        self.library = BookLinkedList()
        self.undo_stack = []
        self.load_books()

    def load_books(self):
        if not os.path.exists(FILE_NAME):
            print("No existing book file found. Starting with an empty inventory.")
            return

        with open(FILE_NAME, "r") as file:
            for line in file:
                try:
                    title, author, is_borrowed_str = line.strip().split(",", 2)
                    is_borrowed = is_borrowed_str == "1"
                    self.library.add_book(title, author, is_borrowed)
                except ValueError:
                    continue # Skip malformed lines

    def save_books(self):
        with open(FILE_NAME, "w") as file:
            current = self.library.head
            while current:
                is_borrowed_str = "1" if current.is_borrowed else "0"
                file.write(f"{current.title},{current.author},{is_borrowed_str}\n")
                current = current.next
    
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        self.library.add_book(title, author)
        print(f"Book '{title}' added successfully.")

    def view_books(self):
        books = self.library.get_all_books()
        if not books:
            print("The library is empty.")
            return

        print("\n--- Current Book Inventory ---")
        for i, book in enumerate(books, 1):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{i}. {book.title} by {book.author} [{status}]")

    def find_book_by_number(self, num):
        current = self.library.head
        count = 1
        while current and count < num:
            current = current.next
            count += 1
        return current

    def borrow_book(self):
        self.view_books()
        try:
            choice = int(input("Enter the number of the book to borrow: "))
            book_to_borrow = self.find_book_by_number(choice)

            if not book_to_borrow:
                print("Invalid book number.")
            elif book_to_borrow.is_borrowed:
                print("Sorry, that book is already borrowed.")
            else:
                book_to_borrow.is_borrowed = True
                self.undo_stack.append({'book': book_to_borrow, 'action': 'borrow'})
                print(f"'{book_to_borrow.title}' has been borrowed.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def return_book(self):
        self.view_books()
        try:
            choice = int(input("Enter the number of the book to return: "))
            book_to_return = self.find_book_by_number(choice)

            if not book_to_return:
                print("Invalid book number.")
            elif not book_to_return.is_borrowed:
                print("That book is not currently borrowed.")
            else:
                book_to_return.is_borrowed = False
                self.undo_stack.append({'book': book_to_return, 'action': 'return'})
                print(f"'{book_to_return.title}' has been returned.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def search_books(self):
        query = input("Enter title or author to search for: ").lower()
        found_books = []
        current = self.library.head
        while current:
            if query in current.title.lower() or query in current.author.lower():
                found_books.append(current)
            current = current.next

        if not found_books:
            print("No books found matching your query.")
        else:
            print("\n--- Search Results ---")
            for book in found_books:
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"{book.title} by {book.author} [{status}]")

    def undo_action(self):
        if not self.undo_stack:
            print("No actions to undo.")
            return

        last_action = self.undo_stack.pop()
        book = last_action['book']
        action_type = last_action['action']

        if action_type == 'borrow':
            book.is_borrowed = False
            print(f"Undid the last borrow action for '{book.title}'. It is now available.")
        elif action_type == 'return':
            book.is_borrowed = True
            print(f"Undid the last return action for '{book.title}'. It is now borrowed.")
    
    def run(self):
        while True:
            print("\n--- E-Library Book Management ---")
            print("1. Add a new book")
            print("2. View all books")
            print("3. Borrow a book")
            print("4. Return a book")
            print("5. Search/Filter books")
            print("6. Undo last action")
            print("7. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.view_books()
            elif choice == '3':
                self.borrow_book()
            elif choice == '4':
                self.return_book()
            elif choice == '5':
                self.search_books()
            elif choice == '6':
                self.undo_action()
            elif choice == '7':
                self.save_books()
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ELibraryApp()
    app.run()
