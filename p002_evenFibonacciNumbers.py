# Computing sum of even-valued Fibonacci terms below 4,000,000

import time as t


def fibonacci_sequence(bound):
    """ Input : A bound value for value of fibonacci numbers
    Output : The fibonacci sequence whose maximum value is less than bound """
    fib = [1, 2]
    if bound == 1: 
        return []
    elif bound == 2: 
        return fib[:1]
    elif bound == 3: 
        return fib
    else:
        app = fib.append
        while fib[-1]+fib[-2] < bound:
            app(fib[-1]+fib[-2])
    return fib


if __name__ == '__main__':
    start = t.time()
    
    print(sum(fibonacci_sequence(4000000)[1::3]))
    
    end = t.time()
    print("Run time : " + str(end-start))
