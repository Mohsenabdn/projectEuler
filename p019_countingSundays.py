# Finding the number of Sundays falling on the first of the month during\
# twentieth century (1 Jan 1901 to 31 Dec 2000) knowing the following information:
# -- 1 Jan 1900 was a Monday -- September, April, June and November have 30 days\
# and all the rest have 31 days except February having 28 days and 29 days on\
# leap years -- A leap year occurs on any year evenly divisible by 4, but not on\
# a century unless it is divisible by 400.

import itertools
import time as t

start = t.time()


def is_leap(year):
    # Input : The year in integer type
    # Output : Boolean answer that the input is a leap year or not

    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


def first_day_year(year):
    # Input : The year in integer type
    # Output : The value of the first day of the input year
    # {Sunday:0, Monday:1, Tuesday:2, Wednesday:3, Thursday:4, Friday:5, Saturday:6}

    first_day = 1
    if year > 1900:
        leap_list = [is_leap(i) for i in range(1900, year)]
        first_day = (first_day + year - 1900 + sum(leap_list)) % 7
        return first_day
    elif year < 1900:
        leap_list = [is_leap(i) for i in range(year, 1900)]
        first_day = (first_day + year - 1900 - sum(leap_list)) % 7
        return first_day
    else:
        return first_day


def count_first_months(year, day=0):
    # Input : The year and day in integer type\
    # {Sunday:0, Monday:1, Tuesday:2, Wednesday:3, Thursday:4, Friday:5, Saturday:6}
    # Output : The number of day fallen in the first of the months of the year

    count = 0
    first_day = first_day_year(year)
    months = [(28 if i == 0 else (30 if i == 3 or i == 5 or i == 8 or i == 10
                                  else 31))for i in range(11)]
    if is_leap(year):
        months[1] += 1
    months = [first_day] + months
    first_months = list(itertools.accumulate(months))
    for firsts in first_months:
        if firsts % 7 == day:
            count += 1
    return count


if __name__ == '__main__':
    yearInterval = [1901, 2000]
    counting = 0
    for y in range(yearInterval[0], yearInterval[1]+1):
        counting += count_first_months(y)
    print(counting)
