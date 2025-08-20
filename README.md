⚙️ Core Concepts & Features
Book Inventory: The library's collection is stored and managed using a Python list or a dictionary, offering efficient addition and removal of books.

Borrow/Return Functionality: Users can borrow or return books, which updates the book's availability status.

Undo/Redo Actions: A Python list is used to simulate a stack to store recent borrow/return actions. You can undo the last action, which reverts the book's status and updates the inventory.

Search & Filter: Easily find books by title or author. The search functionality is not case-sensitive.

Data Persistence: The book inventory is saved to and loaded from a file (e.g., books.json or books.txt), so your data is preserved between sessions.

🚀 How to Run
Prerequisites: Ensure you have Python installed on your system.

Execution:

Save the Python code in a file (e.g., e_library.py).

Open your terminal or command prompt.

Run the script with the following command:

Bash

python e_library.py
Follow the on-screen menu to interact with the library system.

📋 Sample Output
When you run the application for the first time, it will start with an empty list.

Welcome to the E-Library!

--- Main Menu ---
1. Add a book
2. View all books
3. Borrow a book
4. Return a book
5. Undo last action
6. Search for a book
7. Exit
Enter your choice: 1
Enter book title: The Hitchhiker's Guide to the Galaxy
Enter author name: Douglas Adams
Book "The Hitchhiker's Guide to the Galaxy" added successfully.

--- Main Menu ---
1. Add a book
2. View all books
3. Borrow a book
4. Return a book
5. Undo last action
6. Search for a book
7. Exit
Enter your choice: 2

--- All Books ---
Title: The Hitchhiker's Guide to the Galaxy, Author: Douglas Adams, Status: Available

--- Main Menu ---
1. Add a book
2. View all books
3. Borrow a book
4. Return a book
5. Undo last action
6. Search for a book
7. Exit
Enter your choice: 3
Enter the title of the book to borrow: The Hitchhiker's Guide to the Galaxy
Book "The Hitchhiker's Guide to the Galaxy" borrowed successfully.

--- Main Menu ---
1. Add a book
2. View all books
3. Borrow a book
4. Return a book
5. Undo last action
6. Search for a book
7. Exit
Enter your choice: 2

--- All Books ---
Title: The Hitchhiker's Guide to the Galaxy, Author: Douglas Adams, Status: Borrowed

--- Main Menu ---
1. Add a book
2. View all books
3. Borrow a book
4. Return a book
5. Undo last action
6. Search for a book
7. Exit
Enter your choice: 5
Undoing last action...
Action undone. The book "The Hitchhiker's Guide to the Galaxy" is now Available.

--- Main Menu ---
1. Add a book
2. View all books
3. Borrow a book
4. Return a book
5. Undo last action
6. Search for a book
7. Exit
Enter your choice: 7
Goodbye! Your book inventory has been saved.
