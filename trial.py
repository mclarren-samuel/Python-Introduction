class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is {self.__balance}.")
    def withdraw(self, amount):
        if amount > self.__balance or self.__balance == 0:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")

    def show_balance(self):
        print(f"Balance: ${self.__balance}")

account = BankAccount(350)
account.deposit(2000)
account.withdraw(20)

account.show_balance()
account.__balance = 0
account.show_balance()
print(account.__balance)