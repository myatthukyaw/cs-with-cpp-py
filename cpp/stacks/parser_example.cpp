#include <iostream>
#include <stack>

bool is_blanaced(std::string input_str){

    std::stack<char> stk;
    // std::string open_brackets[3] = {"[", "{", "("};
    // std::string close_brackets[3] = {"]", "}", ")"};

    for (char charac : input_str){
        if (charac == '[' || charac == '{' || charac =='('){
            stk.push(charac);
        } else if (charac == ']' || charac == '}' || charac ==')'){
            //stk.pop();
            char top = stk.top();
            if ((charac == ']' && top != '[') ||
                (charac == ')' && top != '(') ||
                (charac == '}' && top != '{'))
                return false; 
            else{
                stk.pop();
            }
        } else{
            continue;
        }
    }
    return stk.empty();
}

int main(){

    std::string input_str= "[[)]]";
    if (is_blanaced(input_str)){
        std::cout<<"Input string is balanced."<<std::endl;
    } else{
        std::cout<<"Input string is not balanced."<<std::endl;
    }
    
    return 0;
}