#include <iostream>
#include <stack>

int main(){
    std::stack<int> example_stack;
    example_stack.push(10);
    example_stack.push(20);
    example_stack.push(30);
    std::cout<<example_stack.empty()<<"-"<<example_stack.top()<<std::endl;
    for (int i=0; i<3; i++){
        example_stack.pop();
    }
    std::cout<<example_stack.empty()<<std::endl;
};