#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER 

# PROBLEM 5:

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def find_smallest_number(n):
  div_numbers = range(int(n/2+1), n+1)
  flag = True
  smallest_number = 1
  while flag:
    for i in div_numbers:
      if smallest_number % i == 0:
        if i == n: 
          print 'smallest_number: %s' % smallest_number
          flag = False
          return
        continue
      else:
        smallest_number += 1
        break

# INCREDIBLY BETTER AND FASTER WAY TO SOLVE THIS:
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)
####################################################

if (__name__ == "__main__"):
  try: 
    input_range = range(1,int(sys.argv[1])+1)
    t = timeit.Timer(setup='from __main__ import lcmm, input_range', stmt='lcmm(*input_range)') 
    print 'smallest number: %s' % lcmm(*input_range)
    print t.timeit(1)
  except:
    print 'Usage: python file_name.py ARG'
