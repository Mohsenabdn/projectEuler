# Finding the product of Pythagorean triplet(num1 < num2 < num3 && num3**2
# = num2**2 + num1**2) whose sum is 1000 (There is exactly one)

import time as t


def pythgorean_triple(trip_sum):
    """ Input : The sum of Pythagorean Triplet.
    Output : Three integers forming Pythagorean triplet whose sum is Input. """

    for num1 in range(1, trip_sum//3):
        for num2 in range(num1+1, (trip_sum-num1)//2 + 1):
            if (trip_sum-num1-num2)**2 == num1**2 + num2**2:
                return num1, num2, (trip_sum-num1-num2)
    raise Exception('There are no Pythagorean triplet whose sum is {}'.format
                    (trip_sum))


if __name__ == '__main__':    
    start = t.time()

    pythTripSum = 1000
    num1, num2, num3 = pythgorean_triple(pythTripSum)
    print('The Pythagorean triplet are {}, {}, {}. and their product is {}'.
          format(num1, num2, num3, num1*num2*num3))

    end = t.time()
    print('Run time : ' + str(end-start))
