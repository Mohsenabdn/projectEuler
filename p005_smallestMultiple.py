# Finding the smallest positive number that is evenly divisible by all the
# numbers from 1 to 20

import numpy as np
import time as t


def prime_finder(bound):
    """ Input : A bound number
    Output : A bool list of prime numbers below bound (True: is prime,
    False: is not prime)"""

    prime_nums = [True]*(bound+1)
    prime_nums[0] = False
    prime_nums[1] = False

    for i in range(2, int(bound ** 0.5)):
        if prime_nums[i]:
            for k in range(i*2, bound+1, i):
                prime_nums[k] = False
    return prime_nums


if __name__ == '__main__':
    start = t.time()

    topNum = 20
    smallest = 1
    primes = np.where(prime_finder(topNum))[0]

    for p in primes:
        i = 1
        while p**i < topNum:
            smallest *= p
            i += 1

    print(smallest)

    end = t.time()
    print('Run time : ' + str(end-start))
