# Finding 13 adjacent digits of a big Number (a 1000-digit number saved in the
# file named p008_1000DigitNumber.txt) having the greatest product.

import numpy as np
import time as t


def product_adjacent(big_num, num_adj):
    """ Input : A large number of type string (big_num) and the number of
     adjacent digits (num_adj).
    Output : A list of all products of num_adj adjacent digits. """
    
    prod_len = len(big_num)-num_adj+1
    digits = [int(i) for i in big_num]
    prod = [np.prod(digits[i:i+num_adj]) for i in range(prod_len)]
    return prod


if __name__ == '__main__:
    start = t.time()
    
    file = open('p008_1000DigitNumber.txt')
    bigNum = file.read()
    file.close()
    bigNum = bigNum.replace('\n', '')

    print(np.max(product_adjacent(bigNum, 13)))

    end = t.time()
    print('Run time : ' + str(end-start))
