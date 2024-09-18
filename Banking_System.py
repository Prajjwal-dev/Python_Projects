class Account:
    """Represents a bank account with basic operations."""

    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        """Return the current balance."""
        return self.balance


class Bank:
    """Represents a bank managing multiple accounts."""

    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder_name, initial_balance=0):
        """Create a new account."""
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, holder_name, initial_balance)
            print(f"Account created for {holder_name} with account number {account_number}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        """Retrieve an account by its number."""
        return self.accounts.get(account_number, None)

    def deposit(self, account_number, amount):
        """Deposit money into an account."""
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        """Withdraw money from an account."""
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        """Check the balance of an account."""
        account = self.get_account(account_number)
        if account:
            print(f"Account balance for {account_number}: ${account.get_balance()}")
        else:
            print("Account not found.")


def main():
    """Main function to run the banking system."""
    bank = Bank()

    print("\n--- Banking System ---\n")

    while True:
        print("\nBanking System Menu")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            acc_number = input("Enter account number: ")
            holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(acc_number, holder_name, initial_balance)

        elif choice == '2':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(acc_number, amount)

        elif choice == '3':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(acc_number, amount)

        elif choice == '4':
            acc_number = input("Enter account number: ")
            bank.check_balance(acc_number)

        elif choice == '5':
            print("Exiting the banking system.")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()
