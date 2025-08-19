📚 E-Library Book Management (C++)
This is a console-based E-Library Book Management system built in C++. It simulates a simple library, allowing you to manage a collection of books. The key feature is the "undo" functionality for borrow and return actions, implemented using a stack.

⚙️ Core Concepts & Features
Book Inventory: The library's collection is stored and managed using a doubly linked list. This allows for efficient addition and removal of books.

Borrow/Return Functionality: Users can borrow or return books, which updates the book's availability status.

Undo/Redo Actions: A stack is used to store recent borrow/return actions. You can undo the last action, which reverts the book's status and updates the inventory.

Search & Filter: Easily find books by title or author. The search functionality is not case-sensitive.

Data Persistence: The book inventory is saved to and loaded from a file (books.txt), so your data is preserved between sessions.

🚀 How to Run
Prerequisites: Ensure you have a C++ compiler (like g++).

Compilation:

Navigate to the src directory in your terminal.

Compile the source code:

Bash

g++ main.cpp -o e-library
Execution:

Run the compiled executable:

Bash

./e-library
Follow the on-screen menu to interact with the library system.

📋 Sample Output
When you run the application for the first time, it will start with an empty list.

Welcome to your To-Do List Manager!

--- Main Menu ---
1. View all tasks
2. Add a new task
3. Mark a task as complete
4. Delete a task
5. Exit
Enter your choice: 2
Enter the new task description: Go for a run at the park
Task successfully added.

--- Main Menu ---
1. View all tasks
2. Add a new task
3. Mark a task as complete
4. Delete a task
5. Exit
Enter your choice: 2
Enter the new task description: Prepare for the meeting tomorrow
Task successfully added.

--- Main Menu ---
1. View all tasks
2. Add a new task
3. Mark a task as complete
4. Delete a task
5. Exit
Enter your choice: 1

--- Your Tasks ---
1. [ ] Go for a run at the park
2. [ ] Prepare for the meeting tomorrow

--- Main Menu ---
1. View all tasks
2. Add a new task
3. Mark a task as complete
4. Delete a task
5. Exit
Enter your choice: 3
Enter the number of the task to mark as complete: 1
Task #1 marked as complete.

--- Main Menu ---
1. View all tasks
2. Add a new task
3. Mark a task as complete
4. Delete a task
5. Exit
Enter your choice: 1

--- Your Tasks ---
1. [x] Go for a run at the park
2. [ ] Prepare for the meeting tomorrow

--- Main Menu ---
1. View all tasks
2. Add a new task
3. Mark a task as complete
4. Delete a task
5. Exit
Enter your choice: 5
Goodbye! Your tasks have been saved.
