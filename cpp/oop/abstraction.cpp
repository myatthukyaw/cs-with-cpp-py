#include <iostream>
#include <string>

class Account{
    protected:
        std::string account_num;
        float balance;
    public:
        Account(std::string acc_num, float bal) : account_num(acc_num), balance(bal) {}

        virtual void deposit(float amount) =0;
        virtual void withdraw(float amount) =0;

        std::string get_account_num(){
            return account_num;
        }

        float get_balance(){
            return balance; 
        }     
};

class SavingsAccount : public Account{
    public : 
        SavingsAccount(std::string acc_num, float balance) : Account(acc_num, balance) {}
    
    void deposit(float amount) override{
        balance += amount;
        std::cout<<"Deposit "<<amount<<" to Savings Account."<<std::endl;
    } 

    void withdraw(float amount) override{
        if (balance >= amount){
            balance -= amount;
            std::cout<<"Withdrew "<<amount<<" from Savings Account."<<std::endl;
        } else{
            std::cout<<"Insufficient funds in Savings Account"<<std::endl;
        }
    }
};

class CurrentAccount : public Account {
    public:
        CurrentAccount(std::string acc_num, float bal) : Account(acc_num, balance) {}
    
    void deposit(float amount){
        balance += amount;
        std::cout<<"Deposit "<<amount<<" to Current Account."<<std::endl;
    }

    void withdraw(float amount){
        if (balance >= amount){
            balance -= amount;
            std::cout<<"Withdrew "<<amount<<" from Current Account."<<std::endl;
        } else{
            std::cout<<"Insufficient funds in Current Account"<<std::endl;
        }
    }
};

int main(){
    Account* my_savings = new SavingsAccount("1234 5678 90", 100);
    my_savings->deposit(1000);
    my_savings->withdraw(500);
    std::cout<<"Savings Account Balance :"<<my_savings->get_balance()<<std::endl<<std::endl;

    Account* my_current = new CurrentAccount("1234 5678 90", 1000);
    my_current->deposit(1000);
    my_current->withdraw(2500);
    my_current->withdraw(200);
    std::cout<<"Current Account Balance :"<<my_current->get_balance()<<std::endl;

    return 0;
};
