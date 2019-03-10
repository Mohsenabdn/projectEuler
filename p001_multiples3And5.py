# Computing sum of all the multiples 3 or 5 below 1000

import time as t

start = t.time()

# Input : A bound and two prime numbers
# Output : Sum of multiples of prime1 or prime2 less than bound

def multipleSum(bound, prime1, prime2):
    sum = 0
    for i in range(1,int((bound-1)/prime1)+1):
        sum += i*prime1
    for i in range(1,int((bound-1)/prime2)+1):
        sum += i*prime2
    for i in range(1,int((bound-1)/(prime1*prime2))+1):
        sum -= i*prime1*prime2
    return(sum)

if __name__ == '__main__':
    print(multipleSum(1000,3,5))

    end = t.time()
    print("Run time : " + str(end-start))
