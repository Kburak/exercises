"""
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""


class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Added {deposit_amount} to the balance")

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f"{withdraw_amount},Withdrawal Accepted")
        else:
            print("Funds Unavailable!")

    def __str__(self):
        return f"Account Owner :{self.owner} \nAccount balance: {self.balance}$ "


acc = Account("Burak", 100)

print(acc)
print(acc.owner)
print(acc.balance)

acc.deposit(50)
acc.withdraw(75)
acc.withdraw(500)
