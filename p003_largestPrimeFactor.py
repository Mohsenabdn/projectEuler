# Finding the largest prime factor of 600851475143

import time as t


def prime_factors(num):
    """ Input : The positive integer number.
    Output : The list of prime factors (with repetition) of the Input. """

    p_facts = []
    app = p_facts.append
    p = 2
    while p*p < num:
        if num % p:
            p += 1
        else:
            app(p)
            num //= p
    if num > 1:
        app(num)
    return p_facts


if __name__ == '__main__':
    start = t.time()

    num = 600851475143
    print('The largest Factor : ' + str(prime_factors(num)[-1]))

    end = t.time()
    print('Run time : ' + str(end - start))
