# Finding the 10,001st prime number

from problem3 import primeFinder
import numpy as np
import time as t

start = t.time()

bound = 200000
primes = np.where(primeFinder(bound))[0]
print(primes[10000])

end = t.time()
print('Run time : ' + str(end-start))
