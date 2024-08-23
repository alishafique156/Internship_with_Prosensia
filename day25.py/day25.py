Here's the Python code for a simple Expense Tracker:

```python
def add_expense(expenses):
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    if amount <= 0:
        print("Amount must be positive.")
        return

    expenses.append({'description': description, 'amount': amount, 'category': category})
    print(f"Expense '{description}' added successfully.")

def display_summary(expenses):
    summary = {}
    
    for expense in expenses:
        category = expense['category']
        if category in summary:
            summary[category] += expense['amount']
        else:
            summary[category] = expense['amount']
    
    if not summary:
        print("No expenses to display.")
        return

    print("Expense Summary:")
    for category, total in summary.items():
        print(f"Category: {category}, Total: {total}")

def main():
    expenses = []
    
    while True:
        print("\n1. Add Expense")
        print("2. View Expense Summary")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_summary(expenses)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
```