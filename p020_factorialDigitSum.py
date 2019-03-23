# Finding sum of the digits of number 100!

import numpy as np
import time as t

start = t.time()


def factorial(n):
    # Input : Positive integer number
    # Output : factorial of the input

    f = 1
    if n == 0:
        return f
    for i in range(1, n+1):
        f *= i
    return f


if __name__ == '__main__':
    num = 100
    numString = str(factorial(num))
    digits = np.array([int(i) for i in numString])
    print(np.sum(digits))

    end = t.time()
    print('Run time : ' + str(end-start))
