import math as m
import sys

def sumofFactors(n):

        residual = 1
        for i in range(2, int(m.sqrt(n) + 1)):
             count = 0
             current_tot = 1
             current = 1
         
             while n % i == 0:
                 count = count + 1
                 n = n / i;
 
                 current = current * i;
                 current_tot += current_tot;
             
             residual = residual * current_tot
        if n > 2:
            residual = residual * (1 + n)
 
        return residual;

for strnumber in sys.stdin:

    number = int(strnumber)
    sum = sumofFactors(number)/2
    if number-2 < sum <= number+2:
        if sum == number:
            print(number,'perfect')
        else:
            print(number,'almost perfect')
    else:
        print(number,'not perfect')