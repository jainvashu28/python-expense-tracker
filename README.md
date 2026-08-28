# Python Expense Tracker

A command-line expense tracker built with Python. The application allows users to add, view, edit, and delete expenses, with data stored persistently in a CSV file.

## Features

* Add expenses
* View all expenses
* Edit expenses by ID
* Delete expenses by ID
* Categorize expenses
* Calculate total spending
* Store expenses in a CSV file
* Input validation
* Automatic expense IDs

## Project Structure

```text
python-expense-tracker/
│
├── main.py          # Application flow and user interaction
├── expense.py       # Expense class
├── storage.py       # CSV reading and writing
├── expense.csv      # Expense data
└── README.md        # Project documentation
```

## Technologies Used

* Python
* CSV module
* Object-Oriented Programming
* File Handling
* Python Modules

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/jainvashu28/python-expense-tracker.git
```

2. Navigate into the project:

```bash
cd python-expense-tracker
```

3. Run the application:

```bash
python main.py
```

## Example

```text
===== Expense Tracker =====

1. Add expense
2. View expenses
3. Delete expense
4. Edit expense
5. Exit
```

Expenses are stored in `expense.csv` so they remain available after the program closes.

## What I Learned

This project helped me practice:

* Python functions
* Classes and objects
* File handling
* CSV data handling
* Exception handling
* Input validation
* Modules and imports
* CRUD operations
* Working with IDs
* Separating application logic from storage logic

## Future Improvements

* Add expense dates
* Add monthly spending summaries
* Add search and filtering
* Replace CSV storage with SQLite
* Build a REST API using FastAPI

## Author

Vashu Jain
