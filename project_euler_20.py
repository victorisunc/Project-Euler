#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER 
# PROBLEM 20:

# Find the sum of digits in 100!

def sum_of_factorial_digits(n):
	n = int(n)
	# calculate the factorial	
	factorial = reduce(lambda x,y: x * y, [i for i in range(1,n+1)])
	print factorial
	# calculate the sum of digits
	factorial = str(factorial)
	sum_digits = 0
	for i in range(len(factorial)):
		sum_digits += int(factorial[i])
	print 'Sum of digits in the factorial: %s' % sum_digits
	return
if (__name__ == "__main__"):
	try: 
		t = timeit.Timer(setup='from __main__ import sum_of_factorial_digits', stmt='sum_of_factorial_digits(sys.argv[1])') 
		print t.timeit(1)
	except:
		print 'Usage: python file_name.py <n>'
