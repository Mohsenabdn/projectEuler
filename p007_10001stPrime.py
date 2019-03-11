# Finding the 10,001st prime number

from p003_largestPrimeFactor import prime_finder
import numpy as np
import time as t

start = t.time()

bound = 200000
primes = np.where(prime_finder(bound))[0]
print(primes[10000])

end = t.time()
print('Run time : ' + str(end-start))
