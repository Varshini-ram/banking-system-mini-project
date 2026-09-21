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
