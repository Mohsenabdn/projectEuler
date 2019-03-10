# Finding sum of all primes below 2,000,000

from problem3 import primeFinder
import numpy as np
import time as t

start = t.time()

primes = np.where(primeFinder(2000000))[0]
print(sum(primes))

end = t.time()
print('Run time : ' + str(end-start))