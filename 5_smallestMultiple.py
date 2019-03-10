# Finding the smallest positive number that is evenly divisible by all the numbers from 1 to 20

from problem3 import primeFinder
import numpy as np
import time as t

start = t.time()

topNum = 20
smallest = 1
primes = np.where(primeFinder(topNum))[0]

for i in range(len(primes)):
    k = 1
    while(primes[i]**k < topNum):
        smallest *= primes[i]
        k += 1

print(smallest)

end = t.time()
print('Run time : ' + str(end-start))
