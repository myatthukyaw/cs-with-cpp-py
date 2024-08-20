#include <iostream>
#include <string>

class BankAccount{
    private:
        std::string account_num;
        int balance;

    public:
        BankAccount(std::string account_num, int balance) : account_num(account_num), balance(balance){}
    
        float get_account_balance(){
            return balance;
        }

        std::string get_account_num(){
            return account_num;
        }

        void deposit(float amount){
            balance += amount;
        }

        void withdraw(float amount){
            if (balance >= amount){
                balance -= amount;
            } else {
                std::cout<<"Insufficient funds!"<<std::endl;
            }
        }

};

int main(){

    BankAccount myaccount("1234 5678 90", 1000);
    std::cout<<myaccount.get_account_num()<<std::endl;          // 1234 5678 90
    std::cout<<myaccount.get_account_balance()<<std::endl;      // 1000
    myaccount.deposit(1000);
    myaccount.withdraw(100);
    myaccount.withdraw(2000);                                   // Insufficient funds!
    return 0;
}