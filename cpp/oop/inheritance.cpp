#include <iostream>
#include <string>

class BankAccount{
    protected:
        std::string account_num;
        double balance;
    
    public:
        BankAccount(std::string account_n, double bal) : account_num(account_n), balance(bal) {}
    
        std::string get_account_num(){
            return account_num;
        }

        double get_balance(){
            return balance;
        }
    
        void deposit(double amount){
            balance += amount;
            std::cout<<"Deposited "<<amount<<" to account "<<account_num<<". New balance: "<<balance<<std::endl;
        }
    
        void withdraw(double amount){
            if (amount <= balance) {
                balance -= amount;
                std::cout<<"Withdrew "<<amount<<" from account "<<account_num<<". New balance: "<<balance<<std::endl;
            } else {
                std::cout<<"Insufficient funds!"<<std::endl;
            }
        }
};

class SavingsAccount : public BankAccount{
    private : 
        float interest_rate;
    public : 
        SavingsAccount(std::string account_n, double balance, float int_rate=0.03) 
            : BankAccount(account_n, balance), interest_rate(int_rate) {}
    
        void add_interest(){
            double interest = balance * interest_rate;
            deposit(interest);
            std::cout<<"Interest of "<<interest<<" added to account "<<account_num<<". New balance: "<<balance<<std::endl;
        }
};

class CurrentAccount : public BankAccount{
    public:
        CurrentAccount(std::string account_n, double balance) 
            : BankAccount(account_n, balance) {}
};

int main(){
    SavingsAccount savings("SA1234567890", 1000.0);
    savings.deposit(500.0);
    savings.add_interest();
    savings.withdraw(300.0);
    std::cout << "Savings Account Balance: " << savings.get_balance() << std::endl<<std::endl;

    CurrentAccount current("CA1234567890", 200.0);
    current.deposit(300.0);
    current.withdraw(600.0);
    current.withdraw(200.0);  // This should exceed the overdraft limit
    std::cout << "Current Account Balance: " << current.get_balance() << std::endl;
    return 0;
};