# 🏦 Banking System

This project was developed as part of the NTT DATA Bootcamp - Data Engineering with Python challenge on [Digital Innovation One (DIO)](https://www.dio.me/). The goal is to implement a simple banking system with deposit, withdrawal, statement, user, and account management functionalities.

## ⚙️ Features

The banking system includes the following features:
1. **Deposit**: Allows the user to deposit positive amounts into their bank account. Deposits are handled by positional arguments.
2. **Withdraw**: Allows up to 3 withdrawals per day, with a maximum limit of R$ 500.00 per withdrawal. Withdrawals are handled by named arguments.
3. **Statement**: Displays all deposits and withdrawals made, as well as the current account balance. It can receive both positional and named arguments.
4. **Create User**: Users can be created by providing their name, date of birth, CPF (validated as a unique and 11-digit number), and address.
5. **Create Account**: Each user can have one or more accounts. Accounts are stored with a unique sequential number, tied to a user.
6. **List Accounts**: Displays all the accounts created, showing the account number, agency, and associated user.
7. **List Clients**: Lists all registered clients, displaying their name, CPF, and address.
8. **Exit**: Closes the system.

## 🔒 System Rules

- **Deposits**: 
  - Must be positive amounts.
  - All deposits are recorded in the statement.
  - Handled by positional arguments.
- **Withdrawals**:
  - Limit of 3 withdrawals per day.
  - Maximum limit of R$ 500.00 per withdrawal.
  - Check available balance before making a withdrawal.
  - Handled by named arguments.
- **Statement**: 
  - Lists all transactions (deposits and withdrawals).
  - If no transactions were made, it informs the user.
  - Can be accessed with both positional and named arguments.
- **Users**:
  - Users are registered with a unique CPF, which is validated to ensure it consists of 11 numeric digits.
  - No duplicate CPFs are allowed in the system.
- **Accounts**:
  - Each user can have multiple accounts.
  - Accounts are tied to a unique sequential number starting from 1 and linked to an agency (fixed as 0001).
  - Only users with valid CPFs can create accounts.
=======
- **Statement**: Lists all transactions (deposits and withdrawals). If there are no transactions, it informs that no transactions were made.

## 🛠️ Technologies Used

- **Language**: Python 3

## 📋 Prerequisites

- Python 3 installed on your machine.

## 🚀 How to Run

To run the banking system, follow these steps:
1. Make sure you have Python installed on your machine.
2. Clone this repository.
```bash
git clone https://github.com/your-username/banking-system.git
```
3. Navigate to the project directory.
```bash
cd Banking-Challenge
```
4. Run the script:
```bash
python challenge.py
```

## 🔗 Links

* [Digital Innovation One (DIO)](https://www.dio.me/)
* [Bootcamp NTT DATA - Engenharia de Dados com Python](https://www.dio.me/bootcamp/engenharia-dados-python)

## 🤝 Contribution

Contributions, issues, and pull requests are welcome! Feel free to check the issues page if you have any questions or suggestions.
## 📄 License

This project is free for educational purposes.
This project is licensed under the MIT License.
See the LICENSE file for more details.
