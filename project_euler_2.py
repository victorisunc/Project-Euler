#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER

# PROBLEM 2:
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibo(n-1) + fibo(n-2)

def calculate(n):
  result = 0
  i = 1
  while True:
    temp = fibo(i)
    if temp > n:
      break
    if temp % 2 == 0:
      result = result + temp
    i = i + 1
  print result
  return result

# helper sum function that takes a list as input
def sum(result):
  summed = reduce(lambda x, y: x + y, result)
  print summed
  return summed

if (__name__ == "__main__"):
  try:
    t = timeit.Timer(setup='from __main__ import calculate', stmt='calculate(int(sys.argv[1]))')
    print t.timeit(1)
    #calculate(int(sys.argv[1]))
  except:
    print 'Usage: python file_name.py ARG'
