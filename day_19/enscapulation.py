'''print("day 19 enscapulation started")'''

#basic syntax
#encapsulation means process of bundling data and methods restricting access to some of the object's components. 

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance+=amount

    def show_balance(self):
        print(f"balance is {self.__balance}")

account=BankAccount(1500)
account.deposit(500)
account.show_balance()