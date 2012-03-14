#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER

# PROBLEM 7:

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?

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
  # find all primes until the n
  counter = 0
  prime = 0
  i = 2
  while counter != n:
    if isprime(i):
      prime = i
      counter += 1
      i += 1
    else:
      i += 1
  print prime
  return prime

if (__name__ == "__main__"):
  try:
    t = timeit.Timer(setup='from __main__ import primes', stmt='primes(int(sys.argv[1]))')
    print t.timeit(1)
  except:
    print 'Usage: python file_name.py ARG'
