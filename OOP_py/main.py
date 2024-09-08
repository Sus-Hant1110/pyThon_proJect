# Bank Account using oop in python
class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initial_amount,accName,):
        self.balance=initial_amount
        self.name=accName
        print(f"\n Account '{self.name}'created.\n Current balance=${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposite(self,amount):
        self.balance=self.balance+amount
        print("\n Deposite Complete ")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"\n Sorry! Account '{self.name}'has balance of ${self.balance:.2f} \n Transaction not possible")
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance=self.balance-amount
            print("\n Withdrawal Complete ")
            self.getBalance()

        except BalanceException as error:
            print(f'\n Withdrawal not possible : {error}')

    def transfer(self,amount,account):
        try:
            print('\n************\n Transfering...🚀🚀🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print('\nTransfer Complete...✔✔✔')

        except BalanceException as error:
            print(f'\n Transfer not possible 😢: {error}')

class InterestAccount(BankAccount):
    def deposite(self, amount):
        self.balance=self.balance+(amount*1.05)
        print("\n Deposite Complete ")
        self.getBalance()

class SavingAccount(InterestAccount):
    def __init__(self, initial_amount, accName):
        super().__init__(initial_amount, accName)
        self.fee=5

    def withdraw(self, amount):
        try:
             self.viableTransaction(amount+self.fee) 
             self.balance=self.balance-(amount+self.fee) 
             print("\n Withdrawal Complete ")
             self.getBalance()

        except BalanceException as error:
            print(f'\n Withdrawal not possible : {error}')