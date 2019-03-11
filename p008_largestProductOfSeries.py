# Finding 13 adjacent digits in bigNum (a 1000-digit number) having the greatest product.

import numpy as np
import time as t

start = t.time()


def product_adjacent(big_num, num_adj):
    # Input : A large number of type string and the number of adjacent digits of type int
    # Output : A numpy array of all products of num_adj adjacent digits
    
    prod_len = len(big_num)-num_adj+1
    digits = np.array([int(i) for i in big_num])
    prod = np.array([np.prod(digits[i:i+num_adj]) for i in range(prod_len)])
    return prod


file = open('1000DigitNumber.txt')
bigNum = file.read()
file.close()
bigNum = bigNum.replace('\n', '')

print(np.max(product_adjacent(bigNum, 13)))

end = t.time()
print('Run time : ' + str(end-start))
