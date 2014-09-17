#!/usr/bin/env python

import sys
import time
from random import randint, shuffle

def gaussian_sum(n):
  return (n * (n + 1)) / 2

def missing_number_unsorted(list_missing_number):

  list_length = len(list_missing_number) + 1
  total_sum = gaussian_sum(list_length)
  array_sum = sum(list_missing_number)
  missing = total_sum - array_sum
  if missing == list_length:
    print '-1'
    return -1
  print 'missing_number_unsorted, result: %s' % missing
  return missing


def missing_number_sorted(list_missing_number):
  # for index, item in enumerate(sorted(list_missing_number), start = 1):
  for index, item in enumerate(list_missing_number, start = 1):
    if index != item:
      print 'missing_number_sorted, result: %s' % index
      return index
  return -1

def missing_number_log_g(list_missing_number):
  # sorted_list_missing_number = sorted(list_missing_number)
  sorted_list_missing_number = list_missing_number
  length = len(list_missing_number)
  left = 0
  right = length - 1
  while (left <= right):
    middle = (left + right) / 2
    if (middle + 1 == sorted_list_missing_number[middle]):
      left = middle + 1
    else:
      right = middle - 1
  if left + 1 > length:
    print '-1'
    return -1
  else:
    print 'missing_number_log_g, result: %s' % (left + 1)
    return left + 1


def setup(list_length):
  list_length = int(list_length)
  array = range(1, list_length + 1)
  #shuffle(array)

  # Randomly remove one number from the array
  number_to_remove = randint(1, list_length)
  print 'number to be removed: %s' % number_to_remove
  array.remove(number_to_remove)

  start = time.time()
  missing_number_unsorted(array)
  elapsed = time.time() - start
  print 'missing_number_unsorted took: %s seconds' % elapsed

  start = time.time()
  missing_number_sorted(array)
  elapsed = time.time() - start
  print 'missing_number_sorted took: %s seconds' % elapsed

  start = time.time()
  missing_number_log_g(array)
  elapsed = time.time() - start
  print 'missing_number_log_g took: %s ms' % (elapsed * 1000)


if (__name__ == '__main__'):
  try:
    setup(sys.argv[1])
  except:
    print 'Usage: python filename.py list_length'