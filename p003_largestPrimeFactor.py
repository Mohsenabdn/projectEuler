# Finding the largest prime factor of 600851475143

import numpy as np
import time as t

start = t.time()


def prime_finder(bound):
    # Input : A bound number
    # Output : A bool list of prime numbers below bound (True: is prime, False: is not prime)

    prime_nums = [True]*(bound+1)
    prime_nums[0] = False
    prime_nums[1] = False

    for i in range(2, int(np.sqrt(bound))+1):
        if prime_nums[i]:
            for k in range(2, int(bound/i)+1):
                prime_nums[i*k] = False
    return prime_nums


if __name__ == '__main__':
    num = 600851475143
    largestFact = 1
    primes = np.where(prime_finder(int(np.sqrt(num))+1))[0]

    for p in primes:
        while num % p == 0:
            num = int(num/p)
            largestFact = p

    if num > largestFact:
        largestFact = num
    print('The largest Factor : ' + str(largestFact))

    end = t.time()
    print('Run time : ' + str(end - start))
