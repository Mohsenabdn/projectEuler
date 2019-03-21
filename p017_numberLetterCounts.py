# Counting letters to be used to write numbers from 1 to 1000

import numpy as np
import time as t

start = t.time()


def letter_count(num_digits=1):
    # Input : the number of digits of numbers to count their letters\
    # (1: 1-digit numbers, 2: 2-digit numbers and else: 3digit numbers)
    # Output : counting the number of letters

    keys = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
            'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty',
            'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'and']
    ind1 = keys.index('ten')
    ind2 = keys.index('twenty')
    ind3 = keys.index('hundred')
    if num_digits == 1:
        vals = np.array([len(i) for i in keys[:ind1]])
        return np.sum(vals)
    elif num_digits == 2:
        vals = np.array([len(i) for i in keys[:ind3]])
        vals[:ind1] = vals[:ind1]*8
        vals[ind2:] = vals[ind2:]*10
        return np.sum(vals)
    else:
        vals = np.array([len(i) for i in keys])
        vals[:ind1] = vals[:ind1]*181
        vals[ind1:ind2] = vals[ind1:ind2]*9
        vals[ind2:ind3] = vals[ind2:ind3]*90
        vals[ind3] = vals[ind3]*900
        vals[-1] = vals[-1]*891
        return np.sum(vals)


if __name__ == '__main__':
    print(letter_count()+letter_count(2)+letter_count(3)+len('onethousand'))

    end = t.time()
    print('Run time : ' + str(end-start))
