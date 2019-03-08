# Finding 13 adjacent numbers in bigNum (a 1000-digit number) having the greatest product.

import time as t

start = t.time()

file = open('1000DigitNumber.txt')
bigNum = file.read()
file.close()
bigNum = bigNum.replace('\n', '')

numAdj = 13
prodLen = len(bigNum)-numAdj+1
prod = [1]*prodLen
digits = [int(i) for i in bigNum]

for i in range(prodLen):
    for j in range(i, i+numAdj):
        prod[i] *= digits[j]

print(max(prod))

end = t.time()
print('Run time : ' + str(end-start))
