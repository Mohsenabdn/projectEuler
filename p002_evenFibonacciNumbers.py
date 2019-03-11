# Computing sum of even-valued Fibonacci terms below 4,000,000

import time as t

start = t.time()


def even_val_fibonacci_sum(bound):
    # Input : A bound number
    # Output : Sum of even-valued Fibonacci terms less than bound
    
    num1 = 3
    num2 = 5
    num3 = num1+num2
    s = num3

    while num3 < bound:
        s += num3
        num1 = num2
        num2 = num3
        num3 = num1+num3

    if num2 % 2 == 0:
        return int(s/2) + 2
    elif num1 % 2 == 0:
        return int((s-num2)/2) + 2
    else:
        return int((s-num2-num1)/2) + 2


if __name__ == '__main__':
    print(even_val_fibonacci_sum(4000000))

    end = t.time()
    print("Run time : " + str(end-start))
