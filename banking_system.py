import random
from datetime import datetime

accounts = {}
def create_account():
    print("\n--- CREATE ACCOUNT ---")

    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    pin = input("Create a 4-digit PIN: ")

    account_number = random.randint(10000, 99999)

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("Your Account Number:", account_number)

def login():
    print("\n--- LOGIN ---")

    account_number = int(input("Enter your account number: "))
    pin = input("Enter your PIN: ")

    if account_number in accounts:
        if accounts[account_number]["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome,", accounts[account_number]["name"])
            return account_number
        else:
            print("Incorrect PIN.")
    else:
        print("Account not found.")

    return None

def check_balance(account_number):
    balance = accounts[account_number]["balance"]
    print("\n--- ACCOUNT BALANCE ---")
    print("Current Balance: ₹", balance)
def deposit(account_number):
    amount = float(input("Enter amount to deposit: ₹ "))

    if amount > 0:
        accounts[account_number]["balance"] += amount
        accounts[account_number]["transactions"].append(
    f"Deposited ₹{amount} on {datetime.now().strftime('%d-%m-%Y %H:%M')}"
)
        print("Deposit successful!")
        print("New Balance: ₹", accounts[account_number]["balance"])
    else:
        print("Please enter a valid amount.")
def withdraw(account_number):
    amount = float(input("Enter amount to withdraw: ₹ "))

    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
    else:
        accounts[account_number]["balance"] -= amount
        accounts[account_number]["transactions"].append(
    f"Withdrew ₹{amount} on {datetime.now().strftime('%d-%m-%Y %H:%M')}"
)
        print("Withdrawal successful!")
        print("New Balance: ₹", accounts[account_number]["balance"])
def transfer(account_number):
    receiver = int(input("Enter receiver account number: "))
    amount = float(input("Enter amount to transfer: ₹ "))

    if receiver not in accounts:
        print("Receiver account not found.")
    elif amount <= 0:
        print("Please enter a valid amount.")
    elif amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
    else:
        accounts[account_number]["balance"] -= amount
        accounts[receiver]["balance"] += amount
        accounts[account_number]["transactions"].append(
    f"Transferred ₹{amount} to Account {receiver} on {datetime.now().strftime('%d-%m-%Y %H:%M')}"
)

    accounts[receiver]["transactions"].append(
        f"Received ₹{amount} from Account {account_number} on    {datetime.now().strftime('%d-%m-%Y %H:%M')}"
    )
    print("Transfer successful!")
    print("Amount transferred: ₹", amount)
    print("New Balance: ₹", accounts[account_number]["balance"])
def transaction_history(account_number):
    print("\n--- TRANSACTION HISTORY ---")

    if len(accounts[account_number]["transactions"]) == 0:
        print("No transactions yet.")
    else:
        for transaction in accounts[account_number]["transactions"]:
            print(transaction)
def account_menu(account_number):
    while True:
        print("\n===== ACCOUNT MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account_number)
        elif choice == "2":
            deposit(account_number)
        elif choice == "3":
            withdraw(account_number)
        elif choice == "4":
            transfer(account_number)
        elif choice == "5":
            transaction_history(account_number)
        elif choice == "7":
            print("Logged out successfully.")
            break
        else:
            print("This feature will be added soon.")
def main():
    while True:
        print("\n===== SIMPLE SMART BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            account_number = login()
            if account_number is not None:
                account_menu(account_number)
        elif choice == "3":
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
   
