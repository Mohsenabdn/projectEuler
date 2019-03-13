# Finding the first triangle number to have over 500 divisors

from p006_sumSquareDifference import sum_nums
import numpy as np
import time as t

start = t.time()

count = 0
nth = 1
triNum = 1
while count <= 500:
    nth += 1
    triNum = sum_nums(nth)
    count = 2
    for i in range(2, int(np.sqrt(triNum))):
        if triNum % i == 0:
            count += 2
        if count > 500:
            break
print(triNum)

end = t.time()
print("Run time : " + str(end-start))
