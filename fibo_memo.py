#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER

# PROBLEM 2:
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

fibo_memo = {}
def fibo(n):
  if n not in fibo_memo:
      fibo_memo[n] = n if n < 2 else fibo(n-2) + fibo(n-1)
      return fibo_memo[n]
  else:
    return fibo_memo[n]


def output(original, pre):

    if len(original) == 0:
        print pre
        return
    if len(original) == 1:
        print pre + chr(96 + int(original))
        return


    if int(original[0:2]) < 27:
        new_chr = chr(96 + int(original[0:2]))
        output(original[2:], pre + new_chr)
    new_chr = chr(96 + int(original[0:1]))
    output(original[1:], pre + new_chr)

def paly(input):
  count = len(input)
  for i in range(len(input)-1):
    str = input[i]
    print str
    for j in range(i+1,len(input)):
      str += input[j]
      print "str: " + str
      if str == str[::-1]:
        print "yes"
        count += 1
  return count

# /**
# *
# * @param chars a string represented as a list of chars
# * @return true if the string contains a balanced number of parentheses, false o/w
# */
# def balance(chars: List[Char]): Boolean = {
#   @tailrec
#   def balance(chars: List[Char], acc: Int): Boolean = {
#    if (chars.isEmpty) (acc == 0)
#    else if (acc >= 0) {
#      if ('('.equals(chars.head)) balance(chars.tail, acc + 1)
#      else if (')'.equals(chars.head)) balance(chars.tail, acc - 1)
#      else balance(chars.tail, acc)
#    } else false
#  }
#  balance(chars, 0)
# } 


if (__name__ == "__main__"):
  # try:
  # print fibo(int(sys.argv[1]))
  # print output('1123', '')
  print paly('abba')
    # t = timeit.Timer(setup='from __main__ import fibo', stmt='fibo(int(sys.argv[1]))')
    # print t.timeit(1)
    #calculate(int(sys.argv[1]))
  # except:
    # print 'Usage: python file_name.py ARG'
