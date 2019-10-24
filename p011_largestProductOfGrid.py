# Finding the greatest product of four adjacent numbers in all directions
# (up & down, left & right, or diagonally) of the 20 by 20 grid given in the
# file '20By20Grid.txt'.

import numpy as np
import time as t


def all_direction_products(g, num_adj):
    """ Input : A square grid and number of adjacent numbers.
    Output : Four arrays consisting products of num_adj adjacent numbers in
     each direction. """

    g_size = g.shape[0]
    row_prods = [np.prod(g[i:i+num_adj, j]) for j in range(g_size)
                 for i in range(g_size-num_adj+1)]
    col_prods = [np.prod(g[i, j:j+num_adj]) for i in range(g_size)
                 for j in range(g_size-num_adj+1)]
    main_diag_prods = [np.prod(np.diagonal(g, offset=i)[j:j+numAdj])
                       for i in range(-(g_size-num_adj), g_size-num_adj+1)
                       for j in range((g_size-num_adj)-np.absolute(i)+1)]
    oppos_diag_prods = [np.prod(np.diagonal(np.rot90(g), offset=i)[j:j+numAdj])
                        for i in range(-(g_size-num_adj), g_size-num_adj+1)
                        for j in range((g_size-num_adj)-np.absolute(i)+1)]
    return row_prods, col_prods, main_diag_prods, oppos_diag_prods


if __name__ == '__main__':
    start = t.time()
    
    grid = np.genfromtxt('p011_20By20Grid.txt', dtype='int8')
    numAdj = 4
    rows, cols, mainDiags, opposDiags = all_direction_products(grid, numAdj)
    maximums = [np.max(rows), np.max(cols), np.max(mainDiags), np.max(opposDiags)]
    print(max(maximums))
    
    end = t.time()
    print('Run time : ' + str(end-start))
