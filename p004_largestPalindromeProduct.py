# Finding the largest palindrome number made by product of two 3-digits numbers

import numpy as np
import time as t


def is_palindrome(num):
    """ Input : An integer number
    Output : A bool type (True: input is palindrome, False: input is not
    palindrome) """

    numStr = str(num)
    for i in range(len(numStr)//2):
        if numStr[i] != numStr[-(i+1)]:
            return False
    return True


if __name__ == '__main__':
    start = t.time()
    
    prods = (np.reshape(np.arange(100, 1000), (1, 900)) *
             np.reshape(np.arange(100, 1000), (900, 1)))[np.tril_indices(900)]
    prods = np.sort(prods)[::-1]

    for j in multiples:
        if is_palindrome(j):
            print(j)
            break

    end = t.time()
    print('Run time : ' + str(end - start))
