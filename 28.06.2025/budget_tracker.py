balance = 0
while True:
    action = input("Add income, expense, view, or exit: ").lower()
    if action == 'income':
        balance += float(input("Enter amount: "))
    elif action == 'expense':
        balance -= float(input("Enter amount: "))
    elif action == 'view':
        print(f"Current balance: ${balance:.2f}")
    elif action == 'exit':
        break