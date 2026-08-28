from expense import Expense
import storage



def main():
    expense_file_path = "expense.csv"
    while True:
        match(get_choice()):
            case 1:
                expense = add_expense(expense_file_path)
                storage.save_expense(expense, expense_file_path)
            
            case 2:
                view_expense(expense_file_path)
            
            case 3:
                delete_expense(expense_file_path)
            
            case 4:
                edit_expense(expense_file_path)
                
            case 5:
                return


def get_choice():
    while True:
        try:
            choice = int(input("""
=====EXPENSE TRACKER=====
1 -> Add expense
2 -> View all expenses
3 -> Delete an expense
4 -> Edit an expense
5 -> Exit
Enter choice = """))
        
        except ValueError:
            print("Please enter a number.\n")
        else:
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice.\nPlease enter from the given choices\n")


def add_expense(file_path):
    add_name = input("Enter the expense name = ")
    while True:
        try:
            add_amount = float(input("Enter the expense amount = "))
            if add_amount > 0:
                break
            else:
                print("Please enter a valid amount.")
        except ValueError:
            print("Please enter a valid amount.")
    
    expense_categories = ["Food", "Home", "Work", "Fun", "Misc"]
    
    csv_file = storage.load_expenses(file_path)
        
    new_list = []
    for i in csv_file:
        new_list.append(int(i["ID"]))
            
    if new_list == []:
        new_list.append(0)
            
    maximum = max(new_list)
    
    while True:
        print("\nSelect a category :")
        for line, category_name in enumerate(expense_categories):
            print(f"{line+1} - {category_name}")

        try:
            add_category = int(input(f"Enter the expense category [{f"1 - {len(expense_categories)}"}] : ")) - 1
        except ValueError:
            print("Please enter a number to choose category.")
        else:
            if add_category in range(len(expense_categories)):
                selected_category = expense_categories[add_category]
                new_expense = Expense(id=maximum+1, name=add_name, category=selected_category, amount=add_amount)
                
                return new_expense
            
            else:
                print("Invalid category! Please try again.")


def view_expense(file_path):
    print("\n=> Your Expenses :")
        
    print("-" * 50)
    
    total_spent = 0
    
    lines = storage.load_expenses(file_path)
        
    for line in lines:
        print(f"{line["ID"]} | {line["Name"]} | {line["Category"]} | {line["Amount"]}")    
        
        total_spent += float(line["Amount"])
        
    print("-" * 50)

    print(f"=> Total spent = ₹{total_spent}")


def delete_expense(file_path):
    new_rows = storage.load_expenses(file_path)

    if not new_rows:
        print("There are no expenses to delete.")
        return

    print("=> Your Expenses:")

    for row in new_rows:
        print(f"{row["ID"]} | {row["Name"]} | {row["Category"]} | {row["Amount"]}")

    try:
        delete_choice = int(input("Choose expense ID to delete: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    if not any(int(row["ID"]) == delete_choice for row in new_rows):
        print("Expense ID does not exist.")
        return

    remaining_rows = []

    for row in new_rows:
        if int(row["ID"]) != delete_choice:
            remaining_rows.append(row)

    storage.write_expense(file_path, remaining_rows)

    print("Expense deleted successfully.")


def edit_expense(file_path):
    new_rows = storage.load_expenses(file_path)

    if not new_rows:
        print("There are no expenses to edit.")
        return

    print("\n=> Your Expenses:")

    for row in new_rows:
        print(f"{row["ID"]} | {row["Name"]} | {row["Category"]} | {row["Amount"]}")

    try:
        editing_choice = int(input("Choose expense ID to edit: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    if not any(int(row["ID"]) == editing_choice for row in new_rows):
        print("Expense ID does not exist.")
        return

    new_name = input("Enter the new expense name: ")

    while True:
        try:
            new_amount = float(input("Enter the new expense amount: "))
            if new_amount > 0:
                break
            print("Please enter a valid amount.")
        except ValueError:
            print("Please enter a valid amount.")

    expense_categories = ["Food", "Home", "Work", "Fun", "Misc"]

    while True:
        print("\nSelect a category:")

        for number, category_name in enumerate(expense_categories,start=1):
            print(f"{number} - {category_name}")

        try:
            category_choice = int(input("Enter category: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 1 <= category_choice <= len(expense_categories):
            new_selected_category = expense_categories[category_choice - 1]
            break

        print("Invalid category! Please try again.")

    remaining_rows = []

    for row in new_rows:
        if int(row["ID"]) != editing_choice:
            remaining_rows.append(row)
        else:
            updated_row = {
                "ID": row["ID"],
                "Name": new_name,
                "Category": new_selected_category,
                "Amount": new_amount
            }

            remaining_rows.append(updated_row)

    storage.write_expense(file_path, remaining_rows)

    print("Expense edited successfully.")


if __name__ == '__main__':
    main()
