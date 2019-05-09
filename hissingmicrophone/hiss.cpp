#include <iostream>
#include<stdio.h> 

int main (){

    int count = 0;

    std::string str;
    std::getline(std::cin, str);

    for (int i = 0; i < str.size(); i++) {

        if (str[i] == 's' && str[i+1] == 's'){count++;} 

    }

    if (count >= 1){std::cout << "hiss";}
    else {std::cout << "no hiss";}
  

}