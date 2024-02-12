#Author: Henry Våg
#File name: Exercise_3.10.py
#Description: Exercise 3.10


class BankAccount:

    def __init__(self, owner, account_number, balance):
        self.owner = owner 
        self.account_number = account_number
        self.balance = balance
    

    def deposit(self, balance):
        