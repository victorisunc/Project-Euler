#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER
# PROBLEM 
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
def d(n):
  the_sum = 0
  for i in range(1,(n/2)+1):
    if n%i == 0: the_sum += i
  return the_sum
 
def sum_amicable_numbers(limit): 
  total = 0
  for i in range(1, int(limit)):
    x = d(i) 
    y = d(x)
    if i == y and i != x:
      total += i
  print total

if (__name__ == "__main__"):
  try:
    t = timeit.Timer(setup='from __main__ import sum_amicable_numbers', stmt='sum_amicable_numbers(sys.argv[1])')
    print t.timeit(1)
  except:
    print 'Usage: python file_name.py <first n-digits>'
