# 🏦 Banking System

This project was developed as part of the NTT DATA Bootcamp - Data Engineering with Python challenge on [Digital Innovation One (DIO)](https://www.dio.me/). The goal is to implement a simple banking system with deposit, withdrawal, and statement functionalities.

## ⚙️ Features

The banking system includes the following features:
1. **Deposit**: Allows the user to deposit positive amounts into the bank account.
2. **Withdraw**: Allows up to 3 withdrawals per day, with a maximum limit of R$ 500.00 per withdrawal.
3. **Statement**: Displays all deposits and withdrawals made, as well as the current account balance.
4. **Exit**: Closes the system.

## 🔒 System Rules

- **Deposits**: Must be positive amounts. All deposits are recorded in the statement.
- **Withdrawals**:
  - Limit of 3 withdrawals per day.
  - Maximum limit of R$ 500.00 per withdrawal.
  - Check available balance before making a withdrawal.
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
