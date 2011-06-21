#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER 

# PROBLEM 3:

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
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

def primeFactors(n, factor):
    factors = []
    while (n % factor != 0):
        factor = factor + 1

    factors.append(factor)

    if n > factor:
        factors.extend(primeFactors(n / factor, factor))

    return factors

def find_largest_prime(n):

  print max(primeFactors(n, 2))
  #largest_prime = []
  #x = n**0.5+1
  #nums = range(int(x))
  #for i in nums:
  #  if isprime(i):
  #    if n % i == 0:
	#largest_prime.append(i)
  #print 'largest_prime: %s' % largest_prime[-1:]
  return

# helper sum function that takes a list as input
def sum(result):
  summed = reduce(lambda x, y: x + y, result)
  print summed 
  return summed


if (__name__ == "__main__"):
  try: 
    t = timeit.Timer(setup='from __main__ import find_largest_prime', stmt='find_largest_prime(int(sys.argv[1]))') 
    print t.timeit(1)
  except:
    print 'Usage: python file_name.py ARG'
