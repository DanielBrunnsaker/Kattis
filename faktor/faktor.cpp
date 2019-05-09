#include <iostream>

int main (){

    double A;
    double I;
    double bribes;

    std::cin >> A;
    std::cin >> I;
    
    bribes = A*I-A+1;

    std::cout << bribes;
}