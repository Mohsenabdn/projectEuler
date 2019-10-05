# Finding total names' scores Given in the file "p022_names.txt". Each name
# score is the sum of alphabetic values (A=1, B=2, C=3, ..., Z=26) of the name
# multiply by the position number of the name in the sorted list of the file
# "p022_names.txt".

import time as t
import string

start = t.time()

file = open('p022_names.txt')
names = file.read().split(',')
file.close()

names = [eval(name) for name in names]
names.sort()
alphabets = list(string.ascii_uppercase)

nameScores = [sum([alphabets.index(alpha)+1 for alpha in names[i]])*(i+1)
              for i in range(len(names))]
print(sum(nameScores))

end = t.time()
print('Run time : ' + str(end-start))
