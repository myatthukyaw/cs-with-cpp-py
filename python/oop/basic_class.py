"""
Python has no private variables like in cpp.
You can use name conventions for private variables in python. 
Name mangling is used here.
"""

class Bankaccount():
    def __init__(self, account_num : str, balance : float):
        self.__account_num = account_num
        self.__balance = balance
    
    def get_account_balance(self) -> float:
        return self.__balance
    
    def get_account_number(self) -> str:
        return self.__account_num

    def deposit(self, amount : float) -> None:
        self.__balance += amount
    
    def withdraw(self, amount : float) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient Funds!")

account = Bankaccount("1234 5678 90", 1000)
#print(account.__account_num)           # This will give error. 
#print(account.__balance)               # 'Bankaccount' object has no attribute '__balance'

print(account.get_account_number())     # 1234 5678 90
print(account.get_account_balance())    # 1000

account.deposit(1000)
account.withdraw(100)
account.withdraw(2000)                  # Insufficient funds!

