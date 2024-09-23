# 🏦 Banking System

This project was developed as part of the NTT DATA Bootcamp - Data Engineering with Python challenge on [Digital Innovation One (DIO)](https://www.dio.me/). The goal is to implement a simple banking system with deposit, withdrawal, statement, user, and account management functionalities.

## ⚙️ Features

The banking system includes the following features:
1. **Deposit**: Allows users to deposit positive amounts into their bank accounts.
2. **Withdraw**: Users can make up to 3 withdrawals per day, with a maximum limit of R$ 500.00 per withdrawal.
3. **Statement**: Displays all deposits and withdrawals made, as well as the current account balance.
4. **Create User**: Users can be created by providing their name, date of birth, CPF (validated as a unique 11-digit number), and address.
5. **Create Account**: Each user can have one or more accounts. Accounts are created with a unique sequential number tied to a user.
6. **List Accounts**: Displays all the accounts created, showing the account number, branch, and associated user.
7. **List Customers**: Lists all registered customers, displaying their name, CPF, and address.
8. **Exit**: Closes the system.

## 🔒 System Rules

- **Deposits**: 
  - Only positive amounts are allowed.
  - All deposits are recorded in the account statement.
- **Withdrawals**:
  - Limit of 3 withdrawals per day.
  - Maximum limit of R$ 500.00 per withdrawal.
  - The system checks the account balance before allowing a withdrawal.
- **Statement**: 
  - Lists all transactions (deposits and withdrawals).
  - Informs the user if no transactions were made.
- **Users**:
  - Users are registered with a unique CPF (validated to ensure it is a valid 11-digit number).
  - Duplicate CPFs are not allowed.
- **Accounts**:
  - Each user can have multiple accounts.
  - Accounts are created with a unique sequential number and tied to a fixed branch (0001).
  - Only users with a valid CPF can create accounts.

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
