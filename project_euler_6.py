#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER 

# PROBLEM 6:

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# the square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# helper sum function that takes a list as input
def sum(result):
  summed = reduce(lambda x, y: x + y, result)
  return summed

def difference_sums(n):
  n = int(n)+1
  sum_squares = 0
  for i in range(1, n):
    sum_squares += i**2
  print 'sum_squares: %s' % sum_squares
  square_of_sum = sum(range(1,n))**2
  print 'square_of_sum: %s' % square_of_sum
  print ( square_of_sum - sum_squares )
  return

if (__name__ == "__main__"):
  try: 
    t = timeit.Timer(setup='from __main__ import difference_sums', stmt='difference_sums(sys.argv[1])') 
    print t.timeit(1)
  except:
    print 'Usage: python file_name.py ARG'
