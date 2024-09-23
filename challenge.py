import re
from datetime import datetime

class Customer:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def perform_transaction(self, account, transaction):
        transaction.record(account)

    def add_account(self, account):
        self.accounts.append(account)


class Individual(Customer):
    def __init__(self, name, birth_date, cpf, address):
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf


class Account:
    def __init__(self, number, customer):
        self._balance = 0
        self._number = number
        self._branch = "0001"
        self._customer = customer
        self._history = History()

    @classmethod
    def new_account(cls, customer, number):
        return cls(number, customer)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def branch(self):
        return self._branch

    @property
    def customer(self):
        return self._customer

    @property
    def history(self):
        return self._history

    def withdraw(self, amount):
        balance = self.balance
        exceeded_balance = amount > balance

        if exceeded_balance:
            print("\n@@@ Transaction failed! Insufficient balance. @@@")
            return False
        elif amount > 0:
            self._balance -= amount
            print("\n=== Withdrawal successful! ===")
            return True
        else:
            print("\n@@@ Transaction failed! Invalid amount. @@@")
            return False

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("\n=== Deposit successful! ===")
            return True
        else:
            print("\n@@@ Transaction failed! Invalid amount. @@@")
            return False


class CheckingAccount(Account):
    def __init__(self, number, customer, limit=500, withdrawal_limit=3):
        super().__init__(number, customer)
        self.limit = limit
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        withdrawal_count = len(
            [transaction for transaction in self.history.transactions if transaction["type"] == Withdrawal.__name__]
        )

        exceeded_limit = amount > self.limit
        exceeded_withdrawals = withdrawal_count >= self.withdrawal_limit

        if exceeded_limit:
            print("\n@@@ Transaction failed! Amount exceeds the withdrawal limit. @@@")
        elif exceeded_withdrawals:
            print("\n@@@ Transaction failed! Maximum number of withdrawals exceeded. @@@")
        else:
            return super().withdraw(amount)

        return False


class History:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "amount": transaction.amount,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transaction:
    def record(self, account):
        pass


class Withdrawal(Transaction):
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def record(self, account):
        transaction_success = account.withdraw(self.amount)
        if transaction_success:
            account.history.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def record(self, account):
        transaction_success = account.deposit(self.amount)
        if transaction_success:
            account.history.add_transaction(self)


users = []
accounts = []
account_number = 1

def display_menu():
    print(f"""
=== Banking System ===
1. Deposit
2. Withdrawal
3. Statement
4. Create User
5. Create Account
6. List Accounts
7. List Customers
8. Exit
    """)

    while True:
        option = input("Choose an option: ")
        if option.isdigit() and 1 <= int(option) <= 8:
            return int(option)
        else:
            print("Invalid option. Choose a number between 1 and 8.")

def is_valid_cpf(cpf):
    return bool(re.match(r"^\d{11}$", cpf))

def create_user():
    global users
    name = input("Enter your name: ")
    birth_date = input("Enter your birth date (dd/mm/yyyy): ")

    while True:
        cpf = input("Enter your CPF (numbers only): ")
        if not is_valid_cpf(cpf):
            print("Invalid CPF. Enter a valid 11-digit CPF.")
        elif any(user['cpf'] == cpf for user in users):
            print("User with this CPF already exists.")
        else:
            break

    address = input("Enter your address (Format: Street, Number - Neighborhood - City/State): ")
    user = Individual(name, birth_date, cpf, address)
    users.append(user)
    print(f"User {name} was created successfully!")

def create_account():
    global accounts, account_number
    cpf = input("Enter the user's CPF to create an account: ")

    user = next((user for user in users if user.cpf == cpf), None)
    if user is None:
        print("No user found with this CPF.")
        return

    account = CheckingAccount(account_number, user)
    user.add_account(account)
    accounts.append(account)
    print(f"Account number {account_number} created for user {user.name}.")
    account_number += 1

def list_accounts():
    if not accounts:
        print("No accounts created yet.")
    else:
        for account in accounts:
            print(f"Branch: {account.branch}, Account: {account.number}, User: {account.customer.name}")

def list_customers():
    if not users:
        print("No customers registered yet.")
    else:
        for user in users:
            print(f"Name: {user.name}, CPF: {user.cpf}, Address: {user.address}")

def select_account():
    cpf = input("Enter the CPF to select an account: ")

    user_accounts = [acc for acc in accounts if acc.customer.cpf == cpf]
    if not user_accounts:
        print("No account found for this CPF.")
        return None

    print("Available accounts for the provided CPF:")
    for account in user_accounts:
        print(f"Account number: {account.number}")

    while True:
        account_number = input("Enter the desired account number: ")
        selected_account = next((acc for acc in user_accounts if str(acc.number) == account_number), None)

        if selected_account:
            return selected_account
        else:
            print("Invalid account number. Try again.")

def deposit():
    account = select_account()
    if account is None:
        return

    value = float(input("Enter the deposit amount: "))
    transaction = Deposit(value)
    account.customer.perform_transaction(account, transaction)

def withdraw():
    account = select_account()
    if account is None:
        return

    value = float(input("Enter the withdrawal amount: "))
    transaction = Withdrawal(value)
    account.customer.perform_transaction(account, transaction)

def statement():
    account = select_account()
    if account is None:
        return

    print("\n=== Account Statement ===")
    for transaction in account.history.transactions:
        print(f"{transaction['type']} of R$ {transaction['amount']} on {transaction['date']}")
    print(f"\nCurrent balance: R$ {account.balance:.2f}")

while True:
    option = display_menu()

    if option == 1:
        deposit()
    elif option == 2:
        withdraw()
    elif option == 3:
        statement()
    elif option == 4:
        create_user()
    elif option == 5:
        create_account()
    elif option == 6:
        list_accounts()
    elif option == 7:
        list_customers()
    elif option == 8:
        break
