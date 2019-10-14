# Finding sum of all positive integers which cannot be written as the sum of
# two abundant numbers.
# if the sum of proper divisors of a number is greater than the number itself,
# it is called abundant number.
# It is proved that all integers greater than 28123 can be written as the sum
# of two abundant numbers.

import time as t
import numpy as np


def proper_divisors(num):
    """ Input : A positive integer.
    Output : The set of all proper divisors of Input. """

    proDiv = [1]
    app = proDiv.append
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            app(i)
            app(num//i)
    return(set(proDiv))


def is_abundant(num):
    """ Input : A positive integer.
    Output : A boolean type whether Input is an abundant or not (an abundant a
     number which the sum of its proper divisors are greater than itself) """

    if num < 12:
        return False  # The positive integers less than 12 are not abundant.
    elif sum(proper_divisors(num)) > num:
        return True
    else:
        return False


if __name__ == '__main__':
    start = t.time()

    abundNums = []
    app = abundNums.append
    for i in range(1, 28123):
        if is_abundant(i):
            app(i)

    abundSums = []
    app = abundSums.append
    for i in range(len(abundNums)):
        j = i
        while (abundNums[i]+abundNums[j]) < 28124:
            app(abundNums[i]+abundNums[j])
            j += 1

    print(np.sum(range(28124)) - sum(set(abundSums)))

    end = t.time()
    print('Running time : ' + str(end-start))
