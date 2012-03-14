#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER
# PROBLEM 12:

# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

def factorize(n): #returns list of all the factors in n
	n = int(n)
	div_n=[1]
	max = n
	i = 2
	while i <= max:
		if n % i == 0:
			div_n.append(i)
			div_n.append(n/i) #if n is divisible then append n and result
		if n%2==0:
			i+=1
		else:
			i+=2
			max=int((n/i)+1)
	set_of_factors = set(div_n)
	#return div_n
	return len(set_of_factors)


def triangle_number(n):
  # n is how many divisors we want the number to have
	n = int(n) + 1

	triangle_number = 0
	counter = 0
	index = 0
	n_divisors = 0
	while n_divisors < n:
		n_divisors = 0
		counter += index
		index += 1
		triangle_number = (counter+index)
		triangle_root = int(triangle_number**0.5)
		for i in range(1, triangle_root):
			if triangle_number % i == 0:
				n_divisors += 2
		if triangle_number == triangle_root**2:
			n_divisors -= 1
	print "Number of divisors for triangle number: %s is %s" % (triangle_number, n_divisors)
	return

if (__name__ == "__main__"):
	try:
		t = timeit.Timer(setup='from __main__ import triangle_number', stmt='triangle_number(sys.argv[1])')
		print t.timeit(1)
	except:
		print 'Usage: python file_name.py <number of divisors>'
