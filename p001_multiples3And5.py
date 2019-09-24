# Computing sum of all the multiples 3 or 5 below 1000

import numpy as np
import time as t

start = t.time()


def multiple_sum(bound, prime1, prime2):
    """ Input : A bound and two prime numbers 
    Output : Sum of multiples of prime1 and prime2 less than bound """
    
    mult = prime1*prime2
    s = np.sum(np.arange(prime1, bound, prime1))
    s += np.sum(np.arange(prime2, bound, prime2))
    s -= np.sum(np.arange(mult, bound, mult))
    return s


if __name__ == '__main__':
    print(multiple_sum(1000, 3, 5))

    end = t.time()
    print("Run time : " + str(end-start))
