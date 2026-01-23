# Personal Finance Tracker

balance = 0
transactions = []

def add_income(amount, source):
    global balance
    balance += amount
    transactions.append(("Income", source, amount))
    print("Income added successfully.\n")

def add_expense(amount, category):
    global balance
    if amount > balance:
        print("Insufficient balance.\n")
    else:
        balance -= amount
        transactions.append(("Expense", category, amount))
        print("Expense added successfully.\n")

def view_balance():
    print(f"Current Balance: ₹{balance}\n")

def view_transactions():
    if not transactions:
        print("No transactions yet.\n")
        return
    print("Transaction History:")
    for i, t in enumerate(transactions, 1):
        print(f"{i}. {t[0]} | {t[1]} | ₹{t[2]}")
    print()

while True:
    print("---- Personal Finance Tracker ----")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        source = input("Enter income source: ")
        add_income(amount, source)

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        add_expense(amount, category)

    elif choice == "3":
        view_balance()

    elif choice == "4":
        view_transactions()

    elif choice == "5":
        print("Thank you for using the Finance Tracker.")
        break

    else:
        print("Invalid choice. Please try again.\n")
