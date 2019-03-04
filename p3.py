# Finding the largest prime factor of 600851475143

import numpy as np
import time as t

start = t.time()

# Input : A bound number
# Output : A bool list of prime numbers below bound (True: is prime, False: is not prime)

def primeFinder(bound):
    primes = [True for i in range(bound+1)]
    primes[0] = False
    primes[1] = False

    for i in range(2,int(np.sqrt(bound))+1):
        if primes[i]:
            for k in range(2,int(bound/i)+1):
                primes[i*k] = False
    return primes

if __name__ == '__main__':
    num = 600851475143
    largestFact = 1
    primes = np.where(primeFinder(int(np.sqrt(num))+1))[0]

    for i in range(len(primes)):
        while(num%primes[i] == 0):
            num = int(num/primes[i])
            largestFact = primes[i]

    if num > largestFact :
        largestFact = num
    print('The largest Factor : ' + str(largestFact))

    end = t.time()
    print('Run time : ' + str(end - start))