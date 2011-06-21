#!/usr/bin/env python

import sys
import timeit
from itertools import product
from math import sqrt
# PROJECT EULER 

# PROBLEM 8:

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def pythagorean_triplet():
	triplets = []
	a = [x**2 for x in range(3, 500)]
	b = [x**2 for x in range(4, 500)]
	c = [x**2 for x in range(5, 500)]
	for i in a:
		for j in b:
			for k in c:
				if i + j == k and (i < j) and (j < k):
					if sqrt(i) + sqrt(j) + sqrt(k) == 1000:
						triplets.append([sqrt(i), sqrt(j), sqrt(k)])
	print "Triplet: %s" % triplets[0] 
	product = reduce(lambda x, y: x * y, triplets[0])
	print "Product of triplets: %s" % int(product)
	return

if (__name__ == "__main__"):
  try: 
    t = timeit.Timer(setup='from __main__ import pythagorean_triplet', stmt='pythagorean_triplet()') 
    print t.timeit(1)
  except:
    print 'Usage: python file_name.py'
