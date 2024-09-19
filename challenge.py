import re

# List to store users and accounts
users = []
accounts = []
account_number = 1

def display_menu():
    print(f"""
=== Banking System ===
1. Deposit
2. Withdraw
3. Statement
4. Create User
5. Create Account
6. List Accounts
7. List Clients
8. Exit
    """)
    
    while True:
        option = input("Choose an option: ")
        if option.isdigit() and 1 <= int(option) <= 8:
            return int(option)
        else:
            print("Invalid option. Please choose a number between 1 and 8.")

# CPF validator function
def is_valid_cpf(cpf):
    return bool(re.match(r"^\d{11}$", cpf))

# Function to create a user
def create_user():
    global users
    name = input("Enter your name: ")
    birth_date = input("Enter your birth date (dd/mm/yyyy): ")

    # Keep asking for a valid CPF until the user inputs it correctly
    while True:
        cpf = input("Enter your CPF (numbers only): ")

        # Check if CPF is valid
        if not is_valid_cpf(cpf):
            print("Invalid CPF. Please enter a valid 11-digit CPF number.")
        else:
            # Check if user with this CPF already exists
            if any(user['cpf'] == cpf for user in users):
                print("User with this CPF already exists.")
            else:
                break  # CPF is valid and unique, we can exit the loop

    address = input("Enter your address (Format: Street, Number - Neighborhood - City/State): ")
    
    users.append({
        'name': name,
        'birth_date': birth_date,
        'cpf': cpf,
        'address': address
    })
    print(f"User {name} was successfully created!")

# Function to create an account
def create_account():
    global accounts, account_number
    cpf = input("Enter the CPF of the user to create an account: ")
    
    # Find user by CPF
    user = next((user for user in users if user['cpf'] == cpf), None)
    if user is None:
        print("No user found with this CPF.")
        return
    
    # Create account
    accounts.append({
        'agency': '0001',
        'account_number': account_number,
        'user': user,
        'balance': 0,          # Each account starts with a zero balance
        'statement': [],       # Each account has its own statement history
        'daily_withdrawals': 0  # Track daily withdrawals
    })
    print(f"Account number {account_number} created for user {user['name']}.")
    account_number += 1

# Function to list all accounts
def list_accounts():
    if not accounts:
        print("No accounts created yet.")
    else:
        for account in accounts:
            print(f"Agency: {account['agency']}, Account Number: {account['account_number']}, User: {account['user']['name']}")

# Function to list all clients
def list_clients():
    if not users:
        print("No clients registered yet.")
    else:
        for user in users:
            print(f"Name: {user['name']}, CPF: {user['cpf']}, Address: {user['address']}")

# Function to select an account by CPF and account number
def select_account():
    cpf = input("Enter the CPF to select an account: ")
    
    # Find accounts for the given CPF
    user_accounts = [acc for acc in accounts if acc['user']['cpf'] == cpf]
    
    if not user_accounts:
        print("No accounts found for this CPF.")
        return None
    
    print("Available accounts:")
    for acc in user_accounts:
        print(f"Account Number: {acc['account_number']} - Balance: R$ {acc['balance']:.2f}")
    
    acc_number = int(input("Enter the account number: "))
    
    # Find the account with the matching account number
    selected_account = next((acc for acc in user_accounts if acc['account_number'] == acc_number), None)
    
    if selected_account is None:
        print("Invalid account number.")
        return None
    
    return selected_account

# Modified deposit function to work with the selected account
def deposit(account):
    try:
        amount = float(input("Enter the deposit amount: R$ "))
        if amount > 0:
            account['balance'] += amount
            account['statement'].append(f"Deposit: R$ {amount:.2f}")
            print(f"Deposit of R$ {amount:.2f} was successful!")
        else:
            print("Invalid deposit amount.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Modified withdraw function with limit and max withdrawals per day, receiving arguments by name
def withdraw(*, account, daily_withdrawal_limit, max_withdrawals):
    if account['daily_withdrawals'] >= max_withdrawals:
        print(f"Daily withdrawal limit reached. You can make a maximum of {max_withdrawals} withdrawals per day.")
        return
    
    try:
        amount = float(input("Enter the withdrawal amount: R$ "))
        if amount > account['balance']:
            print("Insufficient balance for the withdrawal.")
        elif amount > daily_withdrawal_limit:
            print(f"Amount exceeds the maximum limit of R$ {daily_withdrawal_limit:.2f} per withdrawal.")
        elif amount > 0:
            account['balance'] -= amount
            account['statement'].append(f"Withdrawal: R$ {amount:.2f}")
            account['daily_withdrawals'] += 1
            print(f"Withdrawal of R$ {amount:.2f} was successful!")
        else:
            print("Invalid withdrawal amount.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Modified statement function to work with the selected account
def display_statement(account):
    print("\n=== Statement ===")
    if account['statement']:
        for item in account['statement']:
            print(item)
    else:
        print("No transactions were made.")
    print(f"Current balance: R$ {account['balance']:.2f}")

def main():
    daily_withdrawal_limit = 500
    max_withdrawals = 3
    
    while True:
        option = display_menu()
        
        if option == 1:  # Deposit
            selected_account = select_account()
            if selected_account:
                deposit(selected_account)
        
        elif option == 2:  # Withdraw
            selected_account = select_account()
            if selected_account:
                withdraw(account=selected_account, daily_withdrawal_limit=daily_withdrawal_limit, max_withdrawals=max_withdrawals)
        
        elif option == 3:  # Statement
            selected_account = select_account()
            if selected_account:
                display_statement(selected_account)
        
        elif option == 4:  # Create User
            create_user()
        
        elif option == 5:  # Create Account
            create_account()
        
        elif option == 6:  # List Accounts
            list_accounts()

        elif option == 7:  # List Clients
            list_clients()
        
        elif option == 8:  # Exit
            print("Exiting the system. Thank you for using our bank!")
            break
        
        input("Press Enter to return to the menu.")

if __name__ == "__main__":
    main()
