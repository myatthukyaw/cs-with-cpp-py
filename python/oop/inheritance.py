class BankAccount:
    def __init__(self, account_num, balance):
        self._account_num = account_num
        self._balance = balance

    def get_account_num(self):
        return self._account_num

    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount} to account {self._account_num}. New balance: {self._balance}")

    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount} from account {self._account_num}. New balance: {self._balance}")
        else:
            print("Insufficient funds!")

class SavingsAccount(BankAccount):
    def __init__(self, account_num, balance, interest_rate=0.03):
        super().__init__(account_num, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} added to account {self._account_num}. New balance: {self._balance}")

class CurrentAccount(BankAccount):
    def __init__(self, account_num, balance):
        super().__init__(account_num, balance)

def main():
    savings = SavingsAccount("SA 1234 5678 90", 1000.0)
    savings.deposit(500.0)
    savings.add_interest()
    savings.withdraw(300.0)
    print(f"Savings Account Balance: {savings.get_balance()}\n")

    current = CurrentAccount("CA 1234 5678 90", 200.0)
    current.deposit(300.0)
    current.withdraw(600.0)
    current.withdraw(200.0) 
    print(f"Current Account Balance: {current.get_balance()}")


if __name__ == "__main__":
    main()