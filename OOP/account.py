class Account:
    def __init__(self,number,pin,balance):
        self.number = number
        self.__pin = pin
        self._balance = 0

    def show_balance(self,pin):
        if pin ==self.__pin:
            print(self.__balance)
        else:
            print("wrong pin")
        
    def display_balance(self):
        print("account owner:", self.ower_name)
        print("current balance:", self.balance)

    def update_owner(self,new_onwer_name):
        self.ower_name = new_onwer_name
        print("account owner update successful.")

    def deposit(self, amount):
        self.balance += amount
        self.transaction.append(("deposit",amount))
        print("Deposit of", amount, "successful.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction.append(("withdraw1", amount))
            print("withdraw1 of", amount, "successful.")
        else:
            print("Insufficient funds.")

    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def view_account_details(self):
        """Display account owner's details and current balance."""
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")

    def set_overdraft_limit(self, overdraft_limit):
        """Set an overdraft limit for the account."""
        self.overdraft_limit = overdraft_limit

    def transfer_funds(self, target_account, amount):
        """Transfer funds from this account to another account."""
        if self.balance >= amount:
            self.withdraw(amount)
            target_account.deposit(amount)
        else:
            print("Insufficient balance for transfer")

    def close_account(self):
        """Close the account."""
        print(f"Account {self.account_number} closed. Thank you!")

