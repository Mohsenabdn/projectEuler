# Finding the difference between the sum of the squares of the first hundred natural numbers
# and the square of the sum

import time as t

start = t.time()


def sum_squares(bound):
    # Input : A bound number
    # Output : Sum of square of numbers smaller than input
    
    return int((bound*(bound+1)*(2*bound+1))/6)


def sum_nums(bound):
    # Input : A bound number
    # Output : Sum of numbers smaller than input
    
    return int((bound*(bound+1))/2)


if __name__ == '__main__':
    limit = 100
    diff = sum_nums(limit)**2 - sum_squares(limit)
    print(diff)

    end = t.time()
    print('Run time : ' + str(end-start))
