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

## 🖥️ Main Screens
<table>
  <tr>
    <td>Home Screen</td>
    <td>Deposit Screen</td>
   <td>Withdraw Screen</td>
   <td>Statement Screen</td>
   <td>Exit Screen</td>
  <tr>
    <td>
      <a href="https://github.com/user-attachments/assets/4b75e885-c0c7-42dc-88e6-6de3a72321a0" target="_blank">
        <img src="https://github.com/user-attachments/assets/da71b141-233f-4d29-83a5-5bb4c04cbe34" alt="Imagem 1" width="200"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/user-attachments/assets/875b9865-0f42-4716-885c-7bda358a4f0c" target="_blank">
        <img src="https://github.com/user-attachments/assets/875b9865-0f42-4716-885c-7bda358a4f0c" alt="Imagem 2" width="200"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/user-attachments/assets/5648dc61-0dc4-4a91-9d3b-9393a7075718" target="_blank">
        <img src="https://github.com/user-attachments/assets/5648dc61-0dc4-4a91-9d3b-9393a7075718" alt="Imagem 3" width="200"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/user-attachments/assets/7c6fe50c-3175-4dd1-8153-5feb285d4dbb" target="_blank">
        <img src="https://github.com/user-attachments/assets/7c6fe50c-3175-4dd1-8153-5feb285d4dbb" alt="Imagem 4" width="200"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/user-attachments/assets/26ff5932-375a-48e9-8322-badffae32dd6" target="_blank">
        <img src="https://github.com/user-attachments/assets/26ff5932-375a-48e9-8322-badffae32dd6" alt="Imagem 5" width="200"/>
      </a>
    </td>
  </tr>
</table>

## 🖥️⚠️ User Warning Screens
<table>
  <tr>
    <td>Wrong Key</td>
    <td>Invalid Deposit</td>
   <td>Withdrawal Limit (Maximum rounds)</td>
   <td>Withdrawal Limit (Value per Rounds)</td>
   <td>Insufficient balance</td>
   <td>Invalid Withdrawal</td>
   <td>No Transactions</td>
  <tr>
    <td>
      <a href="https://github.com/user-attachments/assets/2ec588d0-1516-416b-84b9-4f67c8311400" target="_blank">
        <img src="https://github.com/user-attachments/assets/2ec588d0-1516-416b-84b9-4f67c8311400" alt="Imagem 1" width="200"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/user-attachments/assets/f35920f3-bf9a-4fd0-9804-8ea2faf2f698" target="_blank">
        <img src="https://github.com/user-attachments/assets/f35920f3-bf9a-4fd0-9804-8ea2faf2f698" alt="Imagem 2" width="200"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/user-attachments/assets/c7cadeb7-72b8-49ac-9782-8cd68f2fd3e6" target="_blank">
        <img src="https://github.com/user-attachments/assets/c7cadeb7-72b8-49ac-9782-8cd68f2fd3e6" alt="Imagem 3" width="200"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/user-attachments/assets/8f70b59f-2887-4265-8d69-8b36b2bdf452" target="_blank">
        <img src="https://github.com/user-attachments/assets/8f70b59f-2887-4265-8d69-8b36b2bdf452" alt="Imagem 4" width="200"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/user-attachments/assets/f5ed5437-b8d3-4bc7-ae69-3e6046608885" target="_blank">
        <img src="https://github.com/user-attachments/assets/f5ed5437-b8d3-4bc7-ae69-3e6046608885" alt="Imagem 5" width="200"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/user-attachments/assets/46b19453-15ab-435f-b69e-d75db07621ac" target="_blank">
        <img src="https://github.com/user-attachments/assets/46b19453-15ab-435f-b69e-d75db07621ac"" alt="Imagem 6" width="200"/>
      </a>
    </td>
    <td>
      <a href="https://github.com/user-attachments/assets/f8c4ae91-a562-4d16-96ae-28d95acb0905" target="_blank">
        <img src="https://github.com/user-attachments/assets/f8c4ae91-a562-4d16-96ae-28d95acb0905" alt="Imagem 7" width="200"/>
      </a>
    </td>
  </tr>
</table>

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
