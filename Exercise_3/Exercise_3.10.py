#Author: Henry Våg
#File name: Exercise_3.10.py
#Description: Exercise 3.10


class BankAccount:

    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner 
        self.__account_number = account_number
        self.__balance = balance


    @staticmethod
    def __service_charge():
        amount = account.__balance * 0.01
        account.__balance -= amount
        
    
    @staticmethod
    def deposit(amount: float):
        account.__balance += amount
        BankAccount.__service_charge()
        print(f'Added ${amount} to account')
    
    @staticmethod
    def withdraw(amount: float):
        account.__balance -= amount
        BankAccount.__service_charge()
        print(f'Withdrew ${amount} from account')

    @property
    def balance(self):
        return(self.__balance)
    
   




account = BankAccount("Randy Riches","12345-6789",1000)
account.withdraw(100)
print(account.balance)
account.deposit(100)
print(account.balance)
    




