# Finding the difference between the sum of the squares of the first hundred natural numbers
# and the square of the sum

import time as t

start = t.time()

def sumSquares(bound):
    return int((bound*(bound+1)*(2*bound+1))/6)
def sumNums(bound):
    return int((bound*(bound+1))/2)

if __name__ == '__main__':
    bound = 100
    diff = sumNums(bound)**2 - sumSquares(bound)
    print(diff)

    end = t.time()
    print('Run time : ' + str(end-start))
