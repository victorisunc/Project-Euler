#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER

# PROBLEM 10:

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

def isprime(n):
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0

    max = n**0.5+1
    i = 3

    while i <= max:
        if n % i == 0:
            return 0
        i+=2

    return 1

def primes(n):
    # find all primes below two million and sum them up
    i = 2
    result = 0
    while i < n:
        if isprime(i):
            result += i
        i+=1
    print result
    return result

# helper sum function that takes a list as input
def sum(result):
    summed = reduce(lambda x, y: x + y, result)
    print summed
    return summed


if (__name__ == "__main__"):
    try:
        t = timeit.Timer(setup='from __main__ import primes', stmt='primes(int(sys.argv[1]))')
        print t.timeit(1)
    except:
        print 'Usage: python file_name.py ARG'
