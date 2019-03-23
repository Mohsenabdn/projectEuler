# Finding the sum of all amicable numbers under 10000

import numpy as np
import time as t

start = t.time()


def sum_prop_div(n):
    # Input : Positive integer
    # Output : Sum of the proper divisors of input

    if n == 0 or n == 1:
        return 0
    s = 1
    for i in range(2, int(np.sqrt(n))+1):
        if n % i == 0:
            s += i
            if i != int(n/i):
                s += int(n/i)
    return s


def amicable_finder(sum_divs):
    # Input : A list type including sum of proper divisors of positive numbers\
    # starting from 0
    # Output : a list of type boolean (True: amicable, False: not amicable)

    size = len(sum_divs)
    ami = [False] * size
    for s in sum_divs:
        if 0 < s < size and sum_divs[s] == sum_divs.index(s) and s != sum_divs[s]:
            ami[s] = True
            ami[sum_divs.index(s)] = True
    return ami


if __name__ == '__main__':
    bound = 10000
    sumDivs = [sum_prop_div(num) for num in range(bound)]
    amiNums = np.where(amicable_finder(sumDivs))[0]
    print(sum(amiNums))

    end = t.time()
    print('Run time : ' + str(end-start))
