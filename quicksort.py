#!/usr/bin/env python

import sys
import timeit


def quicksort(l):
    if l == []:
        return []
    else:
        pivot = l[0]
        lesser = quicksort([x for x in l[1:] if x < pivot])
        greater = quicksort([x for x in l[1:] if x >= pivot])
        return lesser + [pivot] + greater

if (__name__ == "__main__"):
    try:
        # t = timeit.Timer(setup='from __main__ import quicksort', stmt="quicksort(sys.argv[1].replace(' ', '').split(','))")
        print t.timeit(1)
        # print quicksort(sys.argv[1].replace(' ', '').split(','))
        print quicksort([2,1,3])
    except:
        print 'Usage: python file_name.py LIST_TO_SORT'
