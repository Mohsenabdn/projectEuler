# Finding the product of Pythagorean triplet(num1 < num2 < num3 && num3**2 = num2**2 + num1**2)\
# whose sum is 1000 (There is exactly one)

import time as t

start = t.time()

pythTripSum = 1000
isPythTrip = False

for num1 in range(1, int(pythTripSum/3)):
    for num2 in range(num1+1, int((pythTripSum-num1)/2)):
        if (pythTripSum-num1-num2)**2 == num1**2 + num2**2:
            isPythTrip = True
            print(num1*num2*(pythTripSum-num2-num1))
            break
    if isPythTrip:
        break

end = t.time()
print('Run time : ' + str(end-start))
