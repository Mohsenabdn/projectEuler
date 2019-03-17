# Finding the number of all routes from top left corner of a 20 by 20 grid\
# to the bottom right corner such that it can move either right or down

import time as t

start = t.time()


def factorial(num):
    # Input : An integer number
    # Output : The factorial of input

    fact = 1
    if num == 0 or num == 1:
        return fact
    else:
        for i in range(2, num+1):
            fact *= i
        return fact


if __name__ == '__main__':
    gSize = 20
    routNum = int(factorial(gSize*2)/(factorial(gSize)**2))
    print(routNum)

    end = t.time()
    print('Run time : ' + str(end-start))
