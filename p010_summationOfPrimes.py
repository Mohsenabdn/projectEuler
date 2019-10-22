# Finding sum of all primes below 2,000,000

from p005_smallestMultiple import prime_finder
import numpy as np
import time as t

start = t.time()

primes = np.where(prime_finder(2000000))[0]
print(sum(primes))

end = t.time()
print('Run time : ' + str(end-start))
