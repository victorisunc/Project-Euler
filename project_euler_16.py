#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER
# PROBLEM 16:

# Find the sum of digits in 2^1000!

def sum_of_power(n):
    # x to the yth power
    a = str(n)
    x = int(a[:a.find('^')])
    y = int(a[a.find('^')+1:])
    power = x**y
    print 'power: %s' % power
    sum_digits = 0
    power_temp = str(power)
    for i in range(len(power_temp)):
        sum_digits += int(power_temp[i])
    print 'Sum of the digits in power: %s' % sum_digits
    return
if (__name__ == "__main__"):
    try:
        t = timeit.Timer(setup='from __main__ import sum_of_power', stmt='sum_of_power(sys.argv[1])')
        print t.timeit(1)
    except:
        print 'Usage: python file_name.py <n>'
