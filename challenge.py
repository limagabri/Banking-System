def display_menu():
    print(f"""
=== Banking System ===
1. Deposit
2. Withdraw
3. Statement
4. Exit
    """)
    
    while True:
        option = input("Choose an option: ")
        if option.isdigit() and 1 <= int(option) <= 4:
            return int(option)
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

def deposit(balance, statement):
    try:
        amount = float(input("Enter the deposit amount: R$ "))
        if amount > 0:
            balance += amount
            statement.append(f"Deposit: R$ {amount:.2f}")
            print(f"Deposit of R$ {amount:.2f} was successful!")
        else:
            print("Invalid deposit amount.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance

def withdraw(balance, statement, daily_withdrawals, daily_withdrawal_limit, max_withdrawals):
    if daily_withdrawals >= max_withdrawals:
        print(f"Daily withdrawal limit reached. You can make a maximum of {max_withdrawals} withdrawals per day.")
        return balance, daily_withdrawals
    
    try:
        amount = float(input("Enter the withdrawal amount: R$ "))
        if amount > balance:
            print("Insufficient balance for the withdrawal.")
        elif amount > daily_withdrawal_limit:
            print(f"Amount exceeds the maximum limit of R$ {daily_withdrawal_limit:.2f} per withdrawal.")
        elif amount > 0:
            balance -= amount
            statement.append(f"Withdrawal: R$ {amount:.2f}")
            daily_withdrawals += 1
            print(f"Withdrawal of R$ {amount:.2f} was successful!")
        else:
            print("Invalid withdrawal amount.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance, daily_withdrawals

def display_statement(statement, balance):
    print("\n=== Statement ===")
    if statement:
        for item in statement:
            print(item)
    else:
        print("No transactions were made.")
    print(f"Current balance: R$ {balance:.2f}")

def main():
    balance = 0
    statement = []
    daily_withdrawals = 0
    daily_withdrawal_limit = 500
    max_withdrawals = 3
    
    while True:
        option = display_menu()
        
        if option == 1:
            balance = deposit(balance, statement)
        
        elif option == 2:
            balance, daily_withdrawals = withdraw(balance, statement, daily_withdrawals, daily_withdrawal_limit, max_withdrawals)
        
        elif option == 3:
            display_statement(statement, balance)
        
        elif option == 4:
            print("Exiting the system. Thank you for using our bank!")
            break
        
        input("Press Enter to return to the menu.")

if __name__ == "__main__":
    main()
