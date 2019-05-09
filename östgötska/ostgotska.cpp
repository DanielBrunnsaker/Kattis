#include <iostream>
#include<stdio.h> 

int main (){

    double aecount = 0;
    double spaces = 0;
    double fraction;
    double aeword = 0;

    std::string str;
    std::getline(std::cin, str);

    for (int i = 0; i <= str.size(); i++) {

        if (str[i] == 'a' && str[i+1] == 'e'){aecount++;} 
        if (str[i] == ' '){

            spaces++;

            if (aecount > 0){
                aeword++;
                aecount = 0;
                }

        } 
        if (i == str.size() && aecount > 0){aeword++;}
    }

    fraction = aeword/(spaces+1);

    if (fraction >= 0.4){std::cout << "dae ae ju traeligt va";}
    else {std::cout << "haer talar vi rikssvenska";}

}