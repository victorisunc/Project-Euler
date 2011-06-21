#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER 

# PROBLEM 4:

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
	number = str(n)
	return number == number[::-1]
  
	"""
	half_string = len(number)/2
	last_index = len(number)-1
	for i in range(half_string):
		if number[i] == number[last_index]:
			last_index -= 1
		else:
			#print 'Not Palindrome'
			return False
	#print "It's a palindrome!"	
	return True
	"""

def find_largest_palindrome(n):
  # where n is n-digit numbers
	# construct the largest n-digit number from the input
	largest_A = '9'
	n = int(n)-1
	for i in range(n):
		largest_A += '9'
	largest_A = int(largest_A)
	largest_B = largest_A
	
	largest_palindrome = 0
	# largest_A and largest_B should be something like NN or NNN depending on the n
	# brute force test every possible multiplication of largest_A and largest_B
	for i in reversed(range(600, largest_A+1)):
		for j in reversed(range(600, largest_B+1)):
			test = i*j
			if test < 10000: 
				continue
			elif isPalindrome(test):
				if test > largest_palindrome:
					print 'Product A: %s' % i
					print 'Product B: %s' % j
					largest_palindrome = test 
	print 'Largest Palindrome: %s' % largest_palindrome
	return


if (__name__ == "__main__"):
  try: 
    t = timeit.Timer(setup='from __main__ import find_largest_palindrome', stmt='find_largest_palindrome((sys.argv[1]))') 
    print t.timeit(1)
  except:
    print 'Usage: python file_name.py ARG'
