# Finding the largest prime factor of 600851475143

from numpy import where
import time as t

start = t.time()


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
    num = 600851475143
    largestFactor = 1
    primes = where(prime_finder(int(num ** 0.5)))[0]

    for p in primes:
        while num % p == 0:
            num = int(num/p)
            largestFactor = p

    if num > largestFactor:
        largestFactor = num
    print('The largest Factor : ' + str(largestFactor))

    end = t.time()
    print('Run time : ' + str(end - start))

