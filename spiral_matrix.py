#!/usr/bin/env python

import sys
import timeit

"""
Input: 3 4
Result:
 1  2 3
10 11 4
 9 12 5
 8  7 6

Input: 3 3
Result:
 1 2 3
 8 9 4
 7 6 5

Input: 5 6
Result:
 1  2  3  4  5
18 19 20 21  6
17 28 29 22  7
16 27 30 23  8
15 26 25 24  9
14 13 12 11 10
"""


def spiral_matrix(cols, rows):
  matrix = [[0 for _ in range(cols)] for _ in range(rows)]
  top, left = 0, 0
  down, right = rows - 1, cols - 1
  number_to_write = 1

  while(True):
    for i in range(left, right + 1): # top row
      matrix[top][i] = '{0:2}'.format(number_to_write)
      number_to_write += 1
    top += 1
    if top > down or left > right: break
    for i in range(top, down + 1): # rightmost row
      matrix[i][right] = '{0:2}'.format(number_to_write)
      number_to_write += 1
    right -= 1
    if top > down or left > right: break
    for i in range(right, left - 1, -1): # bottom row
      matrix[down][i] = '{0:2}'.format(number_to_write)
      number_to_write += 1
    down -= 1
    if top > down or left > right: break
    for i in range(down, top - 1, -1): # leftmost row
      matrix[i][left] = '{0:2}'.format(number_to_write)
      number_to_write += 1
    left += 1
    if top > down or left > right: break
  print_matrix(matrix)
  return

def print_matrix(matrix):
  print('\n'.join(''.join(['{0:4}'.format(item)]).replace("'", '') for item in matrix))

if __name__ == '__main__':
  try:
    t = timeit.Timer(setup='from __main__ import spiral_matrix',
      stmt='spiral_matrix(int(sys.argv[1]), int(sys.argv[2]))')
    print t.timeit(1)
  except:
    print sys.exc_info()
    print 'Usage: python spiral_matrix.py <columns> <rows>'
