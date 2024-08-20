from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_num, balance):
        self._account_num = account_num
        self._balance = balance
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    def get_account_num(self):
        return self._account_num

    def get_balance(self):
        return self._balance
    
class SavingsAccount(Account):
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount} in Savings Account.")

    def withdraw(self, amount):
        if self._balance > amount : 
            self._balance -= amount
            print(f"Withdrew {amount} from Savings Account.")
        else:
            print("Insufficient Funds in Savings Account.")
    
class CurrentAccount(Account):
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount} in Current Account.")

    def withdraw(self, amount):
        if self._balance > amount : 
            self._balance -= amount
            print(f"Withdrew {amount} from Current Account.")
        else:
            print("Insufficient Funds in Current Account.")

class CheckingAccount(Account):
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount} in Checking Account.")

def main():
    my_savings = SavingsAccount("1234 5678 90", 500.0)
    my_savings.deposit(200.0)
    my_savings.withdraw(100.0)
    print(f"Savings Account Balance: {my_savings.get_balance()}\n")

    my_current = CurrentAccount("1234 5678 90", 1000.0)
    my_current.deposit(500.0)
    my_current.withdraw(1500.0)
    print(f"Current Account Balance: {my_current.get_balance()}\n")

    # This will give you error because withdraw method wasn't implemented for CheckingAccount.
    # my_checking = CheckingAccount("1234 5678 90", 2000)
    # my_checking.deposit(100.0)

if __name__ == "__main__":
    main()
