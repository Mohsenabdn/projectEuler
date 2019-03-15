# Finding the first 10 digits of the sum of 100 50-digit numbers saved in\
# the file named '100FiftyDigitNumbers.txt'

import numpy as np
import time as t

start = t.time()

bigNums = np.genfromtxt('100FiftyDigitNumbers.txt')
bigNumSum = np.sum(bigNums)
bigNumSum = format(bigNumSum, '.0f')
print(str(bigNumSum)[:10])

end = t.time()
print('Run time : ' + str(end-start))
