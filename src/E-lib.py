# === Node for Linked List ===
class BookNode:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        self.next = None

# === Stack for Undo ===
undo_stack = []

# === Linked List Library ===
class Library:
    def __init__(self):
        self.head = None

    def add_book(self, title, author):
        node = BookNode(title, author)
        node.next = self.head
        self.head = node

    def find_book(self, title):
        curr = self.head
        while curr:
            if curr.title.lower() == title.lower():
                return curr
            curr = curr.next
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book and book.available:
            book.available = False
            undo_stack.append(("return", book))
            print(f"Borrowed: {book.title}")
        else:
            print("Book not available.")

    def return_book(self, title):
        book = self.find_book(title)
        if book and not book.available:
            book.available = True
            undo_stack.append(("borrow", book))
            print(f"Returned: {book.title}")
        else:
            print("Book not found or already available.")

    def search(self, keyword):
        curr = self.head
        found = False
        while curr:
            if keyword.lower() in curr.title.lower() or keyword.lower() in curr.author.lower():
                status = "Available" if curr.available else "Borrowed"
                print(f"{curr.title} by {curr.author} [{status}]")
                found = True
            curr = curr.next
        if not found:
            print("No matching books found.")

    def list_books(self):
        curr = self.head
        while curr:
            status = "Available" if curr.available else "Borrowed"
            print(f"{curr.title} by {curr.author} [{status}]")
            curr = curr.next

    def undo(self):
        if not undo_stack:
            print("Nothing to undo.")
            return
        action, book = undo_stack.pop()
        if action == "return":
            book.available = True
            print(f"Undo: Returned {book.title}")
        elif action == "borrow":
            book.available = False
            print(f"Undo: Borrowed {book.title}")

# === Menu ===
def menu():
    lib = Library()
    # Sample books
    lib.add_book("The Alchemist", "Paulo Coelho")
    lib.add_book("1984", "George Orwell")
    lib.add_book("Python Basics", "John Doe")

    while True:
        print("\n1.List 2.Search 3.Borrow 4.Return 5.Undo 6.Exit")
        choice = input("Choice: ")
        if choice == "1":
            lib.list_books()
        elif choice == "2":
            key = input("Title/Author keyword: ")
            lib.search(key)
        elif choice == "3":
            title = input("Title to borrow: ")
            lib.borrow_book(title)
        elif choice == "4":
            title = input("Title to return: ")
            lib.return_book(title)
        elif choice == "5":
            lib.undo()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
