# Computing sum of all the multiples 3 or 5 below 1000

import time as t

start = t.time()


def multiple_sum(bound, prime1, prime2):
    """ Input : A bound and two prime numbers 
    Output : Sum of multiples of prime1 and prime2 less than bound """
    
    s = sum([i*prime1 for i in range(1, (bound-1)//prime1+1)])
    s += sum([i*prime2 for i in range(1, (bound-1)//prime2+1)])
    s -= sum([i*prime1*prime2 for i in range(1, (bound-1)//(prime1*prime2)+1)])
    return s

if __name__ == '__main__':
    print(multiple_sum(1000, 3, 5))

    end = t.time()
    print("Run time : " + str(end-start))
