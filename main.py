import json

expenses_list = []
total_expense = 0

def main():
    print(" Welcome to Jolly's Personal Finance Tracker")
    loadExpenses()
    
    while True:
        print("Available Commands:")
        print("[1] Add expense")
        print("[2] View all expenses")
        print("[3] Delete Expenses")
        print("[4] Edit Expenses")
        print("[5] Filter by category")
        print("[6] Filter by date")
        print("[7] Exit")
        
        user_input = int(input("Enter a command number: "))
        
        if user_input == 1:
            print("Adding an expense...")
            addExpense()
            saveExpenses()
        elif user_input == 2:
            print("Viewing all expenses...")
            viewExpenses()
        elif user_input == 3:
            print("Deleting an expense...")
            deleteExpenses()
            saveExpenses()
        elif user_input == 4:
            print("Editing an expense...")
            editExpenses()
            saveExpenses()
        elif user_input == 5:
            print("Filtering by category...")
            filterByCategory()
        elif user_input == 6:
            print("Filtering by date...")
            filterbyDate()
        elif user_input == 7:
            saveExpenses()
            print("Exiting the program...")
            break
        else:
            print("Invalid command. Please try again.")

def addExpense():
    expense_amount = float(input("Enter amount: "))
    category = input("Enter category: (e.g., Food, Transport, Other): ")
    date = input("(YYYY-MM-DD) [or press Enter for today]: ")
    description = input("Enter a short description: ")
    
    expense = {"amount":  expense_amount, "category": category, "date": date, "description": description}
    expenses_list.append(expense)
    
    print("Expense added successfully!")

def viewExpenses():
    global total_expense
    print(f"{'Date':<12} | {'Amount':>10} | {'Category':<12} | {'Description':<30}")
    print("-" * 70)
    total_expense = 0  # Reset total_expense to avoid accumulation across calls

    for expense in expenses_list:
        amount = expense["amount"]
        category = expense["category"]
        date = expense["date"]
        description = expense["description"]
        
        current_expenses = f"{date:<12} | {amount:>10.2f} | {category:<12} | {description:<30}"
        total_expense += amount
        print(current_expenses)
        
    print(f"{'Total Amount:':<12} | {total_expense:>10.2f}")
    
def deleteExpenses():
    global total_expense
    print(f"{'Date':<12} | {'Amount':>10} | {'Category':<12} | {'Description':<30}")
    print("-" * 70)
    total_expense = 0  # Reset total_expense to avoid accumulation across calls
    index = 0

    for expense in expenses_list:
        amount = expense["amount"]
        category = expense["category"]
        date = expense["date"]
        description = expense["description"]
        index += 1
        
        current_expenses = f"[{index}] | {date:<12} | {amount:>10.2f} | {category:<12} | {description:<30}"
        total_expense += amount
        print(current_expenses)
    
    while True:
        selected_expense = input("Enter the index number of the expense to delete (or 'c' to cancel): ")
        
        if selected_expense.lower() == 'c':
            print("Deletion canceled.")
            return
        elif selected_expense.isdigit():
            selected_index = int(selected_expense) - 1
            if 0 <= selected_index < len(expenses_list):
                deleted_expense = expenses_list.pop(selected_index)
                print(f"Deleted expense: {deleted_expense}")
                break
            else:
                print("Invalid index. Please try again.")
        else:
            print("Invalid input. Please enter a valid index or 'c' to cancel.")
    
def editExpenses():
    global total_expense
    print(f"{'Date':<12} | {'Amount':>10} | {'Category':<12} | {'Description':<30}")
    print("-" * 70)
    total_expense = 0  # Reset total_expense to avoid accumulation across calls
    index = 0

    for expense in expenses_list:
        amount = expense["amount"]
        category = expense["category"]
        date = expense["date"]
        description = expense["description"]
        index += 1
        
        current_expenses = f"[{index}] | {date:<12} | {amount:>10.2f} | {category:<12} | {description:<30}"
        total_expense += amount
        print(current_expenses)
    
    selected_expense = input("Enter the index number of the expense to delete (or 'c' to cancel): ")

    if selected_expense.lower() == 'c':
        print("Editing canceled.")
        return
    elif selected_expense.isdigit():
        selected_index = int(selected_expense) - 1
        if 0 <= selected_index < len(expenses_list):
            expense_to_edit = expenses_list[selected_index]
            print(f"Selected expense: {expense_to_edit}")
            
            while True:
                print("Which field would you like to edit?")
                print("[1] Amount")
                print("[2] Category")
                print("[3] Date")
                print("[4] Description")
                print("[c] Cancel")
                
                field_choice = input("Enter the number of the field to edit (or 'c' to cancel): ")
                
                if field_choice.lower() == 'c':
                    print("Editing canceled.")
                    return
                elif field_choice == '1':
                    new_amount = input("Enter the new amount: ")
                    try:
                        expense_to_edit["amount"] = float(new_amount)
                        print("Amount updated successfully.")
                    except ValueError:
                        print("Invalid amount. Please enter a valid number.")
                elif field_choice == '2':
                    new_category = input("Enter the new category: ")
                    expense_to_edit["category"] = new_category
                    print("Category updated successfully.")
                elif field_choice == '3':
                    new_date = input("Enter the new date (YYYY-MM-DD): ")
                    expense_to_edit["date"] = new_date
                    print("Date updated successfully.")
                elif field_choice == '4':
                    new_description = input("Enter the new description: ")
                    expense_to_edit["description"] = new_description
                    print("Description updated successfully.")
                else:
                    print("Invalid choice. Please try again.")
                
                saveExpenses()
                print("Changes saved.")
                break
        else:
            print("Invalid index. No expense edited.")
    else:
        print("Invalid input. No expense edited.")

def filterByCategory():
    global total_expense
    filter_category = input("Choose a category to filter by: ")
    print(f"{'Date':<12} | {'Amount':>10} | {'Category':<12} | {'Description':<30}")
    print("-" * 70)
    total_expense = 0 
    
    for expense in expenses_list:
        amount = expense["amount"]
        category = expense["category"]
        date = expense["date"]
        description = expense["description"]
        
        if category == filter_category:
            current_expenses = f"{date:<12} | {amount:>10.2f} | {category:<12} | {description:<30}"
            total_expense += amount
            print(current_expenses)
        
    print(f"{'Total Amount:':<12} | {total_expense:>10.2f}")

def filterbyDate():
    global total_expense
    filter_date = input("Choose a category to filter by: ")
    print(f"{'Date':<12} | {'Amount':>10} | {'Category':<12} | {'Description':<30}")
    print("-" * 70)
    total_expense = 0
    
    for expense in expenses_list:
        amount = expense["amount"]
        category = expense["category"]
        date = expense["date"]
        description = expense["description"]
        
        if date == filter_date:
            current_expenses = f"{date:<12} | {amount:>10.2f} | {category:<12} | {description:<30}"
            total_expense += amount
            print(current_expenses)
        
    print(f"{'Total Amount:':<12} | {total_expense:>10.2f}")


def saveExpenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses_list, file)

def loadExpenses():
    global expenses_list
    try:
        with open("expenses.json", "r") as file:
            expenses_list = json.load(file)
    except FileNotFoundError:
        expenses_list = []
    
if __name__ == "__main__":
    main()