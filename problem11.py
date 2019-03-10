# Finding the greatest product of four adjacent numbers in the same direction\
# (up & down, left & right, or diagonally) in the 20 by 20 grid given in the file\
# 20By20Grid.txt

import numpy as np
import time as t

start = t.time()

grid = np.genfromtxt('20By20Grid.txt', dtype='int8')
gSize = grid.shape[0]
numAdj = 4

UD = np.array([np.prod(grid[i:i+numAdj, j]) for j in range(gSize)\
               for i in range(gSize-numAdj+1)])

LR = np.array([np.prod(grid[i, j:j+numAdj]) for i in range(gSize)\
               for j in range(gSize-numAdj+1)])

mainDiag = np.array([np.prod(np.diagonal(grid, offset=i)[j:j+numAdj])\
                     for i in range(-(gSize-numAdj), gSize-numAdj+1)\
                     for j in range((gSize-numAdj)-np.absolute(i)+1)])

opposDiag = np.array([np.prod(np.diagonal(np.rot90(grid), offset=i)[j:j+numAdj])\
                      for i in range(-(gSize-numAdj), gSize-numAdj+1)\
                      for j in range((gSize-numAdj)-np.absolute(i)+1)])

maximums = np.array([np.max(UD), np.max(LR), np.max(mainDiag), np.max(opposDiag)])
print(np.max(maximums))

end = t.time()
print('Run time : ' + str(end-start))
