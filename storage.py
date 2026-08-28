from expense import Expense
import csv



def save_expense(expense: Expense, file_path):
    with open(file_path, "a", newline="") as f:
        expense_writer = csv.writer(f)
        expense_writer.writerow([expense.id,expense.name,expense.category,expense.amount])
        print("Successfully added expense.")
        

def load_expense(file_path):
    with open(file_path, "r", newline="") as f:
        return list(csv.DictReader(f))


def write_expense(file_path, rows):
    fieldnames = ["ID", "Name", "Category", "Amount"]
    
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)
