#include <iostream>
#include <string>

int main() {

    //std::string x,y;
    int x,y;

    std::cin >> x;
    std::cin >> y;

    //x negativ, y negativ
    if (x < 0 && y < 0){
        std::cout << 3;
    }
    //x negativ, y positiv
    else if (x < 0 && y > 0){

        std::cout << 2;
    
    }
    //x positiv, y negativ
    else if (x > 0 && y < 0){

        std::cout << 4;
    
    }
    //x positiv, y positiv
    else {

        std::cout << 1;

    }

}