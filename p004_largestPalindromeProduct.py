# Finding the largest palindrome number made by product of two 3-digits numbers

import numpy as np
import time as t

start = t.time()


def is_palindrome(num):
    # Input : An integer number
    # Output : A bool type (True: input is palindrome, False: input is not palindrome)

    digits = []
    while num:
        digits.append(num % 10)
        num = int(num/10)
    for i in range(int(len(digits)/2)):
        if digits[i] != digits[-(i+1)]:
            return False
    return True


if __name__ == '__main__':
    multiples = np.array([k*j for k in range(100, 1000) for j in range(k, 1000)])
    multiples[::-1].sort()

    for j in multiples:
        if is_palindrome(j):
            print(j)
            break

    end = t.time()
    print('Run time : ' + str(end - start))
