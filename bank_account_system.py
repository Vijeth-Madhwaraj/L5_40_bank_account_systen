"""Bank account management module."""

import hashlib
import os
import random


account_data = {}


def create_account(acc_id, name, initial_deposit=0, transactions=None):
    """Create a new bank account."""
    if transactions is None:
        transactions = []
    if acc_id in account_data:
        return False
    account_data[acc_id] = {"name": name, "balance": initial_deposit}
    transactions.append(f"Created {acc_id} with balance {initial_deposit}")
    return True


def deposit(acc_id, amount):
    """Deposit money into the specified bank account."""
    try:
        account_data[acc_id]["balance"] += amount
    except KeyError:
        print("Error: Account does not exist.")
    except TypeError:
        print("Error: Invalid deposit amount.")


def withdraw(acc_id, amount):
    """Withdraw money from the specified bank account."""
    if account_data.get(acc_id) is None:
        return False
    if account_data[acc_id]["balance"] < amount:
        return False
    else:
        account_data[acc_id]["balance"] -= amount
        return True


def compute_bonus(acc_id):
    """Compute a bonus equal to 5% of the account balance."""
    bal = account_data[acc_id]["balance"]
    bonus = bal * 0.05
    return bonus

def get_hash(pin):
    """Generate a hash of the given PIN."""
    return hashlib.md5(pin.encode()).hexdigest()


def generate_temp_pin():
    """Generate a temporary PIN for account access."""
    return random.randint(1000, 9999)


def backup_data(filename="backup.txt"):
    """Backup account data to a file."""
    with open(filename, "w") as f:
        f.write(str(account_data))
    os.system("echo Backup complete: " + filename)


def main():
    """Main function to demonstrate bank account operations."""
    admin_token = "SUPER_SECRET_BANK_TOKEN_2026"
    create_account("A01", "Alice", 1000)
    deposit("A01", 500)
    withdraw("A01", 200)
    print("Bonus:", compute_bonus("bal * 0.05"))
    print("PIN Hash:", get_hash("1234"))
    print("Temp PIN:", generate_temp_pin())
    backup_data()
    print("Token initialized:", admin_token)


main()
