# Finding the largest palindrome number made by product of two 3-digits numbers

import time as t

start = t.time()

# Input : An integer number
# Output : A bool type (True: input is palindrome, False: input is not palindrome)


def is_palindrome(num):
    digits = []
    while num:
        digits.append(num % 10)
        num = int(num/10)
    for i in range(int(len(digits)/2)):
        if digits[i] != digits[-(i+1)]:
            return False
    return True


if __name__ == '__main__':
    multiples = []
    for k in range(100, 1000):
        for j in range(k, 1000):
            multiples.append(k*j)

    multiples.sort(reverse=True)

    for j in range(len(multiples)):
        if is_palindrome(multiples[j]):
            print(multiples[j])
            break

    end = t.time()
    print('Run time : ' + str(end - start))
