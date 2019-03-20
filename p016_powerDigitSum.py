# Finding the sum of digits of 2**1000

import time as t

start = t.time()


def sum_digits(num):
    # Input : number of int type
    # Output : sum of the digits of input

    str_num = str(num)
    digits = [int(i) for i in str_num]
    return sum(digits)


if __name__ == '__main__':
    print(sum_digits(2**1000))

    end = t.time()
    print('Run time : ' + str(end-start))
