#include <iostream>
#include <algorithm>
#include <string>

int main (){

    std::string x;
    std::string y;

    std::cin >> x;
    std::cin >> y;

    
    std::reverse(x.begin(), x.end());
    std::reverse(y.begin(), y.end());
    

    int x_rev = std::stoi(x);
    int y_rev = std::stoi(y);

    if (x_rev > y_rev){std::cout << x_rev;}
    else {std::cout << y_rev;}
    
}