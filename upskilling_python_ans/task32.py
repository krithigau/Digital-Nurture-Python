def add_expense(expenses, new_expense):
    if not isinstance(expenses, list):
        return "Please provide a valid list."
    if not isinstance(new_expense, (int, float)) or new_expense < 0:
        return "Expense must be a positive number."
        
    expenses.append(new_expense)
    print(f"Updated Expenses: {expenses}")

current_expenses = [50, 120]
add_expense(current_expenses, 45.5)