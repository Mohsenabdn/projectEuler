# Finding starting number under 1,000,000 creating the longest Collatz sequence

import numpy as np
import time as t

start = t.time()


def collatz_len_seq(bound):
    # Input : A bound number
    # Output : A numpy array of size input including length of Collatz sequence

    len_seq = np.zeros(bound, dtype='int64')
    len_seq[0] = 1
    len_seq[1] = 1
    for i in range(bound):
        cache = []
        while i > bound-1 or len_seq[i] < 1:
            cache.append(i)
            if i % 2 == 0:
                i = int(i/2)
            else:
                i = int(i*3 + 1)
        cache_len = len(cache)
        for j in cache:
            if j < bound:
                len_seq[j] = len_seq[i]+cache_len-cache.index(j)
    return len_seq


if __name__ == '__main__':
    collSeqLen = collatz_len_seq(1000000)
    maxLen = np.max(collSeqLen)
    print((np.where(collSeqLen == maxLen)[0][0], maxLen))

    end = t.time()
    print('Run time : ' + str(end-start))
