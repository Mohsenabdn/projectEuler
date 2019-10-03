# Finding the largest palindrome number made by product of two 3-digits numbers

import numpy as np
import time as t

start = t.time()


def is_palindrome(num):
    """ Input : An integer number
    Output : A bool type (True: input is palindrome, False: input is not
    palindrome) """

    digits = []
    while num:
        digits.append(num % 10)
        num = int(num/10)
    for i in range(int(len(digits)/2)):
        if digits[i] != digits[-(i+1)]:
            return False
    return True


if __name__ == '__main__':
    prods = (np.reshape(np.arange(100, 1000), (1, 900)) *
             np.reshape(np.arange(100, 1000), (900, 1)))[np.tril_indices(900)]
    prods = np.unique(np.sort(prods))[::-1]

    for j in multiples:
        if is_palindrome(j):
            print(j)
            break

    end = t.time()
    print('Run time : ' + str(end - start))
