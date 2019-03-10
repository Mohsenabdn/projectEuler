# Finding the largest palindrome number made by product of two 3-digits numbers

import time as t

start = t.time()

# Input : An integer number
# Output : A bool type (True: input is palindrome, False: input is not palindrome)

def isPalindrome(num):
    digits = []
    while(num):
        digits.append(num%10)
        num = int(num/10)
    for i in range(int(len(digits)/2)):
        if digits[i] != digits[-(i+1)]:
            return False
    return True

if __name__ == '__main__':
    multiples = []
    for i in range(100, 1000):
        for j in range(i, 1000):
            multiples.append(i*j)

    multiples.sort(reverse=True)

    for i in range(len(multiples)):
        if isPalindrome(multiples[i]):
            print(multiples[i])
            break

    end = t.time()
    print('Run time : ' + str(end - start))
