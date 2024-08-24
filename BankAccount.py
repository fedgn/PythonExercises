class BankAccount:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print(f"Balance of {self.holder_name} is {self.balance}$")

    def display_info(self):
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Operation done succesfully. The balance is {self.balance}$ now.")

    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
            print(f"Operation done succesfully. The balance is {self.balance}$ now.")
        else:
            print(f"Your balance is not enough for this operation. Maximum amount you can withdraw is ${self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}
        self.last_account_number = 0

    def generate_account_number(self):
        self.last_account_number += 1
        return str(self.last_account_number)
    
    def create_account(self, holder_name, initial_balance):
        new_account_number = self.generate_account_number()
        new_account = BankAccount(holder_name, new_account_number, initial_balance)
        self.accounts[new_account_number] = new_account
        print(f"Account successfully created with the account number: {new_account_number}!")
    
    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"The account with number {account_number} is deleted")
        else:
            print(f"Operation Failed! Such an account does not exist, it can't be deleted!")
            
    def find_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return None

    def list_accounts(self):
        if not self.accounts:
            print("No accounts in the bank.")
        else:
            print("List of all accounts:")
            for account_number, account in self.accounts.items():
                print(f"Account Number: {account_number}")
                print(f"Holder Name: {account.holder_name}")
                print(f"Balance: ${account.balance}")
                print("-" * 20)

if __name__ == "__main__":
    
    #TODO add GUI instead of silly menu below

    Banka = Bank()
    while True:
        print(f"Select an Operation:")
        print(f"a. Create a new account")
        print(f"b. Find an account")
        print(f"c. Remove an account")
        print(f"d. List all accounts")
        print(f"e. Deposit money")
        print(f"f. Withdraw money")
        print(f"g. Exit")

        op = input()

        match op:
            case "a":
                name = input("Full Name of the holder: ")
                initial_balance = float(input("Initial money: "))
                Banka.create_account(name, initial_balance)
            case "b":
                account_number_to_find = input("Enter account number you want to search: ")
                account = Banka.find_account(account_number_to_find)
                if not account:
                    print(f"Account not found!")
                else:
                    print(f"Account found")
                    print(f"Name: {account.holder_name}")
                    print(f"Balance: {account.balance}$")
            case "c":
                account_number_to_remove = input("Enter account number you want to remove")
                Banka.remove_account(account_number_to_remove)
            case "d":
                Banka.list_accounts()
            case "e":
                account_number_to_find = input("Enter account number you want to search: ")
                account = Banka.find_account(account_number_to_find)
                if not account:
                    print(f"Account not found!")
                else:
                    deposit_amount = float(input(f"Enter the amount to be deposited"))
                    account.deposit(deposit_amount)
            case "f":
                account_number_to_find = input("Enter account number you want to search: ")
                account = Banka.find_account(account_number_to_find)
                if not account:
                    print(f"Account not found!")
                else:
                    withdraw_amount = float(input(f"Enter the amount to be withdrawn"))
                    account.withdraw(withdraw_amount)
            case "g":
                exit(0)
            case _:
                print("Please select a valid operation")
        


    